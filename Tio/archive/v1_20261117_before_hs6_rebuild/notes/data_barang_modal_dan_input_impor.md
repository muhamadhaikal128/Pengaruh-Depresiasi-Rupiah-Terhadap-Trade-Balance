# Barang modal, input impor, dan data yang diperlukan

Pembaruan 17 November 2026. Pertanyaan penelitian ini memerlukan dua lapisan data yang berbeda: klasifikasi penggunaan barang yang diperdagangkan dan ukuran input asing yang tertanam dalam ekspor. Data publik dapat diambil tanpa meminta pengguna membeli/mengunggah dataset baru untuk tahap awal.

## 1. Pisahkan jenis barang dari ketergantungan produsen

- BEC mengelompokkan penggunaan barang: **intermediate inputs**, **capital goods / gross fixed capital formation**, dan **final consumption**. Bahan baku dan input antara adalah fokus paling langsung untuk kanal kenaikan biaya produksi saat rupiah melemah. Mesin/barang modal mempunyai kanal investasi dan produktivitas yang berbeda, sehingga perlu dipisahkan.
- Ekspor suatu barang berlabel BEC intermediate berarti barang itu merupakan input bagi pembelinya. Label tersebut tidak menunjukkan bahwa produsen Indonesia memakai bahan baku impor.
- Mengimpor dan mengekspor HS4 yang sama juga belum mengukur ketergantungan input: input untuk membuat produk ekspor sering berada pada kode HS lain, dan perusahaan pengimpor/pengekspor belum tentu sama.
- Impor input dari sepuluh mitra hanya mencakup sumber tersebut. Eksportir ke AS, misalnya, dapat memakai input impor dari negara lain. Ukuran eksposur produksi perlu memperhitungkan seluruh asal input yang relevan.

## 2. Data yang sudah berhasil diambil

Raw: `Tio/input/raw/import_input_sources_20261117/`.

| Keluaran intermediate | Isi dan status |
|---|---|
| `TiVA_IDN_Export_Foreign_Content_Annual.csv` | 2.212 observasi industri-tahun, Indonesia, 1995-2022; 79 kode industri termasuk agregat yang saling tumpang tindih. Pangsa FVA dan DVA dalam ekspor bruto, satuan persen. |
| `TiVA_IDN_Foreign_Content_Baseline_2003_2005.csv` | Rata-rata FVA industri selama tiga tahun sebelum awal sampel perdagangan 2006; kandidat eksposur struktural untuk interaksi dengan kurs. |
| `BEC5_EndUse_Dictionary.csv` | 178 kategori BEC5, hierarki, label barang/jasa, dan kelompok penggunaan. Ini kamus BEC, bukan klasifikasi HS4 yang sudah selesai. |
| `Import_Input_Source_Validation_Report.json` | Pemeriksaan checksum, keunikan industri-tahun, satuan, negara, frekuensi, dan identitas FVA+DVA. |

