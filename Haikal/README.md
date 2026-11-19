# Folder kerja Haikal

Pengaruh depresiasi rupiah terhadap trade balance Indonesia dengan 10 mitra utama (bulanan 2006–2026):
(1) efek agregat, (2) per mitra dagang, (3) per kelompok barang. Metode: ARDL dan local projections.

**Hasil terbaru (versi HS-6): [output/3_ppt/Depresiasi_Rupiah_Trade_Balance.pptx](output/3_ppt/Depresiasi_Rupiah_Trade_Balance.pptx)** (template DEN).
Catatan hasil versi HS-4 lama ada di `archive/v1_hs4_20261116/`.

## Struktur

```
Haikal/
├── notes/
│   ├── 4_litrev_metode.md      tinjauan literatur + alasan pilihan metode
│   ├── catatan_data.md         sumber, definisi, keterbatasan data
│   └── definisi_kelompok_hs6_tio.md  aturan 7 kelompok HS-6 (dari Tio)
├── script/                     nomor = urutan jalan
│   ├── 00_master.do            jalankan semuanya
│   ├── 01_build_panel.py       (Tio) data mentah -> intermediate/dari_tio/
│   ├── 02_prep_data.do         dataset analisis HS-6 + harga komoditas DEN
│   ├── 03_prep_kurs_bilateral.do  kurs riil bilateral (BIS) + data LP
│   ├── 04_ardl_agregat.do      RQ1
│   ├── 05_ardl_mitra.do        RQ2
│   ├── 06_ardl_kelompok.do     RQ3
│   ├── 07_local_projections.do RQ1–RQ3 dengan LP
│   ├── 08_deskriptif_episode.py episode depresiasi, event study, driver R², statistik deskriptif
│   ├── 09_build_ppt.py         bangun PPT dari output/ (template DEN)
│   ├── 10_indeks_harga_volume.py indeks harga (unit value Fisher) & volume dari kuantitas HS-6
│   ├── 11_harga_volume.do      dekomposisi harga vs volume (LP) + uji Marshall-Lerner dengan volume (ARDL)
│   └── helper_ardl.do          program bantu ARDL
├── output/
│   ├── 0_deskriptif/           grafik TB vs REER, uji akar unit, pangsa kelompok
│   ├── 1_ardl/                 tabel (CSV) + grafik ARDL
│   ├── 2_lp/                   tabel (CSV) + grafik LP
│   └── 3_ppt/                  deck PPT + grafik gaya DEN
├── intermediate/
│   ├── dari_tio/               data Tio: Trade_Total/Goods_Month (HS-6), HS6_Classification, Panel_Country_Month
│   └── analisis/               dataset olahan, dibuat ulang oleh script 02–03
├── input/raw/                  data unduhan: fred/ (harga komoditas, USD, inflasi VN), bis/ (kurs, CPI)
├── input/reference/            template_DEN.pptx (layout DEN dari deck Banking Stress Test)
└── archive/v1_hs4_20261116/    versi HS-4 (data, output, catatan hasil)
```

## Menjalankan

Butuh Stata 17+ (dikembangkan di StataNow 19 MP). Dari folder `Haikal/`:

```stata
do script/00_master.do
```

Atau dari terminal (mode batch, log di `00_master.log`):

```bash
MSYS_NO_PATHCONV=1 "/c/Program Files/StataNow19/StataMP-64.exe" /e do script/00_master.do
```

Paket SSC `ardl`, `xtpmg` dan `xtscc` diinstal otomatis. Waktu jalan sekitar 14 menit (LP sekitar 10 menit).

Indeks harga dan volume dibuat SEBELUM Stata (butuh kuantitas HS-6 Trade Map di `input/raw/trademap_hs6_qty/`,
atau cache `intermediate/analisis/hs6_qty_long.csv.gz`; nilai USD dibaca dari `../Tio/intermediate/hs6/`):

```bash
uv run --with pandas --with openpyxl python script/10_indeks_harga_volume.py
```

PPT dibangun setelah Stata selesai (butuh `uv`):

```bash
uv run --with pandas --with matplotlib python script/08_deskriptif_episode.py
uv run --with python-pptx --with pandas --with matplotlib python script/09_build_ppt.py
```

## Konvensi

- **Trade balance** = ln(Ekspor/Impor). Efek dilaporkan sebagai % perubahan rasio X/M akibat depresiasi riil 10%; **positif = membaik**.
- **Hasil akhir hanya CSV dan PNG** di `output/`. Tabel `.dta` sementara tidak disimpan.

## Changelog

- **16 Nov 2026:** ARDL RQ1–RQ3, NARDL, PMG/MG, klasifikasi HS-4.
- **16 Nov 2026:** local projections dengan kurs riil bilateral (BIS).
- **16 Nov 2026:** struktur folder dirapikan: notes bernomor, output per metode, data Tio dipisah dari dataset olahan, script bernomor sesuai urutan jalan.
- **18 Nov 2026:** versi HS-6: kelompok barang dari klasifikasi UNSD (data Tio), agregat Indonesia–dunia, kontrol harga komoditas BCOM/batu bara/CPO (database DEN), uji tambahan (10 mitra, indeks IMF, PDB Indonesia). Versi HS-4 diarsipkan.
- **18 Nov 2026 (2):** PPT disusun ulang (35 slide): teori Marshall-Lerner & J-curve, literatur Indonesia, pertanyaan riset, statistik deskriptif 8 episode depresiasi (event study, heatmap mitra/kelompok, driver R²), literatur metode, daftar variabel, hasil, diagnostik & robustness.
- **19 Nov 2026:** PPT disusun ulang alurnya (ringkasan eksekutif, 6 bagian dengan pertanyaan pemandu, konvensi warna cokelat = memburuk / oranye = membaik). Dekomposisi harga vs volume dari kuantitas HS-6 (Trade Map, 10 mitra): indeks unit value Fisher berantai tahunan, LP terms of trade vs rasio volume, dan uji Marshall-Lerner dengan elastisitas volume.
