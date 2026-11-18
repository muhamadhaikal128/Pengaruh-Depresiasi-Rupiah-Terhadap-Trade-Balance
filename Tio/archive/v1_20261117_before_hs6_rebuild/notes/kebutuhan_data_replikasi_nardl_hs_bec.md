# Kebutuhan Data untuk Replikasi NARDL J-Curve dan Ekstensi HS/BEC

> Pembaruan sumber input impor: OECD TiVA Indonesia 1995-2022 dan kamus BEC5 telah diunduh; pemetaan HS-BEC/HS-industri belum digabungkan. Lihat [data_barang_modal_dan_input_impor.md](data_barang_modal_dan_input_impor.md).


> Pembaruan klasifikasi HS4 17 November 2026: komoditas/nonkomoditas telah dipisahkan pada `intermediate/hs_classified/`; kode campuran dan khusus disimpan tersendiri. Lihat [klasifikasi_komoditas_hs4.md](klasifikasi_komoditas_hs4.md). Pemetaan BEC dan intensitas input impor masih perlu dilengkapi.


Disusun 17 November 2026. Dasar pemeriksaan: PDF pengguna `bahmani-oskooee2015.pdf`, header CSV, kelengkapan panel Tio, serta dokumentasi klasifikasi resmi. Ini audit kebutuhan data, bukan hasil estimasi.

## 1. Paper yang benar dan konsekuensi untuk metode

PDF lampiran adalah **Bahmani-Oskooee & Fariditavana, Nonlinear ARDL Approach and the J-Curve Phenomenon**, DOI 10.1007/s11079-015-9369-5; online 2015, edisi *Open Economies Review* 27:51–70 tahun 2016. Ia memakai ARDL linear dan NARDL pada perdagangan AS dengan enam mitra, data kuartalan 1971Q1–2013Q3. Ini berbeda dari paper Bahmani-Oskooee & Harvey (2015) tentang industri AS–Indonesia.

Pada persamaan (1) dan appendix PDF, outcome paper adalah log rasio **impor/ekspor**, bukan log selisih ekspor minus impor. Pendapatan memakai **indeks level PDB riil**, bukan GDP YoY atau IPI YoY. Kursnya riil bilateral, dibangun dari kurs nominal dan CPI kedua negara. Replikasi Indonesia dengan periode, negara dan klasifikasi berbeda lebih tepat disebut replikasi metode/adaptasi, bukan reproduksi angka paper asli.

