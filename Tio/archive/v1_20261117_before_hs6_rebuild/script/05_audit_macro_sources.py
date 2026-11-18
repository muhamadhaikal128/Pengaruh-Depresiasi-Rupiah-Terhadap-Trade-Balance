"""Cross-source audit; does not overwrite research observations.

python Tio/script/05_audit_macro_sources.py --download
python Tio/script/05_audit_macro_sources.py

Requires pandas, numpy, httpx. Shared original national providers mean comparisons
between compilers are not fully independent statistical measurements.
"""
from pathlib import Path
import argparse
import importlib
import json
import hashlib
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
MID=ROOT/'intermediate'
RAW=ROOT/'input/raw/macro_external_20261117'
AUD=RAW/'audit_cross_sources'
COUNTRIES='IDN;CHN;USA;SGP;JPN;MYS;IND;KOR;THA;VNM;AUS'
REQUESTS=[
    ('wdi_real_gdp_annual','https://api.worldbank.org/v2/country/'+COUNTRIES+'/indicator/NY.GDP.MKTP.KN?format=json&per_page=3000','.json'),
    ('gem_cpi_all','https://api.worldbank.org/v2/sources/15/country/'+COUNTRIES+'/series/CPTOTNSXN/time/all?format=json&per_page=30000','.json'),
    ('gem_fx_all','https://api.worldbank.org/v2/sources/15/country/'+COUNTRIES+'/series/DPANUSLCU/time/all?format=json&per_page=30000','.json'),
    ('gdp_idn_imf_sa','https://fred.stlouisfed.org/graph/fredgraph.csv?id=NGDPRSAXDCIDQ','.csv'),
    ('gdp_jpn_imf_sa','https://fred.stlouisfed.org/graph/fredgraph.csv?id=NGDPRSAXDCJPQ','.csv'),
    ('gdp_usa_imf_sa','https://fred.stlouisfed.org/graph/fredgraph.csv?id=NGDPRSAXDCUSQ','.csv'),
]

def download():
    mod=importlib.import_module('02_download_macro_sources');mod.RAW=AUD
    AUD.mkdir(exist_ok=True)
    old=AUD/'download_manifest.json'
    rows=json.loads(old.read_text('utf-8')) if old.exists() else []
    ok={r['label'] for r in rows if r.get('status')==200}
    with ThreadPoolExecutor(max_workers=3) as pool:
        for result in pool.map(mod.fetch,[r for r in REQUESTS if r[0] not in ok]):
            rows=[r for r in rows if r['label']!=result['label']]+[result]
            old.write_text(json.dumps(rows,indent=2),encoding='utf-8')
            print(result['label'],result.get('status'),flush=True)

def gem(filename,frequency='M'):
    d=json.loads((AUD/filename).read_text('utf-8'));assert d['pages']==1
    rows=[]
    for r in d['source']['data']:
        v={x['concept']:x['id'] for x in r['variable']};t=v['Time']
        if r['value'] is not None and t[4:5]==frequency:
            key='Date' if frequency=='M' else 'Quarter'
            period=t[:4]+'-'+t[5:] if frequency=='M' else t
            rows.append({'ISO3':v['Country'],key:period, 'Reference':r['value']})
    return pd.DataFrame(rows,columns=['ISO3','Date' if frequency=='M' else 'Quarter','Reference'])

