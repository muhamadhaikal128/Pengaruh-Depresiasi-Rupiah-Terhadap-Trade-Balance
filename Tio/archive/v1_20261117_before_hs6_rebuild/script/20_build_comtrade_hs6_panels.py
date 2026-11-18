"""Build audited HS6 panels without replacing existing Trade Map/GEM datasets.

Raw responses are immutable; frequency, HS edition, quantity units and coverage
are explicit. Product-month absence is not automatically converted into zero.
"""
from pathlib import Path
import csv
import gzip
import hashlib
import io
import json
import math
import numpy as np
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'input/raw/un_comtrade_hs6_20261117'
OUT=ROOT/'intermediate/comtrade_hs6'
AUDIT=ROOT/'output/diagnostics/comtrade_hs6'
YEARS={'H0':1992,'H1':1996,'H2':2002,'H3':2007,'H4':2012,'H5':2017,'H6':2022}

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def csvout(df,path):
    path.parent.mkdir(parents=True,exist_ok=True)
    df.to_csv(path,index=False,float_format='%.17g',encoding='utf-8',
              compression={'method':'gzip','compresslevel':3} if path.name.endswith('.gz') else None)
def readraw(name,record):
    p=RAW/name
    assert sha(p)==record['file_sha256'],name
    with gzip.open(p,'rb') as f:blob=f.read()
    assert hashlib.sha256(blob).hexdigest()==record['response_sha256'],name
    if name.endswith('.csv.gz'):
        d=pd.read_csv(io.BytesIO(blob),dtype={'cmdCode':str,'period':str},encoding='utf-8-sig')
    else:d=pd.DataFrame(json.loads(blob)['data'])
    assert len(d)==record['records'],name
    return d

def boolcol(d,name):
    if name not in d:return pd.Series(False,index=d.index)
    return d[name].astype(str).str.lower().isin(['true','1'])

def hs6_classification():
    p=ROOT/'intermediate/HS6_SITC3_Commodity_Crosswalk.csv'
    d=pd.read_csv(p,dtype={'HS6':str,'SITC3':str})
    def consensus(v):
        values=set(v.dropna());return next(iter(values)) if len(values)==1 else 'mixed' if values else 'unclassified'
    g=d.groupby(['HS_Edition','HS6'],sort=True)
    result=g.agg(Commodity_Class=('Commodity_Class',consensus),
        SITC3_Possible=('SITC3',lambda v:';'.join(sorted(set(v)))),
        Commodity_Subgroups=('Commodity_Subgroup',lambda v:';'.join(sorted(set(v))))).reset_index()
    result=result.rename(columns={'HS_Edition':'HS_Edition_Year'})
    result['Commodity_Flag']=result.Commodity_Class.map({'commodity':1,'noncommodity':0}).astype('Int64')
    assert not result.duplicated(['HS_Edition_Year','HS6']).any()
    # Anchor classifications check the underlying definition independently of data size.
    for year in [2012,2017,2022]:
        assert result[(result.HS_Edition_Year.eq(year)) & result.HS6.str.startswith('2701')].Commodity_Class.eq('commodity').all()
        assert result[(result.HS_Edition_Year.eq(year)) & result.HS6.str.startswith('8703')].Commodity_Class.eq('noncommodity').all()
    csvout(result,OUT/'HS6_Commodity_Classification_By_Edition.csv')
    return result

