# Penelitian HS-6: Indonesia, mitra, dan tujuh kelompok barang

Run baru menggunakan 22 workbook Trade Map, nilai perdagangan bulanan 2006-01 sampai 2026-08. Kanal dependensi input impor/TiVA dikeluarkan.

- `input/raw/trademap_hs6_20261117/`: workbook asli dan manifest SHA256.
- `input/reference/`: paper, paket ardl, korelasi HS/SITC/BEC dan audit makro historis.
- `intermediate/`: panel hasil skrip; `hs6/` menyimpan nilai per produk; `macro/` menyimpan snapshot kontrol.
- `script/`: do-file Stata bernomor, master pipeline, dan helper Python di subfolder `python/`.
- `output/tables/oskooee/`: koefisien dan ringkasan, workbook, PNG/PDF tabel.
- `output/figures/oskooee/`: grafik PNG/PDF; `output/gph/oskooee/`: grafik Stata editable.
- `output/diagnostics/`: audit data, registry sampel, log, uji dan validasi.
- `notes/`: definisi kelompok serta narasi hasil setelah estimasi selesai.
- `archive/v1_20261117_before_hs6_rebuild/`: seluruh pekerjaan sebelumnya.

Jalankan pipeline lengkap dari folder Tio dengan `& .\script\00_run.ps1`. Parameter PythonExe, StataExe dan PythonPackages dapat disesuaikan. Bila dataset sudah disiapkan, `do script/00_master.do "F:/Trade-Balance/Tio"` menjalankan estimasi dan diagnostik Stata; wrapper juga menghasilkan tabel gambar, grafik, laporan dan validasi akhir.

Model memakai ln(M/X), q naik=apresiasi, ARDL dan NARDL dengan AIC maksimum 4 lag levels serta sensitivitas cap 2. Tujuh kelompok mencakup dua sumbu klasifikasi dan tidak boleh dijumlahkan: manufaktur nonkomoditas, konsumsi, pertanian/pangan, intermediate, modal, komoditas total, energi/tambang. Kategori ambigu dipertahankan. Workbook tidak menyatakan revisi HS per sel; konsensus lintas revisi digunakan secara konservatif. Baca notes/definisi_kelompok_hs6.md dan audit klasifikasi.

Hasil estimasi dan jumlah artefak final dinyatakan dalam output/diagnostics/oskooee/delivery_validation.json setelah pipeline selesai. Lulus pemeriksaan komputasi tidak berarti setiap model mendukung hubungan jangka panjang atau identifikasi kausal. Semua model tetap dilaporkan beserta diagnostiknya.