def compare(primary,reference,keys,value,family,note):
    a=primary[keys+[value]].rename(columns={value:'Primary'}).merge(reference,on=keys,how='inner',validate='one_to_one')
    a=a.dropna(subset=['Primary','Reference']);a['Relative_Difference_pct']=(a.Primary/a.Reference-1)*100
    a['Family']=family;a['Note']=note
    return a

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--download',action='store_true');args=parser.parse_args()
    if args.download:download()
    missing=[name for name,_,ext in REQUESTS if not (AUD/(name+ext)).exists()]
    if missing:raise RuntimeError('Missing audit references: '+','.join(missing))
    manifest=json.loads((AUD/'download_manifest.json').read_text('utf-8'))
    for name,_,ext in REQUESTS:
        record=next(r for r in manifest if r['label']==name)
        assert record.get('status')==200,name
        assert hashlib.sha256((AUD/(name+ext)).read_bytes()).hexdigest()==record['sha256'],name
    cpi=pd.read_csv(MID/'CPI_Monthly.csv');fx=pd.read_csv(MID/'FX_Bilateral_Monthly.csv');gdp=pd.read_csv(MID/'GDP_Real_Quarterly.csv')
    comparisons=[]
    # Normalize both price compilers to the same 2015 monthly mean.
    ref=gem('gem_cpi_all.json')
    for iso,g in ref.groupby('ISO3'):
        b=g.loc[g.Date.str.startswith('2015'),'Reference'];assert b.count()==12
        ref.loc[g.index,'Reference']=g.Reference/b.mean()*100
    comparisons.append(compare(cpi,ref,['ISO3','Date'],'CPI_Index_2015mean100','CPI',
        'BIS vs WB GEM after 2015 rebase; VNM has same provider, not independent; IND pre2013 excluded'))
    arq=gem('gem_cpi_all.json','Q');arq=arq[arq.ISO3.eq('AUS')].copy()
    ac=cpi[cpi.ISO3.eq('AUS')].copy();ac['Quarter']=pd.PeriodIndex(ac.Date,freq='M').asfreq('Q').astype(str)
    ac=ac.groupby(['ISO3','Quarter']).CPI_Index_2015mean100.agg(lambda x:x.mean() if x.count()==3 else np.nan).reset_index()
    if len(arq):
        b=arq.loc[arq.Quarter.str.startswith('2015'),'Reference'];assert b.count()==4
        arq.Reference=arq.Reference/b.mean()*100
        comparisons.append(compare(ac,arq,['ISO3','Quarter'],'CPI_Index_2015mean100','CPI_quarterly',
            'Australia: BIS interpolated-month mean vs WB quarterly CPI, rebased 2015'))
    # Nominal quotes are compared before derived RER; domestic IDR is included.
    fxref=gem('gem_fx_all.json')
    dom=fx[['Date','IDR_per_USD_BIS']].drop_duplicates().rename(columns={'IDR_per_USD_BIS':'LCU_per_USD'});dom['ISO3']='IDN'
    rates=pd.concat([fx[['ISO3','Date','LCU_per_USD']],dom],ignore_index=True)
    comparisons.append(compare(rates,fxref,['ISO3','Date'],'LCU_per_USD','FX',
        'BIS vs WB official period averages; fixing times and providers may differ'))
    alt=fxref.rename(columns={'Reference':'LCU_per_USD_WBGEM'}).copy()
    domestic=alt[alt.ISO3.eq('IDN')][['Date','LCU_per_USD_WBGEM']].rename(columns={'LCU_per_USD_WBGEM':'IDR_per_USD_WBGEM'})
    alt=alt[~alt.ISO3.eq('IDN')].merge(domestic,on='Date',validate='many_to_one')
    alt=alt[alt.Date.between('2006-01','2026-10')].copy()
    alt['NER_IDR_per_PartnerCurrency_WBGEM']=alt.IDR_per_USD_WBGEM/alt.LCU_per_USD_WBGEM
    alt['Source']='World Bank GEM DPANUSLCU, full alternative series; not spliced into BIS'
    alt.to_csv(MID/'FX_Bilateral_WBGEM_Alternative.csv',index=False,float_format='%.12g')
    # Quarterly SA GDP vs IMF/FRED SA, rebased individually, no level-scale matching.
    for iso,file in [('IDN','gdp_idn_imf_sa.csv'),('JPN','gdp_jpn_imf_sa.csv'),('USA','gdp_usa_imf_sa.csv')]:
        z=pd.read_csv(AUD/file);z.columns=['Date','Reference'];z.Reference=pd.to_numeric(z.Reference,errors='coerce')
        z['Quarter']=pd.to_datetime(z.Date).dt.to_period('Q').astype(str);z['ISO3']=iso
        b=z.loc[z.Quarter.str.startswith('2015'),'Reference'];assert b.count()==4
        z.Reference=z.Reference/b.mean()*100
        comparisons.append(compare(gdp[gdp.ISO3.eq(iso)],z[['ISO3','Quarter','Reference']],['ISO3','Quarter'],
            'GDP_Real_Index_2015mean100','GDP_quarterly', 'GEM SA vs IMF/FRED SA; vintage/base revisions may differ'))
    # Annual GDP is an additional check, not evidence of equal quarterly dynamics.
    d=json.loads((AUD/'wdi_real_gdp_annual.json').read_text('utf-8'));assert d[0]['pages']==1
    ar=pd.DataFrame([{'ISO3':r['countryiso3code'],'Year':r['date'],'Reference':r['value']} for r in d[1] if r['value'] is not None])
    for iso,g in ar.groupby('ISO3'):
        b=g.loc[g.Year.eq('2015'),'Reference'];assert len(b)==1
        ar.loc[g.index,'Reference']=g.Reference/b.iloc[0]*100
    annual_base=gdp.copy();period=pd.PeriodIndex(annual_base.Quarter,freq='Q')
    year=period.year.to_numpy().copy();quarter=period.quarter.to_numpy()
    india=annual_base.ISO3.eq('IND').to_numpy();australia=annual_base.ISO3.eq('AUS').to_numpy()
    year[india & (quarter==1)]-=1
    year[australia & (quarter>=3)]+=1
    annual_base['Year']=year.astype(str)
    annual=annual_base.groupby(['ISO3','Year']).GDP_Real_Index_2015mean100.agg(
        lambda x:x.mean() if x.count()==4 else np.nan).reset_index()
    for iso,g in annual.groupby('ISO3'):
        b=g.loc[g.Year.eq('2015'),'GDP_Real_Index_2015mean100'];assert b.notna().sum()==1
        annual.loc[g.index,'GDP_Real_Index_2015mean100']=g.GDP_Real_Index_2015mean100/b.iloc[0]*100
    comparisons.append(compare(annual,ar,['ISO3','Year'],'GDP_Real_Index_2015mean100','GDP_annual',
        'GEM vs WDI annual volume; IND/AUS fiscal-year aligned; fiscal-year 2015 rebase; annual check only'))
    detail=pd.concat(comparisons,ignore_index=True)
    detail.to_csv(MID/'Macro_Audit_CrossSource_Detail.csv',index=False,float_format='%.12g')
    summary=[]
    for (family,iso),g in detail.groupby(['Family','ISO3']):
        err=g.Relative_Difference_pct.abs()
        summary.append({'Family':family,'ISO3':iso,'N_Compared':len(g),
            'Median_Abs_Difference_pct':err.median(),'P95_Abs_Difference_pct':err.quantile(.95),
            'Max_Abs_Difference_pct':err.max(),'N_Over_1pct':int((err>1).sum()),
            'Assessment':'REVIEW_DIFFERENCE' if (err>1).any() else 'WITHIN_1PCT_SCREEN',
            'Note':g.Note.iloc[0]})
    if not len(arq):
        summary.append({'Family':'CPI','ISO3':'AUS','N_Compared':0,
            'Assessment':'NOT_COMPARED_REFERENCE_UNAVAILABLE',
            'Note':'BIS monthly is interpolated quarterly CPI; GEM reference has no nonmissing monthly/quarterly observations'})
    summary=pd.DataFrame(summary);summary.to_csv(MID/'Macro_Audit_CrossSource_Summary.csv',index=False,float_format='%.12g')
    # Screening threshold is an alert rule, never a guarantee of statistical validity.
    p=pd.read_csv(MID/'Panel_Country_Month.csv');time=[]
    for iso,g in p.groupby('ISO3'):
        g=g.sort_values('Date')
        for col in ['Partner_CPI_Index_2015mean100','LCU_per_USD','IDR_per_USD_BIS']:
            ch=(g[col]/g[col].shift(1)-1)*100
            for i in g.index[ch.abs()>10]:
                time.append({'ISO3':iso,'Date':g.loc[i,'Date'],'Variable':col,'Change_pct':ch.loc[i]})
    pd.DataFrame(time,columns=['ISO3','Date','Variable','Change_pct']).to_csv(MID/'Macro_Audit_Large_Monthly_Changes.csv',index=False)
    print(summary[['Family','ISO3','N_Compared','Max_Abs_Difference_pct','Assessment']].to_string(index=False))
    print('Large monthly changes (>10%):',len(time))

if __name__=='__main__':main()