def normalize(d,name,mapping,cross,hs6=True):
    d=d.copy();d.columns=[str(c).strip('\ufeff') for c in d.columns]
    for col in ['reporterCode','partnerCode','partner2Code','motCode']:
        d[col]=pd.to_numeric(d[col],errors='raise').astype(int)
    assert d.reporterCode.eq(360).all(),name
    assert set(d.partnerCode)<=set(mapping),name
    assert d.partner2Code.eq(0).all() and d.motCode.eq(0).all(),name
    assert d.customsCode.eq('C00').all() and set(d.flowCode)<=set(['X','M']),name
    assert boolcol(d,'isOriginalClassification').all(),name
    hs=d.cmdCode.astype(str)
    assert hs.str.fullmatch(r'\d{6}').all() if hs6 else hs.eq('TOTAL').all(),name
    keys=['period','partnerCode','flowCode','classificationCode','cmdCode']
    assert not d.duplicated(keys).any(),('Duplicate source key',name)
    n=pd.DataFrame({'Period':d.period.astype(str),'ISO3':d.partnerCode.map(mapping),
        'Partner_Code':d.partnerCode,'Flow':d.flowCode,'HS_Edition':d.classificationCode,
        'HS6':hs,'HS_Edition_Year':d.classificationCode.map(YEARS),
        'Source_File':name,'Original_HS_Classification':True})
    assert n.HS_Edition_Year.notna().all(),name
    rename={'primaryValue':'Trade_Value_USD','fobvalue':'FOB_Value_USD','cifvalue':'CIF_Value_USD',
        'netWgt':'Net_Weight_kg','qty':'Quantity','qtyUnitCode':'Quantity_Unit_Code',
        'altQty':'Alt_Quantity','altQtyUnitCode':'Alt_Quantity_Unit_Code'}
    for source,dest in rename.items():n[dest]=pd.to_numeric(d[source],errors='coerce') if source in d else np.nan
    for source,dest in [('isNetWgtEstimated','Net_Weight_Estimated'),('isQtyEstimated','Quantity_Estimated'),
        ('isAltQtyEstimated','Alt_Quantity_Estimated'),('isReported','Is_Reported'),('isAggregate','Is_Aggregate')]:
        n[dest]=boolcol(d,source)
    assert n.Trade_Value_USD.notna().all() and n.Trade_Value_USD.ge(0).all(),name
    n['Trade_Value_USDk']=n.Trade_Value_USD/1000
    n['Weight_Usable']=n.Net_Weight_kg.gt(0)&n.Trade_Value_USD.ge(0)
    n['Quantity_Usable']=n.Quantity.gt(0)&n.Quantity_Unit_Code.gt(0)
    n['Positive_Value_Without_Positive_Weight']=n.Trade_Value_USD.gt(0)&~n.Net_Weight_kg.gt(0)
    n['Unit_Value_USD_per_kg']=n.Trade_Value_USD.div(n.Net_Weight_kg.where(n.Weight_Usable))
    n['Unit_Value_USD_per_Quantity']=n.Trade_Value_USD.div(n.Quantity.where(n.Quantity_Usable))
    if hs6:
        n['HS4_Parent']=n.HS6.str[:4]
        n=n.merge(cross,on=['HS_Edition_Year','HS6'],how='left',validate='many_to_one')
        n['Commodity_Class']=n.Commodity_Class.fillna('unclassified')
        n['Commodity_Flag']=n.Commodity_Class.map({'commodity':1,'noncommodity':0}).astype('Int64')
    return n

def macro_sources():
    pm=pd.read_csv(ROOT/'intermediate/Panel_Country_Month.csv')
    pq=pd.read_csv(ROOT/'intermediate/Panel_Country_Quarter.csv')
    worldq=pd.read_csv(ROOT/'intermediate/Panel_World_Quarter.csv')
    common=pd.read_csv(ROOT/'intermediate/Macro_Monthly.csv')
    # Monthly panels include only monthly FX/prices/commodity controls, never pseudo-monthly GDP.
    cols=['ISO3','Date']+[c for c in pm if c.startswith(('NER_','RER_','REER_','CPI_','Partner_CPI_','IDR_per_','CMD_','Price_Index_'))]
    macro_m=pm[cols].copy()
    world_m=common[['Date']+[c for c in common if c.startswith(('REER_','CPI_','IDR_per_','CMD_'))]].copy()
    world_m['ISO3']='WLD';macro_m=pd.concat([macro_m,world_m],ignore_index=True)
    cols=['ISO3','Quarter']+[c for c in pq if c.startswith(('NER_','RER_','REER_','CPI_','Partner_','IDN_','CMD_','Uses_WPI'))]
    macro_q=pq[cols].copy()
    wcols=['Quarter']+[c for c in worldq if c.startswith(('IDN_','REER_','Foreign_Activity_','CMD_'))]
    world_q=worldq[wcols].copy();world_q['ISO3']='WLD'
    macro_q=pd.concat([macro_q,world_q],ignore_index=True)
    assert not macro_m.duplicated(['ISO3','Date']).any()
    assert not macro_q.duplicated(['ISO3','Quarter']).any()
    old=pm[['ISO3','Date','Exports_USDk','Imports_USDk']].copy()
    old_world=common[['Date','World_Exports_USDk','World_Imports_USDk']].rename(columns={
        'World_Exports_USDk':'Exports_USDk','World_Imports_USDk':'Imports_USDk'})
    old_world['ISO3']='WLD'
    return macro_m,macro_q,pd.concat([old,old_world],ignore_index=True)