Sumber pembanding metadata dan appendix: [halaman penerbit](https://link.springer.com/article/10.1007/s11079-015-9369-5). Teks lengkap dibaca dari PDF pengguna. Untuk sumber lokal lihat `C:/Users/Administrator/Downloads/bahmani-oskooee2015.pdf`.

**Revisi rekomendasi metode setelah tujuan diperjelas:** ARDL/NARDL menjadi utama untuk replikasi ini. PPML dalam review sebelumnya adalah alternatif untuk pertanyaan ekspor level dengan banyak nol; tidak perlu menggantikan model utama trade balance sekarang.

## 2. Depresiasi, volatilitas, dan ketergantungan input adalah tiga hal berbeda

- **Depresiasi/apresiasi:** arah perubahan level kurs. NARDL memisahkan partial sums perubahan positif dan negatif.
- **Volatilitas:** ketidakpastian/fluktuasi kurs; tidak sama dengan depresiasi. Dapat meningkat tanpa depresiasi bersih.
- **Input impor:** eksposur biaya produksi; harus diukur melalui kebutuhan input/foreign value added, bukan kategori output ekspor saja.

Paper lampiran berfokus pada arah perubahan kurs dan asimetri, bukan memasukkan variabel volatilitas. Untuk replikasi inti, rumuskan hipotesis sebagai sensitivitas terhadap depresiasi/apresiasi. Jika volatilitas juga ingin diuji, tambahkan sebagai ekstensi tersendiri dengan definisi, frekuensi, dan lag yang jelas.

BEC menjelaskan penggunaan barang yang diperdagangkan; barang ekspor kategori intermediate adalah input bagi pengguna di luar negeri, bukan bukti bahwa produsennya di Indonesia memakai input impor.

## 3. Apa yang sudah ada?

`Tio/intermediate/Panel_Country_Month.csv` memuat ekspor/impor total bilateral, identitas negara, IPI/GDP YoY, REER nasional, dan JISDOR nasional. `hs_panel` memuat nilai ekspor/impor HS4 untuk sepuluh mitra: CHN, USA, SGP, JPN, MYS, IND, KOR, THA, VNM, AUS. Identifikasi “top 10” masih perlu dikonfirmasi dari ranking dunia dengan kriteria yang ditetapkan.

Hasil pembacaan aktual panel:

| ISO3 | Baris kalender | Ekspor nonmissing | IPI YoY nonmissing | GDP YoY nonmissing |
|---|---:|---:|---:|---:|
| CHN | 250 | 248 | 215 | 0 |
| USA | 250 | 248 | 249 | 83 |
| SGP | 250 | 248 | 249 | 0 |
| JPN | 250 | 248 | 249 | 82 |
| MYS | 250 | 248 | 129 | 42 |
| IND | 250 | 248 | 246 | 0 |
| KOR | 250 | 248 | 249 | 83 |
| THA | 250 | 248 | 241 | 82 |
| VNM | 250 | 248 | 106 | 0 |
| AUS | 250 | 248 | 181 | 82 |

Catatan: hitungan nonmissing bukan uji validitas semua observasi. GDP YoY berada pada bulan akhir kuartal, sehingga angka 82/83 tidak berarti hanya 82/83 bulan ekonomi diamati. Sebaliknya GDP level tetap belum tersedia untuk replikasi.

REER nasional: 249 observasi, Jan-2006–Sep-2026. JISDOR rata-rata: 161 observasi, Jun-2013–Okt-2026. Panel kalender Jan-2006–Okt-2026 tidak berarti semua variabel lengkap sampai Oktober. Menurut catatan repo, perdagangan berakhir Agustus 2026.

Di Tio, folder data mentah saat diperiksa hanya berisi .gitkeep. Haikal memiliki indeks komoditas umum FRED PALLFNFINDEXM, PFANDBINDEXM dan PNRGINDEXM; ini dapat menjadi sumber bersama setelah mengecek definisi dan asal seri, tetapi belum pengganti seluruh harga komoditas spesifik.

## 4. Matriks kebutuhan menurut bagian penelitian

| Bagian | Sudah tersedia | Tambahan yang diperlukan | Batas interpretasi |
|---|---|---|---|
| A. Trade balance total Indonesia–dunia | REER; bilateral sepuluh mitra | Ekspor dan impor total dunia; PDB riil level Indonesia; indeks aktivitas/PDB riil luar negeri berbobot tetap | Jumlah sepuluh mitra bukan total dunia |
| B. Trade balance tiap sepuluh mitra | Ekspor/impor bilateral; beberapa aktivitas YoY | PDB riil level seluruh mitra dan Indonesia; kurs nominal bilateral + CPI Indonesia/mitra; data ranking mitra | REER nasional tidak dapat disebut kurs riil bilateral |
| C. Respons HS4 komoditas vs nonkomoditas | Nilai ekspor/impor HS4, nama produk | Definisi dan mapping komoditas; versi/konsistensi HS; harga global spesifik; volume/indeks volume untuk klaim ekspor riil | Tidak adanya J-curve bukan bukti tidak ada respons ekspor |
| D1. Trade balance menurut BEC | Perdagangan HS4 | Konkordansi HS–BEC sesuai versi; idealnya nilai HS6 atau bobot HS6 ke HS4 | Menguji jenis penggunaan barang, belum kandungan input impor |
| D2. Ketergantungan bahan baku impor eksportir | Belum ada ukuran kebutuhan input | Tabel penggunaan input impor sektoral BPS I-O/SUT atau OECD ICIO/TiVA, serta mapping HS–industri | Ukuran sektor yang ditempel ke HS adalah proksi sektor, bukan pengukuran kandungan impor unik tiap HS |
| E. Volatilitas tambahan | Rata-rata kurs nasional bulanan | Kurs bilateral nominal harian bila memakai volatilitas dalam bulan; atau seri bulanan panjang untuk GARCH/rolling measure yang ditetapkan | Rata-rata bulanan tidak dapat merekonstruksi volatilitas harian dalam bulan |

### PDB riil dan frekuensi

Ambil **level PDB riil kuartalan** Indonesia dan kesepuluh mitra dari BPS/lembaga statistik nasional, IMF atau OECD sesuai coverage. Indeks semua seri ke basis yang sama; satuan level tidak harus sama untuk regresi bilateral log, tetapi jangan menjumlahkan PDB mata uang lokal lintas negara untuk indeks aktivitas dunia.

Untuk agregat dunia, gunakan indeks PDB/aktivitas mitra yang dinormalisasi dan bobot perdagangan periode dasar; jelaskan apakah cakupannya seluruh tujuan atau hanya sepuluh mitra. Periode dasar untuk pemilihan mitra dan pembobotan sebaiknya ditentukan sebelum hasil estimasi.

**Pilihan paling dekat paper: kuartalan.** Jumlahkan nilai perdagangan tiga bulan; rata-ratakan indeks/kurs bulanan sesuai konvensi yang dipilih, dan gunakan GDP riil kuartalan. Dengan perdagangan sekarang, 2006Q1–2026Q2 merupakan kandidat jendela lengkap sekitar 82 kuartal sebelum kehilangan observasi karena lag/variabel lain. Agustus tidak cukup untuk membentuk 2026Q3 penuh. Verifikasi ulang coverage semua seri sebelum menetapkan sampel.

Sampel ini jauh lebih pendek daripada paper asli. Jangan menyalin batas maksimum delapan lag kuartalan secara mekanis; NARDL dengan terlalu banyak lag dan kontrol mudah kehilangan derajat bebas. Pilihan bulanan dengan level IPI Indonesia/mitra adalah adaptasi lain, tetapi harus mengakui perbedaan proksi dan ketidaklengkapan cakupan sekarang.

### Kurs bilateral

Jika `E_jt` adalah rupiah per unit mata uang mitra:

```text
q_jt = E_jt × CPI_jt / CPI_ID_t
q naik = depresiasi riil rupiah
```

Alternatif yang lebih dekat konvensi paper adalah kebalikannya, dengan penurunan berarti depresiasi. Keduanya sah jika tanda dan partial sums konsisten. Cross rate dari IDR/USD dan kurs mata uang mitra/USD boleh digunakan setelah menyamakan tanggal, quotation dan frekuensi.

JISDOR hanya terhadap USD, sehingga tidak mewakili kurs rupiah terhadap yuan, yen, won, dan lain-lain. REER tetap cocok sebagai ukuran agregat, tetapi bukan sepuluh kurs bilateral yang berbeda.

## 5. Komoditas dan BEC: mapping yang benar

“Commodity” dalam judul/deskripsi studi perdagangan dapat berarti jenis barang secara umum, tidak selalu primary commodity/sumber daya alam. Dalam desain ini, tetapkan komoditas sebagai kategori ekonomi yang eksplisit: misalnya komoditas primer dan produk olahan berbasis sumber daya, dengan definisi sempit/luas sebagai sensitivitas.

Siapkan minimal:

```text
hs_commodity_map.csv
HS_version, HS4, Commodity_flag, Resource_based_flag,
Commodity_group, Price_benchmark, Classification_source

hs_bec_map.csv
HS_version, HS6, HS4, BEC_version, BEC_code,
End_use, Primary_or_processed, Allocation_weight, Mapping_source
```

Jangan memaksa satu label BEC pada semua HS4: satu HS4 dapat mencakup HS6 dengan end-use berbeda. Pilihan terbaik adalah klasifikasi di HS6 terlebih dahulu lalu agregasi. Jika hanya HS4 tersedia, gunakan kelompok campuran atau bobot tahun dasar yang transparan; jangan menggandakan total nilai HS4 untuk setiap kategori BEC yang terhubung.

Sumber: [UNSD BEC](https://unstats.un.org/unsd/trade/classifications/bec.asp), [konkordansi resmi](https://unstats.un.org/unsd/classifications/Econ/), [panduan konversi UN Comtrade](https://uncomtrade.org/docs/hs-sitc-bec-conversion-and-correspondence-tables/).

Harga global: cari benchmark batu bara, sawit, karet, logam, minyak/gas yang sesuai. Harga LME nikel tidak identik harga seluruh produk nikel/feronikel. Pisahkan nilai USD dari harga dan kuantitas; jangan menyimpulkan volume tidak sensitif hanya karena nilai ekspor USD tidak naik. Sumber awal: [World Bank Commodity Markets](https://www.worldbank.org/en/research/commodity-markets).

## 6. Mengukur input impor dalam barang ekspor

Contoh: barang ekspor pakaian dapat memakai benang/kain/kimia impor dengan HS berbeda. Membandingkan impor pakaian dan ekspor pakaian tidak mengukur input pakaian tersebut. Label BEC pakaian sebagai konsumsi juga tidak memberi informasi asal kainnya.

Tiga tingkat data:

1. **Praktis:** intensitas input impor langsung industri = input antara impor yang dipakai industri / seluruh input antara industri. Membutuhkan tabel penggunaan impor menurut industri, bukan tabel impor agregat atau total I-O domestik saja.
2. **Lebih luas:** foreign value-added share dalam gross exports menurut industri dari TiVA; mencakup jaringan input langsung/tidak langsung, tetapi konsepnya berbeda dari pangsa biaya input.
3. **Paling rinci:** data perusahaan yang menghubungkan produk ekspor, bahan baku impor, biaya produksi dan sumber input. Ini diperlukan jika ingin mengetahui kandungan aktual pada eksportir/produk tertentu, tetapi bukan prasyarat studi proksi sektoral.

Mapping HS–ISIC/KBLI–sektor I-O diperlukan pada pilihan 1/2. Jika semua produk sektor diberi MI sama, laporkan itu secara eksplisit. Eksposur 2016 tidak boleh disebut data praperiode untuk sampel sejak 2006. Ambil eksposur yang lebih awal atau desain subsampel setelah tahun dasar, dengan sensitivitas perubahan struktur.

Sumber: [BPS I-O Indonesia 2016](https://www.bps.go.id/id/publication/2021/03/31/081f6b0af2c15c524d72b660/tabel-input---output-indonesia-2016.html), [OECD TiVA/ICIO](https://www.oecd.org/en/topics/sub-issues/trade-in-value-added.html).

Untuk deskripsi impor input nasional yang lengkap, gunakan impor dari **seluruh dunia**, bukan hanya sepuluh mitra ekspor. Klasifikasi BEC impor dapat membantu membentuk kelompok intermediate; tetap tidak cukup untuk mengalokasikan input itu ke industri pengguna tanpa tabel penggunaan.

## 7. Outcome, nol perdagangan, dan pengujian hipotesis

Untuk replikasi literal, gunakan ln(M/X). Bila memakai ln(X/M), jelaskan bahwa itu membalik tanda outcome, bukan model sama dengan interpretasi tanda yang tidak berubah. Dengan X−M sebagai outcome, jangan log saat nol/negatif.

Bila memakai `TB=ln(X/M)` dan `D=-ln(REER)` atau ln(q) yang naik saat depresiasi:

```text
TB_jt = a + b ln(Y_ID_t) + c ln(Y_jt)
        + d_plus Dplus_jt + d_minus Dminus_jt + error

Dplus_t  = sum max(DeltaD_t, 0)
Dminus_t = sum min(DeltaD_t, 0)
```

Ini hanya notasi hubungan level untuk kemudian ditulis dalam ECM/NARDL. Dengan definisi ini, d_plus positif konsisten perbaikan TB saat depresiasi. Respons apresiasi memakai perubahan Dminus yang negatif; tanda koefisien dan tanda kejutan tidak boleh tertukar.

Banyak HS4 memiliki X atau M nol, sehingga log(X/M) tidak terdefinisi. Sebelum memutuskan ribuan NARDL, audit coverage, nol dan panjang seri. Jangan otomatis menambah 1 ke semua nilai: itu mengubah estimand dan bergantung satuan. Pilih seri dengan perdagangan dua arah yang cukup panjang dan laporkan seleksi, atau agregasikan ke kelompok komoditas/BEC yang layak. PPML ekspor/impor terpisah dapat menjadi robustness untuk nol, tetapi bukan replikasi langsung NARDL rasio.

Untuk hipotesis “komoditas kurang sensitif”, uji beda respons antarkelompok beserta ketidakpastiannya. Kelompok A tidak signifikan dan B signifikan belum berarti koefisien A dan B berbeda. Pada ribuan produk, kendalikan multiple testing dan jangan hanya menghitung persentase signifikan.

Trade balance tidak mengidentifikasi kanal ekspor sendiri. Tetap laporkan X dan M terpisah; perbaikan rasio dapat berasal dari penurunan impor. Dominasi komoditas di Indonesia harus dihitung dari pangsa dunia/nasional, bukan diasumsikan dari sampel sepuluh mitra.

## 8. Urutan pengumpulan yang direkomendasikan

1. Tentukan frekuensi kuartalan dan periode bersama, serta definisi “top 10” (misalnya total X+M selama periode dasar).
2. Dapatkan ekspor/impor Indonesia–dunia dan data ranking mitra lengkap.
3. Dapatkan GDP riil level Indonesia + sepuluh mitra, kurs bilateral dan CPI kedua sisi.
4. Jalankan replikasi inti agregat dan per mitra, sambil menguji integrasi (tidak I(2)), stabilitas, kointegrasi dan asimetri formal.
5. Tambahkan mapping komoditas dan harga spesifik; audit kelayakan seri HS4 dan kumpulkan volume.
6. Tambahkan konkordansi BEC/HS6; bedakan end-use dari kandungan input.
7. Dapatkan I-O/ICIO/TiVA dan konkordansi industri untuk menguji moderator impor.
8. Jika tetap meneliti volatilitas, kumpulkan seri kurs berfrekuensi memadai dan pisahkan spesifikasi tambahannya.

Kesimpulan audit: data perdagangan bilateral dan HS4 sudah menjadi fondasi yang baik, tetapi replikasi penuh dan dua mekanisme tambahan belum bisa diselesaikan hanya dengan CSV yang ada. Pengumpulan paling mendesak adalah **GDP riil level, kurs riil bilateral, perdagangan dunia, klasifikasi HS, harga komoditas, dan ukuran input impor sektoral**.

