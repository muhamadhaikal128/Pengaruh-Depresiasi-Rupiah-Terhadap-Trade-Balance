"""Separate HS4 panels into conservative UNCTAD commodity classes, offline.
Retains zero trade, unknown/mixed categories, missing values and all input files.
Builds monthly/quarterly two-flow HS4 panels and macro-joined group subtotals.
"""
from pathlib import Path
import hashlib,json,tempfile
import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal

ROOT=Path(__file__).resolve().parents[1]
MID=ROOT/'intermediate'
OUT=MID/'hs_classified'
CLASSES=['commodity','noncommodity','mixed','unclassified']
FLOWS=['Exports_USDk','Imports_USDk']

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def csvout(df,p):
    p.parent.mkdir(parents=True,exist_ok=True)
    df.to_csv(p,index=False,float_format='%.12g',encoding='utf-8')

def ratios(df):
    df['Trade_Balance_USDk']=df.Exports_USDk-df.Imports_USDk
    df['Total_Trade_USDk']=df.Exports_USDk+df.Imports_USDk
    ok=df.Exports_USDk.gt(0)&df.Imports_USDk.gt(0)
    df['Positive_Both_Flows']=ok
    df['Ln_Exports_Imports']=np.log(df.Exports_USDk.where(ok)/df.Imports_USDk.where(ok))
    df['Ln_Imports_Exports']=-df.Ln_Exports_Imports
    return df

def macro_columns(df,key):
    keys=['ISO3',key]
    if 'Country' in df:keys.append('Country')
    return keys+[c for c in df if c not in keys and c.startswith(
        ('CMD_','IDN_','Partner_','REER_','CPI_','NER_','RER_','JISDOR_','Uses_WPI_'))]

def read_source(iso,flow,known):
    name=f'{flow}_{iso}.csv';p=MID/'hs_panel'/name
    d=pd.read_csv(p,dtype={'HS_Code':str,'ISO3':str,'Date':str})
    assert d.ISO3.eq(iso).all() and d.Flow.eq(flow).all(),name
    assert d.HS_Code.str.fullmatch(r'\d{4}').all(),name
    assert not d.duplicated(['HS_Code','Date']).any(),name
    assert set(d.HS_Code)<=known,(name,'Code not present in classification')
    assert d.Value_USDk.notna().all(),(name,'Unexpected missing source values; review before processing')
    return d

