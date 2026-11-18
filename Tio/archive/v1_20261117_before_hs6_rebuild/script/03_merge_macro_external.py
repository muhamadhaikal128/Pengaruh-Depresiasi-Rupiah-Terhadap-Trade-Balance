"""Build monthly/quarterly research data from saved source files, offline.

Dependencies: pandas, numpy, openpyxl. Run from any directory.
Quarterly GDP appears only in quarter-end months of the monthly panel.
No GDP interpolation, extrapolation or forecast substitution is performed.
"""
from pathlib import Path
import csv
import io
import json
import re
import shutil
import zipfile
import hashlib
from datetime import datetime, timezone
import numpy as np
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.utils.dataframe import dataframe_to_rows

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT/'input/raw/macro_external_20261117'
MID = ROOT/'intermediate'
BASE = RAW/'baseline_before_merge'
ISO = {'ID':'IDN','CN':'CHN','US':'USA','SG':'SGP','JP':'JPN','MY':'MYS',
       'IN':'IND','KR':'KOR','TH':'THA','VN':'VNM','AU':'AUS'}
MONTHS = pd.period_range('2006-01','2026-10',freq='M').astype(str)
MANIFEST = {r['label']:r for r in json.loads((RAW/'download_manifest.json').read_text('utf-8'))}

def source(label):
    r=MANIFEST[label]
    if r.get('status')!=200:
        raise ValueError(f'Source failed: {label}')
    p=ROOT/r['path'].replace('\\','/')
    assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256'], label
    return p

def gem(label,frequency):
    d=json.loads(source(label).read_text('utf-8'))
    assert d['pages']==1, 'Truncated API response'
    rows=[]
    for r in d['source']['data']:
        v={x['concept']:x['id'] for x in r['variable']}
        t=v['Time']
        if r['value'] is not None and re.fullmatch(r'\d{4}'+frequency+r'\d{1,2}',t):
            date=(t[:4]+'-'+t[5:].zfill(2)) if frequency=='M' else t
            rows.append({'ISO3':v['Country'],'Date':date,'Value':float(r['value'])})
    out=pd.DataFrame(rows)
    assert not out.duplicated(['ISO3','Date']).any(),label
    return out

def bis(label,filter_dict):
    z=zipfile.ZipFile(source(label)); assert len(z.namelist())==1
    rows=[]
    with io.TextIOWrapper(z.open(z.namelist()[0]),encoding='utf-8-sig') as f:
        for r in csv.DictReader(f):
            if r['REF_AREA'] not in ISO or not all(r.get(k)==v for k,v in filter_dict.items()):
                continue
            for t,val in r.items():
                if t and re.fullmatch(r'\d{4}-\d{2}',t) and val and t in MONTHS:
                    # UNIT_MULT is the SDMX decimal scale, not a currency quote inversion.
                    mult=int(r.get('UNIT_MULT') or 0)
                    rows.append({'ISO3':ISO[r['REF_AREA']],'Date':t,
                                 'Value':float(val)*10**mult,
                                 'Series':r.get('Series'), 'Currency':r.get('CURRENCY','')})
    out=pd.DataFrame(rows)
    assert not out.duplicated(['ISO3','Date']).any(),label
    return out

def index2015(g,value):
    base=g.loc[g['Date'].str.startswith('2015'),value]
    assert base.notna().sum() in (4,12), (g['ISO3'].iloc[0],len(base))
    return g[value]/base.mean()*100

def write(df,name):
    p=MID/name; temp=p.with_suffix(p.suffix+'.tmp')
    df.to_csv(temp,index=False,float_format='%.12g',encoding='utf-8')
    temp.replace(p)

def add_ratios(df,x,m,prefix=''):
    df[prefix+'Trade_Balance_USDk']=df[x]-df[m]
    df[prefix+'Total_Trade_USDk']=df[x]+df[m]
    valid=(df[x]>0)&(df[m]>0)
    df[prefix+'Ln_Exports_Imports']=np.log(df[x].where(valid)/df[m].where(valid))
    df[prefix+'Ln_Imports_Exports']=-df[prefix+'Ln_Exports_Imports']