def quarterly(m,calendar_months):
    keys=['ISO3','HS_Edition','HS_Edition_Year','HS6','Flow','Quarter']
    groups=m.groupby(keys,sort=True,dropna=False)
    q=groups.agg(NMonths_Source_Rows=('Period','nunique'),
        Quantity_Unit_Count=('Quantity_Unit_Code','nunique'),Quantity_Unit_Code=('Quantity_Unit_Code','first'),
        NMonths_Usable_Weight=('Weight_Usable','sum'),NMonths_Usable_Quantity=('Quantity_Usable','sum'),
        Net_Weight_Estimated_Any=('Net_Weight_Estimated','max'),Quantity_Estimated_Any=('Quantity_Estimated','max'),
        Commodity_Class=('Commodity_Class','first'),HS4_Parent=('HS4_Parent','first')).reset_index()
    sums=groups[['Trade_Value_USD','Net_Weight_kg','Quantity']].sum(min_count=1).rename(columns={
        'Trade_Value_USD':'Observed_Trade_Value_USD','Net_Weight_kg':'Observed_Net_Weight_kg',
        'Quantity':'Observed_Quantity'}).reset_index()
    q=q.merge(sums,on=keys,validate='one_to_one')
    q['NMonths_Dataset_Available']=calendar_months
    q['Complete_Product_Quarter']=q.NMonths_Source_Rows.eq(3)&(calendar_months==3)
    q['Trade_Value_USD']=q.Observed_Trade_Value_USD.where(q.Complete_Product_Quarter)
    q['Trade_Value_USDk']=q.Trade_Value_USD/1000
    q['Net_Weight_kg']=q.Observed_Net_Weight_kg.where(q.Complete_Product_Quarter&q.NMonths_Usable_Weight.eq(3))
    q['Quantity']=q.Observed_Quantity.where(q.Complete_Product_Quarter&q.NMonths_Usable_Quantity.eq(3)&q.Quantity_Unit_Count.eq(1))
    q['Unit_Value_USD_per_kg']=q.Trade_Value_USD/q.Net_Weight_kg.where(q.Net_Weight_kg.gt(0))
    q['Unit_Value_USD_per_Quantity']=q.Trade_Value_USD/q.Quantity.where(q.Quantity.gt(0))
    q['Commodity_Flag']=q.Commodity_Class.map({'commodity':1,'noncommodity':0}).astype('Int64')
    assert q.loc[~q.Complete_Product_Quarter,'Trade_Value_USD'].isna().all()
    assert q.loc[q.Quantity_Unit_Count.ne(1),'Quantity'].isna().all()
    return q

def twoflow(q,macro):
    keys=['ISO3','HS_Edition','HS_Edition_Year','HS6','Quarter','Commodity_Class','HS4_Parent']
    values=['Trade_Value_USD','Trade_Value_USDk','Net_Weight_kg','Quantity','Quantity_Unit_Code',
        'Unit_Value_USD_per_kg','NMonths_Source_Rows','Complete_Product_Quarter']
    ex=q[q.Flow.eq('X')][keys+values].rename(columns={c:'Export_'+c for c in values})
    im=q[q.Flow.eq('M')][keys+values].rename(columns={c:'Import_'+c for c in values})
    out=ex.merge(im,on=keys,how='outer',validate='one_to_one')
    out['Trade_Balance_USD']=out.Export_Trade_Value_USD-out.Import_Trade_Value_USD
    positive=out.Export_Trade_Value_USD.gt(0)&out.Import_Trade_Value_USD.gt(0)
    out['Ln_Imports_Exports']=np.log(out.Import_Trade_Value_USD.where(positive)/out.Export_Trade_Value_USD.where(positive))
    out=out.merge(macro,on=['ISO3','Quarter'],how='left',validate='many_to_one')
    foreign=out.Partner_GDP_Real_Index_2015mean100.where(out.ISO3.ne('WLD'),out.Foreign_Activity_Top10_FixedWeight_Index)
    rer=out.RER_Bilateral_Index_2015mean100.where(out.ISO3.ne('WLD'),out.REER_BIS_broad)
    out['Macro_Controls_Available']=out.IDN_GDP_Real_Index_2015mean100.gt(0)&foreign.gt(0)&rer.gt(0)
    out['Positive_Both_Flows_With_Macro']=positive&out.Macro_Controls_Available
    # This flag is data availability only, not a unit-root/cointegration certificate.
    return out

