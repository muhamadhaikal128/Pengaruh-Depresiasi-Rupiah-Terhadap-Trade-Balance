"""Offline integration checks of saved macro sources and merged research datasets."""
from pathlib import Path
import json
import hashlib
import numpy as np
import pandas as pd
from openpyxl import load_workbook

ROOT=Path(__file__).resolve().parents[1]
MID=ROOT/'intermediate'
RAW=ROOT/'input/raw/macro_external_20261117'

def main():
    p=pd.read_csv(MID/'Panel_Country_Month.csv')
    m=pd.read_csv(MID/'Macro_Monthly.csv')
    q=pd.read_csv(MID/'Panel_Country_Quarter.csv')
    gd=pd.read_csv(MID/'GDP_Real_Quarterly.csv')
    w=pd.read_csv(MID/'Trade_World_Monthly.csv')
    f=pd.read_csv(MID/'FX_Bilateral_Monthly.csv')
    old=pd.read_csv(RAW/'baseline_before_merge/Panel_Country_Month.csv')
    oldm=pd.read_csv(RAW/'baseline_before_merge/Macro_Monthly.csv')
    pd.testing.assert_frame_equal(p[old.columns],old,check_dtype=False,rtol=1e-10,atol=1e-8)
    pd.testing.assert_frame_equal(m[oldm.columns],oldm,check_dtype=False,rtol=1e-10,atol=1e-8)
    assert len(p)==2500 and not p.duplicated(['ISO3','Date']).any()
    assert len(q)==840 and not q.duplicated(['ISO3','Quarter']).any()
    assert gd.ISO3.nunique()==11 and not gd.duplicated(['ISO3','Quarter']).any()
    assert (gd.GDP_Real_Level_SourceUnits>0).all()
    assert (gd.GDP_Adjustment=='SA').all()
    np.testing.assert_allclose(gd[gd.Quarter.str.startswith('2015')].groupby('ISO3').GDP_Real_Index_2015mean100.mean(),100)
    # GDP alignment cannot create monthly observations in non-quarter-end months.
    assert p.loc[~p.Date.str[-2:].isin(['03','06','09','12']),'Partner_GDP_Real_Index_2015mean100'].isna().all()
    usa=f[f.ISO3.eq('USA')]
    np.testing.assert_allclose(usa.NER_IDR_per_PartnerCurrency,usa.IDR_per_USD_BIS,rtol=1e-9)
    np.testing.assert_allclose(f.NER_IDR_per_PartnerCurrency,f.IDR_per_USD_BIS/f.LCU_per_USD,rtol=1e-9)
    india=f[f.ISO3.eq('IND')&f.Date.lt('2013-01')]
    assert india.RER_Bilateral_Index_2015mean100.isna().all()
    assert india.Price_Index_Is_WPI_Proxy.all()
    assert india.RER_With_WPI_Proxy_Index_2015mean100.notna().all()
    assert f.loc[f.ISO3.eq('AUS'),'Price_Index_SourceInterpolated_FromQuarterly'].all()
    assert f.loc[f.ISO3.eq('USA')&f.Date.eq('2025-10'),'CPI_Index_2015mean100'].isna().all()
    assert f.loc[f.ISO3.eq('VNM')&f.Date.eq('2025-08'),'NER_IDR_per_PartnerCurrency'].isna().all()
    assert not f.FX_Source.dropna().str.contains('fills BIS missing').any()
    # Full-quarter sums, incomplete-quarter treatment, and log ratios.
    for _,r in q.iterrows():
        g=p[(p.ISO3==r.ISO3)&(p.Quarter==r.Quarter)]
        for col in ['Exports_USDk','Imports_USDk','World_Exports_USDk','World_Imports_USDk']:
            expected=g[col].sum(min_count=3)
            np.testing.assert_allclose(r[col],expected,rtol=1e-9,equal_nan=True)
    np.testing.assert_allclose(w.World_Trade_Balance_USDk,w.World_Exports_USDk-w.World_Imports_USDk,equal_nan=True)
    np.testing.assert_allclose(q.Ln_Exports_Imports,-q.Ln_Imports_Exports,equal_nan=True)
    # Unit checks against source bytes; annual cross-source discrepancies are
    # reported, not erased. Historical GEM customs and revised WTO differ.
    annual=pd.read_csv(MID/'Trade_World_Annual_Source_Check.csv')
    anchor=annual[annual.Year.eq(2010)].iloc[0]
    assert abs(anchor.Exports_GEM_vs_WDI_pct)<1 and abs(anchor.Imports_GEM_vs_WDI_pct)<1
    raw_export=json.loads((RAW/'wb_gem_idn_DXGSRMRCHNSCD.json').read_text('utf-8'))
    value=next(r['value'] for r in raw_export['source']['data']
               if any(v['id']=='2006M01' for v in r['variable']))
    assert np.isclose(w.iloc[0].World_Exports_USDk,value*1000)
    # Confirm all primary source bytes still match acquisition SHA-256 hashes.
    sources=pd.read_csv(MID/'Macro_Source_Manifest.csv')
    for _,r in sources.iterrows():
        path=ROOT/r['path'].replace('\\','/')
        assert hashlib.sha256(path.read_bytes()).hexdigest()==r.sha256
    wb=load_workbook(MID/'Panel_Gabungan_Indonesia.xlsx',read_only=True,data_only=True)
    assert wb['Panel_Country_Month'].max_row==2501
    assert wb['Country_Quarter'].max_row==841
    assert 'HS_Lookup' in wb and 'Catatan' in wb
    wb.close()
    counts=q.groupby('ISO3')[['Ready_NARDL_CPI','Ready_NARDL_WithPriceProxy']].sum()
    report={'status':'PASS','integrity_status':'PASS','substantive_validity':'CONDITIONAL_REVIEW_REQUIRED',
            'audit_note':'PASS is integration/integrity only; see audit_validitas_data_macro.md',
            'monthly_rows':len(p),'monthly_columns':len(p.columns),
            'quarterly_rows':len(q),'gdp_countries':gd.ISO3.nunique(),
            'world_months':int(w.World_Exports_USDk.notna().sum()),
            'annual_source_discrepancies_over_1pct':annual.loc[
                annual[['Exports_GEM_vs_WDI_pct','Imports_GEM_vs_WDI_pct']].abs().gt(1).any(axis=1),
                ['Year','Exports_GEM_vs_WDI_pct','Imports_GEM_vs_WDI_pct']].to_dict('records'),
            'quarter_availability_by_country':counts.to_dict('index'),
            'scope':'availability and data integrity; not stationarity, cointegration or causal identification'}
    (MID/'Macro_Validation_Report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
