# Folder kerja Haikal

Analisis ARDL pengaruh depresiasi rupiah terhadap trade balance, untuk menjawab tiga pertanyaan:
(1) efek agregat, (2) per mitra dagang, (3) per kelompok barang.

- **Hasil:** [notes/hasil_rq.md](notes/hasil_rq.md)
- **Tinjauan literatur metode (apakah ARDL terbaik):** [notes/litrev_metode_ardl.md](notes/litrev_metode_ardl.md)

## Menjalankan

Butuh Stata 17+ (dikembangkan di StataNow 19 MP). Dari folder `Haikal/`:

```stata
do script/00_master.do
```

Paket `ardl` dan `xtpmg` diinstal otomatis dari SSC bila belum ada. Waktu jalan sekitar 3 menit.

| Script | Isi |
|:--|:--|
| `01_build_panel.py` | (Tio) data mentah → `intermediate/` panel & HS-4 |
| `02_prep_data.do` | dataset analisis, harga komoditas IMF (FRED), klasifikasi HS-4 → kelompok |
| `ardl_helpers.do` | program `ardl_post`: ARDL-EC, uji bounds, diagnostik, dynamic multiplier |
| `03_ardl_agregat.do` | RQ1: agregat, 10 spesifikasi robustness, NARDL, grafik J-curve |
| `04_ardl_mitra.do` | RQ2: ARDL per negara + panel PMG/MG |
| `05_ardl_kelompok.do` | RQ3: per kelompok barang (komoditas/manufaktur, konsumsi/bahan baku/modal) |

## Data tambahan

`input/raw/fred/`: indeks harga komoditas IMF (all, energi, pangan; 2016 = 100), diunduh dari FRED pada 16 Nov 2026. Seri: `PALLFNFINDEXM`, `PNRGINDEXM`, `PFANDBINDEXM`. IPI Indonesia (`IDNPROINDMISMEI`) tidak tersedia di FRED, sehingga pendapatan domestik belum masuk model.

## Changelog Haikal

- **16 Nov 2026:** analisis ARDL RQ1–RQ3, NARDL, PMG/MG, klasifikasi HS-4, catatan hasil dan litrev.
