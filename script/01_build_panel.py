"""Gabungkan panel IPI/GDP 10 negara + BIS REER + JISDOR + trade HS-4 per mitra.
Pakai:  python script/01_build_panel.py input intermediate
  input/        : 4 file sumber
  intermediate/ : hs_panel/*.csv, Macro_Monthly.csv, HS_Lookup.csv,
                  Panel_Country_Month.csv, Panel_Gabungan_Indonesia.xlsx
raw_dir berisi 4 file (nama dicocokkan pakai pola, prefix hash di nama file diabaikan):
  *Panel_10Negara_IPI_GDP_YoY*.xlsx, *bis_dp_search_export*.xlsx, *Informasi_Kurs_Jisdor*.xlsx, *Indonesia_trade_by_product_10partners*.xlsx
"""
import sys, glob, os
import numpy as np, pandas as pd
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter as L

raw, mid = sys.argv[1], sys.argv[2]
out = mid  # panel gabungan juga disimpan di intermediate/ (dataset olahan)
f = lambda pat: glob.glob(os.path.join(raw, pat))[0]
os.makedirs(os.path.join(mid, 'hs_panel'), exist_ok=True); os.makedirs(out, exist_ok=True)

# ---- kunci negara (panel IPI/GDP vs nama ITC Trade Map)
ISO = {'China':'CHN','United States':'USA','Singapore':'SGP','Japan':'JPN','Malaysia':'MYS','India':'IND',
       'South Korea':'KOR','Thailand':'THA','Vietnam':'VNM','Australia':'AUS'}
ITC = {'China':'China','United States of America':'United States','Singapore':'Singapore','Japan':'Japan',
       'Malaysia':'Malaysia','India':'India','Korea, Republic of':'South Korea','Thailand':'Thailand',
       'Viet Nam':'Vietnam','Australia':'Australia'}
months = pd.date_range('2006-01-01', '2026-10-01', freq='MS')

# ---- REER (BIS, broad, real, 2020=100)
b = pd.read_excel(f('*bis_dp_search_export*'), sheet_name='timeseries observations')
reer = pd.DataFrame({'Date': pd.to_datetime(b['TIME_PERIOD:Period']).dt.to_period('M').dt.to_timestamp(),
                     'REER_BIS_broad': b['OBS_VALUE:Value'].astype(float)}).set_index('Date')

# ---- JISDOR harian -> bulanan (bulan parsial dibuang: Mei-2013 mulai tgl 20, Nov-2026 belum selesai)
j = pd.read_excel(f('*Jisdor*'), header=4).iloc[:, :3]
j.columns = ['NO', 'Tanggal', 'Kurs']
j['Tanggal'] = pd.to_datetime(j['Tanggal'], format='%m/%d/%Y %I:%M:%S %p')
j['Kurs'] = j['Kurs'].astype(str).str.replace('.', '', regex=False).str.replace(',', '.', regex=False).astype(float)
j = j.sort_values('Tanggal'); j['Date'] = j['Tanggal'].dt.to_period('M').dt.to_timestamp()
g = j.groupby('Date')['Kurs']
jis = pd.DataFrame({'JISDOR_avg': g.mean(), 'JISDOR_eop': g.last(), 'JISDOR_nobs': g.count()})
jis = jis.drop([pd.Timestamp('2013-05-01'), pd.Timestamp('2026-11-01')], errors='ignore')

macro = pd.DataFrame(index=months).join(reer).join(jis)
macro.index.name = 'Date'
yoy = lambda s: (s / s.shift(12) - 1) * 100
macro['REER_YoY_pct'] = yoy(macro['REER_BIS_broad'])
macro['JISDOR_avg_YoY_pct'] = yoy(macro['JISDOR_avg'])   # + = rupiah melemah
macro['JISDOR_eop_YoY_pct'] = yoy(macro['JISDOR_eop'])
macro = macro[['REER_BIS_broad','REER_YoY_pct','JISDOR_avg','JISDOR_eop','JISDOR_nobs','JISDOR_avg_YoY_pct','JISDOR_eop_YoY_pct']]

