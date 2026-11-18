# Sumber Data Makro dan Hasil Penggabungan

> Pembaruan komoditas 17 November 2026: kolom CMD_ telah ditambahkan. Lihat [data_komoditas_den.md](data_komoditas_den.md). Jika membangun ulang makro, jalankan skrip 03 -> 06 -> 04 agar kolom komoditas ikut dipulihkan.


> **Pembaruan audit 17 November 2026:** lihat [audit_validitas_data_macro.md](audit_validitas_data_macro.md). Status PASS hanya untuk integritas, bukan jaminan seluruh seri sudah harmonis. Penyambungan satu bulan kurs Vietnam dari GEM ke BIS yang disebut pada versi awal telah dibatalkan; seri GEM penuh disimpan sebagai alternatif terpisah.

Disusun 17 November 2026. Pengunduhan dilakukan sekitar 17 November 2026 waktu Asia/Bangkok; manifest menyimpan waktu UTC. Ini penambahan data, belum estimasi ARDL/NARDL.

## 1. File yang dipakai

Raw disimpan sebagai byte sumber tanpa perubahan pada [macro_external_20261117](../input/raw/macro_external_20261117/). Tersedia JSON/CSV/ZIP asli, metadata, serta SHA-256 dan URL di `download_manifest.json`. Respons gagal disimpan terpisah di `failed_requests/` dan **tidak dipakai sebagai data**. Sumber kandidat yang tidak dipilih juga tetap disimpan untuk audit; hanya sumber pada `Macro_Source_Manifest.csv` yang masuk proses utama.

