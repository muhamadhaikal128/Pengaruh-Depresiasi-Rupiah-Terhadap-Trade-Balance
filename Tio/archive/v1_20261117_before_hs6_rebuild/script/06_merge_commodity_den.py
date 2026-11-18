"""Import the supplied commodity workbook, preserve raw bytes, and merge offline.
Run AFTER 03_merge_macro_external.py; rerun this step after any macro rebuild.
No interpolation, duplicate-block splicing, unit conversion, or vendor validation.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import argparse
import hashlib
import json
import math
import shutil
import tempfile
import numpy as np
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill
from openpyxl.utils.dataframe import dataframe_to_rows

ROOT = Path(__file__).resolve().parents[1]
MID = ROOT / 'intermediate'
RAW = ROOT / 'input/raw/commodity_den_20261117'
DEFAULT_SOURCE = Path(r'C:\Users\Administrator\Downloads\Database DEN_26 October_temp.xlsx')
# Labels describe the supplied Legend, not independent vendor confirmation.
NAMES = ['WTI', 'Brent', 'Coal_Newcastle', 'Gold', 'CPO_Active', 'CPO_Front',
         'Nickel_Front', 'BCOM', 'SCFI', 'WCI', 'DOW_Unverified',
         'Nickel_3M_UnverifiedUnit', 'NickelOre_15', 'NickelOre_18', 'IronOre_62',
         'Urea', 'Sulfur', 'Graphite', 'Methanol', 'JetKerosene']
TARGETS = {
    'Macro_Monthly.csv': ('Date', 'Macro_Monthly'),
    'Panel_Country_Month.csv': ('Date', 'Panel_Country_Month'),
    'Trade_World_Monthly.csv': ('Date', 'Trade_World_Monthly'),
    'Panel_Country_Quarter.csv': ('Quarter', 'Country_Quarter'),
    'Panel_World_Quarter.csv': ('Quarter', 'World_Quarter'),
}

def sha(path):
    with path.open('rb') as f:
        h = hashlib.sha256()
        for chunk in iter(lambda: f.read(1024 * 1024), b''): h.update(chunk)
    return h.hexdigest()

def number(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)

def csv_out(df, path):
    df.to_csv(path, index=False, float_format='%.12g', encoding='utf-8')

def check_equal(a, b):
    pd.testing.assert_frame_equal(a, b, check_dtype=False, check_exact=False,
                                  rtol=1e-10, atol=1e-8)

def extract(path):
    w = load_workbook(path, read_only=True, data_only=True)
    legend = {str(r[1]).strip().upper(): (r[2], r[3])
              for r in w['Legend'].iter_rows(values_only=True)
              if len(r) >= 4 and r[1] and r[2] and r[3]}
    records, audit, dictionaries = [], [], []
    now = pd.Timestamp.now().normalize()
    for sheet, n, second_date, offset in [('Commodities', 15, 20, 0),
                                         ('Sulfur etc.', 5, 7, 15)]:
        s = w[sheet]
        headers = list(s.iter_rows(min_row=4, max_row=6, values_only=True))
        assert headers[2][0] == 'Dates' and headers[2][second_date] == 'Dates'
        tickers = [headers[0][i+1] for i in range(n)]
        for i, t in enumerate(tickers):
            assert t == headers[0][second_date+i+1], (sheet, i)
            name = NAMES[offset+i]
            desc, unit = legend[t.strip().upper()]
            excluded = {'CPO_Active': 'Duplicate blocks have conflicting values; do not splice.',
                        'DOW_Unverified': 'Instrument identity and unit need vendor confirmation.',
                        'Nickel_3M_UnverifiedUnit': 'Legend unit is ambiguous (6 metric tons price quote).'}
            dictionaries.append({'Series': name, 'Ticker': t, 'Description_AsSupplied': desc,
                'Unit_AsSupplied': unit, 'Sheet': sheet, 'Primary_Excel_Column': i+2,
                'Duplicate_Excel_Column': second_date+i+2,
                'Group': 'Freight' if name in ['SCFI', 'WCI'] else
                         'BroadCommodityIndex' if name == 'BCOM' else 'CommodityPrice',
                'Merge_Eligible': name not in excluded,
                'Review_Note': excluded.get(name, ''),
                'Metadata_Status': 'Supplied workbook Legend; not vendor-verified',
                'Primary_Block': 'Left block only; never fill from right block'})
        for row in s.iter_rows(min_row=7, values_only=True):
            a_date, b_date = row[0], row[second_date]
            if not isinstance(a_date, datetime): continue
            assert isinstance(b_date, datetime) and a_date == b_date, (sheet, a_date, b_date)
            assert pd.Timestamp(a_date) <= now, ('Future date', a_date)
            day = a_date.strftime('%Y-%m-%d')
            for i, t in enumerate(tickers):
                a, b = row[i+1], row[second_date+i+1]
                if a != b:
                    reason = 'numeric_conflict' if number(a) and number(b) else 'missing_or_error_difference'
                    audit.append({'Sheet': sheet, 'Date': day, 'Series': NAMES[offset+i],
                                  'Ticker': t, 'Primary_Value': a, 'Duplicate_Value': b,
                                  'Difference_Type': reason})
                if number(a):
                    records.append({'Date': day, 'Series': NAMES[offset+i],
                                    'Ticker': t, 'Value': float(a)})
    w.close()
    daily = pd.DataFrame(records).sort_values(['Series', 'Date']).reset_index(drop=True)
    dictionary = pd.DataFrame(dictionaries)
    dup = pd.DataFrame(audit)
    assert len(dictionary) == 20 and not daily.duplicated(['Series', 'Date']).any()
    conflicts = dup.loc[dup.Difference_Type.eq('numeric_conflict'), ['Series','Date']].copy()
    conflicts['Duplicate_Numeric_Conflict'] = True
    daily = daily.merge(conflicts, on=['Series','Date'], how='left', validate='one_to_one')
    daily['Duplicate_Numeric_Conflict'] = daily.Duplicate_Numeric_Conflict.eq(True)
    counts = conflicts.groupby('Series').size()
    dictionary['Duplicate_Numeric_Conflict_Days'] = dictionary.Series.map(counts).fillna(0).astype(int)
    dictionary['Conflict_Policy'] = 'Any conflicting day excludes the entire month from panel Mean; raw left-block values retained.'
    return daily, dictionary, dup

def aggregate(daily, dictionary):
    d = daily.copy()
    d['Date'] = pd.to_datetime(d.Date)
    d['Month'] = d.Date.dt.to_period('M').astype(str)
    # Every mean averages numeric cached observations, not necessarily fresh quotes.
    m = d.groupby(['Series', 'Month'], sort=True).agg(
        Observed_Mean=('Value', 'mean'), Observed_EOP=('Value', 'last'),
        NObs=('Value', 'size'), First_Observation=('Date', 'min'),
        Last_Observation=('Date', 'max'),
        NConflictDays=('Duplicate_Numeric_Conflict', 'sum'), NNonpositive=('Value', lambda x: int(x.le(0).sum()))
    ).reset_index().rename(columns={'Month': 'Date'})
    bounds = d.groupby('Series').Date.agg(['min', 'max'])
    first = m.Series.map(bounds['min']); last = m.Series.map(bounds['max'])
    # Conservative first-month exclusion if observations start after day 1.
    m['Partial_First_Month'] = m.Date.eq(first.dt.to_period('M').astype(str)) & first.dt.day.gt(1)
    # A last business weekday can precede the calendar month-end.
    expected_end = last.dt.to_period('M').dt.to_timestamp('M')
    expected_end = expected_end.map(lambda x: x if x.weekday()<5 else x-pd.offsets.BDay(1))
    m['Partial_Last_Month'] = m.Date.eq(last.dt.to_period('M').astype(str)) & last.lt(expected_end)
    m['Use_In_Panel'] = ~(m.Partial_First_Month | m.Partial_Last_Month) & m.NConflictDays.eq(0)
    m['Mean'] = m.Observed_Mean.where(m.Use_In_Panel)
    m['EOP'] = m.Observed_EOP.where(m.Use_In_Panel)
    m = m.merge(dictionary[['Series', 'Ticker', 'Unit_AsSupplied', 'Merge_Eligible']],
                on='Series', validate='many_to_one')
    m['Quarter'] = pd.PeriodIndex(m.Date, freq='M').asfreq('Q').astype(str)
    qs = []
    for (series, quarter), g in m.groupby(['Series', 'Quarter'], sort=True):
        valid = g.Mean.notna(); complete = int(valid.sum()) == 3
        qs.append({'Series': series, 'Quarter': quarter,
                   'Mean': float(g.loc[valid, 'Mean'].mean()) if complete else np.nan,
                   'NMonths': int(valid.sum()), 'NObs': int(g.loc[valid, 'NObs'].sum()),
                   'Complete_Quarter': complete})
    q = pd.DataFrame(qs).merge(dictionary[['Series', 'Ticker', 'Unit_AsSupplied', 'Merge_Eligible']],
                              on='Series', validate='many_to_one')
    eligible = dictionary.loc[dictionary.Merge_Eligible, 'Series'].tolist()
    def wide(df, key, fields):
        grid = pd.period_range(df[key].min(), df[key].max(), freq='M' if key=='Date' else 'Q').astype(str)
        out = pd.DataFrame({key: grid})
        for name in eligible:
            sub = df.loc[df.Series.eq(name)].set_index(key)
            for field in fields:
                out[f'CMD_{name}_{field}'] = out[key].map(sub[field])
        return out
    mw = wide(m, 'Date', ['Mean', 'NObs', 'NConflictDays'])
    qw = wide(q, 'Quarter', ['Mean', 'NMonths'])
    for c in ['First_Observation', 'Last_Observation']:
        m[c] = m[c].dt.strftime('%Y-%m-%d')
    coverage = []
    for _, r in dictionary.iterrows():
        name=r.Series; ds=d[d.Series.eq(name)]; ms=m[m.Series.eq(name)]; gq=q[q.Series.eq(name)]
        coverage.append({'Series': name, 'Ticker': r.Ticker, 'Merge_Eligible': bool(r.Merge_Eligible),
            'First_Date': str(ds.Date.min().date()), 'Last_Date': str(ds.Date.max().date()),
            'Numeric_Observations': len(ds), 'Usable_Months': int(ms.Mean.notna().sum()),
            'Complete_Quarters': int(gq.Complete_Quarter.sum()),
            'Nonpositive_Observations': int(ds.Value.le(0).sum()),
            'Months_With_Duplicate_Conflict': int(ms.NConflictDays.gt(0).sum()), 'Unit_AsSupplied': r.Unit_AsSupplied})
    return m, q, mw, qw, pd.DataFrame(coverage)

def main():
    p=argparse.ArgumentParser(); p.add_argument('--source', type=Path); args=p.parse_args()
    RAW.mkdir(parents=True, exist_ok=True)
    rawfile=RAW / DEFAULT_SOURCE.name
    original=args.source or (rawfile if rawfile.exists() else DEFAULT_SOURCE)
    digest=sha(original)
    if rawfile.exists():
        assert sha(rawfile)==digest, 'Raw snapshot differs: use a new snapshot directory.'
    else:
        shutil.copy2(original, rawfile)
    assert sha(rawfile)==digest
    manifestfile=RAW/'source_manifest.json'
    if not manifestfile.exists():
        manifestfile.write_text(json.dumps({'original_path':str(original),
            'raw_path':str(rawfile.relative_to(ROOT)), 'sha256':digest,
            'size_bytes':rawfile.stat().st_size, 'copied_utc':datetime.now(timezone.utc).isoformat(),
            'source':'User-supplied workbook; cached Bloomberg-style ticker data',
            'vendor_authenticity':'Not independently verified'},indent=2),encoding='utf-8')
    else: assert json.loads(manifestfile.read_text('utf-8'))['sha256']==digest
    daily,dictionary,dup=extract(rawfile)
    m,q,mw,qw,coverage=aggregate(daily,dictionary)
    frames={}; originals={}
    backup=RAW/'baseline_before_commodity_merge'; backup.mkdir(exist_ok=True)
    for filename,(key,sheet) in TARGETS.items():
        current=pd.read_csv(MID/filename)
        if not (backup/filename).exists(): shutil.copy2(MID/filename,backup/filename)
        old=current.drop(columns=[c for c in current if c.startswith('CMD_')])
        out=old.merge(mw if key=='Date' else qw,on=key,how='left',validate='many_to_one',sort=False)
        assert len(out)==len(current) and not out.columns.duplicated().any()
        check_equal(out[old.columns],old)
        frames[filename]=out; originals[filename]=old
    xlsx=MID/'Panel_Gabungan_Indonesia.xlsx'
    if not (backup/xlsx.name).exists(): shutil.copy2(xlsx,backup/xlsx.name)
    stats={'status':'PASS','scope':'Extraction and merge integrity only; not independent vendor validation',
        'raw_sha256':digest, 'series_extracted':len(dictionary),
        'series_merged':int(dictionary.Merge_Eligible.sum()),
        'excluded_series':dictionary.loc[~dictionary.Merge_Eligible,'Series'].tolist(),
        'raw_numeric_rows':len(daily), 'latest_source_date':daily.Date.max(),
        'duplicate_numeric_conflicts':int(dup.Difference_Type.eq('numeric_conflict').sum()),
        'legacy_values_preserved':True, 'no_interpolation_or_duplicate_splicing':True,
        'monthly_partial_periods_excluded':True,'months_with_duplicate_conflicts_excluded':True,
        'quarter_requires_three_months':True,
        'merged_files':{name:{'rows':len(df),'columns':len(df.columns)} for name,df in frames.items()}}
    # Independent invariants: no partial month or incomplete quarter enters Mean.
    assert m.loc[~m.Use_In_Panel,'Mean'].isna().all()
    assert m.loc[m.NConflictDays.gt(0),'Mean'].isna().all()
    assert q.loc[q.NMonths.ne(3),'Mean'].isna().all()
    assert (dictionary.loc[~dictionary.Merge_Eligible,'Series'].map(
        lambda s: not any(c.startswith('CMD_'+s+'_') for c in mw))).all()
    # Check a source-to-month anchor by direct numeric averaging, and Q1 aggregation.
    anchor=daily[(daily.Series=='BCOM') & daily.Date.str.startswith('2015-01')].Value.mean()
    assert np.isclose(anchor, mw.set_index('Date').loc['2015-01','CMD_BCOM_Mean'])
    expected=mw[mw.Date.isin(['2015-01','2015-02','2015-03'])].CMD_BCOM_Mean.mean()
    assert np.isclose(expected, qw.set_index('Quarter').loc['2015Q1','CMD_BCOM_Mean'])
    assert sha(rawfile)==digest
    standalone={'Commodity_Daily.csv':daily, 'Commodity_Monthly.csv':m,
        'Commodity_Quarterly.csv':q,'Commodity_Monthly_Wide.csv':mw,
        'Commodity_Quarterly_Wide.csv':qw,'Commodity_Data_Dictionary.csv':dictionary,
        'Commodity_Data_Coverage.csv':coverage,'Commodity_Duplicate_Audit.csv':dup}
    # Staging is on F:, so an Excel save never needs space on C:.
    tempfile.tempdir=str(RAW)
    with tempfile.TemporaryDirectory(prefix='stage_', dir=RAW) as stage_name:
        stage=Path(stage_name)
        for name,df in {**standalone,**frames}.items():
            csv_out(df,stage/name)
            if name in originals:
                saved=pd.read_csv(stage/name)
                check_equal(saved[originals[name].columns], originals[name])
        wb=load_workbook(xlsx)
        sheets={TARGETS[n][1]:df for n,df in frames.items()}
        sheets.update({'Commodity_Monthly':m,'Commodity_Quarterly':q,
                       'Commodity_Dictionary':dictionary,'Commodity_Coverage':coverage})
        for name,df in sheets.items():
            if name in wb: del wb[name]
            ws=wb.create_sheet(name)
            for row in dataframe_to_rows(df.astype(object).where(pd.notna(df),None),index=False,header=True):
                ws.append(row)
            ws.freeze_panes='A2'; ws.auto_filter.ref=ws.dimensions
            for cell in ws[1]:
                cell.font=Font(bold=True,color='FFFFFF')
                cell.fill=PatternFill('solid',fgColor='1F3864')
            for col in ws.columns:
                ws.column_dimensions[col[0].column_letter].width=min(44,max(16,len(str(col[0].value))+2))
        if 'Catatan' in wb:
            msg='Komoditas: CMD_ adalah rata-rata bulanan/kuartalan dalam satuan asli. Bulan parsial dikecualikan; kuartal wajib 3 bulan. Lihat Tio/notes/data_komoditas_den.md.'
            if not any(r[0]==msg for r in wb['Catatan'].iter_rows(values_only=True) if r):wb['Catatan'].append([msg])
        wb.save(stage/xlsx.name); wb.close()
        verify=load_workbook(stage/xlsx.name,read_only=True,data_only=True)
        for filename,(_,sheet) in TARGETS.items():
            assert verify[sheet].max_row==len(frames[filename])+1
            assert verify[sheet].max_column==len(frames[filename].columns)
        assert 'HS_Lookup' in verify and 'Catatan' in verify
        verify.close()
        (stage/'Commodity_Validation_Report.json').write_text(json.dumps(stats,indent=2),encoding='utf-8')
        for f in stage.iterdir(): f.replace(MID/f.name)
    print(json.dumps(stats,indent=2))
    print(coverage.to_string(index=False))

if __name__=='__main__':main()
