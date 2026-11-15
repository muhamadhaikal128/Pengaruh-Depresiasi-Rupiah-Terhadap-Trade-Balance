# Catatan data: panel perdagangan × IPI/GDP × REER × JISDOR

Panel bulanan Jan-2006 s.d. Okt-2026 untuk 10 mitra dagang utama Indonesia: China, USA, Singapura, Jepang, Malaysia, India, Korea Selatan, Thailand, Vietnam, Australia. Kunci gabung: `ISO3` + `Date`.

## Lokasi file
| File | Isi |
|---|---|
| `intermediate/Panel_Country_Month.csv` / `Panel_Gabungan_Indonesia.xlsx` | Negara × bulan: ekspor/impor total + YoY, IPI YoY, GDP YoY, REER, JISDOR |
| `intermediate/Macro_Monthly.csv` | REER (BIS) dan JISDOR bulanan + YoY |
| `intermediate/hs_panel/{Export,Import}_{ISO3}.csv` | HS-4 per mitra (±6 juta baris), nilai USD ribu + YoY |
| `intermediate/HS_Lookup.csv` | Nama produk per HS-4 |
| `script/01_build_panel.py` | Pipeline: `python script/01_build_panel.py input intermediate` |

Gabung HS-level ke panel: `hs.merge(panel, on=['ISO3','Date'])`.

## Definisi
- YoY = (t / t-12 − 1) × 100. HS-level: kosong bila nilai t-12 = 0.
- JISDOR harian → `JISDOR_avg` (rata-rata hari kerja) dan `JISDOR_eop` (hari kerja terakhir); `JISDOR_nobs` = jumlah hari. Bulan parsial (Mei-2013, Nov-2026) dibuang. YoY positif = rupiah melemah.
- REER: BIS broad real (64 ekonomi), 2020 = 100, Indonesia; naik = apresiasi riil rupiah. Tanggal akhir bulan diubah ke awal bulan.
- GDP YoY kuartalan: hanya di bulan Mar/Jun/Sep/Des, hanya 6 negara (AUS, THA, JPN, USA, MYS, KOR).
- IPI YoY Thailand dihitung dari level World Bank (USD, 2005 price, NSA); negara lain dari seri YoY sumbernya.
- Satuan perdagangan: USD ribu (ITC Trade Map).

## Keterbatasan
Perdagangan s.d. Agu-2026; REER s.d. Sep-2026; JISDOR s.d. Okt-2026; IPI Thailand s.d. Jan-2026; IPI Australia s.d. Jan-2021; IPI Vietnam mulai 2018; GDP Malaysia YoY mulai 2016. Selisih jumlah HS vs baris TOTAL maksimal 0,023% (pembulatan sumber).

## Lisensi
Seri IPI/GDP dari CEIC (berlisensi) dan ITC Trade Map punya syarat penggunaan; jangan commit data mentah CEIC ke repo publik.