| Variabel | Sumber utama | Definisi/pengolahan |
|---|---|---|
| Perdagangan Indonesia–dunia | [World Bank GEM](https://datacatalog.worldbank.org/search/dataset/0037798/global-economic-monitor), `DXGSRMRCHNSCD` dan `DMGSRMRCHNSCD` | Merchandise/customs, nominal USD juta, tidak disesuaikan musiman; dikalikan 1.000 menjadi USD ribu agar sama satuan dengan panel bilateral |
| GDP riil level, IDN + 10 mitra | World Bank GEM, `NYGDPMKTPSAKN` | Level kuartalan, seasonally adjusted (SA). Nilai native sumber dipertahankan; variabel analisis diindeks ulang ke rata-rata empat kuartal 2015 = 100 |
| Kurs | [BIS WS_XRU](https://data.bis.org/topics/XRU), frekuensi M, collection A | LCU per USD, period average; kurs silang IDR/valuta mitra dihitung dari rasio dua period-average terhadap USD |
| Harga Indonesia dan sembilan mitra selain Vietnam | [BIS long consumer prices](https://data.bis.org/topics/CPI), frekuensi M, measure 628 | Indeks level, bukan persentase inflasi; nilai native dipertahankan dan diindeks ulang ke rata-rata 12 bulan 2015 = 100 |
| CPI Vietnam | World Bank GEM, `CPTOTNSXN` | Level bulanan NSA; diindeks ulang ke rata-rata 2015 = 100 sebelum perhitungan RER |
| Pembanding kurs Vietnam | World Bank GEM, `DPANUSLCU` | Tidak disambung ke BIS setelah audit menemukan perbedaan material. Agustus 2025 pada keluarga BIS tetap missing |
| Pembanding perdagangan | IMF IFS melalui FRED: `VALEXPIDM052N`, `VALIMPIDM052N`; WDI/WTO: `TX.VAL.MRCH.CD.WT`, `TM.VAL.MRCH.CD.WT` | Disimpan terpisah, tidak disambung atau dirata-ratakan dengan seri GEM |

### Investing.com

Percobaan unduhan `https://www.investing.com/currencies/usd-idr-historical-data` mengembalikan **HTTP 403** pada akses langsung. Tidak ada klaim bahwa seri BIS berasal dari Investing.com. Respons percobaan tersimpan pada `failed_requests/investing_usd_idr.response.html`. BIS dipilih sebagai sumber resmi alternatif yang dapat diunduh dan diulang.

## 2. Pilihan sumber perdagangan dan perbedaan historis

Perdagangan utama menggunakan seri GEM yang eksplisit berbasis customs, agar konsep barangnya dekat dengan panel HS/Trade Map. Seri IMF/FRED dan WDI/WTO tidak identik pada seluruh periode historis. Selisihnya tidak diperlakukan sebagai kesalahan pembulatan atau diperbaiki dengan faktor skala arbitrer.

Contoh hasil penjumlahan 2006, dalam USD juta:

| Sumber | Ekspor | Impor |
|---|---:|---:|
| World Bank GEM customs | 100.798,6 | 61.065,5 |
| IMF/FRED | 103.528 | 80.658 |
| WDI/WTO pada vintage unduhan | 103.527 | 80.650 |

Sumber GEM dan WDI/WTO dapat memiliki cakupan, revisi, atau basis pelaporan berbeda. Penyebab spesifik selisih historis ini belum ditetapkan; jangan menyebut semua seri sudah harmonis. Pada 2010 angka ekspor/impor sudah berdekatan, tetapi tetap periksa semua tahun pada [Trade_World_Annual_Source_Check.csv](../intermediate/Trade_World_Annual_Source_Check.csv). Gunakan satu seri penuh yang dipilih dan lakukan sensitivitas sumber/periode saat estimasi.

## 3. Batas data yang tetap nyata

1. **India sebelum Januari 2013:** dokumentasi BIS memakai WPI, bukan CPI. `Price_Index_2015mean100` menyimpan seri tersebut dengan `Price_Index_Is_WPI_Proxy=True`. `CPI_Index_2015mean100` serta RER berbasis CPI dikosongkan untuk periode ini. Alternatif `RER_With_WPI_Proxy_Index_2015mean100` tersedia dan diberi label tersendiri.
2. **Australia:** seri bulanan BIS merupakan interpolasi dari CPI kuartalan oleh penyedia. Kolom `Price_Index_SourceInterpolated_FromQuarterly` menandainya; tidak ada interpolasi GDP oleh skrip ini. Dokumentasi resmi: [BIS consumer prices](https://www.bis.org/pages/statistics/cp-long-series-documentation.pdf).
3. **AS Oktober 2025:** CPI pada sumber utama kosong. BLS menjelaskan bahwa pengumpulan/release CPI bulan itu terganggu shutdown. Nilainya tidak diisi angka buatan; RER kuartal 2025Q4 AS tetap kosong. [Penjelasan BLS](https://www.bls.gov/cpi/additional-resources/2025-federal-government-shutdown-impact-cpi-faq.htm).
4. GDP GEM Australia dan India terakhir pada 2026Q1; sembilan negara lain sampai 2026Q2 dalam vintage ini. Seri kandidat nasional/IMF yang lebih baru tidak disambung otomatis karena perbedaan penyesuaian, skala dan vintage.
5. Perdagangan dunia utama tersedia Jan-2006–Jun-2026: **246 bulan** pada grid proyek. Seri bilateral lama sampai Agustus 2026 dipertahankan. Bulan sesudah batas data sumber tetap missing, bukan nol.
6. Kurs Vietnam BIS berakhir Agustus 2026 dan mempunyai lubang Agustus 2025; CPI Vietnam GEM Juli 2026. CPI Australia BIS Juni 2026 dan Singapura Juli 2026. Negara lain umumnya CPI sampai September 2026. Rincian coverage lihat CSV, bukan tanggal akhir grid kalender.

Dengan demikian “sudah diunduh” tidak berarti semua negara mempunyai setiap bulan lengkap sampai Oktober 2026. Kekosongan resmi tetap terlihat.

## 4. File intermediate dan cara memakainya

| File | Isi dan kunci |
|---|---|
| [Panel_Country_Month.csv](../intermediate/Panel_Country_Month.csv) | Panel lama 2.500 baris ditambah kolom makro. Kunci `ISO3 + Date`. Semua 18 kolom awal dipertahankan |
| [Macro_Monthly.csv](../intermediate/Macro_Monthly.csv) | Makro Indonesia lama ditambah CPI, perdagangan dunia dan GDP Indonesia yang sparse di bulan akhir kuartal |
| [Panel_Gabungan_Indonesia.xlsx](../intermediate/Panel_Gabungan_Indonesia.xlsx) | Workbook diperbarui; sheet lama lookup/catatan tetap ada, ditambah sheet kuartalan dan sumber makro |
| [Panel_Country_Quarter.csv](../intermediate/Panel_Country_Quarter.csv) | Dataset utama untuk adaptasi kuartalan NARDL. Grid 10 mitra × 84 kuartal; kuartal belum lengkap tetap ada sebagai missing |
| [Panel_World_Quarter.csv](../intermediate/Panel_World_Quarter.csv) | Indonesia–dunia, GDP Indonesia, REER, dan proksi aktivitas luar negeri berbobot ekspor sepuluh mitra |
| [GDP_Real_Quarterly.csv](../intermediate/GDP_Real_Quarterly.csv) | Level dan indeks GDP 11 negara; kunci `ISO3 + Quarter` |
| [CPI_Monthly.csv](../intermediate/CPI_Monthly.csv) | CPI/indeks harga native dan rebased, sumber, serta penanda WPI/interpolasi |
| [FX_Bilateral_Monthly.csv](../intermediate/FX_Bilateral_Monthly.csv) | Kurs USD, kurs silang rupiah, CPI kedua sisi, RER dan sumber |
| [Trade_World_Monthly.csv](../intermediate/Trade_World_Monthly.csv) | Perdagangan total dunia utama, alternatif IMF, neraca dan log rasio |
| [Macro_Data_Coverage.csv](../intermediate/Macro_Data_Coverage.csv) | Jumlah kuartal dengan kombinasi data tersedia per mitra |
| [Macro_Source_Manifest.csv](../intermediate/Macro_Source_Manifest.csv) | URL, jalur raw, waktu pengunduhan, peran dan checksum sumber yang dipakai |
| [Trade_World_Annual_Source_Check.csv](../intermediate/Trade_World_Annual_Source_Check.csv) | Rekonsiliasi tahunan lintas sumber dan persentase perbedaan |
| [Macro_Validation_Report.json](../intermediate/Macro_Validation_Report.json) | Hasil pemeriksaan integritas dan ringkasan coverage |

File HS besar tidak diduplikasi atau ditulis ulang. Untuk menghubungkan makro ke HS, gabungkan `ISO3 + Date` dengan panel bulanan atau gunakan quarter yang diturunkan dari Date ke panel kuartalan. Tetap many-to-one; jangan sampai merge menggandakan observasi HS.

### GDP bulanan dan konvensi kuartal

Dalam panel bulanan, GDP Q1 hanya ditempatkan pada Maret, Q2 Juni, Q3 September dan Q4 Desember. Kolom baru bernama `Partner_GDP_...` dan `IDN_GDP_...`; ini penempatan periode, **bukan tanggal publikasi**. Tidak ada pengulangan level GDP pada tiga bulan seolah menjadi observasi bulanan baru. Untuk replikasi gunakan file kuartalan.

GDP asli dibaca dari seri berlabel constant-LCU SA pada GEM. Nilai/scale native ditahan di `GDP_Real_Level_SourceUnits`; tidak dipaksakan menjadi satuan mata uang yang dapat dijumlahkan antarnegara. Gunakan `GDP_Real_Index_2015mean100` atau log indeks untuk analisis. Rebase tidak menyelesaikan semua structural break atau perbedaan metode national accounts.

Perdagangan kuartalan adalah jumlah **tiga** bulan nonmissing. RER, kurs, CPI, dan REER kuartalan adalah rata-rata tiga observasi bulanan, atau missing jika kurang dari tiga. GDP tidak dijumlahkan dari kolom sparse, tetapi digabung langsung dari sumber kuartalan. Q3 2026 yang hanya memiliki dua bulan perdagangan bilateral tidak dianggap kuartal penuh.

Aktivitas luar negeri pada file dunia adalah **proksi sepuluh mitra**, dengan bobot pangsa ekspor 2006–2008 yang dibekukan. Bukan GDP dunia, bukan penjumlahan GDP mata uang lokal. Bobot disimpan di `Top10_Foreign_Activity_Weights.csv`.

### Kurs dan tanda koefisien

```text
NER_IDR_per_PartnerCurrency = (IDR per USD) / (LCU mitra per USD)
RER_Bilateral_Level = NER × CPI mitra / CPI Indonesia
RER_Bilateral_Index_2015mean100 = rebase rata-rata 2015 menjadi 100
```

Kenaikan NER/RER berarti **depresiasi rupiah**. Kebalikannya berbeda dari arah indeks REER BIS lama, yang naik saat apresiasi. Cross rate ini adalah rasio dua rata-rata bulanan, bukan rata-rata kurs silang transaksi harian.

`Ln_Exports_Imports = ln(X/M)` naik berarti perbaikan rasio. `Ln_Imports_Exports` adalah negatifnya dan disediakan untuk konvensi paper. Keduanya missing jika X atau M tidak positif; tidak ada penambahan konstanta 1.

`Ready_NARDL_CPI` dan `Ready_NARDL_WithPriceProxy` **hanya menandai ketersediaan variabel**, bukan kelulusan uji stasioneritas/kointegrasi. Kuartal missing tetap berada di grid. Jangan menghapus kuartal lalu memampatkan indeks waktu: lag ARDL tidak boleh melompati lubang data dan dianggap berjarak satu kuartal.

## 5. Backup dan reproduksi

Versi sebelum merge disalin ke `input/raw/macro_external_20261117/baseline_before_merge/` untuk CSV panel, CSV makro, dan workbook. Builder menolak jika nilai kolom lama panel telah berubah dari baseline, agar edit lokal tidak diam-diam hilang.

Dependensi dicantumkan di `script/requirements_macro.txt`. Dengan Python yang memiliki dependensi tersebut, jalankan dari root repo:

```powershell
python -m pip install -r Tio/script/requirements_macro.txt
python Tio/script/02_download_macro_sources.py
python Tio/script/03_merge_macro_external.py
python Tio/script/04_validate_macro_external.py
```

Downloader default memeriksa checksum dan menggunakan snapshot yang sudah ada. Opsi `--refresh` mengganti vintage sumber secara eksplisit; simpan snapshot lama jika hendak membandingkan revisi. Skrip 03 dan 04 berjalan offline dari file raw.

Pada sesi ini dependensi tambahan openpyxl diletakkan di folder sementara drive F, bukan dimasukkan ke repo. Tidak ada push ke GitHub atau perubahan pada folder Haikal.

## 6. Ruang lingkup pemeriksaan

Pemeriksaan mencakup: seluruh kolom lama tidak berubah; kunci unik dan jumlah baris; GDP merupakan level kuartalan; rata-rata indeks tahun dasar 100; konversi USD juta → ribu; arah kurs silang; flag proksi; agregasi kuartal lengkap; keberadaan lubang CPI AS; SHA-256 sumber; dan jumlah baris workbook.

Perbedaan sumber perdagangan historis dilaporkan sebagai temuan kualitas data, bukan disembunyikan agar tes lolos. Dataset belum mencakup mapping HS–BEC, kandungan input impor, atau volume ekspor; itu tahap pengumpulan lain di luar permintaan empat kelompok makro ini.