def build_group(iso,m,export,imp,classes):
    summaries=[]
    for c in CLASSES:
        sub=m[m.Commodity_Class.eq(c)]
        ex_codes=export.loc[export.HS_Code.map(classes).eq(c),'HS_Code'].nunique()
        im_codes=imp.loc[imp.HS_Code.map(classes).eq(c),'HS_Code'].nunique()
        s=pd.DataFrame({'Date':sorted(m.Date.unique())})
        sums=sub.groupby('Date')[FLOWS].sum(min_count=1)
        count=sub.groupby('Date')[FLOWS].count()
        for field,expected in zip(FLOWS,[ex_codes,im_codes]):
            stem='Exports' if field.startswith('Exports') else 'Imports'
            s['Observed_'+field]=s.Date.map(sums[field])
            s['N_HS4_'+stem+'_Observed']=s.Date.map(count[field]).fillna(0).astype(int)
            s['N_HS4_'+stem+'_SourceUniverse']=expected
            complete=s['N_HS4_'+stem+'_Observed'].eq(expected)&(expected>0)
            s[stem+'_SourceUniverse_Complete']=complete
            s[field]=s['Observed_'+field].where(complete)
        s['ISO3']=iso;s['Commodity_Class']=c
        s['N_HS4_Class_Lookup']=int(classes.eq(c).sum())
        s['Commodity_Flag']=1 if c=='commodity' else 0 if c=='noncommodity' else pd.NA
        summaries.append(ratios(s))
    return pd.concat(summaries,ignore_index=True)

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    mapping=pd.read_csv(MID/'HS4_Commodity_Classification.csv',dtype={'HS_Code':str})
    assert not mapping.HS_Code.duplicated().any()
    classes=mapping.set_index('HS_Code').Commodity_Class
    flags=mapping.set_index('HS_Code').Commodity_Flag
    cr=json.loads((MID/'HS4_Classification_Validation_Report.json').read_text('utf-8'))
    assert cr['classification_sha256']==sha(MID/'HS4_Commodity_Classification.csv')
    pm=pd.read_csv(MID/'Panel_Country_Month.csv',dtype={'ISO3':str,'Date':str})
    pq=pd.read_csv(MID/'Panel_Country_Quarter.csv',dtype={'ISO3':str,'Quarter':str})
    assert not pm.duplicated(['ISO3','Date']).any() and not pq.duplicated(['ISO3','Quarter']).any()
    sources=sorted((MID/'hs_panel').glob('*.csv'))
    assert len(sources)==20,'Expected ten partners and two trade flows'
    initial_hash={str(p.relative_to(ROOT)):sha(p) for p in sources}
    initial_hash['intermediate/HS_Lookup.csv']=sha(MID/'HS_Lookup.csv')
    panels_hash={p.name:sha(p) for p in [MID/'Panel_Country_Month.csv',MID/'Panel_Country_Quarter.csv']}
    file_manifest=[];group_m=[];reconcile=[];inputs=[];last_months=[]
    anchor={}
    # Stage on the project drive. Publish after all conservation checks succeed.
    with tempfile.TemporaryDirectory(prefix='stage_hs_class_',dir=MID) as stage_name:
        stage=Path(stage_name)
        for iso in sorted(pm.ISO3.unique()):
            ex=read_source(iso,'Export',set(classes.index))
            im=read_source(iso,'Import',set(classes.index))
            dates=sorted(pm.loc[pm.ISO3.eq(iso),'Date'].unique())
            assert set(ex.Date)<=set(dates) and set(im.Date)<=set(dates)
            hs=sorted(set(ex.HS_Code)|set(im.HS_Code))
            m=pd.MultiIndex.from_product([hs,dates],names=['HS_Code','Date']).to_frame(index=False)
            m['ISO3']=iso
            for source,field,stem in [(ex,'Exports_USDk','Exports'),(im,'Imports_USDk','Imports')]:
                vals=source[['HS_Code','Date','Value_USDk']].rename(columns={'Value_USDk':field})
                vals[stem+'_Source_Row_Present']=True
                m=m.merge(vals,on=['HS_Code','Date'],how='left',validate='one_to_one',sort=False)
                m[stem+'_Source_Row_Present']=m[stem+'_Source_Row_Present'].eq(True)
                # Exact reconstruction at every originally observed source key.
                back=source[['HS_Code','Date','Value_USDk']].merge(
                    m[['HS_Code','Date',field]],on=['HS_Code','Date'],validate='one_to_one')
                np.testing.assert_allclose(back.Value_USDk,back[field],rtol=0,atol=0)
            m['Commodity_Class']=m.HS_Code.map(classes)
            m['Commodity_Flag']=m.HS_Code.map(flags).astype('Int64')
            assert m.Commodity_Class.notna().all()
            m=ratios(m)
            m=m[['ISO3','HS_Code','Date','Commodity_Class','Commodity_Flag',*FLOWS,
                 'Trade_Balance_USDk','Total_Trade_USDk','Ln_Exports_Imports','Ln_Imports_Exports',
                 'Positive_Both_Flows','Exports_Source_Row_Present','Imports_Source_Row_Present']]
            mm=m[['HS_Code','Date',*FLOWS]].copy()
            mm['Quarter']=pd.PeriodIndex(mm.Date,freq='M').asfreq('Q').astype(str)
            g=mm.groupby(['HS_Code','Quarter'],sort=True)
            q=g[FLOWS].sum(min_count=3).reset_index()
            counts=g[FLOWS].count().rename(columns=dict(zip(FLOWS,['NMonths_Exports','NMonths_Imports']))).reset_index()
            q=q.merge(counts,on=['HS_Code','Quarter'],validate='one_to_one')
            q['ISO3']=iso;q['Commodity_Class']=q.HS_Code.map(classes)
            q['Commodity_Flag']=q.HS_Code.map(flags).astype('Int64')
            q['Complete_Both_Flows']=q.NMonths_Exports.eq(3)&q.NMonths_Imports.eq(3)
            q=ratios(q)
            assert q.loc[q.NMonths_Exports.ne(3),'Exports_USDk'].isna().all()
            assert q.loc[q.NMonths_Imports.ne(3),'Imports_USDk'].isna().all()
            assert m.loc[~m.Positive_Both_Flows,'Ln_Imports_Exports'].isna().all()
            for c in CLASSES:
                for df,freq,key in [(m,'Month','Date'),(q,'Quarter','Quarter')]:
                    sub=df[df.Commodity_Class.eq(c)].copy()
                    name=Path(c)/f'HS4_{iso}_{freq}.csv'
                    csvout(sub,stage/'hs_classified'/name)
                    file_manifest.append({'path':str(Path('intermediate/hs_classified')/name),
                        'ISO3':iso,'Commodity_Class':c,'Frequency':freq,'Rows':len(sub),
                        'N_HS4':sub.HS_Code.nunique(),'First_Period':sub[key].min() if len(sub) else '',
                        'Last_Period':sub[key].max() if len(sub) else '',
                        'Positive_Both_Flows_Rows':int(sub.Positive_Both_Flows.sum())})
                    # Check one serialized key per partition, including code leading zeros.
                    if len(sub):
                        saved=pd.read_csv(stage/'hs_classified'/name,nrows=1,dtype={'HS_Code':str})
                        assert saved.HS_Code.iloc[0]==sub.HS_Code.iloc[0]
                assert set(m.loc[m.Commodity_Class.eq(c),'HS_Code'])<=set(classes[classes.eq(c)].index)
            summary=build_group(iso,m,ex,im,classes)
            group_m.append(summary)
            # Source conservation, including the mixed and unclassified buckets.
            for source,field in [(ex,'Exports_USDk'),(im,'Imports_USDk')]:
                src=source.groupby('Date').Value_USDk.sum(min_count=1)
                dest=summary.groupby('Date')['Observed_'+field].sum(min_count=1).reindex(src.index)
                np.testing.assert_allclose(src,dest,rtol=1e-12,atol=1e-6,equal_nan=True)
                rows=pd.DataFrame({'ISO3':iso,'Date':src.index,'Flow':field,
                    'Source_HS_Sum_USDk':src.values,'Classified_HS_Sum_USDk':dest.values})
                official=pm[pm.ISO3.eq(iso)].set_index('Date')[field]
                rows['Official_AllProducts_USDk']=rows.Date.map(official)
                rows['Partition_Difference_USDk']=rows.Classified_HS_Sum_USDk-rows.Source_HS_Sum_USDk
                rows['HS_vs_Official_Difference_USDk']=rows.Source_HS_Sum_USDk-rows.Official_AllProducts_USDk
                rows['HS_vs_Official_Difference_pct']=100*rows.HS_vs_Official_Difference_USDk/rows.Official_AllProducts_USDk.where(rows.Official_AllProducts_USDk.ne(0))
                reconcile.append(rows)
                inputs.append({'ISO3':iso,'Flow':field,'Rows':len(source),'N_HS4':source.HS_Code.nunique(),
                    'Zero_Value_Rows':int(source.Value_USDk.eq(0).sum()),
                    'Negative_Value_Rows':int(source.Value_USDk.lt(0).sum()),
                    'First_Date':source.Date.min(),'Last_Date':source.Date.max()})
            if iso=='CHN':
                anchor['hs4_1511_CHN_2015Q1']=q.loc[q.HS_Code.eq('1511')&q.Quarter.eq('2015Q1'),FLOWS].iloc[0].to_dict()
            print('BUILT',iso,'HS4',len(hs),'month_rows',len(m),'quarter_rows',len(q),flush=True)
        gm=pd.concat(group_m,ignore_index=True)
        assert not gm.duplicated(['ISO3','Commodity_Class','Date']).any()
        gm=gm.merge(pm[macro_columns(pm,'Date')],on=['ISO3','Date'],how='left',validate='many_to_one')
        gm['Commodity_Flag']=gm.Commodity_Flag.astype('Int64')
        gmc=gm[['ISO3','Commodity_Class','Date',*FLOWS,'Observed_Exports_USDk','Observed_Imports_USDk']].copy()
        gmc['Quarter']=pd.PeriodIndex(gmc.Date,freq='M').asfreq('Q').astype(str)
        g=gmc.groupby(['ISO3','Commodity_Class','Quarter'],sort=True)
        gq=g[FLOWS+['Observed_Exports_USDk','Observed_Imports_USDk']].sum(min_count=3).reset_index()
        n=g[FLOWS].count().rename(columns=dict(zip(FLOWS,['NMonths_Exports','NMonths_Imports']))).reset_index()
        gq=gq.merge(n,on=['ISO3','Commodity_Class','Quarter'],validate='one_to_one')
        gq=ratios(gq)
        gq['Complete_Both_Flows']=gq.NMonths_Exports.eq(3)&gq.NMonths_Imports.eq(3)
        gq['Commodity_Flag']=gq.Commodity_Class.map({'commodity':1,'noncommodity':0}).astype('Int64')
        gq=gq.merge(pq[macro_columns(pq,'Quarter')],on=['ISO3','Quarter'],how='left',validate='many_to_one')
        required=['Ln_Imports_Exports','IDN_GDP_Real_Index_2015mean100',
                  'Partner_GDP_Real_Index_2015mean100','RER_Bilateral_Index_2015mean100']
        gq['Ready_NARDL_CPI_Group']=gq[required].notna().all(axis=1)&gq.Complete_Both_Flows
        gq['Ready_NARDL_CPI_Group_With_BCOM']=gq.Ready_NARDL_CPI_Group&gq.CMD_BCOM_Mean.notna()
        proxy_required=required[:-1]+['RER_With_WPI_Proxy_Index_2015mean100']
        gq['Ready_NARDL_PriceProxy_Group']=gq[proxy_required].notna().all(axis=1)&gq.Complete_Both_Flows
        rec=pd.concat(reconcile,ignore_index=True)
        inp=pd.DataFrame(inputs);manifest=pd.DataFrame(file_manifest)
        # Row/key conservation in each country: partitions cover disjoint HS4 sets.
        for iso in pm.ISO3.unique():
            for freq in ['Month','Quarter']:
                a=manifest[(manifest.ISO3==iso)&(manifest.Frequency==freq)]
                assert len(a)==4 and a.N_HS4.sum()==len(set(
                    pd.read_csv(MID/'hs_panel'/f'Export_{iso}.csv',usecols=['HS_Code'],dtype=str).HS_Code)|set(
                    pd.read_csv(MID/'hs_panel'/f'Import_{iso}.csv',usecols=['HS_Code'],dtype=str).HS_Code))
        totals=gm.groupby(['ISO3','Date'])[['Observed_'+f for f in FLOWS]].sum(min_count=1).rename(columns={'Observed_'+f:f for f in FLOWS}).reset_index()
        share=gm[['ISO3','Date','Commodity_Class','Observed_Exports_USDk','Observed_Imports_USDk']].merge(
            totals,on=['ISO3','Date'],how='left',validate='many_to_one')
        for field in FLOWS:
            share[field.replace('_USDk','_Share_pct')]=100*share['Observed_'+field]/share[field].where(share[field].ne(0))
        shares=share.groupby('Commodity_Class')[['Observed_Exports_USDk','Observed_Imports_USDk']].sum(min_count=1).reset_index()
        shares['Exports_Share_AllObserved_pct']=100*shares.Observed_Exports_USDk/shares.Observed_Exports_USDk.sum()
        shares['Imports_Share_AllObserved_pct']=100*shares.Observed_Imports_USDk/shares.Observed_Imports_USDk.sum()
        small={'Panel_CommodityGroup_Country_Month.csv':gm,'Panel_CommodityGroup_Country_Quarter.csv':gq,
            'HS4_Classified_File_Manifest.csv':manifest,'HS4_Classified_Source_Coverage.csv':inp,
            'HS4_Classified_Reconciliation.csv':rec,'HS4_Commodity_Trade_Shares.csv':share,
            'HS4_Commodity_Trade_Summary.csv':shares}
        for name,df in small.items():csvout(df,stage/name)
        # Validate the serialized group panels, zeros and macro alignment.
        saved=pd.read_csv(stage/'Panel_CommodityGroup_Country_Quarter.csv')
        assert len(saved)==len(pq)*4
        assert saved.loc[saved.NMonths_Exports.ne(3),'Exports_USDk'].isna().all()
        assert saved.loc[saved.NMonths_Imports.ne(3),'Imports_USDk'].isna().all()
        for col in macro_columns(pq,'Quarter'):
            if col in ['ISO3','Quarter','Country']:continue
            cmp=saved[['ISO3','Quarter',col]].merge(pq[['ISO3','Quarter',col]],on=['ISO3','Quarter'],validate='many_to_one',suffixes=('_saved','_original'))
            if pd.api.types.is_numeric_dtype(pq[col]):
                np.testing.assert_allclose(cmp[col+'_saved'],cmp[col+'_original'],rtol=1e-10,atol=1e-8,equal_nan=True)
            else:
                pd.testing.assert_series_equal(cmp[col+'_saved'],cmp[col+'_original'],check_names=False,check_dtype=False)
        assert sha(MID/'HS4_Commodity_Classification.csv')==cr['classification_sha256']
        for path,digest in initial_hash.items():assert sha(ROOT/path)==digest,path
        for name,digest in panels_hash.items():assert sha(MID/name)==digest,name
        report={'status':'PASS','definition':'UNCTAD A11 conservative HS4 consensus',
            'classification_sha256':sha(MID/'HS4_Commodity_Classification.csv'),
            'class_counts':cr['class_counts'],'input_flow_rows':int(inp.Rows.sum()),
            'original_zero_trade_rows_preserved':int(inp.Zero_Value_Rows.sum()),
            'partition_files':len(manifest),'hs4_monthly_rows':int(manifest.loc[manifest.Frequency.eq('Month'),'Rows'].sum()),
            'hs4_quarterly_rows':int(manifest.loc[manifest.Frequency.eq('Quarter'),'Rows'].sum()),
            'group_monthly_rows':len(gm),'group_quarterly_rows':len(gq),
            'all_input_files_unchanged':True,'all_partition_sums_match_source':True,
            'quarter_requires_three_months':True,'zero_to_missing_conversion':False,
            'missing_to_zero_conversion':False,'unknown_groups_retained':True,
            'max_HS_vs_official_abs_pct':float(rec.HS_vs_Official_Difference_pct.abs().max()),
            'ready_group_quarters_by_class':gq.groupby('Commodity_Class').Ready_NARDL_CPI_Group.sum().astype(int).to_dict(),
            'source_hashes':initial_hash,'quarter_anchor':anchor,
            'limits':['Not a claim of full HS temporal harmonisation','Group shares cover ten partners, not world',
                      'Ready flags indicate variable availability only','HS4 ambiguous codes need HS6 or revision confirmation']}
        (stage/'HS4_Classified_Validation_Report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
        # All staged files belong to this script; never delete/move source folders.
        for p in sorted(stage.rglob('*')):
            if p.is_file():
                dest=MID/p.relative_to(stage);dest.parent.mkdir(parents=True,exist_ok=True);p.replace(dest)
        print(json.dumps({k:v for k,v in report.items() if k!='source_hashes'},indent=2),flush=True)
        print(shares.to_string(index=False),flush=True)

if __name__=='__main__':main()