def main():
    BASE.mkdir(exist_ok=True)
    for name in ['Panel_Country_Month.csv','Macro_Monthly.csv','Panel_Gabungan_Indonesia.xlsx']:
        if not (BASE/name).exists():
            shutil.copy2(MID/name,BASE/name)
    panel=pd.read_csv(BASE/'Panel_Country_Month.csv',dtype={'Date':str,'ISO3':str})
    old_cols=panel.columns.tolist()
    macro=pd.read_csv(BASE/'Macro_Monthly.csv',dtype={'Date':str})
    # Refuse to silently discard edits made to legacy values after the snapshot.
    current=pd.read_csv(MID/'Panel_Country_Month.csv')
    pd.testing.assert_frame_equal(current[old_cols],panel,check_dtype=False,
                                  check_exact=False,rtol=1e-10,atol=1e-8)
    assert not panel.duplicated(['ISO3','Date']).any()

    # GDP: use one harmonised World Bank GEM SA-level family for all 11 countries.
    # Source-native level/scale is retained; rebased index is the analysis variable.
    gdp=gem('wb_gem_gdp_real_all','Q').rename(columns={'Date':'Quarter','Value':'GDP_Real_Level_SourceUnits'})
    gdp=gdp[gdp['Quarter'].between('2006Q1','2026Q4')].copy()
    gdp['Date']=gdp['Quarter']
    gdp['GDP_Real_Index_2015mean100']=np.nan
    for iso,g in gdp.groupby('ISO3'):
        gdp.loc[g.index,'GDP_Real_Index_2015mean100']=index2015(g,'GDP_Real_Level_SourceUnits')
    gdp=gdp.drop(columns='Date').sort_values(['ISO3','Quarter'])
    gdp['GDP_Source']='World Bank GEM / NYGDPMKTPSAKN'
    gdp['GDP_Adjustment']='SA'
    gdp['GDP_Frequency']='Q'
    # Do not splice newer national/IMF vintages into the harmonised SA family.

    cpi=bis('bis_cpi_bulk',{'FREQ':'M','UNIT_MEASURE':'628'})
    cpi=cpi.rename(columns={'Value':'Price_Index_SourceLevel','Series':'Price_Index_SourceSeries'})
    cpi['Price_Index_Source']='National sources; BIS long consumer prices'
    vn=gem('wb_gem_vnm_cpi','M')
    vn=vn[vn['Date'].isin(MONTHS)].rename(columns={'Value':'Price_Index_SourceLevel'})
    vn['Price_Index_Source']='World Bank GEM / CPTOTNSXN'
    vn['Price_Index_SourceSeries']='VNM.CPTOTNSXN'
    cpi=pd.concat([cpi,vn],ignore_index=True).drop(columns='Currency',errors='ignore')
    cpi['Price_Index_2015mean100']=np.nan
    for iso,g in cpi.groupby('ISO3'):
        cpi.loc[g.index,'Price_Index_2015mean100']=index2015(g,'Price_Index_SourceLevel')
    cpi['Price_Index_Is_WPI_Proxy']=(cpi.ISO3.eq('IND')&cpi.Date.lt('2013-01'))
    cpi['Price_Index_SourceInterpolated_FromQuarterly']=cpi.ISO3.eq('AUS')
    cpi['CPI_Index_2015mean100']=cpi.Price_Index_2015mean100.mask(cpi.Price_Index_Is_WPI_Proxy)
    assert not cpi.duplicated(['ISO3','Date']).any()

    fx=bis('bis_fx_bulk',{'FREQ':'M','COLLECTION':'A'}).rename(
        columns={'Value':'LCU_per_USD','Series':'FX_SourceSeries'})
    fx['FX_Source']='BIS WS_XRU; period average'
    # Audit: BIS and GEM VND rate concepts differ materially. Do not splice a
    # single GEM observation into the BIS series; retain the missing month.
    assert set(ISO.values())==set(fx.ISO3)
    prices_fx=fx.merge(cpi,on=['ISO3','Date'],how='outer',validate='one_to_one')
    domestic=prices_fx[prices_fx.ISO3.eq('IDN')][['Date','LCU_per_USD','CPI_Index_2015mean100']].rename(
        columns={'LCU_per_USD':'IDR_per_USD_BIS','CPI_Index_2015mean100':'CPI_IDN_Index_2015mean100'})
    bilat=prices_fx[~prices_fx.ISO3.eq('IDN')].merge(domestic,on='Date',validate='many_to_one')
    bilat['NER_IDR_per_PartnerCurrency']=bilat.IDR_per_USD_BIS/bilat.LCU_per_USD
    bilat['RER_Bilateral_Level']=bilat.NER_IDR_per_PartnerCurrency*bilat.CPI_Index_2015mean100/bilat.CPI_IDN_Index_2015mean100
    bilat['RER_With_WPI_Proxy_Level']=bilat.NER_IDR_per_PartnerCurrency*bilat.Price_Index_2015mean100/bilat.CPI_IDN_Index_2015mean100
    for level,idx in [('RER_Bilateral_Level','RER_Bilateral_Index_2015mean100'),
                      ('RER_With_WPI_Proxy_Level','RER_With_WPI_Proxy_Index_2015mean100')]:
        bilat[idx]=np.nan
        for iso,g in bilat.groupby('ISO3'):
            bilat.loc[g.index,idx]=index2015(g,level)
    bilat=bilat.sort_values(['ISO3','Date'])

    # Prefer explicitly customs-based GEM merchandise totals to match HS trade.
    # IMF/FRED is retained separately: historical discrepancies are not mere rounding.
    world=pd.DataFrame({'Date':MONTHS})
    for sid,col in [('VALEXPIDM052N','World_Exports_IMFFRED_USDk'),('VALIMPIDM052N','World_Imports_IMFFRED_USDk')]:
        x=pd.read_csv(source(sid)); x.columns=['Date',col]
        x['Date']=x.Date.str[:7]; x[col]=pd.to_numeric(x[col],errors='coerce')*1000
        world=world.merge(x,on='Date',how='left',validate='one_to_one')
    world['World_Trade_Source']='World Bank GEM customs merchandise; monthly NSA; USD millions converted to USDk'
    for label,col in [('wb_gem_idn_DXGSRMRCHNSCD','World_Exports_USDk'),
                      ('wb_gem_idn_DMGSRMRCHNSCD','World_Imports_USDk')]:
        x=gem(label,'M')[['Date','Value']].rename(columns={'Value':col}); x[col]*=1000
        world=world.merge(x,on='Date',how='left',validate='one_to_one')
    add_ratios(world,'World_Exports_USDk','World_Imports_USDk','World_')
    annual=world.assign(Year=world.Date.str[:4]).groupby('Year').agg(
        Exports_GEM_USDk=('World_Exports_USDk',lambda x:x.sum(min_count=12)),
        Imports_GEM_USDk=('World_Imports_USDk',lambda x:x.sum(min_count=12)),
        Exports_IMFFRED_USDk=('World_Exports_IMFFRED_USDk',lambda x:x.sum(min_count=12)),
        Imports_IMFFRED_USDk=('World_Imports_IMFFRED_USDk',lambda x:x.sum(min_count=12))).reset_index()
    wdi=json.loads(source('wdi_trade_annual').read_text('utf-8'))
    assert wdi[0]['pages']==1
    wr=[]
    for r in wdi[1]:
        if r['value'] is not None:
            wr.append({'Year':r['date'],'Flow':'Exports' if r['indicator']['id'].startswith('TX.') else 'Imports',
                       'Value':r['value']/1000})
    wd=pd.DataFrame(wr).pivot(index='Year',columns='Flow',values='Value').rename(
        columns={'Exports':'Exports_WDI_WTO_USDk','Imports':'Imports_WDI_WTO_USDk'}).reset_index()
    annual=annual.merge(wd,on='Year',how='left',validate='one_to_one')
    for flow in ['Exports','Imports']:
        annual[flow+'_GEM_vs_WDI_pct']=(annual[flow+'_GEM_USDk']/annual[flow+'_WDI_WTO_USDk']-1)*100

    # Keep GDP sparse at quarter-end in monthly data. This is period alignment,
    # NOT an observation publication date and not valid real-time availability.
    gm=gdp.copy(); gm['Date']=pd.PeriodIndex(gm.Quarter,freq='Q').asfreq('M',how='end').astype(str)
    gm=gm.drop(columns='Quarter')
    partner_gm=gm[~gm.ISO3.eq('IDN')].rename(columns={c:'Partner_'+c for c in gm.columns if c not in ['ISO3','Date']})
    idn_gm=gm[gm.ISO3.eq('IDN')].drop(columns='ISO3').rename(columns={c:'IDN_'+c for c in gm.columns if c!='Date'})
    bp=bilat.rename(columns={'CPI_Index_2015mean100':'Partner_CPI_Index_2015mean100'})
    panel=panel.merge(bp,on=['ISO3','Date'],how='left',validate='one_to_one')
    panel=panel.merge(partner_gm,on=['ISO3','Date'],how='left',validate='one_to_one')
    panel=panel.merge(idn_gm,on='Date',how='left',validate='many_to_one')
    panel=panel.merge(world,on='Date',how='left',validate='many_to_one')
    panel['Quarter']=pd.PeriodIndex(panel.Date,freq='M').asfreq('Q').astype(str)
    valid=(panel.Exports_USDk>0)&(panel.Imports_USDk>0)
    panel['Ln_Exports_Imports']=np.log(panel.Exports_USDk.where(valid)/panel.Imports_USDk.where(valid))
    panel['Ln_Imports_Exports']=-panel.Ln_Exports_Imports
    sums=panel.groupby('Date')[['Exports_USDk','Imports_USDk']].sum(min_count=10)
    panel=panel.merge((sums.Exports_USDk/world.set_index('Date').World_Exports_USDk).rename('Top10_Export_Coverage_World'),on='Date',how='left')
    assert panel.shape[0]==2500 and panel.columns.is_unique
    # All legacy monthly columns must be unchanged, including missing patterns.
    original=pd.read_csv(BASE/'Panel_Country_Month.csv')
    pd.testing.assert_frame_equal(panel[old_cols],original,check_dtype=False)

    macro=macro.merge(domestic,on='Date',how='left',validate='one_to_one').merge(world,on='Date',how='left',validate='one_to_one')
    macro=macro.merge(idn_gm,on='Date',how='left',validate='one_to_one')
    quarterly=[]
    for (iso,q),g in panel.groupby(['ISO3','Quarter'],sort=True):
        r={'ISO3':iso,'Country':g.Country.iloc[0],'Quarter':q,
           'Trade_Months_Observed':int((g.Exports_USDk.notna()&g.Imports_USDk.notna()).sum())}
        for col in ['Exports_USDk','Imports_USDk','World_Exports_USDk','World_Imports_USDk']:
            r[col]=g[col].sum(min_count=3)
        for col in ['NER_IDR_per_PartnerCurrency','Partner_CPI_Index_2015mean100',
                    'CPI_IDN_Index_2015mean100','RER_Bilateral_Index_2015mean100',
                    'RER_With_WPI_Proxy_Index_2015mean100','REER_BIS_broad']:
            r[col]=g[col].mean() if g[col].notna().sum()==3 else np.nan
        r['RER_Months_Observed']=int(g.RER_Bilateral_Index_2015mean100.notna().sum())
        r['RER_Proxy_Months_Observed']=int(g.RER_With_WPI_Proxy_Index_2015mean100.notna().sum())
        r['Uses_WPI_Proxy']=bool(g.Price_Index_Is_WPI_Proxy.fillna(False).any())
        r['CPI_SourceInterpolated_FromQuarterly']=bool(iso=='AUS')
        quarterly.append(r)
    qp=pd.DataFrame(quarterly)
    gcols=['GDP_Real_Level_SourceUnits','GDP_Real_Index_2015mean100','GDP_Source','GDP_Adjustment']
    qp=qp.merge(gdp[['ISO3','Quarter']+gcols].rename(columns={c:'Partner_'+c for c in gcols}),on=['ISO3','Quarter'],how='left',validate='one_to_one')
    qp=qp.merge(gdp[gdp.ISO3.eq('IDN')][['Quarter']+gcols].rename(columns={c:'IDN_'+c for c in gcols}),on='Quarter',how='left',validate='many_to_one')
    add_ratios(qp,'Exports_USDk','Imports_USDk')
    add_ratios(qp,'World_Exports_USDk','World_Imports_USDk','World_')
    required=['Ln_Exports_Imports','Partner_GDP_Real_Index_2015mean100','IDN_GDP_Real_Index_2015mean100']
    qp['Ready_NARDL_CPI']=qp[required+['RER_Bilateral_Index_2015mean100']].notna().all(axis=1)
    qp['Ready_NARDL_WithPriceProxy']=qp[required+['RER_With_WPI_Proxy_Index_2015mean100']].notna().all(axis=1)
    worldq=qp[qp.ISO3.eq('USA')][['Quarter','World_Exports_USDk','World_Imports_USDk',
        'World_Trade_Balance_USDk','World_Total_Trade_USDk','World_Ln_Exports_Imports',
        'World_Ln_Imports_Exports','IDN_GDP_Real_Index_2015mean100','REER_BIS_broad']].copy()
    # Foreign activity is explicitly a top-10 fixed-weight proxy, not global GDP.
    b=original[original.Date.between('2006-01','2008-12')].groupby('ISO3').Exports_USDk.sum()
    weights=(b/b.sum()).rename('Export_Weight_2006_2008')
    weighted=qp.merge(weights,on='ISO3',how='left')
    activity={}
    for q,g in weighted.groupby('Quarter'):
        activity[q]=(g.Partner_GDP_Real_Index_2015mean100*g.Export_Weight_2006_2008).sum() if g.Partner_GDP_Real_Index_2015mean100.notna().sum()==10 else np.nan
    worldq['Foreign_Activity_Top10_FixedWeight_Index']=worldq.Quarter.map(activity)
    worldq['Ready_Aggregate_Top10DemandProxy']=worldq[['World_Ln_Exports_Imports','IDN_GDP_Real_Index_2015mean100','REER_BIS_broad','Foreign_Activity_Top10_FixedWeight_Index']].notna().all(axis=1)

    coverage=[]
    for iso,g in qp.groupby('ISO3'):
        for flag in ['Ready_NARDL_CPI','Ready_NARDL_WithPriceProxy']:
            ok=g[g[flag]]
            coverage.append({'ISO3':iso,'Readiness':flag,'N_Quarters':len(ok),
                             'First_Quarter':ok.Quarter.min() if len(ok) else '',
                             'Last_Quarter':ok.Quarter.max() if len(ok) else ''})
    coverage=pd.DataFrame(coverage)
    outputs={'Panel_Country_Month.csv':panel,'Macro_Monthly.csv':macro,
        'GDP_Real_Quarterly.csv':gdp,'CPI_Monthly.csv':cpi,
        'FX_Bilateral_Monthly.csv':bilat,'Trade_World_Monthly.csv':world,
        'Panel_Country_Quarter.csv':qp,'Panel_World_Quarter.csv':worldq,
        'Macro_Data_Coverage.csv':coverage,
        'Trade_World_Annual_Source_Check.csv':annual,
        'Top10_Foreign_Activity_Weights.csv':weights.reset_index()}
    # Source metadata is kept in machine-readable form alongside outputs.
    selected=['bis_fx_bulk','bis_cpi_bulk','wb_gem_vnm_cpi','wb_gem_gdp_real_all',
              'VALEXPIDM052N','VALIMPIDM052N','wb_gem_idn_DXGSRMRCHNSCD','wb_gem_idn_DMGSRMRCHNSCD',
              'wb_gem_vnm_fx','wdi_trade_annual']
    sources=pd.DataFrame([MANIFEST[k] for k in selected])
    sources['role']=['FX primary','Price index primary','Vietnam CPI primary','GDP primary',
                     'Exports comparison (do not splice)','Imports comparison (do not splice)',
                     'World customs exports primary','World customs imports primary',
                     'Vietnam FX reference only; not spliced','Annual merchandise trade cross-check']
    outputs['Macro_Source_Manifest.csv']=sources
    for name,df in outputs.items():
        assert not df.columns.duplicated().any(),name
    # Build Excel from the original snapshot, preserving legacy lookup/notes sheets.
    wb=load_workbook(BASE/'Panel_Gabungan_Indonesia.xlsx')
    sheets={'Panel_Country_Month':panel,'Macro_Monthly':macro,'Country_Quarter':qp,
            'World_Quarter':worldq,'GDP_Real_Quarterly':gdp,'CPI_Monthly':cpi,
            'FX_Bilateral_Monthly':bilat,'Trade_World_Monthly':world,'Data_Coverage':coverage}
    for name,df in sheets.items():
        if name in wb: del wb[name]
        ws=wb.create_sheet(name)
        clean=df.astype(object).where(pd.notna(df),None)
        for row in dataframe_to_rows(clean,index=False,header=True):ws.append(row)
        ws.freeze_panes='D2' if name=='Panel_Country_Month' else 'A2'
        ws.auto_filter.ref=ws.dimensions
        for cell in ws[1]:
            cell.font=Font(bold=True,color='FFFFFF');cell.fill=PatternFill('solid',fgColor='1F3864')
        for column in ws.columns:
            ws.column_dimensions[column[0].column_letter].width=min(42,max(16,len(str(column[0].value))+2))
    if 'Catatan' in wb:
        wb['Catatan'].append(['Tambahan 17 Nov 2026: World Bank GEM GDP SA, CPI/BIS, FX/BIS. GDP monthly hanya pada akhir kuartal, tanpa interpolasi.'])
        wb['Catatan'].append(['India sebelum 2013: BIS memakai WPI. CPI dan RER CPI dikosongkan; alternatif PriceProxy diberi penanda. Australia CPI monthly interpolasi oleh BIS.'])
        wb['Catatan'].append(['RER/NER naik berarti depresiasi. ln(X/M) naik berarti perbaikan. GDP adalah period alignment, bukan waktu publikasi. Lihat Tio/notes/sumber_data_macro_dan_merge.md.'])
    xlsx=MID/'Panel_Gabungan_Indonesia.xlsx'; temp=xlsx.with_suffix('.tmp.xlsx')
    wb.save(temp); temp.replace(xlsx)
    for name,df in outputs.items():write(df,name)
    print(coverage.to_string(index=False))
    print('World complete months:',world.World_Exports_USDk.notna().sum())
    print('Legacy columns preserved:',len(old_cols),'monthly rows:',len(panel))

if __name__=='__main__':main()
