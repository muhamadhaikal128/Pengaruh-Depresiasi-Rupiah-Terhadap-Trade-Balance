"""Prepare auditable quarterly cases for Bahmani-Oskooee/Fariditavana ARDL/NARDL.
TiVA/input-import mechanism is intentionally on hold. No raw data is changed.
"""
from pathlib import Path
import hashlib,json
import numpy as np
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
MID=ROOT/'intermediate'
DIAG=ROOT/'output/diagnostics/oskooee';DIAG.mkdir(parents=True,exist_ok=True)

def longest(g,valid):
    best=[];run=[];prev=None
    for i,ok in zip(g.index,valid):
        t=pd.Period(g.loc[i,'Quarter'],freq='Q').ordinal
        if ok:
            run=run+[i] if prev is not None and t==prev+1 else [i]
            if len(run)>len(best):best=run.copy()
            prev=t
        else:run=[];prev=None
    return best

def main():
    p=pd.read_csv(MID/'Panel_Country_Quarter.csv')
    w=pd.read_csv(MID/'Panel_World_Quarter.csv')
    cg=pd.read_csv(MID/'Panel_CommodityGroup_Country_Quarter.csv')
    fx=pd.read_csv(MID/'FX_Bilateral_WBGEM_Alternative.csv')
    cpi=pd.read_csv(MID/'FX_Bilateral_Monthly.csv')
    cases=[];registry=[]
    def add(code,label,scope,scenario,g,world=False,price=False,start=None,proxy=False,alt=False):
        g=g.sort_values('Quarter').copy()
        if start:g=g[g.Quarter.ge(start)].copy()
        x='World_Exports_USDk' if world else 'Exports_USDk'
        m='World_Imports_USDk' if world else 'Imports_USDk'
        d=pd.DataFrame({'Quarter':g.Quarter,'x':g[x],'m':g[m]})
        d['y']=np.log(d.m.where(d.m.gt(0))/d.x.where(d.x.gt(0)))
        d['yd']=np.log(g.IDN_GDP_Real_Index_2015mean100)
        d['yf']=np.log(g.Foreign_Activity_Top10_FixedWeight_Index if world else g.Partner_GDP_Real_Index_2015mean100)
        r=g.REER_BIS_broad if world else g['RER_With_WPI_Proxy_Index_2015mean100' if proxy else 'RER_Bilateral_Index_2015mean100']
        if alt:r=g.RER_GEM
        # Match paper orientation: an increase is appreciation; NEG is depreciation.
        d['q']=np.log(r) if world else -np.log(r)
        d['cp']=np.log(g.CMD_BCOM_Mean.where(g.CMD_BCOM_Mean.gt(0)))
        d['tb']=d.x-d.m
        need=['y','yd','yf','q']+(['cp'] if price else [])
        ix=longest(d,d[need].notna().all(axis=1));selected=d.loc[ix].copy()
        sid=len(registry)+1
        reg={'sid':sid,'series_id':code,'label':label,'scope':scope,'scenario':scenario,
             'price_control':int(price),'uses_WPI':int(proxy),'N_contiguous':len(selected),
             'first_quarter':selected.Quarter.min() if len(selected) else '',
             'last_quarter':selected.Quarter.max() if len(selected) else '',
             'excluded_incomplete_or_gap':int(len(d)-len(selected)),
             'status':'ESTIMATE' if len(selected)>=48 else 'SHORT_SAMPLE_HOLD',
             'foreign_activity':'Top10 fixed-weight demand proxy' if world else 'Partner real GDP',
             'q_orientation':'up=appreciation, NEG=depreciation',
             'source_caveats': 'World trade before 2010 unresolved; REER and top10 demand proxies' if world else
                 'See macro validity audit; India WPI only in marked sensitivity; AUS CPI source-interpolated'}
        registry.append(reg)
        if len(selected)>=48:
            selected['sid']=sid;selected['series_id']=code;selected['price_control']=int(price)
            selected['scope']=scope;selected['scenario']=scenario;selected['label']=label
            cases.append(selected)
    add('WORLD','Indonesia - World','aggregate','main',w,world=True,start='2010Q1')
    add('WORLD_FULL','Indonesia - World (2006+ audit sensitivity)','aggregate','world_2006_sensitivity',w,world=True)
    for iso,g in p.groupby('ISO3',sort=True):add('BIL_'+iso,iso,'bilateral','main',g)
    for iso in sorted(cg.ISO3.unique()):
        for c in ['commodity','noncommodity']:
            g=cg[cg.ISO3.eq(iso)&cg.Commodity_Class.eq(c)]
            add('TYPE_'+iso+'_'+c,iso+' / '+c,'goods','main',g)
            add('PRICE_'+iso+'_'+c,iso+' / '+c+' + BCOM','goods','BCOM_control',g,price=True)
    add('IND_WPI','IND (WPI proxy sensitivity)','bilateral','WPI_proxy',p[p.ISO3.eq('IND')],proxy=True)
    # Alternative is an entire source family, with existing same CPI; no single-month fills.
    mm=fx.merge(cpi[['ISO3','Date','CPI_Index_2015mean100','CPI_IDN_Index_2015mean100']],on=['ISO3','Date'],validate='one_to_one')
    mm['Quarter']=pd.PeriodIndex(mm.Date,freq='M').asfreq('Q').astype(str)
    mm['RER_GEM']=mm.NER_IDR_per_PartnerCurrency_WBGEM*mm.CPI_Index_2015mean100/mm.CPI_IDN_Index_2015mean100
    aq=mm.groupby(['ISO3','Quarter']).RER_GEM.agg(['mean','count']).reset_index()
    aq['RER_GEM']=aq['mean'].where(aq['count'].eq(3))
    for iso in ['THA','VNM','KOR']:
        g=p[p.ISO3.eq(iso)].merge(aq[['ISO3','Quarter','RER_GEM']],on=['ISO3','Quarter'],validate='one_to_one')
        add('GEM_'+iso,iso+' (GEM FX family sensitivity)','bilateral','GEM_FX',g,alt=True)
    reg=pd.DataFrame(registry);data=pd.concat(cases,ignore_index=True)
    data['tq']=pd.PeriodIndex(data.Quarter,freq='Q').asi8- pd.Period('1960Q1',freq='Q').ordinal
    assert not data.duplicated(['sid','tq']).any()
    for sid,g in data.groupby('sid'):
        assert np.diff(g.tq).min()==1 and g[['y','yd','yf','q']].notna().all().all()
        np.testing.assert_allclose(g.y,np.log(g.m/g.x),atol=1e-12)
    reg.to_csv(DIAG/'case_registry.csv',index=False)
    data.to_csv(MID/'Oskooee_Quarterly_Analysis.csv',index=False,float_format='%.15g')
    # Screen all HS4 series; do not confuse total available observations with continuity.
    screen=[]
    for iso in sorted(p.ISO3.unique()):
        macro=p[p.ISO3.eq(iso)][['ISO3','Quarter','IDN_GDP_Real_Index_2015mean100','Partner_GDP_Real_Index_2015mean100','RER_Bilateral_Index_2015mean100']]
        for c in ['commodity','noncommodity','mixed','unclassified']:
            z=pd.read_csv(MID/'hs_classified'/c/f'HS4_{iso}_Quarter.csv',dtype={'HS_Code':str})
            z=z.merge(macro,on=['ISO3','Quarter'],how='left',validate='many_to_one')
            z['ok']=z[['Ln_Imports_Exports','IDN_GDP_Real_Index_2015mean100','Partner_GDP_Real_Index_2015mean100','RER_Bilateral_Index_2015mean100']].notna().all(axis=1)&z.Complete_Both_Flows
            for h,g in z.groupby('HS_Code',sort=False):
                g=g.sort_values('Quarter');ix=longest(g,g.ok)
                eligible=len(ix)>=48 and c in ['commodity','noncommodity']
                screen.append({'ISO3':iso,'HS_Code':h,'Commodity_Class':c,'Available_Quarters':int(g.ok.sum()),
                    'Longest_Contiguous_Quarters':len(ix),'Start':g.loc[ix,'Quarter'].min() if ix else '',
                    'End':g.loc[ix,'Quarter'].max() if ix else '',
                    'Exports_Zero_Quarters':int(g.Exports_USDk.eq(0).sum()),'Imports_Zero_Quarters':int(g.Imports_USDk.eq(0).sum()),
                    'PreEstimation_Eligible':eligible,'Status':'PRE_ELIGIBLE_NOT_YET_ESTIMATED' if eligible else
                     'AMBIGUOUS_CLASS' if c in ['mixed','unclassified'] else 'INSUFFICIENT_CONTIGUOUS_DATA'})
        print('SCREENED',iso,flush=True)
    sc=pd.DataFrame(screen);sc.to_csv(DIAG/'HS4_estimation_eligibility.csv',index=False)
    sources=['Panel_Country_Quarter.csv','Panel_World_Quarter.csv','Panel_CommodityGroup_Country_Quarter.csv','FX_Bilateral_WBGEM_Alternative.csv','FX_Bilateral_Monthly.csv']
    manifest={f:hashlib.sha256((MID/f).read_bytes()).hexdigest() for f in sources}
    (DIAG/'input_sha256.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    print(reg[['series_id','scenario','N_contiguous','first_quarter','last_quarter','status']].to_string(index=False))
    print('HS4 preliminary eligibility:',sc.PreEstimation_Eligible.sum(),'of',len(sc))

if __name__=='__main__':main()
