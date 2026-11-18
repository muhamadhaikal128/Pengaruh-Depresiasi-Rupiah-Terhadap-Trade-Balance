# Catatan data

## A. Data panel dari Tio (`intermediate/dari_tio/`)

Panel bulanan Jan-2006 s.d. Okt-2026 untuk 10 mitra dagang utama Indonesia: China, USA, Singapura, Jepang, Malaysia, India, Korea Selatan, Thailand, Vietnam, Australia. Kunci gabung: `ISO3` + `Date`.

| File | Isi |
|---|---|
| `Panel_Country_Month.csv` / `Panel_Gabungan_Indonesia.xlsx` | Negara × bulan: ekspor/impor total + YoY, IPI YoY, GDP YoY, REER, JISDOR |
| `Macro_Monthly.csv` | REER (BIS) dan JISDOR bulanan + YoY |
| `hs_panel/{Export,Import}_{ISO3}.csv` | HS-4 per mitra (±6 juta baris), nilai USD ribu + YoY |
| `HS_Lookup.csv` | Nama produk per HS-4 |
| `script/01_build_panel.py` | Pipeline Tio: `python script/01_build_panel.py <folder data mentah> intermediate/dari_tio` |

**Definisi:**
- **YoY** = (t / t-12 − 1) × 100. Di level HS, kosong bila nilai t-12 = 0.
- **Trade_Balance_USDk** = Ekspor − Impor (+ = surplus). Model Haikal memakai **ln(Ekspor/Impor)**.
- **JISDOR:** harian diubah ke `JISDOR_avg` (rata-rata hari kerja) dan `JISDOR_eop` (hari kerja terakhir). Bulan parsial (Mei-2013, Nov-2026) dibuang. YoY positif = rupiah melemah.
- **REER:** BIS broad real (64 ekonomi), 2020 = 100. Naik = apresiasi riil rupiah.
- **GDP YoY** kuartalan, hanya 6 negara (AUS, THA, JPN, USA, MYS, KOR).
- **IPI YoY Thailand** dihitung dari level World Bank; negara lain dari seri YoY sumbernya.
- **Satuan perdagangan:** USD ribu (ITC Trade Map).

**Keterbatasan:**
- Perdagangan s.d. Agu-2026; REER s.d. Sep-2026; JISDOR s.d. Okt-2026.
- IPI: Thailand s.d. Jan-2026, Australia s.d. Jan-2021, Vietnam mulai 2018, Malaysia mulai sekitar 2016.

**Lisensi:** seri IPI/GDP dari CEIC (berlisensi) dan ITC Trade Map punya syarat penggunaan. Jangan commit data mentah CEIC ke repo publik.

## B. Data tambahan Haikal (`input/raw/`, diunduh 16 Nov 2026)

| File | Sumber | Dipakai untuk |
|---|---|---|
| `fred/PALLFNFINDEXM.csv`, `PNRGINDEXM.csv`, `PFANDBINDEXM.csv` | IMF Primary Commodity Prices via FRED (2016 = 100): semua komoditas, energi, pangan | kontrol harga komoditas |
| `fred/DTWEXBGS.csv` | Fed, indeks dolar AS broad (harian, dirata-rata bulanan) | instrumen LP-IV (gagal, lemah) |
| `fred/FPCPITOTLZGVNM.csv` | World Bank, inflasi tahunan Vietnam | CPI Vietnam (pendekatan) |
| `bis/bis_xru_monthly.csv` | BIS WS_XRU, kurs per USD rata-rata bulanan, 10 negara + Indonesia | kurs riil bilateral |
| `bis/bis_cpi_monthly.csv` | BIS WS_LONG_CPI, indeks CPI bulanan, 9 mitra + Indonesia + AS | kurs riil bilateral |

**Penyesuaian:**
- CPI Vietnam tidak ada di BIS. Indeks bulanannya dibentuk dari inflasi tahunan World Bank, dibagi rata per bulan; laju 2026 diasumsikan sama dengan 2025.
- CPI AS Okt-2025 tidak dirilis BLS (government shutdown), dan kurs VND Agu-2025 kosong. Keduanya diisi interpolasi linear.
- IPI Indonesia tidak tersedia di FRED, jadi pendapatan domestik belum masuk model agregat.

## C. Dataset olahan Haikal (`intermediate/analisis/`, dibuat ulang oleh script)

| File | Dibuat oleh | Isi |
|---|---|---|
| `commodity_prices.dta` | 02 | ln indeks harga komoditas |
| `ana_partner.dta`, `ana_aggregate.dta` | 02 | panel mitra × bulan dan agregat 10 mitra, variabel log, dummy |
| `hs4_groups.csv/.dta` | 02 | klasifikasi HS-4: sektor (pertanian / energi & tambang / manufaktur) dan end use (konsumsi / bahan baku / modal) |
| `ana_group.dta`, `trade_group_partner.dta` | 02 | perdagangan per kelompok barang (total dan per mitra) |
| `rer_bilateral.dta` | 03 | kurs riil bilateral rupiah vs 10 mitra |
| `lp_aggregate.dta`, `lp_partner.dta`, `lp_group_partner.dta` | 03 | data untuk local projections |