def quality(d,key):
    w=d.assign(_v=d.Trade_Value_USD.where(d.Weight_Usable,0),_e=d.Trade_Value_USD.where(d.Net_Weight_Estimated,0))
    res=w.groupby(['ISO3',key,'Flow','HS_Edition'],dropna=False).agg(
        Product_Rows=('HS6','size'),HS6_Codes=('HS6','nunique'),Trade_Value_USD=('Trade_Value_USD','sum'),
        Positive_Weight_Rows=('Weight_Usable','sum'),Estimated_Weight_Rows=('Net_Weight_Estimated','sum'),
        Usable_Quantity_Rows=('Quantity_Usable','sum'),Estimated_Quantity_Rows=('Quantity_Estimated','sum'),
        Value_With_Weight_USD=('_v','sum'),Value_Estimated_Weight_USD=('_e','sum'),
        Positive_Value_Without_Weight_Rows=('Positive_Value_Without_Positive_Weight','sum')).reset_index()
    res['Weight_Value_Coverage_pct']=100*res.Value_With_Weight_USD/res.Trade_Value_USD.where(res.Trade_Value_USD.gt(0))
    return res

def main():
    for p in [OUT,AUDIT,OUT/'monthly',OUT/'quarterly',OUT/'annual']:p.mkdir(parents=True,exist_ok=True)
    manifest=json.loads((RAW/'download_manifest.json').read_text(encoding='utf-8'))
    assert manifest.get('download_status')=='complete','Finish/resume script 19 before building final panels'
    for name,rec in manifest['files'].items():
        assert sha(RAW/name)==rec['file_sha256'],name
    protected=[ROOT/'intermediate'/n for n in ['Panel_Country_Month.csv','Panel_Country_Quarter.csv','Panel_World_Quarter.csv','HS6_SITC3_Commodity_Crosswalk.csv']]
    before={str(p.relative_to(ROOT)):sha(p) for p in protected}
    mapping={int(v):k for k,v in manifest['partners'].items()}
    cross=hs6_classification();macro_m,macro_q,old_pm=macro_sources()
    file_index=[];monthly_sums=[];annual_sums=[];qualities=[];monthly_classes=[];missing_code_counts=[]
    files=manifest['files'];month_files={}
    for name,rec in files.items():
        if name.startswith('monthly_') and '_hs6.' in name:
            month_files[int(name.split('_')[1])]=(name,rec)
    assert sorted(month_files)==manifest['available_months']
    byquarter={}
    for period in sorted(month_files):
        quarter=str(pd.Period(str(period),freq='M').asfreq('Q'))
        byquarter.setdefault(quarter,[]).append(period)
    for quarter,periods in byquarter.items():
        frames=[]
        for period in periods:
            name,rec=month_files[period];raw=readraw(name,rec);n=normalize(raw,name,mapping,cross)
            n['Date']=pd.to_datetime(n.Period,format='%Y%m').dt.strftime('%Y-%m');n['Quarter']=quarter
            frames.append(n)
        m=pd.concat(frames,ignore_index=True)
        assert not m.duplicated(['ISO3','Period','HS_Edition','HS6','Flow']).any()
        sums=m.groupby(['ISO3','Period','Flow']).Trade_Value_USD.sum().reset_index();monthly_sums.append(sums)
        qualities.append(quality(m,'Period'))
        cs=m.groupby(['ISO3','Period','Flow','Commodity_Class']).Trade_Value_USD.sum().reset_index();monthly_classes.append(cs)
        mm=m.merge(macro_m,on=['ISO3','Date'],how='left',validate='many_to_one')
        assert len(mm)==len(m)
        mp=OUT/'monthly'/f'HS6_{quarter}_Month.csv.gz';csvout(mm,mp)
        q=quarterly(m,len(periods));qq=twoflow(q,macro_q)
        qp=OUT/'quarterly'/f'HS6_{quarter}_Quarter_Long.csv.gz';csvout(q,qp)
        wp=OUT/'quarterly'/f'HS6_{quarter}_Quarter_TwoFlow_Macro.csv.gz';csvout(qq,wp)
        for p,df,freq in [(mp,mm,'M'),(qp,q,'Q-long'),(wp,qq,'Q-twoflow-macro')]:
            file_index.append({'File':str(p.relative_to(ROOT)),'Frequency':freq,'Period':quarter,'Rows':len(df),'SHA256':sha(p)})
        print('BUILT_QUARTER',quarter,'months',len(periods),'monthly_rows',len(m),'quarter_rows',len(q),'twoflow_rows',len(qq),flush=True)
    # Annual data remain annual and retain their source-specific quantity units.
    for year in manifest['available_years']:
        frames=[]
        for flow in ['X','M']:
            candidates=[(n,r) for n,r in files.items() if n.startswith(f'annual_{year}_{flow}_hs6.')]
            assert len(candidates)==1,(year,flow)
            name,rec=candidates[0];frames.append(normalize(readraw(name,rec),name,mapping,cross))
        a=pd.concat(frames,ignore_index=True);a['Year']=int(year)
        p=OUT/'annual'/f'HS6_{year}_Annual.csv.gz';csvout(a,p)
        annual_sums.append(a.groupby(['ISO3','Period','Flow']).Trade_Value_USD.sum().reset_index())
        aq=quality(a,'Period');aq['Frequency']='A';qualities.append(aq)
        file_index.append({'File':str(p.relative_to(ROOT)),'Frequency':'A','Period':str(year),'Rows':len(a),'SHA256':sha(p)})
        print('BUILT_YEAR',year,'rows',len(a),flush=True)
    monthly=pd.concat(monthly_sums,ignore_index=True);annual=pd.concat(annual_sums,ignore_index=True)
    controls=[]
    for name,rec in files.items():
        if name.startswith('totals_'):
            v=normalize(readraw(name,rec),name,mapping,cross,False)
            v['Frequency']=name.split('_')[1]
            controls.append(v[['ISO3','Period','Flow','Frequency','Trade_Value_USD']])
    control=pd.concat(controls,ignore_index=True).rename(columns={'Trade_Value_USD':'TOTAL_Control_USD'})
    assert not control.duplicated(['ISO3','Period','Flow','Frequency']).any()
    sums=pd.concat([monthly.assign(Frequency='M'),annual.assign(Frequency='A')],ignore_index=True).rename(columns={'Trade_Value_USD':'HS6_Sum_USD'})
    # Normalize period types for the JSON and CSV source formats.
    for z in [control,sums]:z['Period']=z.Period.astype(str)
    reconciliation=sums.merge(control,on=['ISO3','Period','Flow','Frequency'],how='outer',validate='one_to_one',indicator=True)
    assert reconciliation._merge.eq('both').all(),'Missing TOTAL control or detail records'
    reconciliation['Difference_USD']=reconciliation.HS6_Sum_USD-reconciliation.TOTAL_Control_USD
    reconciliation['Difference_pct']=100*reconciliation.Difference_USD/reconciliation.TOTAL_Control_USD.where(reconciliation.TOTAL_Control_USD.ne(0))
    reconciliation['Within_0p01pct']=reconciliation.Difference_pct.abs().le(.01)
    csvout(reconciliation,AUDIT/'HS6_vs_TOTAL_reconciliation.csv')
    # Compare to the previous series without overwriting or rescaling either one.
    pivot=control[control.Frequency.eq('M')].pivot(index=['ISO3','Period'],columns='Flow',values='TOTAL_Control_USD').reset_index()
    pivot['Date']=pd.to_datetime(pivot.Period,format='%Y%m').dt.strftime('%Y-%m')
    old=old_pm[['ISO3','Date','Exports_USDk','Imports_USDk']]
    comparison=pivot.merge(old,on=['ISO3','Date'],how='left',validate='one_to_one')
    for flow,col in [('X','Exports'),('M','Imports')]:
        comparison[col+'_Comtrade_USD']=comparison[flow]
        comparison[col+'_Previous_USD']=comparison[col+'_USDk']*1000
        comparison[col+'_Difference_pct']=100*(comparison[flow]-comparison[col+'_Previous_USD'])/comparison[col+'_Previous_USD'].where(comparison[col+'_Previous_USD'].ne(0))
    csvout(comparison,AUDIT/'Comtrade_vs_previous_bilateral_monthly.csv')
    # Publish the same-source aggregate controls for future aggregate/bilateral models.
    totals_m=pivot[['ISO3','Date','X','M']].rename(columns={'X':'Exports_USD','M':'Imports_USD'})
    totals_m['Quarter']=pd.PeriodIndex(totals_m.Date,freq='M').asfreq('Q').astype(str)
    totals_m['Trade_Balance_USD']=totals_m.Exports_USD-totals_m.Imports_USD
    csvout(totals_m.merge(macro_m,on=['ISO3','Date'],how='left',validate='one_to_one'),OUT/'Trade_Total_Month_Macro.csv')
    gr=totals_m.groupby(['ISO3','Quarter'])
    totals_q=gr[['Exports_USD','Imports_USD']].sum(min_count=3).reset_index()
    counts=gr.Date.nunique().rename('NMonths_Available').reset_index()
    totals_q=totals_q.merge(counts,on=['ISO3','Quarter'],validate='one_to_one')
    totals_q['Trade_Balance_USD']=totals_q.Exports_USD-totals_q.Imports_USD
    positive=totals_q.Exports_USD.gt(0)&totals_q.Imports_USD.gt(0)
    totals_q['Ln_Imports_Exports']=np.log(totals_q.Imports_USD.where(positive)/totals_q.Exports_USD.where(positive))
    totals_q=totals_q.merge(macro_q,on=['ISO3','Quarter'],how='left',validate='one_to_one')
    csvout(totals_q,OUT/'Trade_Total_Quarter_Macro.csv')
    totals_a=control[control.Frequency.eq('A')].pivot(index=['ISO3','Period'],columns='Flow',values='TOTAL_Control_USD').reset_index()
    totals_a=totals_a.rename(columns={'Period':'Year','X':'Exports_USD','M':'Imports_USD'})
    totals_a['Year']=totals_a.Year.astype(int);totals_a['Trade_Balance_USD']=totals_a.Exports_USD-totals_a.Imports_USD
    csvout(totals_a,OUT/'Trade_Total_Annual.csv')
    old_world=old_pm[old_pm.ISO3.eq('WLD')].copy();old_world['Year']=old_world.Date.str[:4].astype(int)
    old_world=old_world.groupby('Year')[['Exports_USDk','Imports_USDk']].sum(min_count=12)*1000
    old_world=old_world.rename(columns={'Exports_USDk':'Exports_Previous_GEM_USD','Imports_USDk':'Imports_Previous_GEM_USD'})
    world_a=totals_a[totals_a.ISO3.eq('WLD')].merge(old_world,on='Year',how='left',validate='one_to_one')
    for stem in ['Exports','Imports']:
        oldcol=stem+'_Previous_GEM_USD'
        world_a[stem+'_Difference_pct']=100*(world_a[stem+'_USD']-world_a[oldcol])/world_a[oldcol].where(world_a[oldcol].ne(0))
    csvout(world_a,AUDIT/'Comtrade_vs_previous_world_annual.csv')
    # Annual vs monthly conservation is meaningful only for 12 available months.
    monthly['Year']=monthly.Period.str[:4].astype(int)
    yearly=monthly.groupby(['ISO3','Year','Flow']).agg(Months_Available=('Period','nunique'),Monthly_Sum_USD=('Trade_Value_USD','sum')).reset_index()
    aa=annual.copy();aa['Year']=aa.Period.astype(int);aa=aa.rename(columns={'Trade_Value_USD':'Annual_HS6_USD'})
    ay=aa.merge(yearly,on=['ISO3','Year','Flow'],how='left',validate='one_to_one')
    ay['Annual_vs_Monthly_pct']=100*(ay.Monthly_Sum_USD-ay.Annual_HS6_USD)/ay.Annual_HS6_USD.where(ay.Annual_HS6_USD.ne(0))
    ay['Comparable_12_Months']=ay.Months_Available.eq(12)
    csvout(ay,AUDIT/'Annual_vs_monthly_HS6_sums.csv')
    qual=pd.concat(qualities,ignore_index=True);qual['Frequency']=qual.Frequency.fillna('M')
    csvout(qual,AUDIT/'Weight_quantity_coverage.csv')
    classes=pd.concat(monthly_classes,ignore_index=True);csvout(classes,OUT/'Commodity_Group_Month_Observed_Values.csv')
    index=pd.DataFrame(file_index);csvout(index,OUT/'File_Index.csv')
    allperiods=pd.period_range('2006-01','2026-10',freq='M')
    calendar=pd.DataFrame({'Date':allperiods.astype(str),'Period':[int(p.strftime('%Y%m')) for p in allperiods]})
    calendar['Available_In_Comtrade_Metadata']=calendar.Period.isin(manifest['available_months'])
    csvout(calendar,AUDIT/'Monthly_availability_calendar.csv')
    after={str(p.relative_to(ROOT)):sha(p) for p in protected};assert before==after
    wq=qual[qual.Frequency.eq('M')&qual.ISO3.eq('WLD')]
    overall_weight=100*wq.Value_With_Weight_USD.sum()/wq.Trade_Value_USD.sum()
    report={'status':'PASS_WITH_DATA_LIMITATIONS','raw_files_verified':len(files),
        'download_status':manifest['download_status'],'monthly_periods':len(manifest['available_months']),
        'first_month':min(manifest['available_months']),'last_month':max(manifest['available_months']),
        'annual_first':min(manifest['available_years']),'annual_last':max(manifest['available_years']),
        'monthly_rows':int(index[index.Frequency.eq('M')].Rows.sum()),
        'quarterly_long_rows':int(index[index.Frequency.eq('Q-long')].Rows.sum()),
        'quarterly_twoflow_rows':int(index[index.Frequency.eq('Q-twoflow-macro')].Rows.sum()),
        'annual_rows':int(index[index.Frequency.eq('A')].Rows.sum()),
        'world_monthly_value_with_positive_weight_pct':overall_weight,
        'max_abs_HS6_vs_TOTAL_pct':float(reconciliation.Difference_pct.abs().max()),
        'HS6_vs_TOTAL_rows_over_0p01pct':int((~reconciliation.Within_0p01pct).sum()),
        'original_panels_unchanged':before==after,'original_panel_sha256':before,
        'hs_revision_harmonized':False,'native_HS_edition_retained':True,
        'annual_data_disaggregated':False,'absent_product_months_filled_zero':False,
        'quarterly_completeness':'Three actual product-month rows; no gaps compressed',
        'quantity_aggregation':'Only same quantity unit within the same HS edition/product/partner/flow',
        'classification':'UNCTAD A11 via edition-specific HS6-SITC3 crosswalk; ambiguous classes retained',
        'macro_source':'Existing audited macro panels; previous limitations remain',
        'models_reestimated':False}
    (AUDIT/'Validation_Report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    (OUT/'README.md').write_text('''# UN Comtrade HS-6 panels

This is a separate data source. Existing Trade Map, GEM, model results and presentation are unchanged.

- `monthly/`: monthly long panels, partitioned by quarter, including monthly macro/price controls.
- `quarterly/*_Long.csv.gz`: strict quarter totals, quantities and coverage flags.
- `quarterly/*_TwoFlow_Macro.csv.gz`: exports/imports joined with quarterly GDP, FX, CPI and commodity controls.
- `annual/`: supplementary annual data beginning 2006. These are never disaggregated to months.
- `HS6_Commodity_Classification_By_Edition.csv`: direct HS6-SITC3 UNCTAD A11 classification.
- `File_Index.csv`: row counts and checksums. All CSV.GZ files can be read by pandas with compression inferred.

Values are current USD; USDk columns divide by 1,000. Reporter is Indonesia; partners include the ten research partners and World. Comtrade India=699; USA trade area=842 includes Puerto Rico and US Virgin Islands. Native HS edition is part of every product key. No temporal HS harmonisation is asserted.

Monthly source absence is not silently treated as zero. Quarter `Observed_*` fields sum available rows; strict `Trade_Value_USD` requires three actual product-month rows. Weight/quantity also require usable source values and consistent units. Missing or zero denominators never yield unit values. Unit values are not pure price indexes; quality/composition can change. No total-weight price index across dissimilar products is constructed.

Quarterly macro availability flags are not estimation eligibility certificates. Unit-root, cointegration, common support, identification and multiple testing require further work. Existing macro audit caveats remain. Annual files are kept annual and have no fabricated quarterly GDP. Diagnostics and provenance are in `output/diagnostics/comtrade_hs6/` and the raw download manifest.
''',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2),flush=True)

if __name__=='__main__':main()
