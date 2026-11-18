"""Save and validate OECD TiVA annual IDN foreign-content data and BEC metadata.
Offline by default. --download restores missing source bytes using pinned requests.
This does not assign industrial foreign content to an HS4 without an industry bridge.
"""
from pathlib import Path
import argparse,hashlib,json
import numpy as np
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'input/raw/import_input_sources_20261117'
MID=ROOT/'intermediate'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def write_csv(df,name):
    p=MID/name;t=p.with_suffix('.tmp.csv');df.to_csv(t,index=False,float_format='%.12g',encoding='utf-8');t.replace(p)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--download',action='store_true');a=ap.parse_args()
    req=json.loads((Path(__file__).parent/'import_input_source_requests.json').read_text('utf-8'))
    RAW.mkdir(parents=True,exist_ok=True)
    for r in req:
        p=RAW/r['filename']
        if not p.exists():
            if not a.download:raise FileNotFoundError(f'{p}; use --download')
            import httpx
            z=httpx.get(r['url'],headers={'Accept':r['accept']},timeout=120,follow_redirects=True);z.raise_for_status()
            assert hashlib.sha256(z.content).hexdigest()==r['sha256'],'Remote source changed; do not replace pinned data silently'
            p.write_bytes(z.content)
        assert sha(p)==r['sha256'],r['filename']
    d=pd.read_csv(RAW/'oecd_tiva_idn_export_va_shares.csv')
    d=d.rename(columns={c:c.split(': ',1)[0] for c in d})
    for c in ['MEASURE','REF_AREA','ACTIVITY','COUNTERPART_AREA','UNIT_MEASURE','FREQ','UNIT_MULT']:
        parts=d[c].astype(str).str.split(': ',n=1,expand=True)
        d[c+'_Label']=parts[1] if parts.shape[1]>1 else ''
        d[c]=parts[0]
    assert d.REF_AREA.eq('IDN').all() and d.COUNTERPART_AREA.eq('W').all()
    assert d.UNIT_MEASURE.eq('PT_EXGR').all() and d.UNIT_MULT.eq('0').all() and d.FREQ.eq('A').all()
    assert set(d.MEASURE)=={'EXGR_FVA','EXGR_DVA'}
    assert not d.duplicated(['ACTIVITY','TIME_PERIOD','MEASURE']).any()
    assert d.OBS_VALUE.notna().all() and d.OBS_VALUE.between(0,100).all()
    p=d.pivot(index=['ACTIVITY','TIME_PERIOD'],columns='MEASURE',values='OBS_VALUE').reset_index()
    p=p.rename(columns={'ACTIVITY':'Industry_ISIC4_OECD','TIME_PERIOD':'Year',
        'EXGR_FVA':'Foreign_Value_Added_Share_Gross_Exports_pct',
        'EXGR_DVA':'Domestic_Value_Added_Share_Gross_Exports_pct'})
    labels=d[['ACTIVITY','ACTIVITY_Label']].drop_duplicates().set_index('ACTIVITY').ACTIVITY_Label
    assert not labels.index.duplicated().any()
    p['Industry_Label']=p.Industry_ISIC4_OECD.map(labels)
    p['ISO3']='IDN';p['Counterpart']='World';p['Frequency']='Annual';p['Unit']='Percent of gross exports'
    p['Source']='OECD TiVA 2025 edition, Principal Indicators shares, v1.1'
    p=p[['ISO3','Industry_ISIC4_OECD','Industry_Label','Year',
         'Foreign_Value_Added_Share_Gross_Exports_pct','Domestic_Value_Added_Share_Gross_Exports_pct',
         'Counterpart','Frequency','Unit','Source']].sort_values(['Industry_ISIC4_OECD','Year']).reset_index(drop=True)
    np.testing.assert_allclose(p.Foreign_Value_Added_Share_Gross_Exports_pct+p.Domestic_Value_Added_Share_Gross_Exports_pct,100,atol=0.002,rtol=0)
    assert not p.duplicated(['ISO3','Industry_ISIC4_OECD','Year']).any()
    write_csv(p,'TiVA_IDN_Export_Foreign_Content_Annual.csv')
    # Predetermined structural measure for an export sample beginning in 2006.
    # It remains a baseline interaction variable, not an observed annual 2023+ share.
    b=p[p.Year.between(2003,2005)].groupby(['ISO3','Industry_ISIC4_OECD','Industry_Label'],as_index=False).agg(
        FVA_Share_Baseline_2003_2005_pct=('Foreign_Value_Added_Share_Gross_Exports_pct','mean'),
        N_Years=('Year','nunique'))
    b.loc[b.N_Years.ne(3),'FVA_Share_Baseline_2003_2005_pct']=np.nan
    b['Interpretation']='Pre-sample industry structural proxy; not time-varying imported-input usage'
    write_csv(b,'TiVA_IDN_Foreign_Content_Baseline_2003_2005.csv')
    # Decode BEC using the official hierarchy, never an assumed digit position.
    js=json.loads((RAW/'unsd_bec5_codes.json').read_text('utf-8'))
    lookup={r['id']:r for r in js['results']};bec=[]
    for code,r in lookup.items():
        current=r;visited=set();enduse='Unclassified_or_not_specified';kind=''
        while current and current['id'] not in visited:
            visited.add(current['id']);txt=current['text'].lower()
            if current.get('aggrlevel')==3:
                if 'intermediate consumption' in txt:enduse='Intermediate_inputs'
                elif 'gross fixed capital formation' in txt:enduse='Capital_goods'
                elif 'final consumption' in txt:enduse='Final_consumption'
            if current.get('aggrlevel')==2:kind='Goods' if '|goods' in txt else 'Services' if '|services' in txt else ''
            current=lookup.get(current.get('parent'))
        bec.append({'BEC5_Code':code,'Description':r['text'],'Parent':r['parent'],
            'Aggregation_Level':r['aggrlevel'],'Is_Leaf':r['isLeaf']=='1','Goods_or_Services':kind,'End_Use':enduse})
    bec=pd.DataFrame(bec);write_csv(bec,'BEC5_EndUse_Dictionary.csv')
    assert bec.loc[bec.BEC5_Code.eq('1111'),'End_Use'].iloc[0]=='Intermediate_inputs'
    assert bec.loc[bec.BEC5_Code.eq('712010'),'End_Use'].iloc[0]=='Capital_goods'
    assert bec.loc[bec.BEC5_Code.eq('113'),'End_Use'].iloc[0]=='Final_consumption'
    report={'status':'PASS','raw_sources_sha256_checked':len(req),'annual_rows':len(p),
        'industry_codes_including_overlapping_aggregates':int(p.Industry_ISIC4_OECD.nunique()),
        'first_year':int(p.Year.min()),'last_year':int(p.Year.max()),
        'FVA_plus_DVA_equals_100_with_rounding_tolerance':True,
        'BEC5_codes':len(bec),'HS4_assignment_performed':False,
        'monthly_or_quarterly_interpolation_performed':False,
        '2023_onward_extrapolation_performed':False,
        'scope':'Industry-level foreign value added proxy, not a direct HS4 imported input coefficient',
        'next_required_bridge':'HS revision/HS6 to ISIC4/OECD industry with ambiguity and aggregation controls'}
    (MID/'Import_Input_Source_Validation_Report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2))
    print(p[p.Industry_ISIC4_OECD.eq('_T')].tail(3).to_string(index=False))

if __name__=='__main__':main()