Sumber utama TiVA: [OECD Trade in Value Added](https://www.oecd.org/en/topics/sub-issues/trade-in-value-added.html), dataset Principal Indicators shares, edisi 2025 versi 1.1. Kode API terbaru yang digunakan adalah **MEASURE=EXGR_FVA, UNIT_MEASURE=PT_EXGR**, dengan pembanding EXGR_DVA pada satuan sama. Ini memisahkan kode indikator dari satuannya; bukan memakai kode EXGR_FVASH lama sebagai kode measure pada API baru.

FVA adalah nilai tambah asing yang tertanam dalam ekspor, termasuk keterkaitan langsung/tidak langsung serta input jasa. Jadi FVA share adalah **proksi keterkaitan input asing**, bukan koefisien bahan baku impor langsung per HS4 atau persentase biaya bahan baku impor perusahaan.

Semua 5 sumber yang disimpan lolos SHA-256. TiVA hanya memuat Indonesia, counterpart World, frekuensi Annual, unit Percentage of gross exports dengan pengali 0. FVA dan DVA masing-masing berada pada 0-100 persen dan jumlahnya 100 dengan toleransi pembulatan 0,002 poin persentase. Pemeriksaan ini memvalidasi ekstraksi/integrasi, bukan membuktikan estimasi underlying ICIO sepenuhnya bebas kesalahan.

Baseline 2003-2005 dipisahkan dari data tahunan aktual. Memakainya setelah 2022 berarti memakai eksposur struktural periode dasar yang tetap, bukan mengklaim telah mengamati FVA tahun 2023-2026. Tidak ada interpolasi bulanan/kuartalan, extrapolasi tahun terakhir, atau penggabungan otomatis ke HS4.

Jangan menjumlahkan 79 industri/agregat tersebut atau merata-ratakan persentasenya untuk mendapatkan total. Agregat manufaktur dan total ekonomi bertumpang tindih dengan industri rinci. Pilih tingkat industri yang konsisten dengan pemetaan HS.

## 3. Yang masih dibutuhkan untuk menghubungkan ke ekspor HS4

1. **Korespondensi HS-HS6 ke industri ISIC4/OECD TiVA**, sesuai revisi HS. Satu HS4 dapat memuat beberapa industri; alokasinya tidak boleh diasumsikan sama rata berdasarkan jumlah subheading.
2. **Korespondensi HS-BEC sesuai revisi** untuk memisahkan jenis impor. Tabel HS-SITC-BEC dan tabel langsung UN sudah tersedia publik; sebagian sumber lengkapnya telah tersimpan di `hs_commodity_classification_20261117/`. Namun kamus BEC5 yang baru dibuat belum menandakan seluruh pemetaan HS4-BEC sudah selesai.
3. **Nilai perdagangan HS6** akan membantu menyelesaikan heading campuran dan memberikan bobot berdasarkan nilai. Bisa dicari melalui UN Comtrade/BPS. File HS6 yang sudah dimiliki pengguna dapat mempercepat pekerjaan, tetapi tidak wajib untuk memulai pemetaan konservatif dengan kategori campuran tetap terpisah.
4. Jika ingin ukuran **input impor langsung** yang lebih dekat biaya produksi, gunakan matriks penggunaan input impor per sektor dari BPS I-O/SUT atau OECD ICIO. Jika memakai selisih matriks transaksi total dan domestik, kesamaan tahun, harga, klasifikasi, dan perlakuan valuasinya harus diverifikasi terlebih dahulu.

Sumber Indonesia yang relevan adalah [BPS Tabel Input-Output Indonesia 2020](https://www.bps.go.id/id/publication/2025/01/27/ea74e60a8662a70a734fa431/input-output-tables-indonesia-2020.html), termasuk tabel transaksi total dan domestik dengan rincian produk. Pada langkah ini tabel BPS tersebut diidentifikasi sebagai sumber alternatif, belum diekstraksi menjadi koefisien input impor.

Kebutuhan pemetaan industri ini berbeda dari BEC: sebuah mesin ekspor dapat termasuk capital goods, tetapi industri pembuatnya tetap dapat sangat bergantung pada komponen impor. Sebaliknya, barang intermediate ekspor belum tentu mengandung input impor besar.

## 4. Implikasi untuk desain penelitian

- Bagian penggunaan barang: bandingkan intermediate, capital, dan consumption berdasarkan BEC, dengan heading campuran disimpan tersendiri.
- Bagian mekanisme biaya: uji apakah respons depresiasi berbeda menurut intensitas input asing industri. Eksposur baseline sebelum awal sampel dapat dipakai sebagai kandidat interaksi, tetapi validitas identifikasinya tetap perlu dipertimbangkan bersama model utama.
- Jika memakai FVA tahunan aktual, periode sampel harus mengikuti ketersediaan 1995-2022 pada unduhan ini. Data 2006-2022 juga perlu diselaraskan dengan data kurs dan perdagangan yang lengkap. Data tahunan tidak boleh diperlakukan sebagai observasi bulanan independen.
- Ukuran industri yang dipetakan ke HS4 harus disebut **proksi sektor**. Ia tidak mengukur input impor unik setiap produk/perusahaan.
- Replikasi NARDL trade balance tetap berbeda dari pengujian respons ekspor saja. Penurunan ln(M/X), misalnya, tidak mengidentifikasi perubahan ekspor tanpa memeriksa kedua arusnya.

Tidak ada pengguna yang perlu menyerahkan kredensial agar langkah awal ini berjalan. Jika unduhan HS6 tertentu memerlukan akun/API berlangganan, cakupan akses sumbernya perlu dijelaskan; data tidak boleh dinyatakan lengkap sebelum diperiksa.

## 5. Reproduksi

```powershell
python Tio/script/10_fetch_import_input_sources.py
```

Skrip berjalan offline dari raw, memeriksa hash, dan menghasilkan CSV serta laporan validasi. `--download` hanya memulihkan sumber yang hilang dari daftar URL/checksum tetap dalam `import_input_source_requests.json`. Data atau unit sumber yang berubah tidak ditimpa diam-diam.

Rujukan BEC: [manual BEC5 UNSD](https://unstats.un.org/unsd/trade/classifications/Manual%20of%20the%20Fifth%20Revision%20of%20the%20BEC%20%28Edited%29-%20EN.pdf) dan [UN Comtrade Intermediate Goods](https://uncomtrade.org/docs/intermediate-goods-in-trade-statistics/).
