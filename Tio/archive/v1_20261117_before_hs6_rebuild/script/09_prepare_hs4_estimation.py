"""Prepare one HS4 x partner estimation table, without estimating a model.
Example: python Tio/script/09_prepare_hs4_estimation.py --hs 1511 --partner CHN
"""
from pathlib import Path
import argparse,json
import numpy as np
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
MID=ROOT/'intermediate'

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--hs',default='1511');ap.add_argument('--partner',default='CHN')
    args=ap.parse_args();h=args.hs.zfill(4);iso=args.partner.upper()
    mapping=pd.read_csv(MID/'HS4_Commodity_Classification.csv',dtype={'HS_Code':str}).set_index('HS_Code')
    if h not in mapping.index:raise ValueError(f'Unknown HS4 {h}')
    c=mapping.loc[h,'Commodity_Class']
    source=MID/'hs_classified'/c/f'HS4_{iso}_Quarter.csv'
    panel=pd.read_csv(source,dtype={'HS_Code':str,'ISO3':str})
    d=panel[panel.HS_Code.eq(h)].copy()
    if d.empty:raise ValueError('HS4 not present in this partner source; no values imputed.')
    macro=pd.read_csv(MID/'Panel_Country_Quarter.csv',dtype={'ISO3':str,'Quarter':str})
    keys=['ISO3','Quarter']
    cols=keys+[x for x in macro if x not in keys and x.startswith(
        ('Country','IDN_','Partner_','REER_','CPI_','NER_','RER_','CMD_','Uses_WPI_'))]
    d=d.merge(macro[cols],on=keys,how='left',validate='one_to_one',sort=False).sort_values('Quarter')
    for stem,col in [('IDN_GDP_Real','IDN_GDP_Real_Index_2015mean100'),
                     ('Partner_GDP_Real','Partner_GDP_Real_Index_2015mean100'),
                     ('RER_Bilateral','RER_Bilateral_Index_2015mean100'),('BCOM','CMD_BCOM_Mean')]:
        d['Ln_'+stem]=np.log(d[col].where(d[col].gt(0)))
    need=['Ln_Imports_Exports','Ln_IDN_GDP_Real','Ln_Partner_GDP_Real','Ln_RER_Bilateral']
    d['Available_NARDL_CPI']=d[need].notna().all(axis=1)&d.Complete_Both_Flows
    d['Available_NARDL_CPI_With_BCOM']=d.Available_NARDL_CPI&d.Ln_BCOM.notna()
    # Keep every calendar quarter. Never collapse gaps by dropping rows here.
    assert not d.duplicated(['ISO3','HS_Code','Quarter']).any()
    folder=MID/'hs_classified/examples';folder.mkdir(exist_ok=True)
    out=folder/f'Estimation_HS4_{h}_{iso}_Quarter.csv'
    d.to_csv(out,index=False,float_format='%.12g',encoding='utf-8')
    run=best=0;start=best_start=best_end=None
    for _,row in d.iterrows():
        if row.Available_NARDL_CPI:
            if run==0:start=row.Quarter
            run+=1
            if run>best:best=run;best_start=start;best_end=row.Quarter
        else:run=0
    report={'output':str(out),'HS4':h,'Product':mapping.loc[h,'Product'],
        'Commodity_Class':c,'quarters':len(d),
        'quarters_variables_available':int(d.Available_NARDL_CPI.sum()),
        'quarters_variables_and_BCOM_available':int(d.Available_NARDL_CPI_With_BCOM.sum()),
        'longest_contiguous_available_quarters':best,
        'longest_contiguous_start':best_start,'longest_contiguous_end':best_end,
        'note':'Availability only; assess continuity, integration order, cointegration and identification separately.'}
    out.with_suffix('.availability.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