# ---- IPI & GDP YoY (dari panel sebelumnya)
p = pd.read_excel(f('*Panel_10Negara_IPI_GDP_YoY*'), sheet_name='Merged_YoY'); p['Date'] = pd.to_datetime(p['Date']); p = p.set_index('Date')
ipi = {c.split('– ')[1]: p[c] for c in p.columns if c.startswith('IPI')}
gdp = {c.split('– ')[1]: p[c] for c in p.columns if c.startswith('GDP')}

# ---- Trade
T = f('*Indonesia_trade_by_product_10partners*')
tot = {k: pd.read_excel(T, sheet_name=f'Total_{k}') for k in ('Exports', 'Imports')}
rows = []
for itc, name in ITC.items():
    d = pd.DataFrame(index=months); d.index.name = 'Date'
    for k in ('Exports', 'Imports'):
        t = tot[k].copy(); t['Date'] = pd.to_datetime(t['Month']); d[k] = t.set_index('Date')[itc].reindex(months)
    d['Trade_Balance'] = d['Exports'] - d['Imports']; d['Total_Trade'] = d['Exports'] + d['Imports']
    d['Exports_YoY_pct'] = yoy(d['Exports']); d['Imports_YoY_pct'] = yoy(d['Imports'])
    d['IPI_YoY_pct'] = ipi[name].reindex(months); d['GDP_YoY_pct'] = gdp.get(name, pd.Series(dtype=float)).reindex(months)
    d.insert(0, 'ISO3', ISO[name]); d.insert(0, 'Country', name)
    rows.append(d.reset_index())
panel = pd.concat(rows, ignore_index=True)
panel = panel.merge(macro.reset_index(), on='Date', how='left')
panel = panel.rename(columns={'Exports':'Exports_USDk','Imports':'Imports_USDk','Trade_Balance':'Trade_Balance_USDk','Total_Trade':'Total_Trade_USDk'})

# ---- HS-4 per mitra (long, per flow x negara)
hs_rows = 0; lookup = {}; check = []
for flow, sh in (('Export', 'Merged_Exports'), ('Import', 'Merged_Imports')):
    d = pd.read_excel(T, sheet_name=sh, dtype={'HS_Code': str, 'Partner_Code': str})
    for _, r in d[['HS_Code', 'Product']].drop_duplicates().iterrows(): lookup.setdefault(r.HS_Code, r.Product)
    mc = [c for c in d.columns if c[:2] == '20']
    for itc, sub in d.groupby('Partner'):
        iso = ISO[ITC[itc]]
        v = sub.set_index('HS_Code')[mc]; v.columns = pd.to_datetime(v.columns)
        check.append((flow, ITC[itc], v.sum()))
        ly = v.shift(12, axis=1)
        y = (v / ly.where(ly > 0) - 1) * 100
        lg = v.stack().rename('Value_USDk').reset_index().rename(columns={'level_1': 'Date'})
        lg['Value_YoY_pct'] = y.stack().values
        lg.insert(0, 'ISO3', iso); lg.insert(0, 'Flow', flow)
        lg = lg.sort_values(['HS_Code', 'Date'])
        lg.to_csv(os.path.join(mid, 'hs_panel', f'{flow}_{iso}.csv'), index=False, float_format='%.4f', date_format='%Y-%m')
        hs_rows += len(lg)
hs_lookup = pd.DataFrame(sorted(lookup.items()), columns=['HS_Code', 'Product'])
# cek: jumlah HS vs total per negara-bulan
mx = 0
for flow, name, s in check:
    tt = tot['Exports' if flow == 'Export' else 'Imports']; tt = tt.assign(Date=pd.to_datetime(tt['Month'])).set_index('Date')
    inv = {v: k for k, v in ITC.items()}[name]
    diff = (s - tt[inv].reindex(s.index)).abs() / tt[inv].reindex(s.index).replace(0, np.nan)
    mx = max(mx, diff.max())
print('HS rows', hs_rows, '| max rel diff sum(HS) vs Total:', round(mx * 100, 3), '%')

