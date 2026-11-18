# Cakupan data: seluruh analisis adalah perdagangan Indonesia

Negara pelapor pada 22 workbook adalah Indonesia (kode 360). Pada file ekspor, Indonesia adalah eksportir. Pada file impor, Indonesia adalah importir.

- Agregat: ekspor Indonesia ke seluruh dunia dan impor Indonesia dari seluruh dunia.
- Bilateral: ekspor dan impor Indonesia dengan masing-masing sepuluh mitra.
- Kelompok barang: arus yang sama dirinci ke tujuh kategori hasil klasifikasi HS-6.

Kode WLD atau label World menunjukkan mitra agregat seluruh dunia. Kolom ISO3 pada panel perdagangan menunjukkan kode mitra, bukan negara pelapor. Tidak ada penjumlahan perdagangan antarsemua negara sebagai outcome.

Regresi barang saat ini adalah regresi kategori, bukan regresi untuk tiap kode HS-6. Dataset produk HS-6 tersedia, tetapi estimasi setiap kode secara individual belum dilakukan.

Permintaan luar negeri untuk model agregat memakai proksi GDP sepuluh mitra berbobot ekspor. Proksi ini bukan GDP seluruh dunia dan sudah dicatat sebagai keterbatasan.

Audit scope_audit_indonesia.json memverifikasi metadata 22 workbook serta kecocokan 5.456 nilai TOTAL bulanan terhadap panel intermediate. Ini pemeriksaan asal dan pengolahan data, bukan validasi statistik independen ke sumber nasional.