# ---- Excel
notes = [
 'Panel gabungan Indonesia — IPI/GDP 10 negara + BIS REER + JISDOR + perdagangan per mitra. Dibangun otomatis oleh scripts/build_panel.py.',
 'Sheet Panel_Country_Month: 10 mitra dagang utama x bulan (Jan-2006 s.d. Okt-2026). Kunci: ISO3 + Date. Satuan perdagangan: USD ribu (ITC Trade Map via file user).',
 'Exports/Imports = Indonesia -> mitra / mitra -> Indonesia. Trade_Balance = Ekspor - Impor (+ = surplus Indonesia). YoY = (t / t-12 - 1) x 100.',
 'IPI_YoY_pct: seri YoY IPI negara mitra (CEIC/IMF/GSO; Thailand dihitung dari level World Bank). GDP_YoY_pct: kuartalan, terisi hanya di Mar/Jun/Sep/Des, hanya 6 negara (AUS, THA, JPN, USA, MYS, KOR).',
 'REER_BIS_broad: BIS real effective exchange rate, broad basket (64 ekonomi), indeks 2020=100, Indonesia (update 2026-11-05). Naik = apresiasi riil rupiah. Nilai sama untuk semua negara di bulan yang sama (variabel Indonesia).',
 'JISDOR: kurs IDR per USD, harian -> rata-rata (avg) dan akhir bulan (eop) per bulan; JISDOR_nobs = jumlah hari observasi. Bulan parsial dibuang (Mei-2013 mulai tgl 20; Nov-2026 belum selesai). YoY positif = rupiah melemah. Tersedia mulai Jun-2013 (YoY mulai Jun-2014).',
 'Cakupan data berbeda: perdagangan s.d. Agu-2026; REER s.d. Sep-2026; JISDOR s.d. Okt-2026; IPI Thailand s.d. Jan-2026; IPI Australia s.d. Jan-2021; IPI Vietnam mulai 2018; GDP Malaysia YoY mulai 2016.',
 f'Data HS-4 per mitra ada di folder intermediate/hs_panel/ (CSV, {hs_rows:,} baris; terlalu besar untuk Excel). Kolom: Flow, ISO3, HS_Code, Date, Value_USDk, Value_YoY_pct (kosong jika basis t-12 = 0). Gabungkan ke sheet ini lewat ISO3 + Date. Nama produk ada di sheet HS_Lookup.',
 f'Cek konsistensi: selisih terbesar jumlah semua HS vs baris TOTAL per negara-bulan = {mx*100:.2f}% (pembulatan sumber).',
 'Lisensi: seri IPI/GDP dari CEIC (berlisensi) dan data perdagangan dari ITC Trade Map punya syarat penggunaan; cek sebelum repo dipublikasikan.']
xl = os.path.join(out, 'Panel_Gabungan_Indonesia.xlsx')
with pd.ExcelWriter(xl, engine='openpyxl', datetime_format='mmm-yyyy') as w:
    macro.reset_index().to_excel(w, 'Macro_Monthly', index=False)
    panel.to_excel(w, 'Panel_Country_Month', index=False)
    hs_lookup.to_excel(w, 'HS_Lookup', index=False)
    pd.DataFrame({'Catatan': notes}).to_excel(w, 'Catatan', index=False)
    for ws in w.book.worksheets:
        for c in ws[1]:
            c.font = Font(bold=True, color='FFFFFF'); c.fill = PatternFill('solid', fgColor='1F3864'); c.alignment = Alignment(wrap_text=True, vertical='center')
        ws.freeze_panes = 'A2' if ws.title in ('Catatan', 'HS_Lookup') else ('B2' if ws.title == 'Macro_Monthly' else 'D2')
        for i in range(1, ws.max_column + 1): ws.column_dimensions[L(i)].width = 16
    w.book['Catatan'].column_dimensions['A'].width = 160; w.book['HS_Lookup'].column_dimensions['B'].width = 80
    for ws in (w.book['Macro_Monthly'], w.book['Panel_Country_Month']):
        for row in ws.iter_rows(min_row=2):
            for c in row:
                if isinstance(c.value, float): c.number_format = '#,##0.00'
    ws = w.book['Panel_Country_Month']
    for row in ws.iter_rows(min_row=2, min_col=4, max_col=7):
        for c in row: c.number_format = '#,##0'
macro.reset_index().to_csv(os.path.join(mid, 'Macro_Monthly.csv'), index=False, date_format='%Y-%m')
panel.to_csv(os.path.join(out, 'Panel_Country_Month.csv'), index=False, date_format='%Y-%m', float_format='%.4f')
hs_lookup.to_csv(os.path.join(mid, 'HS_Lookup.csv'), index=False)
print('done', panel.shape)
