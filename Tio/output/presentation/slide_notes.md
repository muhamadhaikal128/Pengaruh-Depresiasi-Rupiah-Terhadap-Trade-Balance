## 001. Depresiasi Rupiah dan Neraca Perdagangan Indonesia

Penelitian Tio berdasarkan 22 workbook Trade Map HS-6 dan 516 estimasi Stata. Template cover, foto, font dan palet mengikuti benchmark pengguna. Deck utama menguraikan hasil; deck lengkap melampirkan semua respons utama dan sensitivitas.

## 002. Apakah depresiasi selalu memperbaiki neraca perdagangan?

Apakah depresiasi selalu memperbaiki neraca perdagangan?

Hipotesis penelitian adalah bahwa depresiasi tidak memberikan manfaat yang seragam bagi neraca Indonesia. Hipotesis tersebut lebih sempit daripada pernyataan bahwa depresiasi selalu merugikan: beberapa pasar atau jenis barang dapat membaik, sebagian tidak berubah secara terukur, dan sebagian lain memburuk. Kerangka dinamis digunakan karena penyesuaian tidak harus selesai pada kuartal yang sama. Perlu dijaga batas antara pertanyaan tentang ekspor dan pertanyaan tentang neraca. Model mengamati impor relatif terhadap ekspor, sehingga perubahan keduanya dapat menghasilkan pola yang sama.

SUMBER DAN REPRODUKSI
Sumber: data dan keluaran Stata proyek Tio; pembahasan peneliti.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 003. Analisis bergerak dari struktur perdagangan ke respons yang terukur

Analisis bergerak dari struktur perdagangan ke respons yang terukur

Deck utama dibangun untuk pembahasan penelitian. Bagian lampiran dalam versi lengkap berfungsi sebagai atlas: setiap seri utama memiliki halaman ARDL dan NARDL yang berdampingan; sensitivitas disusun menurut perubahan spesifikasi. Grafik koefisien menyajikan interval agar pembaca dapat melihat ketepatan estimasi. Rangkaian ini mencegah pemilihan hanya model yang tampak sesuai hipotesis.

SUMBER DAN REPRODUKSI
Sumber: data dan keluaran Stata proyek Tio; pembahasan peneliti.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 004. Surplus perdagangan tidak dengan sendirinya mengungkapkan pengaruh kurs

Surplus perdagangan tidak dengan sendirinya mengungkapkan pengaruh kurs

Grafik ini adalah statistik deskriptif dari baris TOTAL workbook Indonesia–seluruh dunia, bukan fitted value model. Nilai nominal dipengaruhi harga, volume, permintaan domestik, aktivitas mitra dan perubahan komposisi. Episode surplus juga dapat bertepatan dengan penguatan harga komoditas atau lemahnya impor. Tanpa desain identifikasi tambahan, arah kurs pada suatu tahun tidak dapat diberi tanggung jawab atas seluruh perubahan neraca. Data Juli–Agustus 2026 belum merupakan kuartal atau tahun lengkap dan tidak dipakai dalam grafik tahunan ini.

SUMBER DAN REPRODUKSI
Sumber: Trade_Total_Quarter.csv; baris TOTAL Trade Map. USD ribu dikonversi menjadi USD miliar.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 005. Sampel agregat mencakup 61 kuartal dengan variasi neraca yang besar

Sampel agregat mencakup 61 kuartal dengan variasi neraca yang besar

Statistik dihitung pada tanggal yang benar-benar masuk desain NARDL agregat Indonesia, bukan pada seluruh raw data. Angka ekspor dan impor adalah nilai per kuartal. Neraca dapat negatif meskipun rata-ratanya positif, menunjukkan bahwa rata-rata jangka panjang tidak mewakili seluruh pengalaman sampel. Indeks GDP riil dibentuk pada basis rata-rata 2015 dan bukan pertumbuhan GDP. Indeks aktivitas luar negeri adalah agregat tetap sepuluh mitra. Tanggal awal data tersedia dan tanggal awal estimasi berbeda karena penyiapan lag.

SUMBER DAN REPRODUKSI
Sumber: WORLD_NARDL_AIC4_design.dta; Trade_Total_Quarter.csv; descriptive_world_estimation_sample.csv.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 006. Sepuluh mitra mencakup sebagian besar perdagangan, tetapi polanya berbeda

Sepuluh mitra mencakup sebagian besar perdagangan, tetapi polanya berbeda

Penyebut pangsa pada panel kanan adalah seluruh ekspor Indonesia ke dunia, bukan ekspor yang hanya ditujukan ke sepuluh mitra. Karena itu, pangsa kesepuluh negara tidak dijumlahkan menjadi seratus persen. Negara-negara ini merupakan mitra yang dipilih dalam penelitian; grafik tidak mengklaim bahwa daftar tersebut persis peringkat sepuluh negara terbesar pada setiap tahun. Perbedaan surplus dan defisit bilateral tidak secara langsung menentukan signifikansi koefisien kurs. Model tetap mengendalikan aktivitas riil Indonesia dan masing-masing mitra.

SUMBER DAN REPRODUKSI
Sumber: Trade_Total_Quarter.csv; nilai 2025 lengkap. Pangsa memakai TOTAL perdagangan Indonesia.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 007. Komoditas penting bagi ekspor, tetapi manufaktur juga berperan besar

Komoditas penting bagi ekspor, tetapi manufaktur juga berperan besar

Definisi komoditas menggunakan kelompok A11 UNCTAD: pangan dan bahan mentah pertanian, bahan bakar, bijih dan mineral, serta logam dan komoditas mineral tertentu. Manufaktur nonkomoditas adalah kategori pelengkap yang dapat dipetakan secara konsisten. Penyebut grafik adalah jumlah rincian HS-6, sehingga mixed dan unclassified tetap terlihat. Pangsa yang ditampilkan khusus 2025; angka seluruh periode tidak diberi label sebagai pangsa tahun tersebut. Harga komoditas internasional dapat menjadi salah satu alasan respons kurs berbeda, tetapi komposisi saja tidak mengidentifikasi saluran itu.

SUMBER DAN REPRODUKSI
Sumber: Classification_Coverage_By_Year.csv; UNSD HS–SITC; UNCTAD A11. Mixed tetap terpisah.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 008. BEC menjelaskan penggunaan barang, bukan kandungan impor dalam ekspor

BEC menjelaskan penggunaan barang, bukan kandungan impor dalam ekspor

BEC Rev.5 memisahkan penggunaan SNA dari kategori ekonomi. Karena itu, intermediate goods bukan sinonim nonkomoditas dan barang konsumsi bukan sinonim manufaktur. Bahan pangan dapat menjadi konsumsi akhir, sedangkan komoditas pertanian lain merupakan input produksi. Pengujian kandungan impor ekspor memerlukan informasi hubungan input-output atau transaksi perusahaan yang tidak menjadi bagian run ini. Kode dengan beberapa kemungkinan penggunaan tetap ambigu; pemetaan tersebut tidak dipaksa mengikuti hipotesis.

SUMBER DAN REPRODUKSI
Sumber: UNSD BEC Rev.5 dan korespondensi 2022; Classification_Coverage_By_Year.csv.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 009. Tujuh kelompok memakai dua dimensi klasifikasi yang bertumpang tindih

Tujuh kelompok memakai dua dimensi klasifikasi yang bertumpang tindih

Panel kelompok dibentuk dari kode HS-6, bukan dari pemaksaan klasifikasi di tingkat HS-4. Meski lebih rinci, kode yang berubah makna antar revisi tetap menimbulkan persoalan. Pengelompokan menggunakan konsensus konservatif dari korespondensi resmi, sebab workbook tidak menyebut revisi HS untuk tiap observasi. Cakupan yang tidak dapat ditentukan dikeluarkan dari kelompok terkait tetapi tetap berada dalam TOTAL. Tumpang tindih kelompok juga berarti bahwa hasil tujuh regresi tidak dapat dianggap tujuh eksperimen independen.

SUMBER DAN REPRODUKSI
Sumber: Trade_Goods_Quarter.csv; HS6_Classification.csv. Kelompok tidak boleh dijumlahkan.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 010. Variabel model mempertahankan definisi paper dan orientasi kurs

Variabel model mempertahankan definisi paper dan orientasi kurs

Outcome mempertahankan log impor atas ekspor. GDP bukan pertumbuhan tahunan, melainkan log indeks level riil. Kurs disusun sehingga kenaikannya berarti apresiasi di seluruh model. Untuk dunia dipakai REER BIS, sedangkan untuk bilateral digunakan negatif log RER pada dataset. Partial sums dibentuk berurutan pada sampel tiap kasus; celah waktu tidak dirapatkan. BCOM tidak masuk baseline.

SUMBER DAN REPRODUKSI
Sumber: Bahmani-Oskooee & Fariditavana; konstruksi dataset Tio; kontrol BCOM hanya sensitivitas.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 011. Kurs dan neraca bergerak bersama banyak perubahan ekonomi

Kurs dan neraca bergerak bersama banyak perubahan ekonomi

Rasio impor terhadap ekspor berada di atas satu saat impor melebihi ekspor. REER pada panel bawah disusun pada orientasi apresiasi. Perbandingan dua deret dapat menunjukkan episode yang menarik untuk didiskusikan, tetapi juga rentan terhadap tren, kejutan bersama dan perbedaan waktu penyesuaian. Estimasi dinamis memasukkan aktivitas ekonomi, namun tidak dengan sendirinya menyelesaikan endogenitas kurs. Karena itu, bahasa hasil dipertahankan sebagai hubungan kondisional, bukan efek kausal yang sudah teridentifikasi.

SUMBER DAN REPRODUKSI
Sumber: WORLD_NARDL_AIC4_design.dta; Trade_Total_Quarter.csv. Grafik bersifat deskriptif.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 012. Perbedaan rentang sampel membatasi perbandingan antarmitra

Perbedaan rentang sampel membatasi perbandingan antarmitra

India menggunakan CPI murni mulai 2013 pada data tersedia; setelah holdback lag, sampel estimasi menjadi 49 kuartal. WPI hanya dipakai sebagai sensitivitas terpisah. CPI AS Oktober 2025 dan kurs Vietnam Agustus 2025 kosong pada keluarga seri utama. Program memilih jendela lengkap terpanjang dan tidak menyambung sisa kuartal seolah tidak ada celah. Tindakan ini mempertahankan arti lag, tetapi mengurangi keseragaman rentang waktu. Pembandingan antarmitra belum merupakan uji formal pada sampel yang sama.

SUMBER DAN REPRODUKSI
Sumber: case_registry.csv; results_primary_models.csv; audit_validitas_data_macro.md.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 013. Pengaruh harga relatif bergantung pada cara barang diperdagangkan

Pengaruh harga relatif bergantung pada cara barang diperdagangkan

Uraian ini merupakan penafsiran ekonomi yang memotivasi pengelompokan, bukan mekanisme yang telah diidentifikasi dari regresi. Nilai perdagangan menggabungkan komponen harga dan volume. Keduanya tidak dapat dipisahkan karena file HS-6 tidak berisi kuantitas yang digunakan dalam run. Pembagian komoditas dan manufaktur membantu menguji heterogenitas rasio neraca, tetapi belum mengestimasi pass-through kurs ke harga ekspor atau elastisitas permintaan ekspor secara terpisah. Pengujian kanal input impor sengaja tidak dimasukkan.

SUMBER DAN REPRODUKSI
Sumber: data dan keluaran Stata proyek Tio; pembahasan peneliti.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 014. J-curve memerlukan fase awal memburuk dan fase berikutnya membaik

J-curve memerlukan fase awal memburuk dan fase berikutnya membaik

Paper mendefinisikan J-curve melalui pemburukan jangka pendek yang diikuti perbaikan jangka panjang. Grafik ilustratif hanya membantu menjelaskan urutan tersebut. Dalam data penelitian, ketidakpastian pada kedua fase tetap perlu diperiksa. Karena interval yang dipakai pointwise, pemilihan horizon tertentu sesudah melihat grafik tidak menjadi uji simultan yang sah. Analisis titik kurva selanjutnya diberi nama pemeriksaan visual-operasional agar tidak tertukar dengan pengujian formal paper.

SUMBER DAN REPRODUKSI
Sumber konsep: Bahmani-Oskooee & Fariditavana (2015/2016). Kurva ilustratif, bukan data.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 015. Penelitian ini mengadaptasi paper, bukan menyalin seluruh spesifikasinya

Penelitian ini mengadaptasi paper, bukan menyalin seluruh spesifikasinya

Paper menggunakan enam pasangan bilateral AS, yaitu Kanada, Prancis, Jerman, Italia, Jepang dan Inggris, pada sampel yang jauh lebih panjang. Pembatasan empat lag level dalam penelitian ini adalah penyesuaian terhadap sampel Indonesia yang lebih pendek dan tidak boleh disamakan dengan delapan lag first difference paper. Implementasi bounds memakai paket ardl 1.0.6 dan nilai kritis finite-sample yang tersedia. CUSUMSQ dalam proyek adalah aproksimasi Monte Carlo, bukan salinan tabel kritis paper.

SUMBER DAN REPRODUKSI
Sumber: paper pengguna, bagian metode dan hasil; master do-file Tio.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 016. ARDL memberi satu hubungan kurs untuk apresiasi dan depresiasi

ARDL memberi satu hubungan kurs untuk apresiasi dan depresiasi

Persamaan ini adalah bentuk jangka panjang untuk menjelaskan koefisien. Estimasi aktual tetap memakai dinamika ARDL dan representasi error correction. GDP domestik diharapkan berkaitan dengan permintaan impor, sedangkan aktivitas mitra berkaitan dengan permintaan ekspor, tetapi tanda empiris dapat berbeda karena nilai perdagangan memuat banyak komponen. Kurs yang naik adalah apresiasi. Pada outcome impor atas ekspor, koefisien kurs positif mengarah pada perbaikan ketika depresiasi, sedangkan koefisien negatif mengarah pada pemburukan.

SUMBER DAN REPRODUKSI
Sumber: Bahmani-Oskooee & Fariditavana; implementasi Stata Tio.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 017. NARDL memisahkan akumulasi apresiasi dan depresiasi

NARDL memisahkan akumulasi apresiasi dan depresiasi

Partial sums mempertahankan seluruh urutan perubahan kurs dalam jendela kasus. Variabel depresiasi adalah akumulasi perubahan negatif sehingga nilainya tidak diberi tanda positif secara paksa. Koefisien apresiasi dan depresiasi kemudian dapat berbeda. Dalam penelitian ini tidak ada regressor volatilitas, sehingga perbedaan dua koefisien tidak boleh disebut bukti pengaruh volatilitas. Model nonlinear di sini juga tidak mengidentifikasi perubahan rezim struktural yang tidak dimodelkan.

SUMBER DAN REPRODUKSI
Sumber: persamaan dekomposisi dan NARDL paper; analysis_quarterly.dta.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 018. Error correction menghubungkan penyesuaian awal dan hubungan level

Error correction menghubungkan penyesuaian awal dan hubungan level

Persamaan menunjukkan komponen level tertunda dan first difference. Panjang lag aktual dipilih dengan AIC dan tercantum untuk setiap model dalam atlas. Bentuk umum ini tidak berarti seluruh suku diestimasi bebas pada setiap spesifikasi; ketika lag suatu regressor nol, reparameterisasi error correction dapat mengandung pembatasan yang sesuai dengan persamaan level. Ekuivalensi fitted value dan residual antara model level dan ECM sudah diperiksa. Koefisien jangka panjang diperoleh melalui normalisasi, sehingga interpretasinya bergantung pada keberadaan hubungan level yang valid.

SUMBER DAN REPRODUKSI
Sumber: ardl_helpers.do; Bahmani-Oskooee & Fariditavana; output koefisien Stata.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 019. Asimetri dan kointegrasi menjawab pertanyaan yang berbeda

Asimetri dan kointegrasi menjawab pertanyaan yang berbeda

Wald jangka panjang menguji kesamaan koefisien kedua partial sums. Uji jangka pendek membandingkan jumlah koefisien perubahan dalam parameterisasi yang digunakan. Bounds menilai keberadaan hubungan level dengan distribusi kritis yang tidak sama dengan uji F biasa. Penelitian memakai F dan t bersama, kemudian memeriksa joint-X untuk menghindari pembacaan hubungan level yang terdegenerasi. Risiko integrasi orde dua juga ditandai; gagal menolak unit root bukan bukti pasti integrasi orde dua.

SUMBER DAN REPRODUKSI
Sumber: estat ectest; uji Wald; diagnostic_summary.csv.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 020. Tanda grafik diubah agar perbaikan neraca berada di atas nol

Tanda grafik diubah agar perbaikan neraca berada di atas nol

Semua panel respons dalam deck menggunakan negatif respons model sehingga nilai positif menunjukkan perbaikan log ekspor atas impor. Interval ikut dibalik dengan menukar batas bawah dan atas setelah dikali negatif. Transformasi ini tepat secara aljabar dan tidak mengubah ketidakpastian. Besaran guncangan sama dalam log: kenaikan sepuluh persen pada indeks apresiasi berpasangan dengan penurunan sekitar sembilan koma nol sembilan persen, bukan penurunan tepat sepuluh persen. Poin log kali seratus bukan perubahan persentase surplus dolar.

SUMBER DAN REPRODUKSI
Sumber: transformasi tepat dynamic_multipliers.csv; tidak ada estimasi ulang.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 021. Hanya sebagian model lolos seluruh penyaringan yang digunakan

Hanya sebagian model lolos seluruh penyaringan yang digunakan

Dari 176 model utama, 95 menolak hipotesis tidak ada hubungan level menggunakan F dan t pada taraf lima persen. Syarat tambahan joint-X, kestabilan akar, risiko integrasi orde dua dan minimal lima belas derajat bebas menyisakan 62. Sebanyak 28 juga tidak ditolak oleh himpunan diagnostik yang digunakan. Jumlah ini bukan ukuran probabilitas model benar dan bukan validasi kausal. Penolakan diagnostik bersifat sinyal untuk meninjau spesifikasi, bukan alasan mekanis menghapus observasi atau memilih model yang mendukung hipotesis.

SUMBER DAN REPRODUKSI
Sumber: analysis_validation_report.json; results_primary_models.csv.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 022. Agregat Indonesia belum memberi hubungan jangka panjang yang kuat

Agregat Indonesia belum memberi hubungan jangka panjang yang kuat

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (2,3,0,4). Koefisien kurs yang relevan untuk depresiasi 0,4292, interval nominal 95% [-1,5289; 2,3873], probabilitas nominal 0,661. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -2,18, kuartal keempat -4,11, kuartal ke-24 3,97 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (2,0,3,0,4). Koefisien kurs yang relevan untuk depresiasi 2,5724, interval nominal 95% [0,1277; 5,0172], probabilitas nominal 0,040. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 5,83, kuartal keempat 10,56, kuartal ke-24 24,43 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: dynamic_multipliers.csv; results_primary_models.csv. Band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 023. Signifikansi depresiasi pada NARDL agregat Indonesia belum menyelesaikan masalah level

Signifikansi depresiasi pada NARDL agregat Indonesia belum menyelesaikan masalah level

Pada NARDL agregat Indonesia, koefisien depresiasi positif dan probabilitas nominal berada di bawah lima persen. Wald juga menolak kesamaan dua koefisien. Namun p-value upper bound F sekitar 0,094 dan t sekitar 0,279, sehingga syarat F dan t pada lima persen tidak terpenuhi. CUSUMSQ juga memberi catatan stabilitas. Karena itu, membaca hanya bintang pada koefisien akan menghasilkan kesimpulan yang lebih kuat daripada yang didukung spesifikasi. ARDL agregat Indonesia tidak memiliki koefisien kurs yang signifikan dan tidak mendukung hubungan level.

SUMBER DAN REPRODUKSI
Sumber: WORLD_ARDL_AIC4; WORLD_NARDL_AIC4; koefisien dan bounds Stata.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 024. Perpanjangan sampel menjadi pemeriksaan ketahanan hasil agregat

Perpanjangan sampel menjadi pemeriksaan ketahanan hasil agregat

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (2,3,2,3). Koefisien kurs yang relevan untuk depresiasi 1,7167, interval nominal 95% [-2,5272; 5,9606], probabilitas nominal 0,422. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 1,04, kuartal keempat -0,23, kuartal ke-24 14,02 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (2,3,2,1,3). Koefisien kurs yang relevan untuk depresiasi 6,3205, interval nominal 95% [-5,5919; 18,2330], probabilitas nominal 0,293. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 10,23, kuartal keempat 17,00, kuartal ke-24 52,80 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: dynamic_multipliers.csv; results_primary_models.csv. Band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 025. Respons bilateral tidak dapat dirangkum menjadi satu elastisitas nasional

Respons bilateral tidak dapat dirangkum menjadi satu elastisitas nasional

Garis horizontal memperlihatkan ketepatan estimasi, bukan hanya tanda koefisien. Koefisien yang relevan untuk depresiasi adalah koefisien kurs pada ARDL dan koefisien partial sum negatif pada NARDL. Warna cokelat berarti syarat level dan diagnostik yang digunakan terpenuhi; emas berarti ada dukungan level tetapi catatan diagnostik; simbol kosong berarti syarat level belum lengkap. Perbedaan dua estimasi yang intervalnya berbeda belum merupakan uji langsung perbedaan antar negara. Jendela sampel juga tidak seragam.

SUMBER DAN REPRODUKSI
Sumber: hasil Stata dan data HS-6 proyek Tio; CI nominal 95%, setelah seleksi AIC.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 026. Australia memperlihatkan pemburukan awal sebelum perbaikan

Australia memperlihatkan pemburukan awal sebelum perbaikan

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,4,3). Koefisien kurs yang relevan untuk depresiasi 2,0835, interval nominal 95% [0,7854; 3,3816], probabilitas nominal 0,002. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,07, kuartal keempat 18,20, kuartal ke-24 19,86 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,4,0,4). Koefisien kurs yang relevan untuk depresiasi 3,3560, interval nominal 95% [1,5631; 5,1490], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -7,32, kuartal keempat 25,36, kuartal ke-24 31,99 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: dynamic_multipliers.csv; results_primary_models.csv. Band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 027. Malaysia mengarah pada perbaikan, tetapi dukungan signifikansinya terbatas

Malaysia mengarah pada perbaikan, tetapi dukungan signifikansinya terbatas

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,7162, interval nominal 95% [-1,5241; 0,0916], probabilitas nominal 0,081. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: RESET; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,38, kuartal keempat -6,79, kuartal ke-24 -6,83 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,3461, interval nominal 95% [0,1855; 2,5066], probabilitas nominal 0,024. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 10,26, kuartal keempat 12,83, kuartal ke-24 12,83 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: dynamic_multipliers.csv; results_primary_models.csv. Band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 028. Tanda negatif di Tiongkok dan Jepang belum cukup menjadi kesimpulan

Tanda negatif di Tiongkok dan Jepang belum cukup menjadi kesimpulan

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,3,0,4,4). Koefisien kurs yang relevan untuk depresiasi -2,7272, interval nominal 95% [-7,4269; 1,9724], probabilitas nominal 0,250. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 3,42, kuartal keempat -26,77, kuartal ke-24 -25,75 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,4,2,0,3). Koefisien kurs yang relevan untuk depresiasi -2,4564, interval nominal 95% [-4,1656; -0,7473], probabilitas nominal 0,006. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: ARCH4; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -18,11, kuartal keempat -23,83, kuartal ke-24 -23,41 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: hasil Stata dan data HS-6 proyek Tio; CI nominal 95%, setelah seleksi AIC.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 029. Enam mitra lainnya memperlihatkan variasi bentuk dan ketepatan respons

Enam mitra lainnya memperlihatkan variasi bentuk dan ketepatan respons

NARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,2,1,1,4). Koefisien kurs yang relevan untuk depresiasi -6,4429, interval nominal 95% [-17,2997; 4,4140], probabilitas nominal 0,236. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 5,84, kuartal keempat -51,89, kuartal ke-24 -61,39 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,4,4,1,1). Koefisien kurs yang relevan untuk depresiasi 3,9349, interval nominal 95% [-1,3834; 9,2531], probabilitas nominal 0,144. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; RESET; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -10,89, kuartal keempat 15,99, kuartal ke-24 36,61 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,1,2,4,4). Koefisien kurs yang relevan untuk depresiasi -0,2625, interval nominal 95% [-2,4399; 1,9149], probabilitas nominal 0,810. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 1,72, kuartal keempat -14,77, kuartal ke-24 -2,50 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,1,0,0). Koefisien kurs yang relevan untuk depresiasi 0,9502, interval nominal 95% [-0,7891; 2,6895], probabilitas nominal 0,280. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; ARCH4; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 5,75, kuartal keempat 9,00, kuartal ke-24 9,06 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (2,2,2,2,4). Koefisien kurs yang relevan untuk depresiasi 3,0948, interval nominal 95% [0,9211; 5,2686], probabilitas nominal 0,006. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 2,11, kuartal keempat 22,37, kuartal ke-24 29,50 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (4,0,1,0,0). Koefisien kurs yang relevan untuk depresiasi -0,5505, interval nominal 95% [-3,8055; 2,7045], probabilitas nominal 0,737. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUMSQ instability; ARCH4; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -1,80, kuartal keempat -3,29, kuartal ke-24 -5,18 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: hasil Stata dan data HS-6 proyek Tio; CI nominal 95%, setelah seleksi AIC.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 030. Asimetri, signifikansi, dan kelayakan model tidak selalu sejalan

Asimetri, signifikansi, dan kelayakan model tidak selalu sejalan

Australia dan Malaysia lolos penyaringan gabungan, tetapi hanya Australia mempertahankan signifikansi koefisien depresiasi di bawah lima persen setelah BH pada keluarga bilateral. India memiliki penolakan Wald asimetri tanpa dukungan level yang memadai. Jepang dan AS mempunyai probabilitas koefisien depresiasi nominal yang kecil, tetapi spesifikasinya belum memenuhi keseluruhan syarat. Contoh ini menunjukkan mengapa tabel satu kolom koefisien dan bintang tidak cukup untuk penelitian ini.

SUMBER DAN REPRODUKSI
Sumber: keluaran Stata proyek Tio.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 031. Pemisahan barang mengubah kesimpulan agregat Indonesia

Pemisahan barang mengubah kesimpulan agregat Indonesia

ARDL komoditas total dan energi/tambang memenuhi syarat level serta diagnostik dalam baseline. Koefisien kurs keduanya negatif: dengan depresiasi sebagai penurunan kurs berorientasi apresiasi, tanda ini mengarah pada kenaikan impor relatif terhadap ekspor. NARDL tidak menghasilkan bukti yang sama kuat untuk efek depresiasi kelompok tersebut. Tanda positif barang konsumsi dalam NARDL disertai catatan diagnostik. Seluruh garis tetap ditampilkan, termasuk yang syarat levelnya belum lengkap. Perbandingan kelompok belum menjadi uji formal selisih elastisitas.

SUMBER DAN REPRODUKSI
Sumber: hasil Stata dan data HS-6 proyek Tio; CI nominal 95%, setelah seleksi AIC.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 032. Hubungan negatif komoditas bertahan pada beberapa pembanding linier

Hubungan negatif komoditas bertahan pada beberapa pembanding linier

Koefisien negatif model linier tidak perlu dikesampingkan hanya karena berbeda dari intuisi daya saing. Sebaliknya, hasil tersebut juga tidak boleh dipilih sebagai kesimpulan tunggal karena sesuai hipotesis. NARDL memungkinkan perbedaan arah kurs dan menghasilkan interval depresiasi yang lebih lebar. Perbedaan ini dapat berkaitan dengan tambahan parameter, variasi kurs yang terbatas dan heterogenitas komponen perdagangan. BCOM merupakan indeks harga luas, bukan harga masing-masing produk dan bukan instrumen eksogen. Karena itu, memasukkannya tidak dengan sendirinya membuktikan kanal harga global.

SUMBER DAN REPRODUKSI
Sumber: TYPE_WLD_commodity dan energy_mining; cap dua; sensitivitas PRICE_WLD.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 033. Komoditas total: pembacaan linier dan nonlinear belum sepenuhnya sejalan

Komoditas total: pembacaan linier dan nonlinear belum sepenuhnya sejalan

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,3,0,0). Koefisien kurs yang relevan untuk depresiasi -1,3546, interval nominal 95% [-1,9985; -0,7108], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -10,01, kuartal keempat -12,90, kuartal ke-24 -12,91 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (2,3,0,0,4). Koefisien kurs yang relevan untuk depresiasi -0,5045, interval nominal 95% [-2,1452; 1,1362], probabilitas nominal 0,539. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -7,76, kuartal keempat -8,66, kuartal ke-24 -4,81 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: dynamic_multipliers.csv; results_primary_models.csv. Band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 034. Energi dan tambang: koefisien linier kuat, ketidakpastian nonlinear besar

Energi dan tambang: koefisien linier kuat, ketidakpastian nonlinear besar

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,4,2,0). Koefisien kurs yang relevan untuk depresiasi -2,0399, interval nominal 95% [-2,6286; -1,4512], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -21,34, kuartal keempat -19,44, kuartal ke-24 -19,44 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,0,4,2,0). Koefisien kurs yang relevan untuk depresiasi -0,1117, interval nominal 95% [-1,1341; 0,9106], probabilitas nominal 0,827. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -1,06, kuartal keempat -1,07, kuartal ke-24 -1,07 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: dynamic_multipliers.csv; results_primary_models.csv. Band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 035. Manufaktur nonkomoditas belum menunjukkan perbaikan yang dapat dipastikan

Manufaktur nonkomoditas belum menunjukkan perbaikan yang dapat dipastikan

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,3,3,3). Koefisien kurs yang relevan untuk depresiasi 0,8651, interval nominal 95% [-0,5995; 2,3297], probabilitas nominal 0,241. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 0,59, kuartal keempat 2,25, kuartal ke-24 8,24 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,3,3,3,0). Koefisien kurs yang relevan untuk depresiasi 1,3581, interval nominal 95% [-0,8318; 3,5480], probabilitas nominal 0,218. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 5,71, kuartal keempat 12,24, kuartal ke-24 12,94 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: dynamic_multipliers.csv; results_primary_models.csv. Band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 036. Barang konsumsi memberi arah perbaikan, dengan catatan pada model nonlinear

Barang konsumsi memberi arah perbaikan, dengan catatan pada model nonlinear

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (2,3,0,4). Koefisien kurs yang relevan untuk depresiasi 2,0258, interval nominal 95% [0,1983; 3,8534], probabilitas nominal 0,031. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -9,93, kuartal keempat 8,97, kuartal ke-24 19,31 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (2,0,0,0,4). Koefisien kurs yang relevan untuk depresiasi 4,5800, interval nominal 95% [2,3007; 6,8592], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; heteroskedasticity; RESET; CUSUMSQ instability. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -2,91, kuartal keempat 27,39, kuartal ke-24 43,65 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: dynamic_multipliers.csv; results_primary_models.csv. Band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 037. Pertanian, bahan baku/penolong, dan modal belum memberi satu pola dunia

Pertanian, bahan baku/penolong, dan modal belum memberi satu pola dunia

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,3,0,0,0). Koefisien kurs yang relevan untuk depresiasi -1,6214, interval nominal 95% [-4,0845; 0,8418], probabilitas nominal 0,192. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -11,38, kuartal keempat -15,43, kuartal ke-24 -15,45 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,0,0,3,2). Koefisien kurs yang relevan untuk depresiasi 1,5889, interval nominal 95% [-2,1877; 5,3655], probabilitas nominal 0,402. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -5,64, kuartal keempat 17,02, kuartal ke-24 15,14 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (3,0,1,0,3). Koefisien kurs yang relevan untuk depresiasi 7,8510, interval nominal 95% [-12,0140; 27,7159], probabilitas nominal 0,431. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 11,10, kuartal keempat 18,80, kuartal ke-24 54,76 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: hasil Stata dan data HS-6 proyek Tio; CI nominal 95%, setelah seleksi AIC.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 038. Efek depresiasi berbeda menurut barang dan tujuan perdagangan

Efek depresiasi berbeda menurut barang dan tujuan perdagangan

Matriks mencakup tujuh kelompok dan sebelas pasar termasuk dunia. Warna ditentukan oleh status hubungan level dan diagnostik, bukan oleh arah koefisien. Dengan begitu, pembaca dapat melihat bahwa beberapa koefisien besar berasal dari model yang belum memenuhi syarat level. Kelompok bertumpang tindih dan sampel waktu berbeda. Matriks ini tidak boleh ditafsirkan sebagai 77 eksperimen independen atau uji formal heterogenitas. Grafik interval per pasar tersedia dalam lampiran B.

SUMBER DAN REPRODUKSI
Sumber: hasil Stata dan data HS-6 proyek Tio; CI nominal 95%, setelah seleksi AIC.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 039. Pertanian ke Tiongkok memberi contoh arah pemburukan yang lebih terukur

Pertanian ke Tiongkok memberi contoh arah pemburukan yang lebih terukur

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,1,1,1). Koefisien kurs yang relevan untuk depresiasi -0,8091, interval nominal 95% [-1,8324; 0,2142], probabilitas nominal 0,119. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 10,40, kuartal keempat -1,69, kuartal ke-24 -7,68 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,1,1,0,1). Koefisien kurs yang relevan untuk depresiasi -2,0365, interval nominal 95% [-3,2688; -0,8041], probabilitas nominal 0,002. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 12,14, kuartal keempat -10,16, kuartal ke-24 -19,39 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: dynamic_multipliers.csv; results_primary_models.csv. Band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 040. Sebagian kelompok justru memberi pola J yang lebih jelas

Sebagian kelompok justru memberi pola J yang lebih jelas

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,2,2). Koefisien kurs yang relevan untuk depresiasi 7,1469, interval nominal 95% [0,8363; 13,4574], probabilitas nominal 0,027. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -37,48, kuartal keempat 16,40, kuartal ke-24 67,96 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (2,1,0,2,3). Koefisien kurs yang relevan untuk depresiasi 5,8605, interval nominal 95% [3,2348; 8,4862], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -4,37, kuartal keempat 48,42, kuartal ke-24 55,86 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: hasil Stata dan data HS-6 proyek Tio; CI nominal 95%, setelah seleksi AIC.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 041. Bentuk J lebih sering terlihat daripada dukungan statistik dua fasenya

Bentuk J lebih sering terlihat daripada dukungan statistik dua fasenya

Pola titik didefinisikan sebelum penghitungan deck: setidaknya satu respons negatif dalam horizon nol sampai empat, dan rata-rata respons positif pada horizon enam belas sampai dua puluh empat. Definisi ini bukan koefisien jangka panjang dan bukan uji yang dipraregistrasikan. Syarat interval menuntut ada fase awal dengan batas atas negatif serta batas bawah positif di kuartal ke-24. Pemilihan salah satu horizon awal mengandung pencarian, sehingga dua kasus yang lolos juga tidak menjadi uji simultan. Tumpang tindih kelompok dan pemilihan AIC membatasi pembacaan jumlah kasus.

SUMBER DAN REPRODUKSI
Sumber: jcurve_classification_all_516.csv; semua 176 model utama.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 042. Kontrol harga tidak menghapus arah negatif komoditas pada ARDL

Kontrol harga tidak menghapus arah negatif komoditas pada ARDL

Koefisien kurs linier komoditas total sekitar negatif satu koma tiga sampai satu koma lima; energi/tambang sekitar negatif dua sampai negatif dua koma tiga. Arah ini bertahan pada cap dua maupun tambahan BCOM. Namun syarat diagnostik tidak konsisten untuk seluruh varian, terutama model dengan kontrol harga. BCOM berpotensi menangkap kejutan global yang juga terkait kurs dan permintaan, bukan satu saluran kausal murni. NARDL dan seluruh sensitivitas tetap tersedia dalam atlas C. Tidak dilakukan pemilihan hanya satu kontrol yang menghasilkan tanda yang diinginkan.

SUMBER DAN REPRODUKSI
Sumber: keluaran Stata proyek Tio.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 043. Koreksi pengujian berganda mengubah sebagian pembacaan signifikansi

Koreksi pengujian berganda mengubah sebagian pembacaan signifikansi

BH dihitung terpisah dalam keluarga scope dan estimator pada model utama. Sebagai contoh, probabilitas nominal Malaysia berada di bawah lima persen, sedangkan nilai BH-nya sedikit di atas ambang tersebut. Pertanian Tiongkok tetap berada di bawah lima persen. Koreksi ini bersifat eksploratif karena model dipilih dengan AIC, kelompok saling bertumpang tindih dan spesifikasi sensitivitas juga diperiksa. BH tidak mengoreksi seluruh proses pencarian model dan tidak menggantikan syarat hubungan level.

SUMBER DAN REPRODUKSI
Sumber: keluaran Stata proyek Tio.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 044. Diagnostik menunjukkan bahwa masalahnya tidak hanya ada pada signifikansi

Diagnostik menunjukkan bahwa masalahnya tidak hanya ada pada signifikansi

Penolakan diagnostik dihitung dari hasil yang tersedia. Tidak ditolaknya suatu uji berarti bukti sampel belum cukup untuk menolak hipotesis nol, bukan bahwa asumsi pasti benar. Model dengan sedikit kuartal dan banyak parameter mempunyai daya uji terbatas. Penanganan yang benar bukan menghapus observasi ekstrem secara otomatis, melainkan meninjau sumber, spesifikasi, perubahan struktur dan desain inferensi. Run ini mempertahankan spesifikasi yang sudah ditentukan agar hasil lengkap dapat dinilai pembaca.

SUMBER DAN REPRODUKSI
Sumber: diagnostic_summary.csv; setiap uji mempunyai hipotesis nol tersendiri.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 045. Stabilitas agregat Indonesia berbeda dari Australia dan Malaysia

Stabilitas agregat Indonesia berbeda dari Australia dan Malaysia

CUSUM dan CUSUMSQ mempunyai konstruksi dan pertanyaan yang berbeda. CUSUM utama diekspor langsung dari Stata dan maksimum lintasannya telah dicocokkan dengan statistik yang tersimpan. Perhitungan independen cocok pada matriks awal full rank. Dua model kelompok Australia, yaitu modal dan konsumsi NARDL, mempunyai inisialisasi rank-deficient sehingga diberi catatan khusus; ini bukan model bilateral Australia yang ditampilkan di sini. CUSUMSQ menggunakan referensi Gaussian yang disimulasikan dengan seed tetap dan tidak diklaim sebagai tabel persis paper.

SUMBER DAN REPRODUKSI
Sumber: stability_paths.csv; stata_cusum_paths.csv; CUSUM_cross_implementation_check.csv.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 046. Keterbatasan data tetap memengaruhi arti hasil penelitian

Keterbatasan data tetap memengaruhi arti hasil penelitian

Pemeriksaan sumber meliputi checksum raw, rekonsiliasi HS-6 terhadap TOTAL dengan toleransi pembulatan, kunci waktu, kelengkapan kuartal, konstruksi kurs dan konsistensi hasil estimasi. Semua itu diperlukan tetapi tidak cukup untuk mengesahkan seluruh seri sebagai konsep ekonomi yang seragam. Keterangan sumber lama tetap diarsipkan. Seri perdagangan baru tidak mewarisi klaim selisih GEM dunia yang berasal dari run lama. Tiga kegagalan finite-sample bounds terjadi pada sensitivitas India dengan BCOM; koefisiennya tetap tersedia dan tidak dipakai sebagai dukungan level.

SUMBER DAN REPRODUKSI
Sumber: audit data HS-6; audit_validitas_data_macro.md; delivery_validation.json.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 047. Komposisi barang membantu menjelaskan heterogenitas, tetapi belum menentukan mekanismenya

Komposisi barang membantu menjelaskan heterogenitas, tetapi belum menentukan mekanismenya

Motivasi awal mengenai komoditas tetap relevan karena struktur ekspor Indonesia memang beragam dan komoditas mempunyai pangsa besar. Akan tetapi, ketidakpekaan terhadap kurs tidak dapat disimpulkan dari koefisien yang tidak signifikan. Untuk mendukung klaim itu diperlukan interval yang cukup sempit atau pengujian ekuivalensi dengan batas ekonomi yang dijustifikasi. Hubungan negatif pada suatu model juga dapat berasal dari respons impor, perubahan komposisi atau kejutan bersama. Karena itu, pembahasan menghindari perubahan diam-diam dari hasil rasio neraca menjadi klaim tentang ekspor saja.

SUMBER DAN REPRODUKSI
Sumber: data dan keluaran Stata proyek Tio; pembahasan peneliti.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 048. Hasil belum memberi dasar bahwa depresiasi merupakan jaminan perbaikan neraca

Hasil belum memberi dasar bahwa depresiasi merupakan jaminan perbaikan neraca

Implikasi analitisnya adalah bahwa pembahasan kurs perlu mempertimbangkan jenis barang dan tujuan perdagangan, bukan memakai satu angka nasional sebagai respons universal. Ini bukan rekomendasi target kurs atau simulasi kebijakan yang telah diidentifikasi secara kausal. Langkah penelitian berikutnya yang relevan mencakup harmonisasi revisi HS, penyelarasan window, pemeriksaan musiman, dan pemisahan nilai dari kuantitas apabila data tersedia. Kanal input impor tidak diaktifkan kembali dalam penelitian ini.

SUMBER DAN REPRODUKSI
Sumber: data dan keluaran Stata proyek Tio; pembahasan peneliti.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 049. Sumber dan referensi memungkinkan setiap hasil ditelusuri kembali

Sumber dan referensi memungkinkan setiap hasil ditelusuri kembali

Paper pengguna tersimpan dalam input/reference/oskooee_replication. Dokumentasi BEC menjelaskan penggunaan SNA sebagai dimensi tersendiri: https://unstats.un.org/unsd/trade/classifications/bec.asp. Korespondensi resmi: https://unstats.un.org/unsd/classifications/Econ/. Kelompok komoditas: https://unctadstat.unctad.org/EN/Classifications/DimSitcRev3Products_DsibSpecialGroupings_Hierarchy.pdf. CUSUM: https://www.stata.com/manuals/tsestatsbcusum.pdf. Respons harga BCOM berasal dari file pengguna; tidak ada klaim memakai Investing.com. Deck memakai hasil yang sudah diestimasi, tidak merunning kembali model.

SUMBER DAN REPRODUKSI
Sumber primer dan file referensi lokal Tio; tautan lengkap tersedia dalam speaker notes.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 050. Panduan membaca atlas hasil lengkap

Panduan membaca atlas hasil lengkap

Setiap panel respons mempunyai sumbu dan intervalnya sendiri; skala vertikal tidak selalu sama antar panel. Halaman utama memberikan penafsiran, sedangkan atlas memungkinkan pembaca mengecek apakah penafsiran itu mewakili keseluruhan hasil. Bentuk kurva tidak otomatis menjadi bukti J-curve. Definisi guncangan, orientasi tanda, band pointwise dan ketidakpastian sesudah seleksi AIC berlaku untuk seluruh lampiran. LaTeX asli setiap rumus serta PDF vector disertakan dalam folder equations.

SUMBER DAN REPRODUKSI
Sumber: data dan keluaran Stata proyek Tio; pembahasan peneliti.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 051. Atlas respons model utama

Atlas respons model utama

Seluruh 88 seri utama disajikan dengan ARDL dan NARDL berdampingan: satu Indonesia–seluruh dunia, sepuluh mitra, serta tujuh kelompok Indonesia–seluruh dunia dan tiap mitra. Semua panel menampilkan depresiasi dan apresiasi berikut band pointwise nominal 95%.

SUMBER DAN REPRODUKSI
Sumber: keluaran estimasi Stata HS-6; seluruh spesifikasi tetap ditampilkan.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 052. Atlas A | Indonesia–seluruh dunia

Atlas A | Indonesia–seluruh dunia

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (2,3,0,4). Koefisien kurs yang relevan untuk depresiasi 0,4292, interval nominal 95% [-1,5289; 2,3873], probabilitas nominal 0,661. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -2,18, kuartal keempat -4,11, kuartal ke-24 3,97 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,4806, statistik t -2,2803, probabilitas upper bound F 0,369, probabilitas upper bound t 0,434, probabilitas joint-X 0,259.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (2,0,3,0,4). Koefisien kurs yang relevan untuk depresiasi 2,5724, interval nominal 95% [0,1277; 5,0172], probabilitas nominal 0,040. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 5,83, kuartal keempat 10,56, kuartal ke-24 24,43 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 3,7989, statistik t -2,8874, probabilitas upper bound F 0,094, probabilitas upper bound t 0,279, probabilitas joint-X 0,011.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 053. Atlas A | Indonesia–Australia

Atlas A | Indonesia–Australia

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,4,3). Koefisien kurs yang relevan untuk depresiasi 2,0835, interval nominal 95% [0,7854; 3,3816], probabilitas nominal 0,002. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,07, kuartal keempat 18,20, kuartal ke-24 19,86 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 8,7330, statistik t -5,7175, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X <0,001.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,4,0,4). Koefisien kurs yang relevan untuk depresiasi 3,3560, interval nominal 95% [1,5631; 5,1490], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -7,32, kuartal keempat 25,36, kuartal ke-24 31,99 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 8,5242, statistik t -6,2346, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X <0,001.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 054. Atlas A | Indonesia–Tiongkok

Atlas A | Indonesia–Tiongkok

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,0,0,0). Koefisien kurs yang relevan untuk depresiasi -1,8864, interval nominal 95% [-3,8493; 0,0764], probabilitas nominal 0,059. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -3,76, kuartal keempat -10,20, kuartal ke-24 -17,57 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 3,5032, statistik t -2,9488, probabilitas upper bound F 0,145, probabilitas upper bound t 0,223, probabilitas joint-X 0,066.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,3,0,4,4). Koefisien kurs yang relevan untuk depresiasi -2,7272, interval nominal 95% [-7,4269; 1,9724], probabilitas nominal 0,250. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 3,42, kuartal keempat -26,77, kuartal ke-24 -25,75 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,0408, statistik t -1,9498, probabilitas upper bound F 0,507, probabilitas upper bound t 0,616, probabilitas joint-X 0,148.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 055. Atlas A | Indonesia–India

Atlas A | Indonesia–India

ARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,4,1,3). Koefisien kurs yang relevan untuk depresiasi 5,2536, interval nominal 95% [-8,3114; 18,8185], probabilitas nominal 0,437. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; RESET. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 33,67, kuartal keempat 19,55, kuartal ke-24 49,71 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 1,7834, statistik t -2,0069, probabilitas upper bound F 0,600, probabilitas upper bound t 0,527, probabilitas joint-X 0,759.

NARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,2,1,1,4). Koefisien kurs yang relevan untuk depresiasi -6,4429, interval nominal 95% [-17,2997; 4,4140], probabilitas nominal 0,236. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 5,84, kuartal keempat -51,89, kuartal ke-24 -61,39 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,4626, statistik t -2,2580, probabilitas upper bound F 0,361, probabilitas upper bound t 0,493, probabilitas joint-X 0,124.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 056. Atlas A | Indonesia–Jepang

Atlas A | Indonesia–Jepang

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,4,2,4). Koefisien kurs yang relevan untuk depresiasi -2,1057, interval nominal 95% [-3,8290; -0,3823], probabilitas nominal 0,017. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -16,00, kuartal keempat -21,46, kuartal ke-24 -20,06 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,6975, statistik t -2,5193, probabilitas upper bound F 0,306, probabilitas upper bound t 0,332, probabilitas joint-X 0,319.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,4,2,0,3). Koefisien kurs yang relevan untuk depresiasi -2,4564, interval nominal 95% [-4,1656; -0,7473], probabilitas nominal 0,006. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: ARCH4; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -18,11, kuartal keempat -23,83, kuartal ke-24 -23,41 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 4,8859, statistik t -3,8342, probabilitas upper bound F 0,024, probabilitas upper bound t 0,065, probabilitas joint-X 0,003.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 057. Atlas A | Indonesia–Korea Selatan

Atlas A | Indonesia–Korea Selatan

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,4,4,0). Koefisien kurs yang relevan untuk depresiasi -0,0742, interval nominal 95% [-2,1653; 2,0169], probabilitas nominal 0,944. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; RESET. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -0,16, kuartal keempat -0,42, kuartal ke-24 -0,70 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 1,4866, statistik t -2,1462, probabilitas upper bound F 0,718, probabilitas upper bound t 0,490, probabilitas joint-X 0,969.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,4,4,1,1). Koefisien kurs yang relevan untuk depresiasi 3,9349, interval nominal 95% [-1,3834; 9,2531], probabilitas nominal 0,144. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; RESET; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -10,89, kuartal keempat 15,99, kuartal ke-24 36,61 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 1,9760, statistik t -2,3288, probabilitas upper bound F 0,533, probabilitas upper bound t 0,479, probabilitas joint-X 0,285.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 058. Atlas A | Indonesia–Malaysia

Atlas A | Indonesia–Malaysia

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,7162, interval nominal 95% [-1,5241; 0,0916], probabilitas nominal 0,081. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: RESET; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,38, kuartal keempat -6,79, kuartal ke-24 -6,83 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 9,6175, statistik t -5,8962, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X 0,002.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,3461, interval nominal 95% [0,1855; 2,5066], probabilitas nominal 0,024. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 10,26, kuartal keempat 12,83, kuartal ke-24 12,83 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 12,2269, statistik t -7,4402, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X <0,001.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 059. Atlas A | Indonesia–Singapura

Atlas A | Indonesia–Singapura

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,1,2,3). Koefisien kurs yang relevan untuk depresiasi -0,4506, interval nominal 95% [-1,5879; 0,6867], probabilitas nominal 0,432. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,10, kuartal keempat -6,50, kuartal ke-24 -4,29 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 8,5313, statistik t -5,8055, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X 0,530.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,1,2,4,4). Koefisien kurs yang relevan untuk depresiasi -0,2625, interval nominal 95% [-2,4399; 1,9149], probabilitas nominal 0,810. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 1,72, kuartal keempat -14,77, kuartal ke-24 -2,50 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 6,7051, statistik t -5,6223, probabilitas upper bound F 0,003, probabilitas upper bound t <0,001, probabilitas joint-X 0,594.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 060. Atlas A | Indonesia–Thailand

Atlas A | Indonesia–Thailand

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,1,0). Koefisien kurs yang relevan untuk depresiasi 1,1796, interval nominal 95% [0,3455; 2,0137], probabilitas nominal 0,006. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; ARCH4. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 7,13, kuartal keempat 11,17, kuartal ke-24 11,24 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 14,2296, statistik t -7,3120, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X <0,001.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,1,0,0). Koefisien kurs yang relevan untuk depresiasi 0,9502, interval nominal 95% [-0,7891; 2,6895], probabilitas nominal 0,280. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; ARCH4; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 5,75, kuartal keempat 9,00, kuartal ke-24 9,06 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 11,2577, statistik t -7,2695, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X <0,001.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 061. Atlas A | Indonesia–Amerika Serikat

Atlas A | Indonesia–Amerika Serikat

ARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (2,2,2,0). Koefisien kurs yang relevan untuk depresiasi 0,9888, interval nominal 95% [-0,4115; 2,3892], probabilitas nominal 0,163. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,48, kuartal keempat 7,43, kuartal ke-24 9,42 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 4,4643, statistik t -3,5937, probabilitas upper bound F 0,055, probabilitas upper bound t 0,072, probabilitas joint-X 0,129.

NARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (2,2,2,2,4). Koefisien kurs yang relevan untuk depresiasi 3,0948, interval nominal 95% [0,9211; 5,2686], probabilitas nominal 0,006. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 2,11, kuartal keempat 22,37, kuartal ke-24 29,50 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 4,8182, statistik t -4,4935, probabilitas upper bound F 0,027, probabilitas upper bound t 0,016, probabilitas joint-X 0,060.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 062. Atlas A | Indonesia–Vietnam

Atlas A | Indonesia–Vietnam

ARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (4,0,1,0). Koefisien kurs yang relevan untuk depresiasi 1,3893, interval nominal 95% [-0,7792; 3,5577], probabilitas nominal 0,205. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; RESET; CUSUMSQ instability; ARCH4; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 5,16, kuartal keempat 9,21, kuartal ke-24 13,18 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 5,0586, statistik t -3,6026, probabilitas upper bound F 0,029, probabilitas upper bound t 0,071, probabilitas joint-X 0,001.

NARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (4,0,1,0,0). Koefisien kurs yang relevan untuk depresiasi -0,5505, interval nominal 95% [-3,8055; 2,7045], probabilitas nominal 0,737. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUMSQ instability; ARCH4; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -1,80, kuartal keempat -3,29, kuartal ke-24 -5,18 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 4,8180, statistik t -3,1356, probabilitas upper bound F 0,025, probabilitas upper bound t 0,221, probabilitas joint-X <0,001.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 063. Atlas A | Dunia | Non-komoditas manufaktur

Atlas A | Dunia | Non-komoditas manufaktur

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,3,3,3). Koefisien kurs yang relevan untuk depresiasi 0,8651, interval nominal 95% [-0,5995; 2,3297], probabilitas nominal 0,241. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 0,59, kuartal keempat 2,25, kuartal ke-24 8,24 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 3,6866, statistik t -3,4066, probabilitas upper bound F 0,128, probabilitas upper bound t 0,097, probabilitas joint-X 0,045.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,3,3,3,0). Koefisien kurs yang relevan untuk depresiasi 1,3581, interval nominal 95% [-0,8318; 3,5480], probabilitas nominal 0,218. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 5,71, kuartal keempat 12,24, kuartal ke-24 12,94 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 3,9906, statistik t -4,0464, probabilitas upper bound F 0,077, probabilitas upper bound t 0,044, probabilitas joint-X 0,023.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 064. Atlas A | Dunia | Barang konsumsi

Atlas A | Dunia | Barang konsumsi

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (2,3,0,4). Koefisien kurs yang relevan untuk depresiasi 2,0258, interval nominal 95% [0,1983; 3,8534], probabilitas nominal 0,031. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -9,93, kuartal keempat 8,97, kuartal ke-24 19,31 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 5,4958, statistik t -4,0548, probabilitas upper bound F 0,021, probabilitas upper bound t 0,027, probabilitas joint-X 0,010.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (2,0,0,0,4). Koefisien kurs yang relevan untuk depresiasi 4,5800, interval nominal 95% [2,3007; 6,8592], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; heteroskedasticity; RESET; CUSUMSQ instability. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -2,91, kuartal keempat 27,39, kuartal ke-24 43,65 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 5,7096, statistik t -4,2420, probabilitas upper bound F 0,010, probabilitas upper bound t 0,031, probabilitas joint-X 0,001.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 065. Atlas A | Dunia | Komoditas pertanian & pangan

Atlas A | Dunia | Komoditas pertanian & pangan

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,0,1,0). Koefisien kurs yang relevan untuk depresiasi 0,0053, interval nominal 95% [-1,2485; 1,2591], probabilitas nominal 0,993. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 0,03, kuartal keempat 0,05, kuartal ke-24 0,05 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 8,2677, statistik t -5,2576, probabilitas upper bound F <0,001, probabilitas upper bound t 0,001, probabilitas joint-X 0,939.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,3,0,0,0). Koefisien kurs yang relevan untuk depresiasi -1,6214, interval nominal 95% [-4,0845; 0,8418], probabilitas nominal 0,192. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -11,38, kuartal keempat -15,43, kuartal ke-24 -15,45 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 6,7925, statistik t -5,7158, probabilitas upper bound F 0,003, probabilitas upper bound t <0,001, probabilitas joint-X 0,443.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 066. Atlas A | Dunia | Bahan baku/penolong

Atlas A | Dunia | Bahan baku/penolong

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (3,3,0,3). Koefisien kurs yang relevan untuk depresiasi -0,1390, interval nominal 95% [-6,9050; 6,6270], probabilitas nominal 0,967. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 0,17, kuartal keempat -3,86, kuartal ke-24 -2,84 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 0,7590, statistik t -0,7667, probabilitas upper bound F 0,932, probabilitas upper bound t 0,898, probabilitas joint-X 0,677.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (3,0,1,0,3). Koefisien kurs yang relevan untuk depresiasi 7,8510, interval nominal 95% [-12,0140; 27,7159], probabilitas nominal 0,431. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 11,10, kuartal keempat 18,80, kuartal ke-24 54,76 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 5,6458, statistik t -0,9784, probabilitas upper bound F 0,012, probabilitas upper bound t 0,900, probabilitas joint-X 0,002.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 067. Atlas A | Dunia | Barang modal

Atlas A | Dunia | Barang modal

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,0,0,3). Koefisien kurs yang relevan untuk depresiasi 1,4250, interval nominal 95% [-1,7541; 4,6042], probabilitas nominal 0,373. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -15,19, kuartal keempat 6,74, kuartal ke-24 13,58 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 4,7592, statistik t -4,3061, probabilitas upper bound F 0,043, probabilitas upper bound t 0,016, probabilitas joint-X 0,271.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,0,0,3,2). Koefisien kurs yang relevan untuk depresiasi 1,5889, interval nominal 95% [-2,1877; 5,3655], probabilitas nominal 0,402. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -5,64, kuartal keempat 17,02, kuartal ke-24 15,14 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 5,1040, statistik t -5,0290, probabilitas upper bound F 0,021, probabilitas upper bound t 0,005, probabilitas joint-X 0,398.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 068. Atlas A | Dunia | Komoditas total

Atlas A | Dunia | Komoditas total

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,3,0,0). Koefisien kurs yang relevan untuk depresiasi -1,3546, interval nominal 95% [-1,9985; -0,7108], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -10,01, kuartal keempat -12,90, kuartal ke-24 -12,91 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 11,1364, statistik t -6,6401, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X 0,002.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (2,3,0,0,4). Koefisien kurs yang relevan untuk depresiasi -0,5045, interval nominal 95% [-2,1452; 1,1362], probabilitas nominal 0,539. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -7,76, kuartal keempat -8,66, kuartal ke-24 -4,81 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 6,8359, statistik t -5,6174, probabilitas upper bound F 0,003, probabilitas upper bound t 0,001, probabilitas joint-X 0,120.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 069. Atlas A | Dunia | Komoditas energi & tambang

Atlas A | Dunia | Komoditas energi & tambang

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,4,2,0). Koefisien kurs yang relevan untuk depresiasi -2,0399, interval nominal 95% [-2,6286; -1,4512], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -21,34, kuartal keempat -19,44, kuartal ke-24 -19,44 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 18,6694, statistik t -8,5860, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X <0,001.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,0,4,2,0). Koefisien kurs yang relevan untuk depresiasi -0,1117, interval nominal 95% [-1,1341; 0,9106], probabilitas nominal 0,827. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -1,06, kuartal keempat -1,07, kuartal ke-24 -1,07 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 11,6409, statistik t -7,5002, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X <0,001.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 070. Atlas A | Australia | Non-komoditas manufaktur

Atlas A | Australia | Non-komoditas manufaktur

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 0,9189, interval nominal 95% [-1,5492; 3,3869], probabilitas nominal 0,460. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: ARCH4. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,20, kuartal keempat 7,86, kuartal ke-24 8,76 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 4,1635, statistik t -3,9530, probabilitas upper bound F 0,073, probabilitas upper bound t 0,036, probabilitas joint-X 0,061.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,1,0,4,4). Koefisien kurs yang relevan untuk depresiasi 5,6284, interval nominal 95% [1,9258; 9,3309], probabilitas nominal 0,003. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -7,07, kuartal keempat 28,33, kuartal ke-24 53,64 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 3,7804, statistik t -4,2717, probabilitas upper bound F 0,089, probabilitas upper bound t 0,027, probabilitas joint-X 0,031.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 071. Atlas A | Australia | Barang konsumsi

Atlas A | Australia | Barang konsumsi

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 0,7041, interval nominal 95% [-0,6861; 2,0943], probabilitas nominal 0,316. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 5,76, kuartal keempat 6,71, kuartal ke-24 6,71 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 13,4174, statistik t -7,2441, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X 0,686.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,0881, interval nominal 95% [-0,9258; 3,1020], probabilitas nominal 0,285. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: Recursive initial matrix rank deficient; official Stata CUSUM retained. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 8,93, kuartal keempat 10,37, kuartal ke-24 10,37 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 10,6808, statistik t -7,2244, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X 0,781.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 072. Atlas A | Australia | Komoditas pertanian & pangan

Atlas A | Australia | Komoditas pertanian & pangan

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,3,2). Koefisien kurs yang relevan untuk depresiasi -1,7703, interval nominal 95% [-3,4818; -0,0589], probabilitas nominal 0,043. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -6,16, kuartal keempat -15,10, kuartal ke-24 -16,87 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 7,7158, statistik t -5,5291, probabilitas upper bound F 0,001, probabilitas upper bound t <0,001, probabilitas joint-X 0,284.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,3,0,0,0). Koefisien kurs yang relevan untuk depresiasi -3,3446, interval nominal 95% [-5,0000; -1,6893], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -21,74, kuartal keempat -31,77, kuartal ke-24 -31,88 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 10,1084, statistik t -6,9244, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X 0,005.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 073. Atlas A | Australia | Bahan baku/penolong

Atlas A | Australia | Bahan baku/penolong

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,4,4,0). Koefisien kurs yang relevan untuk depresiasi 1,6082, interval nominal 95% [0,2219; 2,9946], probabilitas nominal 0,024. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 9,65, kuartal keempat 15,22, kuartal ke-24 15,33 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 8,1110, statistik t -5,4602, probabilitas upper bound F 0,001, probabilitas upper bound t <0,001, probabilitas joint-X <0,001.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,4,4,0,0). Koefisien kurs yang relevan untuk depresiasi 2,5180, interval nominal 95% [0,6163; 4,4197], probabilitas nominal 0,010. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 15,63, kuartal keempat 23,87, kuartal ke-24 24,00 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 6,9119, statistik t -5,6232, probabilitas upper bound F 0,002, probabilitas upper bound t <0,001, probabilitas joint-X <0,001.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 074. Atlas A | Australia | Barang modal

Atlas A | Australia | Barang modal

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 4,0019, interval nominal 95% [-1,0640; 9,0678], probabilitas nominal 0,120. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; heteroskedasticity; CUSUMSQ instability; ARCH4. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 21,96, kuartal keempat 37,62, kuartal ke-24 38,14 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 7,8979, statistik t -5,5515, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X 0,284.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 7,4662, interval nominal 95% [0,3024; 14,6300], probabilitas nominal 0,041. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; heteroskedasticity; RESET; CUSUMSQ instability; ARCH4; CUSUM instability or unavailable; Recursive initial matrix rank deficient; official Stata CUSUM retained. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 42,00, kuartal keempat 70,34, kuartal ke-24 71,16 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 6,7499, statistik t -5,6922, probabilitas upper bound F 0,002, probabilitas upper bound t <0,001, probabilitas joint-X 0,233.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 075. Atlas A | Australia | Komoditas total

Atlas A | Australia | Komoditas total

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,4,0). Koefisien kurs yang relevan untuk depresiasi 1,7010, interval nominal 95% [0,4539; 2,9481], probabilitas nominal 0,008. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 11,33, kuartal keempat 16,17, kuartal ke-24 16,21 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 10,5532, statistik t -6,1659, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X <0,001.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,4,0,1). Koefisien kurs yang relevan untuk depresiasi 1,3791, interval nominal 95% [-0,4746; 3,2328], probabilitas nominal 0,142. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -10,61, kuartal keempat 12,97, kuartal ke-24 13,14 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 9,0427, statistik t -6,2773, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X <0,001.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 076. Atlas A | Australia | Komoditas energi & tambang

Atlas A | Australia | Komoditas energi & tambang

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,1,4,0). Koefisien kurs yang relevan untuk depresiasi 3,2646, interval nominal 95% [0,3978; 6,1313], probabilitas nominal 0,026. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 18,70, kuartal keempat 30,80, kuartal ke-24 31,11 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 8,4547, statistik t -5,3420, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X <0,001.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,1,4,0,1). Koefisien kurs yang relevan untuk depresiasi 5,7253, interval nominal 95% [1,6941; 9,7565], probabilitas nominal 0,006. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -13,67, kuartal keempat 53,02, kuartal ke-24 54,57 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 7,4348, statistik t -5,5170, probabilitas upper bound F <0,001, probabilitas upper bound t 0,001, probabilitas joint-X <0,001.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 077. Atlas A | Tiongkok | Non-komoditas manufaktur

Atlas A | Tiongkok | Non-komoditas manufaktur

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,4,1,0). Koefisien kurs yang relevan untuk depresiasi 0,3002, interval nominal 95% [-3,5723; 4,1727], probabilitas nominal 0,878. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; non-normal residuals. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 0,36, kuartal keempat 1,22, kuartal ke-24 2,67 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,4031, statistik t -2,6925, probabilitas upper bound F 0,392, probabilitas upper bound t 0,297, probabilitas joint-X 0,333.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,1,4,1,4). Koefisien kurs yang relevan untuk depresiasi 3,0325, interval nominal 95% [-10,8359; 16,9010], probabilitas nominal 0,663. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 11,22, kuartal keempat 9,74, kuartal ke-24 24,73 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,8826, statistik t -1,7777, probabilitas upper bound F 0,237, probabilitas upper bound t 0,688, probabilitas joint-X 0,102.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 078. Atlas A | Tiongkok | Barang konsumsi

Atlas A | Tiongkok | Barang konsumsi

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,2,3). Koefisien kurs yang relevan untuk depresiasi -0,5694, interval nominal 95% [-2,5424; 1,4037], probabilitas nominal 0,567. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability; ARCH4. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 16,75, kuartal keempat 2,25, kuartal ke-24 -5,43 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 8,2026, statistik t -5,2624, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X 0,063.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,2,3,1). Koefisien kurs yang relevan untuk depresiasi -2,7105, interval nominal 95% [-5,1642; -0,2569], probabilitas nominal 0,031. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 6,43, kuartal keempat -24,98, kuartal ke-24 -25,83 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 8,5959, statistik t -5,7169, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X 0,013.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 079. Atlas A | Tiongkok | Komoditas pertanian & pangan

Atlas A | Tiongkok | Komoditas pertanian & pangan

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,1,1,1). Koefisien kurs yang relevan untuk depresiasi -0,8091, interval nominal 95% [-1,8324; 0,2142], probabilitas nominal 0,119. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 10,40, kuartal keempat -1,69, kuartal ke-24 -7,68 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 5,8428, statistik t -3,8863, probabilitas upper bound F 0,012, probabilitas upper bound t 0,038, probabilitas joint-X 0,031.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,1,1,0,1). Koefisien kurs yang relevan untuk depresiasi -2,0365, interval nominal 95% [-3,2688; -0,8041], probabilitas nominal 0,002. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 12,14, kuartal keempat -10,16, kuartal ke-24 -19,39 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 6,6915, statistik t -4,7781, probabilitas upper bound F 0,002, probabilitas upper bound t 0,008, probabilitas joint-X 0,003.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 080. Atlas A | Tiongkok | Bahan baku/penolong

Atlas A | Tiongkok | Bahan baku/penolong

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,3,0,0). Koefisien kurs yang relevan untuk depresiasi -3,2911, interval nominal 95% [-6,5213; -0,0610], probabilitas nominal 0,046. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,93, kuartal keempat -14,00, kuartal ke-24 -29,12 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 1,2659, statistik t -2,0349, probabilitas upper bound F 0,799, probabilitas upper bound t 0,563, probabilitas joint-X 0,297.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,3,0,4,4). Koefisien kurs yang relevan untuk depresiasi -6,2342, interval nominal 95% [-10,3438; -2,1246], probabilitas nominal 0,004. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 0,12, kuartal keempat -37,14, kuartal ke-24 -57,42 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 1,3875, statistik t -2,1276, probabilitas upper bound F 0,771, probabilitas upper bound t 0,550, probabilitas joint-X 0,174.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 081. Atlas A | Tiongkok | Barang modal

Atlas A | Tiongkok | Barang modal

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,1,4). Koefisien kurs yang relevan untuk depresiasi 1,2107, interval nominal 95% [-1,2265; 3,6479], probabilitas nominal 0,325. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; ARCH4; non-normal residuals. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -6,03, kuartal keempat 6,37, kuartal ke-24 11,54 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 10,5186, statistik t -6,2938, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X <0,001.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,1,0,4). Koefisien kurs yang relevan untuk depresiasi 0,5950, interval nominal 95% [-3,3482; 4,5381], probabilitas nominal 0,764. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; CUSUMSQ instability; ARCH4; non-normal residuals. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 9,63, kuartal keempat -3,75, kuartal ke-24 5,67 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 7,7064, statistik t -6,0043, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X 0,001.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 082. Atlas A | Tiongkok | Komoditas total

Atlas A | Tiongkok | Komoditas total

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,1,1,3). Koefisien kurs yang relevan untuk depresiasi -2,2156, interval nominal 95% [-3,7559; -0,6753], probabilitas nominal 0,005. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 3,16, kuartal keempat -12,41, kuartal ke-24 -20,99 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 5,3588, statistik t -3,9998, probabilitas upper bound F 0,021, probabilitas upper bound t 0,029, probabilitas joint-X 0,012.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,1,3,0,3). Koefisien kurs yang relevan untuk depresiasi -3,4577, interval nominal 95% [-5,0908; -1,8246], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: RESET; CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 12,96, kuartal keempat -25,23, kuartal ke-24 -32,96 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 7,1385, statistik t -5,2414, probabilitas upper bound F 0,001, probabilitas upper bound t 0,002, probabilitas joint-X <0,001.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 083. Atlas A | Tiongkok | Komoditas energi & tambang

Atlas A | Tiongkok | Komoditas energi & tambang

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,2). Koefisien kurs yang relevan untuk depresiasi -1,9236, interval nominal 95% [-4,2355; 0,3883], probabilitas nominal 0,101. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,12, kuartal keempat -13,59, kuartal ke-24 -18,27 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 4,6627, statistik t -3,7582, probabilitas upper bound F 0,043, probabilitas upper bound t 0,051, probabilitas joint-X 0,289.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,1,0,3). Koefisien kurs yang relevan untuk depresiasi -3,6577, interval nominal 95% [-6,7794; -0,5361], probabilitas nominal 0,022. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 9,11, kuartal keempat -26,98, kuartal ke-24 -34,82 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 5,2881, statistik t -4,3896, probabilitas upper bound F 0,014, probabilitas upper bound t 0,021, probabilitas joint-X 0,040.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 084. Atlas A | India | Non-komoditas manufaktur

Atlas A | India | Non-komoditas manufaktur

ARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (2,0,0,1). Koefisien kurs yang relevan untuk depresiasi -4,5016, interval nominal 95% [-15,0384; 6,0352], probabilitas nominal 0,393. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 13,01, kuartal keempat -25,38, kuartal ke-24 -42,80 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,2799, statistik t -2,1741, probabilitas upper bound F 0,433, probabilitas upper bound t 0,505, probabilitas joint-X 0,054.

NARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (2,0,2,0,1). Koefisien kurs yang relevan untuk depresiasi -6,3792, interval nominal 95% [-15,8100; 3,0516], probabilitas nominal 0,179. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 14,94, kuartal keempat -42,19, kuartal ke-24 -60,77 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,4944, statistik t -2,5829, probabilitas upper bound F 0,351, probabilitas upper bound t 0,397, probabilitas joint-X 0,033.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 085. Atlas A | India | Barang konsumsi

Atlas A | India | Barang konsumsi

ARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 3,9821, interval nominal 95% [-8,8526; 16,8169], probabilitas nominal 0,535. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 15,93, kuartal keempat 35,46, kuartal ke-24 37,95 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 4,4693, statistik t -3,3495, probabilitas upper bound F 0,061, probabilitas upper bound t 0,122, probabilitas joint-X 0,161.

NARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (2,2,4,1,4). Koefisien kurs yang relevan untuk depresiasi -8,9044, interval nominal 95% [-19,2714; 1,4625], probabilitas nominal 0,090. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 31,36, kuartal keempat -61,42, kuartal ke-24 -84,87 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 5,7180, statistik t -4,7702, probabilitas upper bound F 0,017, probabilitas upper bound t 0,011, probabilitas joint-X 0,010.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 086. Atlas A | India | Komoditas pertanian & pangan

Atlas A | India | Komoditas pertanian & pangan

ARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (4,4,1,0). Koefisien kurs yang relevan untuk depresiasi 6,3247, interval nominal 95% [-21,2899; 33,9392], probabilitas nominal 0,645. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 11,68, kuartal keempat 25,49, kuartal ke-24 54,56 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 0,7411, statistik t -1,0779, probabilitas upper bound F 0,933, probabilitas upper bound t 0,826, probabilitas joint-X 0,891.

NARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,1,1,0,3). Koefisien kurs yang relevan untuk depresiasi -5,0762, interval nominal 95% [-15,1988; 5,0463], probabilitas nominal 0,316. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 47,20, kuartal keempat -55,35, kuartal ke-24 -48,38 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 5,7981, statistik t -5,0573, probabilitas upper bound F 0,013, probabilitas upper bound t 0,006, probabilitas joint-X 0,006.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 087. Atlas A | India | Bahan baku/penolong

Atlas A | India | Bahan baku/penolong

ARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,4,1,3). Koefisien kurs yang relevan untuk depresiasi 10,8457, interval nominal 95% [-7,5657; 29,2570], probabilitas nominal 0,240. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 49,87, kuartal keempat 40,71, kuartal ke-24 102,81 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,6720, statistik t -2,0256, probabilitas upper bound F 0,320, probabilitas upper bound t 0,519, probabilitas joint-X 0,425.

NARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,2,1,3,3). Koefisien kurs yang relevan untuk depresiasi 2,9378, interval nominal 95% [-12,5378; 18,4134], probabilitas nominal 0,702. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 7,67, kuartal keempat -18,98, kuartal ke-24 27,83 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 3,1243, statistik t -1,9973, probabilitas upper bound F 0,200, probabilitas upper bound t 0,583, probabilitas joint-X 0,070.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 088. Atlas A | India | Barang modal

Atlas A | India | Barang modal

ARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,0118, interval nominal 95% [-17,5869; 19,6106], probabilitas nominal 0,913. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 4,01, kuartal keempat 8,99, kuartal ke-24 9,64 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,8833, statistik t -3,3956, probabilitas upper bound F 0,267, probabilitas upper bound t 0,113, probabilitas joint-X 0,844.

NARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 0,8154, interval nominal 95% [-20,5914; 22,2223], probabilitas nominal 0,939. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,23, kuartal keempat 7,24, kuartal ke-24 7,77 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,2546, statistik t -3,3096, probabilitas upper bound F 0,430, probabilitas upper bound t 0,179, probabilitas joint-X 0,936.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 089. Atlas A | India | Komoditas total

Atlas A | India | Komoditas total

ARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,4,1,4). Koefisien kurs yang relevan untuk depresiasi 5,4757, interval nominal 95% [-12,9124; 23,8639], probabilitas nominal 0,549. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 36,06, kuartal keempat 49,52, kuartal ke-24 52,19 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 1,7922, statistik t -2,5615, probabilitas upper bound F 0,596, probabilitas upper bound t 0,312, probabilitas joint-X 0,783.

NARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,1,1,0,3). Koefisien kurs yang relevan untuk depresiasi -4,5686, interval nominal 95% [-13,7475; 4,6104], probabilitas nominal 0,320. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 33,20, kuartal keempat -52,88, kuartal ke-24 -43,54 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 5,1085, statistik t -4,6876, probabilitas upper bound F 0,026, probabilitas upper bound t 0,013, probabilitas joint-X 0,004.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 090. Atlas A | India | Komoditas energi & tambang

Atlas A | India | Komoditas energi & tambang

ARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,4,0,0). Koefisien kurs yang relevan untuk depresiasi 7,8277, interval nominal 95% [-9,1835; 24,8390], probabilitas nominal 0,358. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 28,75, kuartal keempat 68,06, kuartal ke-24 74,61 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,8788, statistik t -3,1120, probabilitas upper bound F 0,270, probabilitas upper bound t 0,166, probabilitas joint-X 0,189.

NARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (2,3,4,4,4). Koefisien kurs yang relevan untuk depresiasi -4,5058, interval nominal 95% [-14,1408; 5,1292], probabilitas nominal 0,346. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 45,70, kuartal keempat -15,87, kuartal ke-24 -42,94 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 5,2934, statistik t -4,9464, probabilitas upper bound F 0,027, probabilitas upper bound t 0,008, probabilitas joint-X 0,004.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 091. Atlas A | Jepang | Non-komoditas manufaktur

Atlas A | Jepang | Non-komoditas manufaktur

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,0,2). Koefisien kurs yang relevan untuk depresiasi -1,1707, interval nominal 95% [-2,8379; 0,4964], probabilitas nominal 0,166. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; heteroskedasticity; RESET; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -6,39, kuartal keempat -6,60, kuartal ke-24 -11,13 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 4,8624, statistik t -3,7116, probabilitas upper bound F 0,035, probabilitas upper bound t 0,057, probabilitas joint-X 0,190.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,0,0,2). Koefisien kurs yang relevan untuk depresiasi -1,4769, interval nominal 95% [-3,5471; 0,5932], probabilitas nominal 0,159. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; heteroskedasticity; RESET; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -8,13, kuartal keempat -8,07, kuartal ke-24 -14,05 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 3,9366, statistik t -3,7815, probabilitas upper bound F 0,072, probabilitas upper bound t 0,077, probabilitas joint-X 0,266.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 092. Atlas A | Jepang | Barang konsumsi

Atlas A | Jepang | Barang konsumsi

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,1,0). Koefisien kurs yang relevan untuk depresiasi -0,7180, interval nominal 95% [-2,2001; 0,7641], probabilitas nominal 0,337. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -3,81, kuartal keempat -6,72, kuartal ke-24 -6,84 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 8,0177, statistik t -5,4476, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X 0,002.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,1,0,0). Koefisien kurs yang relevan untuk depresiasi -1,2455, interval nominal 95% [-3,3623; 0,8712], probabilitas nominal 0,244. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -6,80, kuartal keempat -11,70, kuartal ke-24 -11,87 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 6,4584, statistik t -5,4378, probabilitas upper bound F 0,003, probabilitas upper bound t 0,001, probabilitas joint-X 0,004.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 093. Atlas A | Jepang | Komoditas pertanian & pangan

Atlas A | Jepang | Komoditas pertanian & pangan

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,0753, interval nominal 95% [-1,6760; 1,5254], probabilitas nominal 0,925. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -0,18, kuartal keempat -0,36, kuartal ke-24 -0,68 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 3,5588, statistik t -2,6581, probabilitas upper bound F 0,137, probabilitas upper bound t 0,321, probabilitas joint-X 0,933.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi -1,7117, interval nominal 95% [-2,9748; -0,4486], probabilitas nominal 0,009. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -7,38, kuartal keempat -11,98, kuartal ke-24 -16,26 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 4,1575, statistik t -3,6240, probabilitas upper bound F 0,055, probabilitas upper bound t 0,105, probabilitas joint-X 0,206.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 094. Atlas A | Jepang | Bahan baku/penolong

Atlas A | Jepang | Bahan baku/penolong

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,2,0,3). Koefisien kurs yang relevan untuk depresiasi -2,3469, interval nominal 95% [-4,3317; -0,3622], probabilitas nominal 0,021. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; RESET; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -14,38, kuartal keempat -17,38, kuartal ke-24 -22,03 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 1,5455, statistik t -2,0913, probabilitas upper bound F 0,698, probabilitas upper bound t 0,523, probabilitas joint-X 0,272.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,2,0,0,2). Koefisien kurs yang relevan untuk depresiasi -3,0484, interval nominal 95% [-4,9110; -1,1857], probabilitas nominal 0,002. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -19,42, kuartal keempat -21,73, kuartal ke-24 -28,96 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 1,8520, statistik t -2,3626, probabilitas upper bound F 0,585, probabilitas upper bound t 0,493, probabilitas joint-X 0,101.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 095. Atlas A | Jepang | Barang modal

Atlas A | Jepang | Barang modal

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,4,0,2). Koefisien kurs yang relevan untuk depresiasi -3,0683, interval nominal 95% [-6,4566; 0,3199], probabilitas nominal 0,075. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -19,39, kuartal keempat -16,51, kuartal ke-24 -28,49 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,3287, statistik t -2,5961, probabilitas upper bound F 0,415, probabilitas upper bound t 0,324, probabilitas joint-X 0,071.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,4,0,1,2). Koefisien kurs yang relevan untuk depresiasi -4,6872, interval nominal 95% [-7,6391; -1,7353], probabilitas nominal 0,002. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -24,26, kuartal keempat -29,18, kuartal ke-24 -44,48 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,7598, statistik t -3,3387, probabilitas upper bound F 0,267, probabilitas upper bound t 0,154, probabilitas joint-X 0,027.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 096. Atlas A | Jepang | Komoditas total

Atlas A | Jepang | Komoditas total

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,2,3). Koefisien kurs yang relevan untuk depresiasi -1,7710, interval nominal 95% [-3,0921; -0,4500], probabilitas nominal 0,009. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: RESET; CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -8,42, kuartal keempat -18,08, kuartal ke-24 -16,88 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 7,8661, statistik t -5,2257, probabilitas upper bound F 0,001, probabilitas upper bound t 0,001, probabilitas joint-X <0,001.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,2,0,3). Koefisien kurs yang relevan untuk depresiasi -0,7102, interval nominal 95% [-2,7675; 1,3471], probabilitas nominal 0,493. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -3,84, kuartal keempat -9,49, kuartal ke-24 -6,77 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 7,0034, statistik t -5,0937, probabilitas upper bound F 0,002, probabilitas upper bound t 0,003, probabilitas joint-X <0,001.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 097. Atlas A | Jepang | Komoditas energi & tambang

Atlas A | Jepang | Komoditas energi & tambang

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,2,3). Koefisien kurs yang relevan untuk depresiasi -2,1067, interval nominal 95% [-3,8029; -0,4106], probabilitas nominal 0,016. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; RESET. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -12,07, kuartal keempat -21,60, kuartal ke-24 -20,08 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 7,5071, statistik t -5,1518, probabilitas upper bound F 0,002, probabilitas upper bound t 0,001, probabilitas joint-X 0,001.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,2,0,3). Koefisien kurs yang relevan untuk depresiasi -0,1602, interval nominal 95% [-2,5423; 2,2218], probabilitas nominal 0,894. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,47, kuartal keempat -4,29, kuartal ke-24 -1,53 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 7,8613, statistik t -5,5388, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X <0,001.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 098. Atlas A | Korea Selatan | Non-komoditas manufaktur

Atlas A | Korea Selatan | Non-komoditas manufaktur

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,4,1,0). Koefisien kurs yang relevan untuk depresiasi 1,7473, interval nominal 95% [-0,0378; 3,5323], probabilitas nominal 0,055. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,78, kuartal keempat 9,39, kuartal ke-24 16,27 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 4,3229, statistik t -3,1146, probabilitas upper bound F 0,063, probabilitas upper bound t 0,163, probabilitas joint-X 0,013.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,4,0,2,3). Koefisien kurs yang relevan untuk depresiasi 4,7173, interval nominal 95% [1,9522; 7,4825], probabilitas nominal 0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -13,99, kuartal keempat 19,80, kuartal ke-24 44,61 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 5,2450, statistik t -3,9210, probabilitas upper bound F 0,016, probabilitas upper bound t 0,054, probabilitas joint-X 0,002.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 099. Atlas A | Korea Selatan | Barang konsumsi

Atlas A | Korea Selatan | Barang konsumsi

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,4,0). Koefisien kurs yang relevan untuk depresiasi 7,9411, interval nominal 95% [-2,0668; 17,9490], probabilitas nominal 0,118. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; heteroskedasticity; RESET. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 11,22, kuartal keempat 28,46, kuartal ke-24 66,27 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,6163, statistik t -2,3258, probabilitas upper bound F 0,329, probabilitas upper bound t 0,434, probabilitas joint-X 0,152.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,4,0,0). Koefisien kurs yang relevan untuk depresiasi 0,8749, interval nominal 95% [-24,3807; 26,1305], probabilitas nominal 0,945. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; heteroskedasticity; RESET. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 1,04, kuartal keempat 2,66, kuartal ke-24 6,81 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,1870, statistik t -1,7309, probabilitas upper bound F 0,452, probabilitas upper bound t 0,726, probabilitas joint-X 0,215.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 100. Atlas A | Korea Selatan | Komoditas pertanian & pangan

Atlas A | Korea Selatan | Komoditas pertanian & pangan

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,4488, interval nominal 95% [-0,0370; 2,9345], probabilitas nominal 0,056. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,52, kuartal keempat 6,93, kuartal ke-24 13,07 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 3,6104, statistik t -2,8180, probabilitas upper bound F 0,130, probabilitas upper bound t 0,263, probabilitas joint-X 0,219.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,6014, interval nominal 95% [-1,0973; 4,3000], probabilitas nominal 0,241. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,98, kuartal keempat 7,80, kuartal ke-24 14,51 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,8513, statistik t -2,5488, probabilitas upper bound F 0,243, probabilitas upper bound t 0,440, probabilitas joint-X 0,354.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 101. Atlas A | Korea Selatan | Bahan baku/penolong

Atlas A | Korea Selatan | Bahan baku/penolong

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,4,4,0). Koefisien kurs yang relevan untuk depresiasi 0,8867, interval nominal 95% [-3,0210; 4,7943], probabilitas nominal 0,652. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 0,94, kuartal keempat 2,59, kuartal ke-24 6,83 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,5255, statistik t -1,6097, probabilitas upper bound F 0,354, probabilitas upper bound t 0,691, probabilitas joint-X 0,818.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,4,4,1,0). Koefisien kurs yang relevan untuk depresiasi 10,9500, interval nominal 95% [-2,2478; 24,1478], probabilitas nominal 0,102. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 12,52, kuartal keempat 33,16, kuartal ke-24 85,57 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 3,7742, statistik t -1,8609, probabilitas upper bound F 0,090, probabilitas upper bound t 0,659, probabilitas joint-X 0,029.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 102. Atlas A | Korea Selatan | Barang modal

Atlas A | Korea Selatan | Barang modal

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,1). Koefisien kurs yang relevan untuk depresiasi 1,4164, interval nominal 95% [-2,0646; 4,8974], probabilitas nominal 0,420. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET; non-normal residuals. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -38,15, kuartal keempat 9,47, kuartal ke-24 13,53 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 3,1329, statistik t -3,2579, probabilitas upper bound F 0,207, probabilitas upper bound t 0,134, probabilitas joint-X 0,242.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,2,2). Koefisien kurs yang relevan untuk depresiasi 7,1469, interval nominal 95% [0,8363; 13,4574], probabilitas nominal 0,027. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -37,48, kuartal keempat 16,40, kuartal ke-24 67,96 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 5,0526, statistik t -4,0870, probabilitas upper bound F 0,019, probabilitas upper bound t 0,040, probabilitas joint-X 0,009.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 103. Atlas A | Korea Selatan | Komoditas total

Atlas A | Korea Selatan | Komoditas total

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,4,4,0). Koefisien kurs yang relevan untuk depresiasi -0,3704, interval nominal 95% [-4,4709; 3,7301], probabilitas nominal 0,857. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -0,72, kuartal keempat -1,63, kuartal ke-24 -3,29 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 0,6179, statistik t -1,5125, probabilitas upper bound F 0,959, probabilitas upper bound t 0,717, probabilitas joint-X 0,998.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,0,4,1,2). Koefisien kurs yang relevan untuk depresiasi 4,6622, interval nominal 95% [-0,7859; 10,1103], probabilitas nominal 0,092. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; CUSUMSQ instability. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 3,48, kuartal keempat 21,25, kuartal ke-24 44,32 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,2010, statistik t -2,7032, probabilitas upper bound F 0,446, probabilitas upper bound t 0,351, probabilitas joint-X 0,310.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 104. Atlas A | Korea Selatan | Komoditas energi & tambang

Atlas A | Korea Selatan | Komoditas energi & tambang

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,4,4,0). Koefisien kurs yang relevan untuk depresiasi -0,7122, interval nominal 95% [-5,6366; 4,2123], probabilitas nominal 0,773. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -1,38, kuartal keempat -3,24, kuartal ke-24 -6,39 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 0,6149, statistik t -1,4747, probabilitas upper bound F 0,959, probabilitas upper bound t 0,729, probabilitas joint-X 0,994.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,0,4,1,2). Koefisien kurs yang relevan untuk depresiasi 5,8149, interval nominal 95% [-1,3264; 12,9563], probabilitas nominal 0,109. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 7,34, kuartal keempat 25,92, kuartal ke-24 55,22 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,2146, statistik t -2,5558, probabilitas upper bound F 0,441, probabilitas upper bound t 0,406, probabilitas joint-X 0,326.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 105. Atlas A | Malaysia | Non-komoditas manufaktur

Atlas A | Malaysia | Non-komoditas manufaktur

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,1,0). Koefisien kurs yang relevan untuk depresiasi 0,2854, interval nominal 95% [-2,6225; 3,1933], probabilitas nominal 0,845. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUMSQ instability; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 0,37, kuartal keempat 0,97, kuartal ke-24 2,34 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 3,3793, statistik t -1,6767, probabilitas upper bound F 0,164, probabilitas upper bound t 0,704, probabilitas joint-X 0,269.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,1,0,0). Koefisien kurs yang relevan untuk depresiasi 1,9391, interval nominal 95% [-2,6844; 6,5626], probabilitas nominal 0,406. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUMSQ instability; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,07, kuartal keempat 7,78, kuartal ke-24 16,84 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,8003, statistik t -1,8320, probabilitas upper bound F 0,256, probabilitas upper bound t 0,711, probabilitas joint-X 0,345.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 106. Atlas A | Malaysia | Barang konsumsi

Atlas A | Malaysia | Barang konsumsi

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,0,4,1). Koefisien kurs yang relevan untuk depresiasi -0,7463, interval nominal 95% [-4,5321; 3,0395], probabilitas nominal 0,695. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; RESET; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -19,88, kuartal keempat -7,84, kuartal ke-24 -7,15 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 3,5332, statistik t -3,3146, probabilitas upper bound F 0,142, probabilitas upper bound t 0,117, probabilitas joint-X 0,049.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,0,2,4,0). Koefisien kurs yang relevan untuk depresiasi 4,4909, interval nominal 95% [-0,3493; 9,3311], probabilitas nominal 0,068. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 18,00, kuartal keempat 33,31, kuartal ke-24 42,76 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 3,2082, statistik t -3,6458, probabilitas upper bound F 0,168, probabilitas upper bound t 0,094, probabilitas joint-X 0,045.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 107. Atlas A | Malaysia | Komoditas pertanian & pangan

Atlas A | Malaysia | Komoditas pertanian & pangan

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,3,1,0). Koefisien kurs yang relevan untuk depresiasi 0,3380, interval nominal 95% [-2,3500; 3,0261], probabilitas nominal 0,803. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 1,12, kuartal keempat 2,84, kuartal ke-24 3,22 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 3,9029, statistik t -3,6977, probabilitas upper bound F 0,097, probabilitas upper bound t 0,059, probabilitas joint-X 0,830.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,3,1,0,0). Koefisien kurs yang relevan untuk depresiasi 3,4645, interval nominal 95% [-1,6552; 8,5842], probabilitas nominal 0,181. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 12,23, kuartal keempat 29,75, kuartal ke-24 33,02 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 3,6342, statistik t -3,9287, probabilitas upper bound F 0,103, probabilitas upper bound t 0,058, probabilitas joint-X 0,535.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 108. Atlas A | Malaysia | Bahan baku/penolong

Atlas A | Malaysia | Bahan baku/penolong

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,2,3). Koefisien kurs yang relevan untuk depresiasi -0,6453, interval nominal 95% [-2,1932; 0,9025], probabilitas nominal 0,408. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 13,38, kuartal keempat 2,75, kuartal ke-24 -6,15 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 7,0397, statistik t -4,8718, probabilitas upper bound F 0,003, probabilitas upper bound t 0,003, probabilitas joint-X 0,136.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,2,4,1). Koefisien kurs yang relevan untuk depresiasi 1,1759, interval nominal 95% [-1,1127; 3,4644], probabilitas nominal 0,309. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 21,76, kuartal keempat 12,18, kuartal ke-24 11,21 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 6,3864, statistik t -4,9556, probabilitas upper bound F 0,003, probabilitas upper bound t 0,005, probabilitas joint-X 0,053.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 109. Atlas A | Malaysia | Barang modal

Atlas A | Malaysia | Barang modal

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,1,0). Koefisien kurs yang relevan untuk depresiasi 0,1775, interval nominal 95% [-0,9338; 1,2889], probabilitas nominal 0,751. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 1,65, kuartal keempat 1,69, kuartal ke-24 1,69 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 15,8107, statistik t -7,7626, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X <0,001.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,3,2,0,0). Koefisien kurs yang relevan untuk depresiasi 0,7838, interval nominal 95% [-1,3612; 2,9288], probabilitas nominal 0,468. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 7,76, kuartal keempat 7,47, kuartal ke-24 7,47 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 13,2701, statistik t -7,8455, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X <0,001.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 110. Atlas A | Malaysia | Komoditas total

Atlas A | Malaysia | Komoditas total

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,0). Koefisien kurs yang relevan untuk depresiasi -1,2903, interval nominal 95% [-2,7766; 0,1959], probabilitas nominal 0,088. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -7,41, kuartal keempat -13,18, kuartal ke-24 -12,30 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 4,8576, statistik t -3,7931, probabilitas upper bound F 0,035, probabilitas upper bound t 0,049, probabilitas joint-X 0,013.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,4444, interval nominal 95% [-1,0804; 3,9693], probabilitas nominal 0,258. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 9,72, kuartal keempat 14,94, kuartal ke-24 13,77 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 5,7888, statistik t -4,5151, probabilitas upper bound F 0,007, probabilitas upper bound t 0,016, probabilitas joint-X 0,001.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 111. Atlas A | Malaysia | Komoditas energi & tambang

Atlas A | Malaysia | Komoditas energi & tambang

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi -1,3762, interval nominal 95% [-3,0997; 0,3473], probabilitas nominal 0,116. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -7,68, kuartal keempat -12,96, kuartal ke-24 -13,12 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 9,6561, statistik t -5,8486, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X <0,001.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,1172, interval nominal 95% [-2,0436; 4,2780], probabilitas nominal 0,483. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 6,54, kuartal keempat 10,56, kuartal ke-24 10,65 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 8,6445, statistik t -6,1564, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X <0,001.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 112. Atlas A | Singapura | Non-komoditas manufaktur

Atlas A | Singapura | Non-komoditas manufaktur

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 0,0075, interval nominal 95% [-2,0801; 2,0951], probabilitas nominal 0,994. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; heteroskedasticity; CUSUMSQ instability; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 0,03, kuartal keempat 0,06, kuartal ke-24 0,07 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 4,7362, statistik t -4,2551, probabilitas upper bound F 0,039, probabilitas upper bound t 0,017, probabilitas joint-X 0,855.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi -1,5439, interval nominal 95% [-4,5399; 1,4521], probabilitas nominal 0,308. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; heteroskedasticity; CUSUMSQ instability; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -6,36, kuartal keempat -13,85, kuartal ke-24 -14,71 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 4,1040, statistik t -4,3634, probabilitas upper bound F 0,058, probabilitas upper bound t 0,024, probabilitas joint-X 0,693.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 113. Atlas A | Singapura | Barang konsumsi

Atlas A | Singapura | Barang konsumsi

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,0,0,0). Koefisien kurs yang relevan untuk depresiasi 2,6163, interval nominal 95% [-2,6493; 7,8819], probabilitas nominal 0,325. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; RESET; CUSUMSQ instability; ARCH4; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 8,57, kuartal keempat 19,51, kuartal ke-24 24,92 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 5,1969, statistik t -3,8100, probabilitas upper bound F 0,023, probabilitas upper bound t 0,048, probabilitas joint-X 0,011.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,1,0,4,0). Koefisien kurs yang relevan untuk depresiasi -0,1019, interval nominal 95% [-10,9807; 10,7770], probabilitas nominal 0,985. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; RESET; CUSUMSQ instability; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -0,28, kuartal keempat -0,71, kuartal ke-24 -0,97 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,1511, statistik t -2,7644, probabilitas upper bound F 0,466, probabilitas upper bound t 0,341, probabilitas joint-X 0,317.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 114. Atlas A | Singapura | Komoditas pertanian & pangan

Atlas A | Singapura | Komoditas pertanian & pangan

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,4). Koefisien kurs yang relevan untuk depresiasi 5,9816, interval nominal 95% [0,7131; 11,2502], probabilitas nominal 0,027. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 4,92, kuartal keempat 14,81, kuartal ke-24 52,35 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,6847, statistik t -2,5689, probabilitas upper bound F 0,310, probabilitas upper bound t 0,338, probabilitas joint-X 0,025.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,0,0,1,3). Koefisien kurs yang relevan untuk depresiasi 4,9405, interval nominal 95% [-0,8349; 10,7160], probabilitas nominal 0,092. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 25,80, kuartal keempat 25,02, kuartal ke-24 46,60 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,1087, statistik t -2,8302, probabilitas upper bound F 0,483, probabilitas upper bound t 0,321, probabilitas joint-X 0,144.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 115. Atlas A | Singapura | Bahan baku/penolong

Atlas A | Singapura | Bahan baku/penolong

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,0,0). Koefisien kurs yang relevan untuk depresiasi 0,4235, interval nominal 95% [-1,1965; 2,0436], probabilitas nominal 0,604. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 1,47, kuartal keempat 3,62, kuartal ke-24 4,04 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 4,1308, statistik t -3,9464, probabilitas upper bound F 0,076, probabilitas upper bound t 0,035, probabilitas joint-X 0,255.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,1,0,0). Koefisien kurs yang relevan untuk depresiasi -2,0320, interval nominal 95% [-3,7613; -0,3027], probabilitas nominal 0,022. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -10,86, kuartal keempat -19,05, kuartal ke-24 -19,37 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 5,3459, statistik t -5,0701, probabilitas upper bound F 0,012, probabilitas upper bound t 0,004, probabilitas joint-X 0,016.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 116. Atlas A | Singapura | Barang modal

Atlas A | Singapura | Barang modal

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,4692, interval nominal 95% [-2,6496; 1,7112], probabilitas nominal 0,669. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -2,84, kuartal keempat -4,44, kuartal ke-24 -4,47 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 8,5700, statistik t -5,8397, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X 0,138.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,1,0,2,0). Koefisien kurs yang relevan untuk depresiasi -1,3034, interval nominal 95% [-4,8827; 2,2758], probabilitas nominal 0,470. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -8,03, kuartal keempat -12,35, kuartal ke-24 -12,42 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 7,2556, statistik t -5,9832, probabilitas upper bound F 0,001, probabilitas upper bound t <0,001, probabilitas joint-X 0,093.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 117. Atlas A | Singapura | Komoditas total

Atlas A | Singapura | Komoditas total

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,0,0). Koefisien kurs yang relevan untuk depresiasi -1,1917, interval nominal 95% [-2,2306; -0,1528], probabilitas nominal 0,025. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -8,69, kuartal keempat -11,35, kuartal ke-24 -11,36 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 12,4041, statistik t -6,9687, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X 0,066.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,1,2,4,0). Koefisien kurs yang relevan untuk depresiasi -0,7007, interval nominal 95% [-2,6860; 1,2847], probabilitas nominal 0,483. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; RESET. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,61, kuartal keempat -6,66, kuartal ke-24 -6,68 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 9,0942, statistik t -6,4767, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X 0,197.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 118. Atlas A | Singapura | Komoditas energi & tambang

Atlas A | Singapura | Komoditas energi & tambang

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,0,0). Koefisien kurs yang relevan untuk depresiasi -1,3833, interval nominal 95% [-2,5018; -0,2647], probabilitas nominal 0,016. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -10,55, kuartal keempat -13,18, kuartal ke-24 -13,18 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 13,0674, statistik t -7,1699, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X 0,157.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,1,2,4,0). Koefisien kurs yang relevan untuk depresiasi -0,7085, interval nominal 95% [-2,8168; 1,3997], probabilitas nominal 0,504. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,90, kuartal keempat -6,74, kuartal ke-24 -6,75 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 9,7660, statistik t -6,7165, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X 0,200.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 119. Atlas A | Thailand | Non-komoditas manufaktur

Atlas A | Thailand | Non-komoditas manufaktur

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,1,1,3). Koefisien kurs yang relevan untuk depresiasi 1,0008, interval nominal 95% [-0,6058; 2,6073], probabilitas nominal 0,218. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; non-normal residuals. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -0,31, kuartal keempat 6,19, kuartal ke-24 9,54 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 3,9345, statistik t -3,8192, probabilitas upper bound F 0,094, probabilitas upper bound t 0,045, probabilitas joint-X 0,115.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,3,1,1,3). Koefisien kurs yang relevan untuk depresiasi 0,5635, interval nominal 95% [-3,1996; 4,3266], probabilitas nominal 0,766. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 7,55, kuartal keempat 4,75, kuartal ke-24 5,37 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 3,1602, statistik t -3,5321, probabilitas upper bound F 0,177, probabilitas upper bound t 0,113, probabilitas joint-X 0,231.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 120. Atlas A | Thailand | Barang konsumsi

Atlas A | Thailand | Barang konsumsi

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 2,5435, interval nominal 95% [0,4987; 4,5883], probabilitas nominal 0,015. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 12,48, kuartal keempat 23,59, kuartal ke-24 24,24 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 7,3004, statistik t -5,3727, probabilitas upper bound F 0,002, probabilitas upper bound t <0,001, probabilitas joint-X <0,001.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,0,0,0,1). Koefisien kurs yang relevan untuk depresiasi 0,3537, interval nominal 95% [-5,0349; 5,7422], probabilitas nominal 0,896. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 28,25, kuartal keempat 6,52, kuartal ke-24 3,37 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 3,6086, statistik t -4,0777, probabilitas upper bound F 0,105, probabilitas upper bound t 0,044, probabilitas joint-X 0,005.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 121. Atlas A | Thailand | Komoditas pertanian & pangan

Atlas A | Thailand | Komoditas pertanian & pangan

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,2,0,2). Koefisien kurs yang relevan untuk depresiasi 1,9059, interval nominal 95% [-1,1431; 4,9549], probabilitas nominal 0,216. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 21,17, kuartal keempat 20,01, kuartal ke-24 18,17 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 4,2854, statistik t -4,1311, probabilitas upper bound F 0,065, probabilitas upper bound t 0,022, probabilitas joint-X 0,075.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,0,0,0,2). Koefisien kurs yang relevan untuk depresiasi 3,8478, interval nominal 95% [-1,4844; 9,1800], probabilitas nominal 0,155. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 49,03, kuartal keempat 43,03, kuartal ke-24 36,67 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 6,8377, statistik t -5,8291, probabilitas upper bound F 0,002, probabilitas upper bound t <0,001, probabilitas joint-X 0,025.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 122. Atlas A | Thailand | Bahan baku/penolong

Atlas A | Thailand | Bahan baku/penolong

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,3,3,0). Koefisien kurs yang relevan untuk depresiasi 1,0630, interval nominal 95% [0,1019; 2,0241], probabilitas nominal 0,031. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 5,59, kuartal keempat 9,95, kuartal ke-24 10,13 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 8,7024, statistik t -5,7535, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X 0,003.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,4,4,0,4). Koefisien kurs yang relevan untuk depresiasi -1,5678, interval nominal 95% [-3,5806; 0,4449], probabilitas nominal 0,124. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -6,96, kuartal keempat -7,01, kuartal ke-24 -14,94 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 8,4614, statistik t -6,2943, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X 0,001.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 123. Atlas A | Thailand | Barang modal

Atlas A | Thailand | Barang modal

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,0,3). Koefisien kurs yang relevan untuk depresiasi -1,0271, interval nominal 95% [-3,6264; 1,5723], probabilitas nominal 0,433. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -41,77, kuartal keempat -11,89, kuartal ke-24 -9,79 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 11,0246, statistik t -6,5494, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X 0,176.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,0,0,3). Koefisien kurs yang relevan untuk depresiasi 2,5931, interval nominal 95% [-2,9641; 8,1503], probabilitas nominal 0,355. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; RESET; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -43,21, kuartal keempat 21,38, kuartal ke-24 24,71 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 9,5010, statistik t -6,6664, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X 0,089.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 124. Atlas A | Thailand | Komoditas total

Atlas A | Thailand | Komoditas total

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,0,1,0). Koefisien kurs yang relevan untuk depresiasi 1,0469, interval nominal 95% [-0,3425; 2,4364], probabilitas nominal 0,137. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 8,69, kuartal keempat 9,71, kuartal ke-24 9,98 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 12,2947, statistik t -6,9577, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X 0,099.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,1,0,0,2). Koefisien kurs yang relevan untuk depresiasi 3,4540, interval nominal 95% [0,4602; 6,4479], probabilitas nominal 0,024. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 35,25, kuartal keempat 37,52, kuartal ke-24 32,92 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 10,8930, statistik t -7,2611, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X 0,059.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 125. Atlas A | Thailand | Komoditas energi & tambang

Atlas A | Thailand | Komoditas energi & tambang

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,0,1,0). Koefisien kurs yang relevan untuk depresiasi -0,5923, interval nominal 95% [-1,6557; 0,4710], probabilitas nominal 0,270. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -5,44, kuartal keempat -5,57, kuartal ke-24 -5,65 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 14,7069, statistik t -7,4577, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X 0,167.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,1,0,1). Koefisien kurs yang relevan untuk depresiasi 0,7551, interval nominal 95% [-2,0566; 3,5668], probabilitas nominal 0,594. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -16,11, kuartal keempat 2,99, kuartal ke-24 7,20 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 4,9373, statistik t -4,5379, probabilitas upper bound F 0,021, probabilitas upper bound t 0,015, probabilitas joint-X 0,342.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 126. Atlas A | Amerika Serikat | Non-komoditas manufaktur

Atlas A | Amerika Serikat | Non-komoditas manufaktur

ARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (2,2,2,0). Koefisien kurs yang relevan untuk depresiasi 1,5174, interval nominal 95% [-0,7999; 3,8347], probabilitas nominal 0,196. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 4,51, kuartal keempat 10,74, kuartal ke-24 14,44 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 3,6566, statistik t -2,8224, probabilitas upper bound F 0,126, probabilitas upper bound t 0,254, probabilitas joint-X 0,016.

NARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (2,2,3,0,2). Koefisien kurs yang relevan untuk depresiasi 2,1894, interval nominal 95% [-0,7507; 5,1295], probabilitas nominal 0,142. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 10,36, kuartal keempat 13,96, kuartal ke-24 20,86 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 3,6674, statistik t -3,3619, probabilitas upper bound F 0,102, probabilitas upper bound t 0,150, probabilitas joint-X 0,013.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 127. Atlas A | Amerika Serikat | Barang konsumsi

Atlas A | Amerika Serikat | Barang konsumsi

ARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (4,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,3352, interval nominal 95% [-4,7642; 4,0938], probabilitas nominal 0,880. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -0,69, kuartal keempat -1,35, kuartal ke-24 -2,87 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 1,1988, statistik t -1,5924, probabilitas upper bound F 0,822, probabilitas upper bound t 0,737, probabilitas joint-X 0,483.

NARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (2,1,0,2,3). Koefisien kurs yang relevan untuk depresiasi 5,8605, interval nominal 95% [3,2348; 8,4862], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -4,37, kuartal keempat 48,42, kuartal ke-24 55,86 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 5,4669, statistik t -5,0093, probabilitas upper bound F 0,012, probabilitas upper bound t 0,004, probabilitas joint-X <0,001.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 128. Atlas A | Amerika Serikat | Komoditas pertanian & pangan

Atlas A | Amerika Serikat | Komoditas pertanian & pangan

ARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,8364, interval nominal 95% [-1,5190; -0,1538], probabilitas nominal 0,017. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -7,07, kuartal keempat -7,97, kuartal ke-24 -7,97 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 17,8986, statistik t -8,2964, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X <0,001.

NARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (1,0,0,1,1). Koefisien kurs yang relevan untuk depresiasi 0,6216, interval nominal 95% [-0,5130; 1,7562], probabilitas nominal 0,278. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -10,97, kuartal keempat 5,92, kuartal ke-24 5,92 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 16,7726, statistik t -9,0435, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X <0,001.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 129. Atlas A | Amerika Serikat | Bahan baku/penolong

Atlas A | Amerika Serikat | Bahan baku/penolong

ARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (1,0,1,0). Koefisien kurs yang relevan untuk depresiasi -0,3133, interval nominal 95% [-1,2718; 0,6452], probabilitas nominal 0,517. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; RESET; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -1,58, kuartal keempat -2,92, kuartal ke-24 -2,99 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 7,2475, statistik t -5,1838, probabilitas upper bound F 0,002, probabilitas upper bound t 0,001, probabilitas joint-X 0,034.

NARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (1,0,2,2,3). Koefisien kurs yang relevan untuk depresiasi 2,9242, interval nominal 95% [1,2686; 4,5798], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; RESET. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -4,77, kuartal keempat 25,37, kuartal ke-24 27,87 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 10,1212, statistik t -6,6788, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X <0,001.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 130. Atlas A | Amerika Serikat | Barang modal

Atlas A | Amerika Serikat | Barang modal

ARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (2,0,0,3). Koefisien kurs yang relevan untuk depresiasi 1,1657, interval nominal 95% [-7,1420; 9,4733], probabilitas nominal 0,780. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 35,46, kuartal keempat 29,96, kuartal ke-24 11,83 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,4056, statistik t -2,1487, probabilitas upper bound F 0,392, probabilitas upper bound t 0,521, probabilitas joint-X 0,138.

NARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (2,0,0,1,3). Koefisien kurs yang relevan untuk depresiasi 4,5302, interval nominal 95% [-6,9697; 16,0301], probabilitas nominal 0,434. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 8,12, kuartal keempat 40,28, kuartal ke-24 43,05 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,1679, statistik t -2,5155, probabilitas upper bound F 0,460, probabilitas upper bound t 0,441, probabilitas joint-X 0,253.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 131. Atlas A | Amerika Serikat | Komoditas total

Atlas A | Amerika Serikat | Komoditas total

ARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (4,0,2,3). Koefisien kurs yang relevan untuk depresiasi -0,0878, interval nominal 95% [-1,6676; 1,4919], probabilitas nominal 0,912. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,20, kuartal keempat -4,33, kuartal ke-24 -0,87 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 3,1196, statistik t -3,0451, probabilitas upper bound F 0,211, probabilitas upper bound t 0,178, probabilitas joint-X 0,103.

NARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (4,1,2,2,3). Koefisien kurs yang relevan untuk depresiasi 3,5917, interval nominal 95% [1,6312; 5,5521], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -2,80, kuartal keempat 25,47, kuartal ke-24 34,21 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 6,9355, statistik t -5,0030, probabilitas upper bound F 0,002, probabilitas upper bound t 0,005, probabilitas joint-X <0,001.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 132. Atlas A | Amerika Serikat | Komoditas energi & tambang

Atlas A | Amerika Serikat | Komoditas energi & tambang

ARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (4,0,1,0). Koefisien kurs yang relevan untuk depresiasi 5,8692, interval nominal 95% [-3,4611; 15,1996], probabilitas nominal 0,214. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 14,03, kuartal keempat 27,71, kuartal ke-24 52,84 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,9139, statistik t -2,5858, probabilitas upper bound F 0,254, probabilitas upper bound t 0,344, probabilitas joint-X 0,015.

NARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (4,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 13,5273, interval nominal 95% [-15,4049; 42,4595], probabilitas nominal 0,354. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 22,14, kuartal keempat 46,12, kuartal ke-24 109,03 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 2,1048, statistik t -1,7226, probabilitas upper bound F 0,484, probabilitas upper bound t 0,751, probabilitas joint-X 0,049.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 133. Atlas A | Vietnam | Non-komoditas manufaktur

Atlas A | Vietnam | Non-komoditas manufaktur

ARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (4,0,0,0). Koefisien kurs yang relevan untuk depresiasi 2,7854, interval nominal 95% [-2,5336; 8,1044], probabilitas nominal 0,300. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 4,82, kuartal keempat 10,93, kuartal ke-24 23,93 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 6,8659, statistik t -1,8523, probabilitas upper bound F 0,004, probabilitas upper bound t 0,645, probabilitas joint-X 0,007.

NARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (4,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,0254, interval nominal 95% [-4,4483; 4,3976], probabilitas nominal 0,991. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -0,06, kuartal keempat -0,13, kuartal ke-24 -0,23 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 5,7282, statistik t -2,1243, probabilitas upper bound F 0,008, probabilitas upper bound t 0,609, probabilitas joint-X 0,010.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 134. Atlas A | Vietnam | Barang konsumsi

Atlas A | Vietnam | Barang konsumsi

ARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 3,9945, interval nominal 95% [1,1858; 6,8032], probabilitas nominal 0,006. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; ARCH4. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 21,71, kuartal keempat 37,51, kuartal ke-24 38,07 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 7,5684, statistik t -5,4590, probabilitas upper bound F 0,002, probabilitas upper bound t <0,001, probabilitas joint-X 0,003.

NARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 4,6844, interval nominal 95% [0,4447; 8,9241], probabilitas nominal 0,031. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; ARCH4. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 25,87, kuartal keempat 44,06, kuartal ke-24 44,65 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 6,0198, statistik t -5,4047, probabilitas upper bound F 0,005, probabilitas upper bound t 0,001, probabilitas joint-X 0,008.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 135. Atlas A | Vietnam | Komoditas pertanian & pangan

Atlas A | Vietnam | Komoditas pertanian & pangan

ARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (2,0,0,0). Koefisien kurs yang relevan untuk depresiasi 5,9112, interval nominal 95% [1,5175; 10,3050], probabilitas nominal 0,009. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 27,04, kuartal keempat 56,99, kuartal ke-24 56,34 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 6,1480, statistik t -4,8625, probabilitas upper bound F 0,008, probabilitas upper bound t 0,003, probabilitas joint-X 0,065.

NARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (2,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 7,2605, interval nominal 95% [0,8901; 13,6309], probabilitas nominal 0,026. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 34,46, kuartal keempat 70,31, kuartal ke-24 69,20 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 4,9321, statistik t -4,7774, probabilitas upper bound F 0,021, probabilitas upper bound t 0,009, probabilitas joint-X 0,112.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 136. Atlas A | Vietnam | Bahan baku/penolong

Atlas A | Vietnam | Bahan baku/penolong

ARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (4,0,1,0). Koefisien kurs yang relevan untuk depresiasi -1,2816, interval nominal 95% [-3,0727; 0,5096], probabilitas nominal 0,158. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; heteroskedasticity; RESET; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -5,49, kuartal keempat -9,27, kuartal ke-24 -12,20 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 6,7944, statistik t -4,4389, probabilitas upper bound F 0,004, probabilitas upper bound t 0,011, probabilitas joint-X <0,001.

NARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (4,0,1,0,0). Koefisien kurs yang relevan untuk depresiasi -2,0689, interval nominal 95% [-5,1617; 1,0240], probabilitas nominal 0,186. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; heteroskedasticity; RESET; CUSUMSQ instability; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -8,53, kuartal keempat -14,56, kuartal ke-24 -19,69 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 5,4808, statistik t -4,1250, probabilitas upper bound F 0,011, probabilitas upper bound t 0,039, probabilitas joint-X <0,001.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 137. Atlas A | Vietnam | Barang modal

Atlas A | Vietnam | Barang modal

ARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (2,0,0,1). Koefisien kurs yang relevan untuk depresiasi 2,7728, interval nominal 95% [-1,0085; 6,5542], probabilitas nominal 0,148. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -19,53, kuartal keempat 18,70, kuartal ke-24 26,42 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 3,4905, statistik t -3,6860, probabilitas upper bound F 0,147, probabilitas upper bound t 0,062, probabilitas joint-X 0,075.

NARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (1,0,0,0,1). Koefisien kurs yang relevan untuk depresiasi -0,9612, interval nominal 95% [-4,8246; 2,9023], probabilitas nominal 0,621. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -77,56, kuartal keempat -11,07, kuartal ke-24 -9,16 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 8,0540, statistik t -6,0362, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X <0,001.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 138. Atlas A | Vietnam | Komoditas total

Atlas A | Vietnam | Komoditas total

ARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 2,1228, interval nominal 95% [-1,5442; 5,7899], probabilitas nominal 0,252. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 10,94, kuartal keempat 19,82, kuartal ke-24 20,23 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 6,6802, statistik t -5,1314, probabilitas upper bound F 0,004, probabilitas upper bound t 0,001, probabilitas joint-X 0,058.

NARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 2,2873, interval nominal 95% [-3,4483; 8,0230], probabilitas nominal 0,429. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 11,83, kuartal keempat 21,36, kuartal ke-24 21,80 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 5,2682, statistik t -4,9782, probabilitas upper bound F 0,014, probabilitas upper bound t 0,005, probabilitas joint-X 0,114.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 139. Atlas A | Vietnam | Komoditas energi & tambang

Atlas A | Vietnam | Komoditas energi & tambang

ARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi -3,9664, interval nominal 95% [-7,2593; -0,6735], probabilitas nominal 0,019. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; heteroskedasticity; CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -33,85, kuartal keempat -37,80, kuartal ke-24 -37,80 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 16,6937, statistik t -8,0236, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X <0,001.

NARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi -4,2059, interval nominal 95% [-9,2909; 0,8790], probabilitas nominal 0,103. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; heteroskedasticity; CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -35,88, kuartal keempat -40,09, kuartal ke-24 -40,09 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag. Bounds F 13,1675, statistik t -7,9592, probabilitas upper bound F <0,001, probabilitas upper bound t <0,001, probabilitas joint-X <0,001.

SUMBER DAN REPRODUKSI
Sumber: model utama Stata; dynamic_multipliers.csv. Guncangan log simetris; band pointwise nominal 95%.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 140. Atlas koefisien tujuh kelompok

Atlas koefisien tujuh kelompok

Setiap pasar mempunyai grafik interval ARDL dan NARDL. Grafik memisahkan tanda koefisien, ketepatan estimasi dan status model. Ketujuh kategori bertumpang tindih; perbedaan signifikansi belum menjadi uji beda koefisien.

SUMBER DAN REPRODUKSI
Sumber: keluaran estimasi Stata HS-6; seluruh spesifikasi tetap ditampilkan.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 141. Atlas B | Kelompok barang: Dunia

Atlas B | Kelompok barang: Dunia

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,0,1,0). Koefisien kurs yang relevan untuk depresiasi 0,0053, interval nominal 95% [-1,2485; 1,2591], probabilitas nominal 0,993. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 0,03, kuartal keempat 0,05, kuartal ke-24 0,05 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,3,0,0,0). Koefisien kurs yang relevan untuk depresiasi -1,6214, interval nominal 95% [-4,0845; 0,8418], probabilitas nominal 0,192. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -11,38, kuartal keempat -15,43, kuartal ke-24 -15,45 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,0,0,3). Koefisien kurs yang relevan untuk depresiasi 1,4250, interval nominal 95% [-1,7541; 4,6042], probabilitas nominal 0,373. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -15,19, kuartal keempat 6,74, kuartal ke-24 13,58 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,0,0,3,2). Koefisien kurs yang relevan untuk depresiasi 1,5889, interval nominal 95% [-2,1877; 5,3655], probabilitas nominal 0,402. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -5,64, kuartal keempat 17,02, kuartal ke-24 15,14 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,3,0,0). Koefisien kurs yang relevan untuk depresiasi -1,3546, interval nominal 95% [-1,9985; -0,7108], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -10,01, kuartal keempat -12,90, kuartal ke-24 -12,91 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (2,3,0,0,4). Koefisien kurs yang relevan untuk depresiasi -0,5045, interval nominal 95% [-2,1452; 1,1362], probabilitas nominal 0,539. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -7,76, kuartal keempat -8,66, kuartal ke-24 -4,81 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (2,3,0,4). Koefisien kurs yang relevan untuk depresiasi 2,0258, interval nominal 95% [0,1983; 3,8534], probabilitas nominal 0,031. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -9,93, kuartal keempat 8,97, kuartal ke-24 19,31 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (2,0,0,0,4). Koefisien kurs yang relevan untuk depresiasi 4,5800, interval nominal 95% [2,3007; 6,8592], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; heteroskedasticity; RESET; CUSUMSQ instability. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -2,91, kuartal keempat 27,39, kuartal ke-24 43,65 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,4,2,0). Koefisien kurs yang relevan untuk depresiasi -2,0399, interval nominal 95% [-2,6286; -1,4512], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -21,34, kuartal keempat -19,44, kuartal ke-24 -19,44 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,0,4,2,0). Koefisien kurs yang relevan untuk depresiasi -0,1117, interval nominal 95% [-1,1341; 0,9106], probabilitas nominal 0,827. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -1,06, kuartal keempat -1,07, kuartal ke-24 -1,07 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (3,3,0,3). Koefisien kurs yang relevan untuk depresiasi -0,1390, interval nominal 95% [-6,9050; 6,6270], probabilitas nominal 0,967. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 0,17, kuartal keempat -3,86, kuartal ke-24 -2,84 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (3,0,1,0,3). Koefisien kurs yang relevan untuk depresiasi 7,8510, interval nominal 95% [-12,0140; 27,7159], probabilitas nominal 0,431. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 11,10, kuartal keempat 18,80, kuartal ke-24 54,76 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,3,3,3). Koefisien kurs yang relevan untuk depresiasi 0,8651, interval nominal 95% [-0,5995; 2,3297], probabilitas nominal 0,241. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 0,59, kuartal keempat 2,25, kuartal ke-24 8,24 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,3,3,3,0). Koefisien kurs yang relevan untuk depresiasi 1,3581, interval nominal 95% [-0,8318; 3,5480], probabilitas nominal 0,218. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 5,71, kuartal keempat 12,24, kuartal ke-24 12,94 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: results_primary_models.csv; HS6_Classification.csv. Interval nominal 95% setelah seleksi AIC.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 142. Atlas B | Kelompok barang: Australia

Atlas B | Kelompok barang: Australia

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,3,2). Koefisien kurs yang relevan untuk depresiasi -1,7703, interval nominal 95% [-3,4818; -0,0589], probabilitas nominal 0,043. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -6,16, kuartal keempat -15,10, kuartal ke-24 -16,87 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,3,0,0,0). Koefisien kurs yang relevan untuk depresiasi -3,3446, interval nominal 95% [-5,0000; -1,6893], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -21,74, kuartal keempat -31,77, kuartal ke-24 -31,88 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 4,0019, interval nominal 95% [-1,0640; 9,0678], probabilitas nominal 0,120. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; heteroskedasticity; CUSUMSQ instability; ARCH4. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 21,96, kuartal keempat 37,62, kuartal ke-24 38,14 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 7,4662, interval nominal 95% [0,3024; 14,6300], probabilitas nominal 0,041. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; heteroskedasticity; RESET; CUSUMSQ instability; ARCH4; CUSUM instability or unavailable; Recursive initial matrix rank deficient; official Stata CUSUM retained. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 42,00, kuartal keempat 70,34, kuartal ke-24 71,16 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,4,0). Koefisien kurs yang relevan untuk depresiasi 1,7010, interval nominal 95% [0,4539; 2,9481], probabilitas nominal 0,008. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 11,33, kuartal keempat 16,17, kuartal ke-24 16,21 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,4,0,1). Koefisien kurs yang relevan untuk depresiasi 1,3791, interval nominal 95% [-0,4746; 3,2328], probabilitas nominal 0,142. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -10,61, kuartal keempat 12,97, kuartal ke-24 13,14 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 0,7041, interval nominal 95% [-0,6861; 2,0943], probabilitas nominal 0,316. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 5,76, kuartal keempat 6,71, kuartal ke-24 6,71 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,0881, interval nominal 95% [-0,9258; 3,1020], probabilitas nominal 0,285. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: Recursive initial matrix rank deficient; official Stata CUSUM retained. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 8,93, kuartal keempat 10,37, kuartal ke-24 10,37 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,1,4,0). Koefisien kurs yang relevan untuk depresiasi 3,2646, interval nominal 95% [0,3978; 6,1313], probabilitas nominal 0,026. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 18,70, kuartal keempat 30,80, kuartal ke-24 31,11 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,1,4,0,1). Koefisien kurs yang relevan untuk depresiasi 5,7253, interval nominal 95% [1,6941; 9,7565], probabilitas nominal 0,006. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -13,67, kuartal keempat 53,02, kuartal ke-24 54,57 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,4,4,0). Koefisien kurs yang relevan untuk depresiasi 1,6082, interval nominal 95% [0,2219; 2,9946], probabilitas nominal 0,024. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 9,65, kuartal keempat 15,22, kuartal ke-24 15,33 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,4,4,0,0). Koefisien kurs yang relevan untuk depresiasi 2,5180, interval nominal 95% [0,6163; 4,4197], probabilitas nominal 0,010. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 15,63, kuartal keempat 23,87, kuartal ke-24 24,00 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 0,9189, interval nominal 95% [-1,5492; 3,3869], probabilitas nominal 0,460. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: ARCH4. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,20, kuartal keempat 7,86, kuartal ke-24 8,76 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,1,0,4,4). Koefisien kurs yang relevan untuk depresiasi 5,6284, interval nominal 95% [1,9258; 9,3309], probabilitas nominal 0,003. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -7,07, kuartal keempat 28,33, kuartal ke-24 53,64 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: results_primary_models.csv; HS6_Classification.csv. Interval nominal 95% setelah seleksi AIC.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 143. Atlas B | Kelompok barang: Tiongkok

Atlas B | Kelompok barang: Tiongkok

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,1,1,1). Koefisien kurs yang relevan untuk depresiasi -0,8091, interval nominal 95% [-1,8324; 0,2142], probabilitas nominal 0,119. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 10,40, kuartal keempat -1,69, kuartal ke-24 -7,68 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,1,1,0,1). Koefisien kurs yang relevan untuk depresiasi -2,0365, interval nominal 95% [-3,2688; -0,8041], probabilitas nominal 0,002. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 12,14, kuartal keempat -10,16, kuartal ke-24 -19,39 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,1,4). Koefisien kurs yang relevan untuk depresiasi 1,2107, interval nominal 95% [-1,2265; 3,6479], probabilitas nominal 0,325. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; ARCH4; non-normal residuals. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -6,03, kuartal keempat 6,37, kuartal ke-24 11,54 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,1,0,4). Koefisien kurs yang relevan untuk depresiasi 0,5950, interval nominal 95% [-3,3482; 4,5381], probabilitas nominal 0,764. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; CUSUMSQ instability; ARCH4; non-normal residuals. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 9,63, kuartal keempat -3,75, kuartal ke-24 5,67 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,1,1,3). Koefisien kurs yang relevan untuk depresiasi -2,2156, interval nominal 95% [-3,7559; -0,6753], probabilitas nominal 0,005. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 3,16, kuartal keempat -12,41, kuartal ke-24 -20,99 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,1,3,0,3). Koefisien kurs yang relevan untuk depresiasi -3,4577, interval nominal 95% [-5,0908; -1,8246], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: RESET; CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 12,96, kuartal keempat -25,23, kuartal ke-24 -32,96 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,2,3). Koefisien kurs yang relevan untuk depresiasi -0,5694, interval nominal 95% [-2,5424; 1,4037], probabilitas nominal 0,567. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability; ARCH4. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 16,75, kuartal keempat 2,25, kuartal ke-24 -5,43 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,2,3,1). Koefisien kurs yang relevan untuk depresiasi -2,7105, interval nominal 95% [-5,1642; -0,2569], probabilitas nominal 0,031. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 6,43, kuartal keempat -24,98, kuartal ke-24 -25,83 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,2). Koefisien kurs yang relevan untuk depresiasi -1,9236, interval nominal 95% [-4,2355; 0,3883], probabilitas nominal 0,101. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,12, kuartal keempat -13,59, kuartal ke-24 -18,27 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,1,0,3). Koefisien kurs yang relevan untuk depresiasi -3,6577, interval nominal 95% [-6,7794; -0,5361], probabilitas nominal 0,022. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 9,11, kuartal keempat -26,98, kuartal ke-24 -34,82 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,3,0,0). Koefisien kurs yang relevan untuk depresiasi -3,2911, interval nominal 95% [-6,5213; -0,0610], probabilitas nominal 0,046. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,93, kuartal keempat -14,00, kuartal ke-24 -29,12 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,3,0,4,4). Koefisien kurs yang relevan untuk depresiasi -6,2342, interval nominal 95% [-10,3438; -2,1246], probabilitas nominal 0,004. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 0,12, kuartal keempat -37,14, kuartal ke-24 -57,42 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,4,1,0). Koefisien kurs yang relevan untuk depresiasi 0,3002, interval nominal 95% [-3,5723; 4,1727], probabilitas nominal 0,878. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; non-normal residuals. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 0,36, kuartal keempat 1,22, kuartal ke-24 2,67 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,1,4,1,4). Koefisien kurs yang relevan untuk depresiasi 3,0325, interval nominal 95% [-10,8359; 16,9010], probabilitas nominal 0,663. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 11,22, kuartal keempat 9,74, kuartal ke-24 24,73 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: results_primary_models.csv; HS6_Classification.csv. Interval nominal 95% setelah seleksi AIC.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 144. Atlas B | Kelompok barang: India

Atlas B | Kelompok barang: India

ARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (4,4,1,0). Koefisien kurs yang relevan untuk depresiasi 6,3247, interval nominal 95% [-21,2899; 33,9392], probabilitas nominal 0,645. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 11,68, kuartal keempat 25,49, kuartal ke-24 54,56 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,1,1,0,3). Koefisien kurs yang relevan untuk depresiasi -5,0762, interval nominal 95% [-15,1988; 5,0463], probabilitas nominal 0,316. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 47,20, kuartal keempat -55,35, kuartal ke-24 -48,38 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,0118, interval nominal 95% [-17,5869; 19,6106], probabilitas nominal 0,913. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 4,01, kuartal keempat 8,99, kuartal ke-24 9,64 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 0,8154, interval nominal 95% [-20,5914; 22,2223], probabilitas nominal 0,939. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,23, kuartal keempat 7,24, kuartal ke-24 7,77 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,4,1,4). Koefisien kurs yang relevan untuk depresiasi 5,4757, interval nominal 95% [-12,9124; 23,8639], probabilitas nominal 0,549. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 36,06, kuartal keempat 49,52, kuartal ke-24 52,19 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,1,1,0,3). Koefisien kurs yang relevan untuk depresiasi -4,5686, interval nominal 95% [-13,7475; 4,6104], probabilitas nominal 0,320. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 33,20, kuartal keempat -52,88, kuartal ke-24 -43,54 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 3,9821, interval nominal 95% [-8,8526; 16,8169], probabilitas nominal 0,535. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 15,93, kuartal keempat 35,46, kuartal ke-24 37,95 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (2,2,4,1,4). Koefisien kurs yang relevan untuk depresiasi -8,9044, interval nominal 95% [-19,2714; 1,4625], probabilitas nominal 0,090. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 31,36, kuartal keempat -61,42, kuartal ke-24 -84,87 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,4,0,0). Koefisien kurs yang relevan untuk depresiasi 7,8277, interval nominal 95% [-9,1835; 24,8390], probabilitas nominal 0,358. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 28,75, kuartal keempat 68,06, kuartal ke-24 74,61 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (2,3,4,4,4). Koefisien kurs yang relevan untuk depresiasi -4,5058, interval nominal 95% [-14,1408; 5,1292], probabilitas nominal 0,346. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 45,70, kuartal keempat -15,87, kuartal ke-24 -42,94 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,4,1,3). Koefisien kurs yang relevan untuk depresiasi 10,8457, interval nominal 95% [-7,5657; 29,2570], probabilitas nominal 0,240. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 49,87, kuartal keempat 40,71, kuartal ke-24 102,81 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,2,1,3,3). Koefisien kurs yang relevan untuk depresiasi 2,9378, interval nominal 95% [-12,5378; 18,4134], probabilitas nominal 0,702. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 7,67, kuartal keempat -18,98, kuartal ke-24 27,83 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (2,0,0,1). Koefisien kurs yang relevan untuk depresiasi -4,5016, interval nominal 95% [-15,0384; 6,0352], probabilitas nominal 0,393. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 13,01, kuartal keempat -25,38, kuartal ke-24 -42,80 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (2,0,2,0,1). Koefisien kurs yang relevan untuk depresiasi -6,3792, interval nominal 95% [-15,8100; 3,0516], probabilitas nominal 0,179. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 14,94, kuartal keempat -42,19, kuartal ke-24 -60,77 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: results_primary_models.csv; HS6_Classification.csv. Interval nominal 95% setelah seleksi AIC.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 145. Atlas B | Kelompok barang: Jepang

Atlas B | Kelompok barang: Jepang

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,0753, interval nominal 95% [-1,6760; 1,5254], probabilitas nominal 0,925. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -0,18, kuartal keempat -0,36, kuartal ke-24 -0,68 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi -1,7117, interval nominal 95% [-2,9748; -0,4486], probabilitas nominal 0,009. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -7,38, kuartal keempat -11,98, kuartal ke-24 -16,26 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,4,0,2). Koefisien kurs yang relevan untuk depresiasi -3,0683, interval nominal 95% [-6,4566; 0,3199], probabilitas nominal 0,075. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -19,39, kuartal keempat -16,51, kuartal ke-24 -28,49 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,4,0,1,2). Koefisien kurs yang relevan untuk depresiasi -4,6872, interval nominal 95% [-7,6391; -1,7353], probabilitas nominal 0,002. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -24,26, kuartal keempat -29,18, kuartal ke-24 -44,48 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,2,3). Koefisien kurs yang relevan untuk depresiasi -1,7710, interval nominal 95% [-3,0921; -0,4500], probabilitas nominal 0,009. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: RESET; CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -8,42, kuartal keempat -18,08, kuartal ke-24 -16,88 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,2,0,3). Koefisien kurs yang relevan untuk depresiasi -0,7102, interval nominal 95% [-2,7675; 1,3471], probabilitas nominal 0,493. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -3,84, kuartal keempat -9,49, kuartal ke-24 -6,77 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,1,0). Koefisien kurs yang relevan untuk depresiasi -0,7180, interval nominal 95% [-2,2001; 0,7641], probabilitas nominal 0,337. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -3,81, kuartal keempat -6,72, kuartal ke-24 -6,84 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,1,0,0). Koefisien kurs yang relevan untuk depresiasi -1,2455, interval nominal 95% [-3,3623; 0,8712], probabilitas nominal 0,244. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -6,80, kuartal keempat -11,70, kuartal ke-24 -11,87 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,2,3). Koefisien kurs yang relevan untuk depresiasi -2,1067, interval nominal 95% [-3,8029; -0,4106], probabilitas nominal 0,016. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; RESET. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -12,07, kuartal keempat -21,60, kuartal ke-24 -20,08 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,2,0,3). Koefisien kurs yang relevan untuk depresiasi -0,1602, interval nominal 95% [-2,5423; 2,2218], probabilitas nominal 0,894. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,47, kuartal keempat -4,29, kuartal ke-24 -1,53 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,2,0,3). Koefisien kurs yang relevan untuk depresiasi -2,3469, interval nominal 95% [-4,3317; -0,3622], probabilitas nominal 0,021. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; RESET; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -14,38, kuartal keempat -17,38, kuartal ke-24 -22,03 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,2,0,0,2). Koefisien kurs yang relevan untuk depresiasi -3,0484, interval nominal 95% [-4,9110; -1,1857], probabilitas nominal 0,002. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -19,42, kuartal keempat -21,73, kuartal ke-24 -28,96 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,0,2). Koefisien kurs yang relevan untuk depresiasi -1,1707, interval nominal 95% [-2,8379; 0,4964], probabilitas nominal 0,166. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; heteroskedasticity; RESET; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -6,39, kuartal keempat -6,60, kuartal ke-24 -11,13 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,0,0,2). Koefisien kurs yang relevan untuk depresiasi -1,4769, interval nominal 95% [-3,5471; 0,5932], probabilitas nominal 0,159. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; heteroskedasticity; RESET; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -8,13, kuartal keempat -8,07, kuartal ke-24 -14,05 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: results_primary_models.csv; HS6_Classification.csv. Interval nominal 95% setelah seleksi AIC.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 146. Atlas B | Kelompok barang: Korea Selatan

Atlas B | Kelompok barang: Korea Selatan

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,4488, interval nominal 95% [-0,0370; 2,9345], probabilitas nominal 0,056. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,52, kuartal keempat 6,93, kuartal ke-24 13,07 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,6014, interval nominal 95% [-1,0973; 4,3000], probabilitas nominal 0,241. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,98, kuartal keempat 7,80, kuartal ke-24 14,51 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,1). Koefisien kurs yang relevan untuk depresiasi 1,4164, interval nominal 95% [-2,0646; 4,8974], probabilitas nominal 0,420. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET; non-normal residuals. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -38,15, kuartal keempat 9,47, kuartal ke-24 13,53 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,2,2). Koefisien kurs yang relevan untuk depresiasi 7,1469, interval nominal 95% [0,8363; 13,4574], probabilitas nominal 0,027. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -37,48, kuartal keempat 16,40, kuartal ke-24 67,96 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,4,4,0). Koefisien kurs yang relevan untuk depresiasi -0,3704, interval nominal 95% [-4,4709; 3,7301], probabilitas nominal 0,857. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -0,72, kuartal keempat -1,63, kuartal ke-24 -3,29 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,0,4,1,2). Koefisien kurs yang relevan untuk depresiasi 4,6622, interval nominal 95% [-0,7859; 10,1103], probabilitas nominal 0,092. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; CUSUMSQ instability. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 3,48, kuartal keempat 21,25, kuartal ke-24 44,32 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,4,0). Koefisien kurs yang relevan untuk depresiasi 7,9411, interval nominal 95% [-2,0668; 17,9490], probabilitas nominal 0,118. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; heteroskedasticity; RESET. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 11,22, kuartal keempat 28,46, kuartal ke-24 66,27 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,4,0,0). Koefisien kurs yang relevan untuk depresiasi 0,8749, interval nominal 95% [-24,3807; 26,1305], probabilitas nominal 0,945. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; heteroskedasticity; RESET. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 1,04, kuartal keempat 2,66, kuartal ke-24 6,81 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,4,4,0). Koefisien kurs yang relevan untuk depresiasi -0,7122, interval nominal 95% [-5,6366; 4,2123], probabilitas nominal 0,773. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -1,38, kuartal keempat -3,24, kuartal ke-24 -6,39 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,0,4,1,2). Koefisien kurs yang relevan untuk depresiasi 5,8149, interval nominal 95% [-1,3264; 12,9563], probabilitas nominal 0,109. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 7,34, kuartal keempat 25,92, kuartal ke-24 55,22 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,4,4,0). Koefisien kurs yang relevan untuk depresiasi 0,8867, interval nominal 95% [-3,0210; 4,7943], probabilitas nominal 0,652. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 0,94, kuartal keempat 2,59, kuartal ke-24 6,83 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,4,4,1,0). Koefisien kurs yang relevan untuk depresiasi 10,9500, interval nominal 95% [-2,2478; 24,1478], probabilitas nominal 0,102. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 12,52, kuartal keempat 33,16, kuartal ke-24 85,57 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,4,1,0). Koefisien kurs yang relevan untuk depresiasi 1,7473, interval nominal 95% [-0,0378; 3,5323], probabilitas nominal 0,055. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,78, kuartal keempat 9,39, kuartal ke-24 16,27 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,4,0,2,3). Koefisien kurs yang relevan untuk depresiasi 4,7173, interval nominal 95% [1,9522; 7,4825], probabilitas nominal 0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -13,99, kuartal keempat 19,80, kuartal ke-24 44,61 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: results_primary_models.csv; HS6_Classification.csv. Interval nominal 95% setelah seleksi AIC.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 147. Atlas B | Kelompok barang: Malaysia

Atlas B | Kelompok barang: Malaysia

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,3,1,0). Koefisien kurs yang relevan untuk depresiasi 0,3380, interval nominal 95% [-2,3500; 3,0261], probabilitas nominal 0,803. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 1,12, kuartal keempat 2,84, kuartal ke-24 3,22 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,3,1,0,0). Koefisien kurs yang relevan untuk depresiasi 3,4645, interval nominal 95% [-1,6552; 8,5842], probabilitas nominal 0,181. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 12,23, kuartal keempat 29,75, kuartal ke-24 33,02 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,1,0). Koefisien kurs yang relevan untuk depresiasi 0,1775, interval nominal 95% [-0,9338; 1,2889], probabilitas nominal 0,751. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 1,65, kuartal keempat 1,69, kuartal ke-24 1,69 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,3,2,0,0). Koefisien kurs yang relevan untuk depresiasi 0,7838, interval nominal 95% [-1,3612; 2,9288], probabilitas nominal 0,468. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 7,76, kuartal keempat 7,47, kuartal ke-24 7,47 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,0). Koefisien kurs yang relevan untuk depresiasi -1,2903, interval nominal 95% [-2,7766; 0,1959], probabilitas nominal 0,088. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -7,41, kuartal keempat -13,18, kuartal ke-24 -12,30 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,4444, interval nominal 95% [-1,0804; 3,9693], probabilitas nominal 0,258. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 9,72, kuartal keempat 14,94, kuartal ke-24 13,77 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,0,4,1). Koefisien kurs yang relevan untuk depresiasi -0,7463, interval nominal 95% [-4,5321; 3,0395], probabilitas nominal 0,695. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; RESET; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -19,88, kuartal keempat -7,84, kuartal ke-24 -7,15 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,0,2,4,0). Koefisien kurs yang relevan untuk depresiasi 4,4909, interval nominal 95% [-0,3493; 9,3311], probabilitas nominal 0,068. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 18,00, kuartal keempat 33,31, kuartal ke-24 42,76 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi -1,3762, interval nominal 95% [-3,0997; 0,3473], probabilitas nominal 0,116. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -7,68, kuartal keempat -12,96, kuartal ke-24 -13,12 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,1172, interval nominal 95% [-2,0436; 4,2780], probabilitas nominal 0,483. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 6,54, kuartal keempat 10,56, kuartal ke-24 10,65 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,2,3). Koefisien kurs yang relevan untuk depresiasi -0,6453, interval nominal 95% [-2,1932; 0,9025], probabilitas nominal 0,408. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 13,38, kuartal keempat 2,75, kuartal ke-24 -6,15 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,2,4,1). Koefisien kurs yang relevan untuk depresiasi 1,1759, interval nominal 95% [-1,1127; 3,4644], probabilitas nominal 0,309. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 21,76, kuartal keempat 12,18, kuartal ke-24 11,21 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,1,0). Koefisien kurs yang relevan untuk depresiasi 0,2854, interval nominal 95% [-2,6225; 3,1933], probabilitas nominal 0,845. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUMSQ instability; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 0,37, kuartal keempat 0,97, kuartal ke-24 2,34 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,1,0,0). Koefisien kurs yang relevan untuk depresiasi 1,9391, interval nominal 95% [-2,6844; 6,5626], probabilitas nominal 0,406. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUMSQ instability; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,07, kuartal keempat 7,78, kuartal ke-24 16,84 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: results_primary_models.csv; HS6_Classification.csv. Interval nominal 95% setelah seleksi AIC.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 148. Atlas B | Kelompok barang: Singapura

Atlas B | Kelompok barang: Singapura

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,4). Koefisien kurs yang relevan untuk depresiasi 5,9816, interval nominal 95% [0,7131; 11,2502], probabilitas nominal 0,027. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 4,92, kuartal keempat 14,81, kuartal ke-24 52,35 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,0,0,1,3). Koefisien kurs yang relevan untuk depresiasi 4,9405, interval nominal 95% [-0,8349; 10,7160], probabilitas nominal 0,092. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 25,80, kuartal keempat 25,02, kuartal ke-24 46,60 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,4692, interval nominal 95% [-2,6496; 1,7112], probabilitas nominal 0,669. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -2,84, kuartal keempat -4,44, kuartal ke-24 -4,47 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,1,0,2,0). Koefisien kurs yang relevan untuk depresiasi -1,3034, interval nominal 95% [-4,8827; 2,2758], probabilitas nominal 0,470. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -8,03, kuartal keempat -12,35, kuartal ke-24 -12,42 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,0,0). Koefisien kurs yang relevan untuk depresiasi -1,1917, interval nominal 95% [-2,2306; -0,1528], probabilitas nominal 0,025. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -8,69, kuartal keempat -11,35, kuartal ke-24 -11,36 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,1,2,4,0). Koefisien kurs yang relevan untuk depresiasi -0,7007, interval nominal 95% [-2,6860; 1,2847], probabilitas nominal 0,483. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; RESET. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,61, kuartal keempat -6,66, kuartal ke-24 -6,68 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,0,0,0). Koefisien kurs yang relevan untuk depresiasi 2,6163, interval nominal 95% [-2,6493; 7,8819], probabilitas nominal 0,325. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; RESET; CUSUMSQ instability; ARCH4; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 8,57, kuartal keempat 19,51, kuartal ke-24 24,92 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,1,0,4,0). Koefisien kurs yang relevan untuk depresiasi -0,1019, interval nominal 95% [-10,9807; 10,7770], probabilitas nominal 0,985. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; RESET; CUSUMSQ instability; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -0,28, kuartal keempat -0,71, kuartal ke-24 -0,97 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,0,0). Koefisien kurs yang relevan untuk depresiasi -1,3833, interval nominal 95% [-2,5018; -0,2647], probabilitas nominal 0,016. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -10,55, kuartal keempat -13,18, kuartal ke-24 -13,18 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,1,2,4,0). Koefisien kurs yang relevan untuk depresiasi -0,7085, interval nominal 95% [-2,8168; 1,3997], probabilitas nominal 0,504. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,90, kuartal keempat -6,74, kuartal ke-24 -6,75 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,0,0). Koefisien kurs yang relevan untuk depresiasi 0,4235, interval nominal 95% [-1,1965; 2,0436], probabilitas nominal 0,604. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 1,47, kuartal keempat 3,62, kuartal ke-24 4,04 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,1,0,0). Koefisien kurs yang relevan untuk depresiasi -2,0320, interval nominal 95% [-3,7613; -0,3027], probabilitas nominal 0,022. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -10,86, kuartal keempat -19,05, kuartal ke-24 -19,37 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 0,0075, interval nominal 95% [-2,0801; 2,0951], probabilitas nominal 0,994. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; heteroskedasticity; CUSUMSQ instability; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 0,03, kuartal keempat 0,06, kuartal ke-24 0,07 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi -1,5439, interval nominal 95% [-4,5399; 1,4521], probabilitas nominal 0,308. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; heteroskedasticity; CUSUMSQ instability; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -6,36, kuartal keempat -13,85, kuartal ke-24 -14,71 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: results_primary_models.csv; HS6_Classification.csv. Interval nominal 95% setelah seleksi AIC.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 149. Atlas B | Kelompok barang: Thailand

Atlas B | Kelompok barang: Thailand

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,2,0,2). Koefisien kurs yang relevan untuk depresiasi 1,9059, interval nominal 95% [-1,1431; 4,9549], probabilitas nominal 0,216. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 21,17, kuartal keempat 20,01, kuartal ke-24 18,17 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,0,0,0,2). Koefisien kurs yang relevan untuk depresiasi 3,8478, interval nominal 95% [-1,4844; 9,1800], probabilitas nominal 0,155. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 49,03, kuartal keempat 43,03, kuartal ke-24 36,67 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,0,3). Koefisien kurs yang relevan untuk depresiasi -1,0271, interval nominal 95% [-3,6264; 1,5723], probabilitas nominal 0,433. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -41,77, kuartal keempat -11,89, kuartal ke-24 -9,79 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,0,0,3). Koefisien kurs yang relevan untuk depresiasi 2,5931, interval nominal 95% [-2,9641; 8,1503], probabilitas nominal 0,355. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; RESET; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -43,21, kuartal keempat 21,38, kuartal ke-24 24,71 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,0,1,0). Koefisien kurs yang relevan untuk depresiasi 1,0469, interval nominal 95% [-0,3425; 2,4364], probabilitas nominal 0,137. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 8,69, kuartal keempat 9,71, kuartal ke-24 9,98 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,1,0,0,2). Koefisien kurs yang relevan untuk depresiasi 3,4540, interval nominal 95% [0,4602; 6,4479], probabilitas nominal 0,024. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 35,25, kuartal keempat 37,52, kuartal ke-24 32,92 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 2,5435, interval nominal 95% [0,4987; 4,5883], probabilitas nominal 0,015. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 12,48, kuartal keempat 23,59, kuartal ke-24 24,24 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,0,0,0,1). Koefisien kurs yang relevan untuk depresiasi 0,3537, interval nominal 95% [-5,0349; 5,7422], probabilitas nominal 0,896. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 28,25, kuartal keempat 6,52, kuartal ke-24 3,37 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,0,1,0). Koefisien kurs yang relevan untuk depresiasi -0,5923, interval nominal 95% [-1,6557; 0,4710], probabilitas nominal 0,270. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -5,44, kuartal keempat -5,57, kuartal ke-24 -5,65 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,1,0,1). Koefisien kurs yang relevan untuk depresiasi 0,7551, interval nominal 95% [-2,0566; 3,5668], probabilitas nominal 0,594. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -16,11, kuartal keempat 2,99, kuartal ke-24 7,20 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,3,3,0). Koefisien kurs yang relevan untuk depresiasi 1,0630, interval nominal 95% [0,1019; 2,0241], probabilitas nominal 0,031. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 5,59, kuartal keempat 9,95, kuartal ke-24 10,13 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,4,4,0,4). Koefisien kurs yang relevan untuk depresiasi -1,5678, interval nominal 95% [-3,5806; 0,4449], probabilitas nominal 0,124. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -6,96, kuartal keempat -7,01, kuartal ke-24 -14,94 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,1,1,3). Koefisien kurs yang relevan untuk depresiasi 1,0008, interval nominal 95% [-0,6058; 2,6073], probabilitas nominal 0,218. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; non-normal residuals. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -0,31, kuartal keempat 6,19, kuartal ke-24 9,54 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,3,1,1,3). Koefisien kurs yang relevan untuk depresiasi 0,5635, interval nominal 95% [-3,1996; 4,3266], probabilitas nominal 0,766. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 7,55, kuartal keempat 4,75, kuartal ke-24 5,37 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: results_primary_models.csv; HS6_Classification.csv. Interval nominal 95% setelah seleksi AIC.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 150. Atlas B | Kelompok barang: Amerika Serikat

Atlas B | Kelompok barang: Amerika Serikat

ARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,8364, interval nominal 95% [-1,5190; -0,1538], probabilitas nominal 0,017. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -7,07, kuartal keempat -7,97, kuartal ke-24 -7,97 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (1,0,0,1,1). Koefisien kurs yang relevan untuk depresiasi 0,6216, interval nominal 95% [-0,5130; 1,7562], probabilitas nominal 0,278. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -10,97, kuartal keempat 5,92, kuartal ke-24 5,92 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (2,0,0,3). Koefisien kurs yang relevan untuk depresiasi 1,1657, interval nominal 95% [-7,1420; 9,4733], probabilitas nominal 0,780. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 35,46, kuartal keempat 29,96, kuartal ke-24 11,83 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (2,0,0,1,3). Koefisien kurs yang relevan untuk depresiasi 4,5302, interval nominal 95% [-6,9697; 16,0301], probabilitas nominal 0,434. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 8,12, kuartal keempat 40,28, kuartal ke-24 43,05 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (4,0,2,3). Koefisien kurs yang relevan untuk depresiasi -0,0878, interval nominal 95% [-1,6676; 1,4919], probabilitas nominal 0,912. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,20, kuartal keempat -4,33, kuartal ke-24 -0,87 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (4,1,2,2,3). Koefisien kurs yang relevan untuk depresiasi 3,5917, interval nominal 95% [1,6312; 5,5521], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -2,80, kuartal keempat 25,47, kuartal ke-24 34,21 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (4,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,3352, interval nominal 95% [-4,7642; 4,0938], probabilitas nominal 0,880. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -0,69, kuartal keempat -1,35, kuartal ke-24 -2,87 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (2,1,0,2,3). Koefisien kurs yang relevan untuk depresiasi 5,8605, interval nominal 95% [3,2348; 8,4862], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -4,37, kuartal keempat 48,42, kuartal ke-24 55,86 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (4,0,1,0). Koefisien kurs yang relevan untuk depresiasi 5,8692, interval nominal 95% [-3,4611; 15,1996], probabilitas nominal 0,214. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 14,03, kuartal keempat 27,71, kuartal ke-24 52,84 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (4,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 13,5273, interval nominal 95% [-15,4049; 42,4595], probabilitas nominal 0,354. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 22,14, kuartal keempat 46,12, kuartal ke-24 109,03 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (1,0,1,0). Koefisien kurs yang relevan untuk depresiasi -0,3133, interval nominal 95% [-1,2718; 0,6452], probabilitas nominal 0,517. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; RESET; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -1,58, kuartal keempat -2,92, kuartal ke-24 -2,99 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (1,0,2,2,3). Koefisien kurs yang relevan untuk depresiasi 2,9242, interval nominal 95% [1,2686; 4,5798], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; RESET. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -4,77, kuartal keempat 25,37, kuartal ke-24 27,87 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (2,2,2,0). Koefisien kurs yang relevan untuk depresiasi 1,5174, interval nominal 95% [-0,7999; 3,8347], probabilitas nominal 0,196. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 4,51, kuartal keempat 10,74, kuartal ke-24 14,44 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (2,2,3,0,2). Koefisien kurs yang relevan untuk depresiasi 2,1894, interval nominal 95% [-0,7507; 5,1295], probabilitas nominal 0,142. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 10,36, kuartal keempat 13,96, kuartal ke-24 20,86 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: results_primary_models.csv; HS6_Classification.csv. Interval nominal 95% setelah seleksi AIC.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 151. Atlas B | Kelompok barang: Vietnam

Atlas B | Kelompok barang: Vietnam

ARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (2,0,0,0). Koefisien kurs yang relevan untuk depresiasi 5,9112, interval nominal 95% [1,5175; 10,3050], probabilitas nominal 0,009. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 27,04, kuartal keempat 56,99, kuartal ke-24 56,34 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (2,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 7,2605, interval nominal 95% [0,8901; 13,6309], probabilitas nominal 0,026. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 34,46, kuartal keempat 70,31, kuartal ke-24 69,20 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (2,0,0,1). Koefisien kurs yang relevan untuk depresiasi 2,7728, interval nominal 95% [-1,0085; 6,5542], probabilitas nominal 0,148. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -19,53, kuartal keempat 18,70, kuartal ke-24 26,42 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (1,0,0,0,1). Koefisien kurs yang relevan untuk depresiasi -0,9612, interval nominal 95% [-4,8246; 2,9023], probabilitas nominal 0,621. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -77,56, kuartal keempat -11,07, kuartal ke-24 -9,16 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 2,1228, interval nominal 95% [-1,5442; 5,7899], probabilitas nominal 0,252. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 10,94, kuartal keempat 19,82, kuartal ke-24 20,23 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 2,2873, interval nominal 95% [-3,4483; 8,0230], probabilitas nominal 0,429. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 11,83, kuartal keempat 21,36, kuartal ke-24 21,80 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 3,9945, interval nominal 95% [1,1858; 6,8032], probabilitas nominal 0,006. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; ARCH4. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 21,71, kuartal keempat 37,51, kuartal ke-24 38,07 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 4,6844, interval nominal 95% [0,4447; 8,9241], probabilitas nominal 0,031. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; ARCH4. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 25,87, kuartal keempat 44,06, kuartal ke-24 44,65 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi -3,9664, interval nominal 95% [-7,2593; -0,6735], probabilitas nominal 0,019. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; heteroskedasticity; CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -33,85, kuartal keempat -37,80, kuartal ke-24 -37,80 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi -4,2059, interval nominal 95% [-9,2909; 0,8790], probabilitas nominal 0,103. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; heteroskedasticity; CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -35,88, kuartal keempat -40,09, kuartal ke-24 -40,09 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (4,0,1,0). Koefisien kurs yang relevan untuk depresiasi -1,2816, interval nominal 95% [-3,0727; 0,5096], probabilitas nominal 0,158. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; heteroskedasticity; RESET; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -5,49, kuartal keempat -9,27, kuartal ke-24 -12,20 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (4,0,1,0,0). Koefisien kurs yang relevan untuk depresiasi -2,0689, interval nominal 95% [-5,1617; 1,0240], probabilitas nominal 0,186. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; heteroskedasticity; RESET; CUSUMSQ instability; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -8,53, kuartal keempat -14,56, kuartal ke-24 -19,69 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (4,0,0,0). Koefisien kurs yang relevan untuk depresiasi 2,7854, interval nominal 95% [-2,5336; 8,1044], probabilitas nominal 0,300. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 4,82, kuartal keempat 10,93, kuartal ke-24 23,93 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (4,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,0254, interval nominal 95% [-4,4483; 4,3976], probabilitas nominal 0,991. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -0,06, kuartal keempat -0,13, kuartal ke-24 -0,23 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: results_primary_models.csv; HS6_Classification.csv. Interval nominal 95% setelah seleksi AIC.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 152. Atlas respons sensitivitas

Atlas respons sensitivitas

Seluruh 340 estimasi pembanding dipertahankan: cap dua, BCOM, window dunia 2006+, WPI India, serta kurs GEM alternatif. Maksimum dua seri per halaman menjaga agar kurva dan interval tetap terbaca.

SUMBER DAN REPRODUKSI
Sumber: keluaran estimasi Stata HS-6; seluruh spesifikasi tetap ditampilkan.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 153. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,3,2,0). Koefisien kurs yang relevan untuk depresiasi -1,8031, interval nominal 95% [-4,2949; 0,6888], probabilitas nominal 0,153. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -6,27, kuartal keempat -15,40, kuartal ke-24 -17,18 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,4,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi -3,6388, interval nominal 95% [-5,3695; -1,9081], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -26,26, kuartal keempat -34,65, kuartal ke-24 -34,68 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 3,9716, interval nominal 95% [-3,0922; 11,0354], probabilitas nominal 0,266. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; heteroskedasticity; CUSUMSQ instability; ARCH4; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 21,79, kuartal keempat 37,33, kuartal ke-24 37,85 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 6,7883, interval nominal 95% [-1,1917; 14,7683], probabilitas nominal 0,094. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; heteroskedasticity; RESET; CUSUMSQ instability; ARCH4; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 38,39, kuartal keempat 63,98, kuartal ke-24 64,70 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 154. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,4,2,2). Koefisien kurs yang relevan untuk depresiasi -0,3735, interval nominal 95% [-2,1632; 1,4161], probabilitas nominal 0,678. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -2,53, kuartal keempat -3,45, kuartal ke-24 -3,56 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,4,0,2,1,2). Koefisien kurs yang relevan untuk depresiasi -0,9138, interval nominal 95% [-2,7115; 0,8839], probabilitas nominal 0,313. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: RESET. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -33,60, kuartal keempat -8,75, kuartal ke-24 -8,71 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,0,0,1). Koefisien kurs yang relevan untuk depresiasi 1,2442, interval nominal 95% [-0,6279; 3,1164], probabilitas nominal 0,189. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 10,55, kuartal keempat 11,86, kuartal ke-24 11,86 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,1,1,0,1). Koefisien kurs yang relevan untuk depresiasi 1,1407, interval nominal 95% [-1,0045; 3,2859], probabilitas nominal 0,292. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 10,03, kuartal keempat 10,87, kuartal ke-24 10,87 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 155. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,3,4,0,2). Koefisien kurs yang relevan untuk depresiasi 2,0800, interval nominal 95% [-1,0944; 5,2545], probabilitas nominal 0,195. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 14,90, kuartal keempat 19,81, kuartal ke-24 19,82 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,1,4,2,1,2). Koefisien kurs yang relevan untuk depresiasi 4,1372, interval nominal 95% [0,6185; 7,6560], probabilitas nominal 0,022. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -37,19, kuartal keempat 39,08, kuartal ke-24 39,43 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 0,9962, interval nominal 95% [-0,7783; 2,7707], probabilitas nominal 0,267. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 6,34, kuartal keempat 9,46, kuartal ke-24 9,50 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,0,2,1,2). Koefisien kurs yang relevan untuk depresiasi 1,6181, interval nominal 95% [-0,4460; 3,6821], probabilitas nominal 0,122. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -13,50, kuartal keempat 15,19, kuartal ke-24 15,42 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 156. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 0,9192, interval nominal 95% [-2,5884; 4,4269], probabilitas nominal 0,603. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: ARCH4. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,20, kuartal keempat 7,86, kuartal ke-24 8,76 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,0,0,4,4,1). Koefisien kurs yang relevan untuk depresiasi 4,6097, interval nominal 95% [0,4916; 8,7278], probabilitas nominal 0,029. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -7,12, kuartal keempat 24,12, kuartal ke-24 43,93 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,1,1,1,0). Koefisien kurs yang relevan untuk depresiasi -0,1709, interval nominal 95% [-0,8987; 0,5568], probabilitas nominal 0,641. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 10,21, kuartal keempat 1,54, kuartal ke-24 -1,61 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,1,1,1,0). Koefisien kurs yang relevan untuk depresiasi -1,3356, interval nominal 95% [-2,4574; -0,2139], probabilitas nominal 0,020. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 16,20, kuartal keempat -5,49, kuartal ke-24 -12,69 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 157. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,1,0,4). Koefisien kurs yang relevan untuk depresiasi 0,9699, interval nominal 95% [-1,6181; 3,5578], probabilitas nominal 0,457. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability; ARCH4; non-normal residuals. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 5,59, kuartal keempat 8,08, kuartal ke-24 9,24 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,1,1,0,4). Koefisien kurs yang relevan untuk depresiasi -1,6671, interval nominal 95% [-5,7500; 2,4157], probabilitas nominal 0,418. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; ARCH4; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -11,93, kuartal keempat -15,87, kuartal ke-24 -15,89 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,1,3,0). Koefisien kurs yang relevan untuk depresiasi -1,4365, interval nominal 95% [-2,8638; -0,0093], probabilitas nominal 0,049. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; CUSUMSQ instability; ARCH4. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 2,59, kuartal keempat -9,69, kuartal ke-24 -13,64 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,1,0,3,0). Koefisien kurs yang relevan untuk depresiasi -2,8405, interval nominal 95% [-5,4257; -0,2552], probabilitas nominal 0,032. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 11,05, kuartal keempat -20,43, kuartal ke-24 -27,05 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 158. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,2,3,0). Koefisien kurs yang relevan untuk depresiasi 0,2111, interval nominal 95% [-1,9238; 2,3460], probabilitas nominal 0,844. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: ARCH4. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 18,11, kuartal keempat 7,38, kuartal ke-24 2,01 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,2,3,1,0). Koefisien kurs yang relevan untuk depresiasi -2,3427, interval nominal 95% [-5,4207; 0,7352], probabilitas nominal 0,133. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 7,40, kuartal keempat -21,57, kuartal ke-24 -22,33 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,2,0). Koefisien kurs yang relevan untuk depresiasi -1,6919, interval nominal 95% [-4,3234; 0,9396], probabilitas nominal 0,204. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -3,74, kuartal keempat -12,28, kuartal ke-24 -16,08 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,1,0,3,0). Koefisien kurs yang relevan untuk depresiasi -3,9213, interval nominal 95% [-9,0018; 1,1592], probabilitas nominal 0,128. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 8,17, kuartal keempat -28,49, kuartal ke-24 -37,33 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 159. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,0,4,0,2). Koefisien kurs yang relevan untuk depresiasi -10,8785, interval nominal 95% [-61,8657; 40,1086], probabilitas nominal 0,671. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,45, kuartal keempat -14,33, kuartal ke-24 -50,10 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,3,0,4,4,2). Koefisien kurs yang relevan untuk depresiasi -5,2764, interval nominal 95% [-10,9742; 0,4213], probabilitas nominal 0,069. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 7,33, kuartal keempat -31,87, kuartal ke-24 -48,81 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,1,1,0,4). Koefisien kurs yang relevan untuk depresiasi -0,6195, interval nominal 95% [-4,4939; 3,2550], probabilitas nominal 0,751. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -0,66, kuartal keempat -2,23, kuartal ke-24 -5,31 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,1,1,0,1,4). Koefisien kurs yang relevan untuk depresiasi 3,3919, interval nominal 95% [-10,7832; 17,5670], probabilitas nominal 0,634. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 13,70, kuartal keempat 15,73, kuartal ke-24 27,82 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 160. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (4,1,0,4,2). Koefisien kurs yang relevan untuk depresiasi 5,9887, interval nominal 95% [-6,4800; 18,4574], probabilitas nominal 0,336. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 66,01, kuartal keempat 41,17, kuartal ke-24 56,26 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (4,1,0,3,0,2). Koefisien kurs yang relevan untuk depresiasi 2,3670, interval nominal 95% [-10,3681; 15,1021], probabilitas nominal 0,708. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 10,82, kuartal keempat 16,47, kuartal ke-24 22,43 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (2,0,2,0,2). Koefisien kurs yang relevan untuk depresiasi 4,0312, interval nominal 95% [-11,4809; 19,5434], probabilitas nominal 0,602. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 19,19, kuartal keempat 39,49, kuartal ke-24 38,42 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (2,0,2,0,0,2). Koefisien kurs yang relevan untuk depresiasi 4,2535, interval nominal 95% [-15,2242; 23,7312], probabilitas nominal 0,661. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 20,30, kuartal keempat 41,68, kuartal ke-24 40,54 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 161. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,0,3,0,4). Koefisien kurs yang relevan untuk depresiasi 4,3717, interval nominal 95% [-0,6547; 9,3980], probabilitas nominal 0,086. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 32,09, kuartal keempat 41,64, kuartal ke-24 41,67 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (4,1,4,2,4,4). Koefisien kurs yang relevan untuk depresiasi -2,0729, interval nominal 95% [-8,4128; 4,2670], probabilitas nominal 0,506. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -0,25, kuartal keempat 14,43, kuartal ke-24 -21,44 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,0,0,0,3). Koefisien kurs yang relevan untuk depresiasi 3,6039, interval nominal 95% [-3,8419; 11,0497], probabilitas nominal 0,334. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 22,92, kuartal keempat 34,21, kuartal ke-24 34,35 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (2,2,4,0,0,3). Koefisien kurs yang relevan untuk depresiasi -4,5085, interval nominal 95% [-11,4033; 2,3862], probabilitas nominal 0,192. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -39,75, kuartal keempat -41,69, kuartal ke-24 -42,97 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 162. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,4,0,0,3). Koefisien kurs yang relevan untuk depresiasi 5,9949, interval nominal 95% [-5,6363; 17,6261], probabilitas nominal 0,303. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 30,57, kuartal keempat 55,90, kuartal ke-24 57,14 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (3,3,4,4,4,3). Koefisien kurs yang relevan untuk depresiasi -7,1809, interval nominal 95% [-13,2714; -1,0904], probabilitas nominal 0,023. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -39,01, kuartal keempat -48,41, kuartal ke-24 -68,33 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (4,4,1,3,4). Koefisien kurs yang relevan untuk depresiasi 15,0593, interval nominal 95% [-23,9189; 54,0375], probabilitas nominal 0,435. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; CUSUMSQ instability; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 39,29, kuartal keempat 18,65, kuartal ke-24 112,90 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (4,4,1,3,3,4). Koefisien kurs yang relevan untuk depresiasi 12,1492, interval nominal 95% [-36,9070; 61,2054], probabilitas nominal 0,614. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 1,79, kuartal keempat -21,15, kuartal ke-24 59,44 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 163. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,0,4,3,4). Koefisien kurs yang relevan untuk depresiasi 0,2718, interval nominal 95% [-3,8861; 4,4297], probabilitas nominal 0,895. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; RESET. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 11,06, kuartal keempat -0,49, kuartal ke-24 2,59 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2014Q1 sampai 2026Q1, 49 kuartal. Lag level (1,3,3,2,4,4). Koefisien kurs yang relevan untuk depresiasi 0,2145, interval nominal 95% [-4,6804; 5,1095], probabilitas nominal 0,929. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; CUSUMSQ instability. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -6,67, kuartal keempat 0,89, kuartal ke-24 2,04 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,0,3). Koefisien kurs yang relevan untuk depresiasi -0,5361, interval nominal 95% [-2,6444; 1,5721], probabilitas nominal 0,613. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; RESET; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -1,16, kuartal keempat -2,31, kuartal ke-24 -4,71 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,0,0,3). Koefisien kurs yang relevan untuk depresiasi -1,9964, interval nominal 95% [-3,7507; -0,2421], probabilitas nominal 0,026. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; RESET; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -7,46, kuartal keempat -12,72, kuartal ke-24 -18,85 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 164. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,0,0,1,2). Koefisien kurs yang relevan untuk depresiasi -3,4681, interval nominal 95% [-8,6726; 1,7364], probabilitas nominal 0,188. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -14,37, kuartal keempat -18,14, kuartal ke-24 -31,31 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,0,0,1,0,2). Koefisien kurs yang relevan untuk depresiasi -6,5467, interval nominal 95% [-10,7709; -2,3225], probabilitas nominal 0,003. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -18,49, kuartal keempat -41,87, kuartal ke-24 -62,00 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,2,0,3). Koefisien kurs yang relevan untuk depresiasi -1,5343, interval nominal 95% [-2,8735; -0,1950], probabilitas nominal 0,025. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -7,99, kuartal keempat -14,34, kuartal ke-24 -14,62 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,3,2,0,0,3). Koefisien kurs yang relevan untuk depresiasi 0,2264, interval nominal 95% [-2,0933; 2,5462], probabilitas nominal 0,846. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 1,13, kuartal keempat 2,10, kuartal ke-24 2,16 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 165. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,4,4,0,4). Koefisien kurs yang relevan untuk depresiasi -0,6592, interval nominal 95% [-2,1473; 0,8288], probabilitas nominal 0,379. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,39, kuartal keempat -6,27, kuartal ke-24 -6,28 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,4,2,4,0,4). Koefisien kurs yang relevan untuk depresiasi -0,4516, interval nominal 95% [-2,8339; 1,9306], probabilitas nominal 0,706. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -2,85, kuartal keempat -4,29, kuartal ke-24 -4,30 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,2,0,3). Koefisien kurs yang relevan untuk depresiasi -2,0066, interval nominal 95% [-3,7176; -0,2955], probabilitas nominal 0,022. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -10,47, kuartal keempat -18,76, kuartal ke-24 -19,12 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,3,2,0,0,3). Koefisien kurs yang relevan untuk depresiasi 0,7714, interval nominal 95% [-2,0566; 3,5993], probabilitas nominal 0,588. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 4,01, kuartal keempat 7,21, kuartal ke-24 7,35 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 166. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,2,0,3,1). Koefisien kurs yang relevan untuk depresiasi -2,5216, interval nominal 95% [-4,8912; -0,1520], probabilitas nominal 0,037. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; RESET; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -13,01, kuartal keempat -18,33, kuartal ke-24 -23,78 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,1,2,0,3,1). Koefisien kurs yang relevan untuk depresiasi -2,9300, interval nominal 95% [-5,9468; 0,0868], probabilitas nominal 0,057. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; heteroskedasticity; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -15,67, kuartal keempat -22,16, kuartal ke-24 -27,68 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,0,2,2,0). Koefisien kurs yang relevan untuk depresiasi -2,2569, interval nominal 95% [-4,5654; 0,0517], probabilitas nominal 0,055. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -8,15, kuartal keempat -13,52, kuartal ke-24 -21,46 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,0,0,2,0). Koefisien kurs yang relevan untuk depresiasi -2,7447, interval nominal 95% [-5,2691; -0,2202], probabilitas nominal 0,034. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -10,19, kuartal keempat -17,49, kuartal ke-24 -26,14 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 167. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,2,2,4,0). Koefisien kurs yang relevan untuk depresiasi 1,3900, interval nominal 95% [0,8767; 1,9033], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -3,29, kuartal keempat 8,43, kuartal ke-24 13,25 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,2,2,4,0). Koefisien kurs yang relevan untuk depresiasi 2,3484, interval nominal 95% [1,5183; 3,1785], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -10,05, kuartal keempat 20,04, kuartal ke-24 22,38 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,1,0). Koefisien kurs yang relevan untuk depresiasi 1,3972, interval nominal 95% [-2,2234; 5,0178], probabilitas nominal 0,444. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET; non-normal residuals. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -38,24, kuartal keempat 9,23, kuartal ke-24 13,34 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,2,2,0). Koefisien kurs yang relevan untuk depresiasi 7,2494, interval nominal 95% [1,2561; 13,2426], probabilitas nominal 0,019. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -38,07, kuartal keempat 20,63, kuartal ke-24 68,93 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 168. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,4,0,0). Koefisien kurs yang relevan untuk depresiasi -0,7184, interval nominal 95% [-5,7165; 4,2797], probabilitas nominal 0,775. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -1,18, kuartal keempat -2,85, kuartal ke-24 -6,20 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,4,1,0,0). Koefisien kurs yang relevan untuk depresiasi 5,1966, interval nominal 95% [-4,3396; 14,7328], probabilitas nominal 0,280. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: non-normal residuals. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 11,15, kuartal keempat 24,92, kuartal ke-24 47,16 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,4,0,0). Koefisien kurs yang relevan untuk depresiasi 8,3284, interval nominal 95% [-0,9514; 17,6081], probabilitas nominal 0,078. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; heteroskedasticity; RESET. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 13,00, kuartal keempat 32,26, kuartal ke-24 71,44 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,4,0,0,0). Koefisien kurs yang relevan untuk depresiasi 2,8992, interval nominal 95% [-19,2567; 25,0550], probabilitas nominal 0,795. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; heteroskedasticity; RESET. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,90, kuartal keempat 9,81, kuartal ke-24 23,63 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 169. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,4,0,0). Koefisien kurs yang relevan untuk depresiasi -1,1686, interval nominal 95% [-7,8138; 5,4767], probabilitas nominal 0,727. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -1,79, kuartal keempat -4,45, kuartal ke-24 -9,95 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,4,1,0,0). Koefisien kurs yang relevan untuk depresiasi 6,7908, interval nominal 95% [-6,2390; 19,8207], probabilitas nominal 0,302. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 13,83, kuartal keempat 31,70, kuartal ke-24 61,29 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,4,4,0,2). Koefisien kurs yang relevan untuk depresiasi 0,8093, interval nominal 95% [-2,3220; 3,9405], probabilitas nominal 0,607. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 1,05, kuartal keempat 2,88, kuartal ke-24 6,78 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,4,4,4,0,3). Koefisien kurs yang relevan untuk depresiasi 14,4661, interval nominal 95% [-6,5747; 35,5068], probabilitas nominal 0,174. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 15,80, kuartal keempat 42,66, kuartal ke-24 111,58 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 170. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,4,1,0,0). Koefisien kurs yang relevan untuk depresiasi 1,7039, interval nominal 95% [-0,1674; 3,5752], probabilitas nominal 0,074. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,59, kuartal keempat 8,96, kuartal ke-24 15,82 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,4,0,2,3,0). Koefisien kurs yang relevan untuk depresiasi 4,7330, interval nominal 95% [1,8185; 7,6475], probabilitas nominal 0,002. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -13,91, kuartal keempat 19,80, kuartal ke-24 44,74 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,3,1,0,0). Koefisien kurs yang relevan untuk depresiasi -0,3895, interval nominal 95% [-2,7805; 2,0016], probabilitas nominal 0,746. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -1,51, kuartal keempat -3,44, kuartal ke-24 -3,71 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,3,0,2,0,0). Koefisien kurs yang relevan untuk depresiasi 2,6687, interval nominal 95% [-0,7131; 6,0505], probabilitas nominal 0,120. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 13,44, kuartal keempat 24,84, kuartal ke-24 25,44 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 171. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,3,0,1). Koefisien kurs yang relevan untuk depresiasi 0,1033, interval nominal 95% [-0,8762; 1,0827], probabilitas nominal 0,834. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 1,09, kuartal keempat 0,98, kuartal ke-24 0,98 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,3,0,0,1). Koefisien kurs yang relevan untuk depresiasi 0,3408, interval nominal 95% [-1,6715; 2,3532], probabilitas nominal 0,736. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,61, kuartal keempat 3,25, kuartal ke-24 3,25 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,7014, interval nominal 95% [-2,2773; 0,8744], probabilitas nominal 0,378. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,05, kuartal keempat -6,91, kuartal ke-24 -6,69 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,1522, interval nominal 95% [-1,3982; 3,7026], probabilitas nominal 0,371. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 7,47, kuartal keempat 11,62, kuartal ke-24 10,98 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 172. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,0,2,1,0). Koefisien kurs yang relevan untuk depresiasi 1,3829, interval nominal 95% [-4,5149; 7,2807], probabilitas nominal 0,641. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; ARCH4; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -13,42, kuartal keempat 2,79, kuartal ke-24 12,41 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,0,2,0,1,4). Koefisien kurs yang relevan untuk depresiasi 6,2566, interval nominal 95% [1,4556; 11,0577], probabilitas nominal 0,011. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUMSQ instability; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -1,46, kuartal keempat 46,60, kuartal ke-24 59,61 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,8106, interval nominal 95% [-2,4069; 0,7856], probabilitas nominal 0,315. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,92, kuartal keempat -7,68, kuartal ke-24 -7,73 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 0,4619, interval nominal 95% [-2,5390; 3,4627], probabilitas nominal 0,760. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 2,84, kuartal keempat 4,38, kuartal ke-24 4,40 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 173. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,2,3,0). Koefisien kurs yang relevan untuk depresiasi -0,5230, interval nominal 95% [-1,7847; 0,7386], probabilitas nominal 0,411. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: ARCH4; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 12,09, kuartal keempat 0,26, kuartal ke-24 -4,99 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,2,4,1,0). Koefisien kurs yang relevan untuk depresiasi 1,5456, interval nominal 95% [-0,1220; 3,2133], probabilitas nominal 0,069. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: ARCH4. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 21,96, kuartal keempat 14,90, kuartal ke-24 14,73 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,0,2). Koefisien kurs yang relevan untuk depresiasi 0,1493, interval nominal 95% [-2,4528; 2,7514], probabilitas nominal 0,909. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 0,23, kuartal keempat 0,57, kuartal ke-24 1,28 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,0,0,2). Koefisien kurs yang relevan untuk depresiasi 1,1285, interval nominal 95% [-3,4422; 5,6991], probabilitas nominal 0,624. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 2,06, kuartal keempat 4,99, kuartal ke-24 10,08 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 174. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,0,4,0). Koefisien kurs yang relevan untuk depresiasi 6,7415, interval nominal 95% [-0,8826; 14,3655], probabilitas nominal 0,082. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,87, kuartal keempat 12,54, kuartal ke-24 55,62 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,0,0,1,3,0). Koefisien kurs yang relevan untuk depresiasi 4,3840, interval nominal 95% [-1,4402; 10,2083], probabilitas nominal 0,138. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 25,85, kuartal keempat 23,95, kuartal ke-24 41,51 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,1,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,6627, interval nominal 95% [-2,9299; 1,6045], probabilitas nominal 0,562. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,09, kuartal keempat -6,28, kuartal ke-24 -6,32 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,0,0,4,0). Koefisien kurs yang relevan untuk depresiasi 0,3657, interval nominal 95% [-4,6260; 5,3574], probabilitas nominal 0,884. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUMSQ instability. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -20,26, kuartal keempat -20,22, kuartal ke-24 3,49 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 175. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,7660, interval nominal 95% [-1,6741; 0,1420], probabilitas nominal 0,097. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -6,39, kuartal keempat -7,30, kuartal ke-24 -7,30 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,1,2,4,0,3). Koefisien kurs yang relevan untuk depresiasi -0,2095, interval nominal 95% [-2,0079; 1,5888], probabilitas nominal 0,817. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -1,57, kuartal keempat -2,00, kuartal ke-24 -2,00 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 2,3328, interval nominal 95% [-3,2834; 7,9491], probabilitas nominal 0,410. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; RESET; CUSUMSQ instability; ARCH4; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 7,80, kuartal keempat 17,58, kuartal ke-24 22,22 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,1,0,4,0,0). Koefisien kurs yang relevan untuk depresiasi -0,2728, interval nominal 95% [-11,4488; 10,9033], probabilitas nominal 0,961. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; RESET; CUSUMSQ instability; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -0,74, kuartal keempat -1,88, kuartal ke-24 -2,59 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 176. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,1,0,3). Koefisien kurs yang relevan untuk depresiasi -0,2681, interval nominal 95% [-1,4869; 0,9507], probabilitas nominal 0,662. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -2,27, kuartal keempat -2,56, kuartal ke-24 -2,56 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,1,2,4,0,3). Koefisien kurs yang relevan untuk depresiasi -0,0334, interval nominal 95% [-1,7303; 1,6635], probabilitas nominal 0,969. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -0,29, kuartal keempat -0,32, kuartal ke-24 -0,32 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,0,0,0). Koefisien kurs yang relevan untuk depresiasi 0,2189, interval nominal 95% [-1,4467; 1,8844], probabilitas nominal 0,794. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 0,78, kuartal keempat 1,89, kuartal ke-24 2,09 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,2,1,0,0,0). Koefisien kurs yang relevan untuk depresiasi -2,0648, interval nominal 95% [-3,8194; -0,3103], probabilitas nominal 0,022. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -11,09, kuartal keempat -19,37, kuartal ke-24 -19,68 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 177. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,2935, interval nominal 95% [-2,3823; 1,7954], probabilitas nominal 0,780. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; heteroskedasticity; CUSUMSQ instability; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -1,12, kuartal keempat -2,58, kuartal ke-24 -2,80 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,1,0,4,0). Koefisien kurs yang relevan untuk depresiasi 0,5003, interval nominal 95% [-3,2681; 4,2687], probabilitas nominal 0,792. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -3,25, kuartal keempat -21,40, kuartal ke-24 4,77 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,1,0,2,0). Koefisien kurs yang relevan untuk depresiasi 1,8639, interval nominal 95% [-0,6221; 4,3500], probabilitas nominal 0,139. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 25,92, kuartal keempat 20,48, kuartal ke-24 17,77 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,1,0,4,3,0). Koefisien kurs yang relevan untuk depresiasi 5,2275, interval nominal 95% [0,3925; 10,0625], probabilitas nominal 0,035. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 66,77, kuartal keempat 58,88, kuartal ke-24 49,82 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 178. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,0,3,1). Koefisien kurs yang relevan untuk depresiasi -1,1810, interval nominal 95% [-3,4512; 1,0892], probabilitas nominal 0,303. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; RESET; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -31,53, kuartal keempat -12,00, kuartal ke-24 -11,26 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,0,0,3,1). Koefisien kurs yang relevan untuk depresiasi 1,9989, interval nominal 95% [-2,8442; 6,8420], probabilitas nominal 0,413. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; RESET; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -24,95, kuartal keempat 17,72, kuartal ke-24 19,05 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,0,1,2,1). Koefisien kurs yang relevan untuk depresiasi 1,2617, interval nominal 95% [-0,2511; 2,7745], probabilitas nominal 0,101. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 21,97, kuartal keempat 14,48, kuartal ke-24 12,03 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,1,0,0,2,1). Koefisien kurs yang relevan untuk depresiasi 3,0297, interval nominal 95% [-0,0040; 6,0634], probabilitas nominal 0,050. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 44,53, kuartal keempat 33,65, kuartal ke-24 28,88 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 179. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 2,4054, interval nominal 95% [0,5148; 4,2959], probabilitas nominal 0,013. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 12,73, kuartal keempat 22,53, kuartal ke-24 22,93 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,0,1,1,1). Koefisien kurs yang relevan untuk depresiasi 0,0871, interval nominal 95% [-3,8622; 4,0364], probabilitas nominal 0,965. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 51,93, kuartal keempat 2,29, kuartal ke-24 0,83 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,1,1,0,2). Koefisien kurs yang relevan untuk depresiasi -0,8107, interval nominal 95% [-1,9004; 0,2790], probabilitas nominal 0,142. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -7,16, kuartal keempat -7,55, kuartal ke-24 -7,73 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,1,1,0,0,2). Koefisien kurs yang relevan untuk depresiasi -0,3780, interval nominal 95% [-2,6322; 1,8761], probabilitas nominal 0,739. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -3,39, kuartal keempat -3,52, kuartal ke-24 -3,60 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 180. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,1,0,1). Koefisien kurs yang relevan untuk depresiasi 0,8595, interval nominal 95% [-0,1683; 1,8874], probabilitas nominal 0,100. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 4,02, kuartal keempat 7,91, kuartal ke-24 8,19 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,1,1,0,4). Koefisien kurs yang relevan untuk depresiasi -0,9613, interval nominal 95% [-3,1118; 1,1892], probabilitas nominal 0,375. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; heteroskedasticity. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,59, kuartal keempat -8,88, kuartal ke-24 -9,16 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,1,1,3,0). Koefisien kurs yang relevan untuk depresiasi 0,8833, interval nominal 95% [-0,7511; 2,5177], probabilitas nominal 0,284. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -0,02, kuartal keempat 5,90, kuartal ke-24 8,42 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (2,1,1,1,3,1). Koefisien kurs yang relevan untuk depresiasi 0,5555, interval nominal 95% [-2,6822; 3,7931], probabilitas nominal 0,733. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 11,16, kuartal keempat 4,36, kuartal ke-24 5,29 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 181. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,7839, interval nominal 95% [-1,5649; -0,0029], probabilitas nominal 0,049. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -6,67, kuartal keempat -7,47, kuartal ke-24 -7,47 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (1,0,0,1,1,0). Koefisien kurs yang relevan untuk depresiasi 0,5942, interval nominal 95% [-0,5616; 1,7500], probabilitas nominal 0,308. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -10,88, kuartal keempat 5,66, kuartal ke-24 5,66 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (2,0,0,3,1). Koefisien kurs yang relevan untuk depresiasi 0,3918, interval nominal 95% [-6,4943; 7,2779], probabilitas nominal 0,910. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 49,95, kuartal keempat 29,19, kuartal ke-24 3,96 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (2,0,0,1,4,0). Koefisien kurs yang relevan untuk depresiasi 0,2584, interval nominal 95% [-10,2345; 10,7514], probabilitas nominal 0,961. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 6,35, kuartal keempat 35,59, kuartal ke-24 2,68 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 182. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (4,2,2,3,0). Koefisien kurs yang relevan untuk depresiasi 1,2146, interval nominal 95% [-2,1405; 4,5697], probabilitas nominal 0,472. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -1,11, kuartal keempat 0,91, kuartal ke-24 11,13 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (4,2,0,2,3,0). Koefisien kurs yang relevan untuk depresiasi 3,3047, interval nominal 95% [1,5082; 5,1013], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -5,49, kuartal keempat 24,66, kuartal ke-24 31,49 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (4,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 0,5016, interval nominal 95% [-5,0460; 6,0493], probabilitas nominal 0,857. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 0,87, kuartal keempat 1,74, kuartal ke-24 4,04 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (2,1,0,2,3,4). Koefisien kurs yang relevan untuk depresiasi 5,1136, interval nominal 95% [2,7584; 7,4689], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -12,57, kuartal keempat 42,06, kuartal ke-24 48,74 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 183. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (4,0,1,0,0). Koefisien kurs yang relevan untuk depresiasi 10,0994, interval nominal 95% [-3,5951; 23,7939], probabilitas nominal 0,146. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 22,21, kuartal keempat 44,11, kuartal ke-24 88,98 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (4,0,4,0,1,1). Koefisien kurs yang relevan untuk depresiasi 11,9616, interval nominal 95% [1,3964; 22,5269], probabilitas nominal 0,027. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -32,25, kuartal keempat 65,87, kuartal ke-24 113,27 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (2,2,2,3,0). Koefisien kurs yang relevan untuk depresiasi 1,9180, interval nominal 95% [-0,8322; 4,6682], probabilitas nominal 0,168. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; heteroskedasticity; RESET. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 0,96, kuartal keempat 8,10, kuartal ke-24 18,26 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (1,0,2,2,3,0). Koefisien kurs yang relevan untuk depresiasi 3,0633, interval nominal 95% [1,3395; 4,7871], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; RESET. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -4,54, kuartal keempat 26,56, kuartal ke-24 29,20 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 184. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (2,0,0,3,1). Koefisien kurs yang relevan untuk depresiasi 0,3839, interval nominal 95% [-1,6353; 2,4032], probabilitas nominal 0,705. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 15,93, kuartal keempat 8,63, kuartal ke-24 3,66 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q3, 75 kuartal. Lag level (2,0,0,1,4,1). Koefisien kurs yang relevan untuk depresiasi 0,6427, interval nominal 95% [-2,6631; 3,9485], probabilitas nominal 0,699. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 5,18, kuartal keempat 15,47, kuartal ke-24 6,13 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (2,0,0,0,3). Koefisien kurs yang relevan untuk depresiasi 6,9343, interval nominal 95% [2,9069; 10,9618], probabilitas nominal 0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 41,33, kuartal keempat 66,83, kuartal ke-24 66,09 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (2,0,0,0,0,3). Koefisien kurs yang relevan untuk depresiasi 8,9518, interval nominal 95% [3,5093; 14,3942], probabilitas nominal 0,002. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 56,51, kuartal keempat 85,65, kuartal ke-24 85,32 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 185. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (2,0,0,1,0). Koefisien kurs yang relevan untuk depresiasi 3,6385, interval nominal 95% [-1,1213; 8,3984], probabilitas nominal 0,132. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -20,42, kuartal keempat 24,44, kuartal ke-24 34,67 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (1,0,0,0,1,0). Koefisien kurs yang relevan untuk depresiasi -1,0522, interval nominal 95% [-5,5198; 3,4155], probabilitas nominal 0,640. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -77,50, kuartal keempat -11,87, kuartal ke-24 -10,03 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (1,0,0,0,3). Koefisien kurs yang relevan untuk depresiasi 3,7069, interval nominal 95% [0,0301; 7,3838], probabilitas nominal 0,048. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 22,56, kuartal keempat 35,11, kuartal ke-24 35,33 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (1,0,0,0,0,3). Koefisien kurs yang relevan untuk depresiasi 4,3728, interval nominal 95% [-1,0230; 9,7686], probabilitas nominal 0,110. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 26,99, kuartal keempat 41,45, kuartal ke-24 41,68 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 186. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (2,0,0,0,3). Koefisien kurs yang relevan untuk depresiasi 4,4658, interval nominal 95% [1,8327; 7,0988], probabilitas nominal 0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; CUSUMSQ instability; ARCH4. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 32,10, kuartal keempat 42,44, kuartal ke-24 42,56 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (2,0,0,1,1,3). Koefisien kurs yang relevan untuk depresiasi 3,7710, interval nominal 95% [0,3427; 7,1994], probabilitas nominal 0,032. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; ARCH4. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 90,03, kuartal keempat 34,74, kuartal ke-24 35,94 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi -4,0436, interval nominal 95% [-7,7419; -0,3452], probabilitas nominal 0,033. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; heteroskedasticity; CUSUMSQ instability; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -34,48, kuartal keempat -38,54, kuartal ke-24 -38,54 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (1,0,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi -4,3650, interval nominal 95% [-10,1007; 1,3706], probabilitas nominal 0,133. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; heteroskedasticity; CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -37,19, kuartal keempat -41,60, kuartal ke-24 -41,60 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 187. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (4,0,1,0,1). Koefisien kurs yang relevan untuk depresiasi -0,1554, interval nominal 95% [-2,1867; 1,8759], probabilitas nominal 0,879. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; heteroskedasticity; RESET; CUSUMSQ instability; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -0,68, kuartal keempat -1,02, kuartal ke-24 -1,47 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (4,0,1,0,0,1). Koefisien kurs yang relevan untuk depresiasi -1,3938, interval nominal 95% [-5,0961; 2,3085], probabilitas nominal 0,455. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; heteroskedasticity; RESET; CUSUMSQ instability; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -5,44, kuartal keempat -8,55, kuartal ke-24 -13,16 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (4,4,1,0,2). Koefisien kurs yang relevan untuk depresiasi -0,0534, interval nominal 95% [-2,1878; 2,0811], probabilitas nominal 0,960. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -0,17, kuartal keempat -0,32, kuartal ke-24 -0,50 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2025Q2, 74 kuartal. Lag level (4,4,1,0,0,2). Koefisien kurs yang relevan untuk depresiasi -1,9639, interval nominal 95% [-4,0923; 0,1644], probabilitas nominal 0,070. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -8,58, kuartal keempat -14,05, kuartal ke-24 -18,68 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 188. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,0,1,0,0). Koefisien kurs yang relevan untuk depresiasi 0,0794, interval nominal 95% [-1,1760; 1,3348], probabilitas nominal 0,900. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: ARCH4. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 0,51, kuartal keempat 0,75, kuartal ke-24 0,76 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,3,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi -1,3350, interval nominal 95% [-3,9176; 1,2476], probabilitas nominal 0,304. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -9,49, kuartal keempat -12,71, kuartal ke-24 -12,72 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (2,0,0,4,3). Koefisien kurs yang relevan untuk depresiasi 3,8996, interval nominal 95% [-1,4269; 9,2261], probabilitas nominal 0,147. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -26,71, kuartal keempat 2,52, kuartal ke-24 37,06 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,0,0,3,2,1). Koefisien kurs yang relevan untuk depresiasi 2,3215, interval nominal 95% [-1,7914; 6,4344], probabilitas nominal 0,262. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -3,50, kuartal keempat 23,84, kuartal ke-24 22,13 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 189. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,3,0,0,0). Koefisien kurs yang relevan untuk depresiasi -1,3778, interval nominal 95% [-2,0335; -0,7221], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -10,17, kuartal keempat -13,12, kuartal ke-24 -13,13 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (2,3,0,0,4,0). Koefisien kurs yang relevan untuk depresiasi -0,3322, interval nominal 95% [-2,2473; 1,5829], probabilitas nominal 0,729. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -7,31, kuartal keempat -7,34, kuartal ke-24 -3,17 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (2,3,0,4,0). Koefisien kurs yang relevan untuk depresiasi 0,7845, interval nominal 95% [-0,5016; 2,0706], probabilitas nominal 0,226. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -12,20, kuartal keempat 5,06, kuartal ke-24 7,48 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (2,0,0,0,4,0). Koefisien kurs yang relevan untuk depresiasi 2,9015, interval nominal 95% [1,0681; 4,7349], probabilitas nominal 0,003. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -3,60, kuartal keempat 22,99, kuartal ke-24 27,65 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 190. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,4,2,2,1). Koefisien kurs yang relevan untuk depresiasi -2,3052, interval nominal 95% [-2,9490; -1,6614], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -19,26, kuartal keempat -21,98, kuartal ke-24 -21,97 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,0,4,2,0,0). Koefisien kurs yang relevan untuk depresiasi -0,5249, interval nominal 95% [-1,6388; 0,5890], probabilitas nominal 0,348. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,98, kuartal keempat -5,00, kuartal ke-24 -5,00 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (3,3,0,4,4). Koefisien kurs yang relevan untuk depresiasi 0,4438, interval nominal 95% [-2,1942; 3,0819], probabilitas nominal 0,736. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 1,48, kuartal keempat -2,91, kuartal ke-24 3,81 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,3,0,0,3,1). Koefisien kurs yang relevan untuk depresiasi 1,5310, interval nominal 95% [-0,6133; 3,6753], probabilitas nominal 0,158. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 10,50, kuartal keempat 9,40, kuartal ke-24 14,59 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 191. Atlas C | Kontrol harga BCOM

Atlas C | Kontrol harga BCOM

Skenario BCOM_control.

ARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,3,1,3,2). Koefisien kurs yang relevan untuk depresiasi 1,3625, interval nominal 95% [-0,1951; 2,9201], probabilitas nominal 0,085. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -2,39, kuartal keempat 4,13, kuartal ke-24 12,98 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2011Q1 sampai 2026Q1, 61 kuartal. Lag level (1,1,0,3,3,3). Koefisien kurs yang relevan untuk depresiasi 3,6762, interval nominal 95% [2,1423; 5,2102], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 4,51, kuartal keempat 30,68, kuartal ke-24 35,04 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 192. Atlas C | Keluarga kurs GEM alternatif

Atlas C | Keluarga kurs GEM alternatif

Skenario GEM_FX.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,4,4,0). Koefisien kurs yang relevan untuk depresiasi -0,0927, interval nominal 95% [-2,1809; 1,9955], probabilitas nominal 0,930. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; RESET. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -0,20, kuartal keempat -0,53, kuartal ke-24 -0,87 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (3,4,4,1,1). Koefisien kurs yang relevan untuk depresiasi 3,8461, interval nominal 95% [-1,5075; 9,1998], probabilitas nominal 0,156. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; RESET; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -10,68, kuartal keempat 15,39, kuartal ke-24 35,74 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,1,0). Koefisien kurs yang relevan untuk depresiasi 1,1172, interval nominal 95% [0,1439; 2,0905], probabilitas nominal 0,025. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; ARCH4. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 6,42, kuartal keempat 10,54, kuartal ke-24 10,65 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (1,0,1,0,0). Koefisien kurs yang relevan untuk depresiasi 0,5532, interval nominal 95% [-1,2913; 2,3978], probabilitas nominal 0,552. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; ARCH4; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,19, kuartal keempat 5,22, kuartal ke-24 5,27 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 193. Atlas C | Keluarga kurs GEM alternatif

Atlas C | Keluarga kurs GEM alternatif

Skenario GEM_FX.

ARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,1,0). Koefisien kurs yang relevan untuk depresiasi 1,3363, interval nominal 95% [-0,8923; 3,5649], probabilitas nominal 0,236. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; RESET; CUSUMSQ instability; ARCH4; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 4,86, kuartal keempat 8,76, kuartal ke-24 12,67 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q2, 78 kuartal. Lag level (4,0,1,0,0). Koefisien kurs yang relevan untuk depresiasi 0,0908, interval nominal 95% [-2,7426; 2,9242], probabilitas nominal 0,949. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUMSQ instability; ARCH4; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 0,31, kuartal keempat 0,56, kuartal ke-24 0,86 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 194. Atlas C | India: WPI alternatif

Atlas C | India: WPI alternatif

Skenario WPI_proxy.

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,4,1,1). Koefisien kurs yang relevan untuk depresiasi 0,1911, interval nominal 95% [-2,1995; 2,5816], probabilitas nominal 0,874. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 17,90, kuartal keempat 4,82, kuartal ke-24 1,82 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (1,4,1,0,1). Koefisien kurs yang relevan untuk depresiasi -2,0951, interval nominal 95% [-6,4414; 2,2513], probabilitas nominal 0,339. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 23,54, kuartal keempat -12,81, kuartal ke-24 -19,97 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 195. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q1, 79 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,0986, interval nominal 95% [-0,0479; 2,2450], probabilitas nominal 0,060. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 6,74, kuartal keempat 10,41, kuartal ke-24 10,47 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q1, 79 kuartal. Lag level (1,0,0,0,1). Koefisien kurs yang relevan untuk depresiasi 1,8180, interval nominal 95% [0,1048; 3,5313], probabilitas nominal 0,038. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -3,95, kuartal keempat 17,02, kuartal ke-24 17,33 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi -1,6135, interval nominal 95% [-3,4844; 0,2573], probabilitas nominal 0,090. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -3,42, kuartal keempat -11,00, kuartal ke-24 -15,35 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi -1,6156, interval nominal 95% [-4,7826; 1,5515], probabilitas nominal 0,313. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; CUSUMSQ instability; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -3,42, kuartal keempat -11,01, kuartal ke-24 -15,37 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 196. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2013Q3 sampai 2026Q1, 51 kuartal. Lag level (1,2,2,1). Koefisien kurs yang relevan untuk depresiasi -0,9648, interval nominal 95% [-8,9698; 7,0402], probabilitas nominal 0,809. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 30,54, kuartal keempat 4,40, kuartal ke-24 -9,13 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2013Q3 sampai 2026Q1, 51 kuartal. Lag level (1,2,1,1,1). Koefisien kurs yang relevan untuk depresiasi -4,6445, interval nominal 95% [-10,2076; 0,9186], probabilitas nominal 0,099. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 15,97, kuartal keempat -35,96, kuartal ke-24 -44,27 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,2,2). Koefisien kurs yang relevan untuk depresiasi -2,4719, interval nominal 95% [-4,0244; -0,9194], probabilitas nominal 0,002. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: ARCH4; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -13,49, kuartal keempat -18,77, kuartal ke-24 -23,55 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,2,0,2). Koefisien kurs yang relevan untuk depresiasi -2,8319, interval nominal 95% [-4,8765; -0,7872], probabilitas nominal 0,007. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -18,97, kuartal keempat -22,65, kuartal ke-24 -26,98 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 197. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,0430, interval nominal 95% [-1,2573; 1,1713], probabilitas nominal 0,944. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -0,16, kuartal keempat -0,38, kuartal ke-24 -0,41 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,0,1,2). Koefisien kurs yang relevan untuk depresiasi 1,4961, interval nominal 95% [-0,6903; 3,6824], probabilitas nominal 0,177. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -8,36, kuartal keempat 8,88, kuartal ke-24 14,26 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,7132, interval nominal 95% [-1,5283; 0,1020], probabilitas nominal 0,085. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,26, kuartal keempat -6,75, kuartal ke-24 -6,80 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,3556, interval nominal 95% [0,2143; 2,4969], probabilitas nominal 0,021. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 10,20, kuartal keempat 12,91, kuartal ke-24 12,92 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 198. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,2,0,0). Koefisien kurs yang relevan untuk depresiasi -0,6403, interval nominal 95% [-1,6063; 0,3257], probabilitas nominal 0,191. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -3,82, kuartal keempat -6,06, kuartal ke-24 -6,10 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,2,1,0,0). Koefisien kurs yang relevan untuk depresiasi -1,5219, interval nominal 95% [-2,9537; -0,0901], probabilitas nominal 0,038. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -10,25, kuartal keempat -14,47, kuartal ke-24 -14,51 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,1,0). Koefisien kurs yang relevan untuk depresiasi 1,1442, interval nominal 95% [0,0341; 2,2542], probabilitas nominal 0,044. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; CUSUMSQ instability; ARCH4; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 5,63, kuartal keempat 10,62, kuartal ke-24 10,91 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,1,0,0). Koefisien kurs yang relevan untuk depresiasi -0,4002, interval nominal 95% [-2,3504; 1,5500], probabilitas nominal 0,684. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; ARCH4; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -2,07, kuartal keempat -3,74, kuartal ke-24 -3,81 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 199. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2025Q3, 77 kuartal. Lag level (2,2,2,0). Koefisien kurs yang relevan untuk depresiasi 1,0804, interval nominal 95% [-0,5380; 2,6988], probabilitas nominal 0,187. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,55, kuartal keempat 7,86, kuartal ke-24 10,29 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2025Q3, 77 kuartal. Lag level (2,2,2,2,2). Koefisien kurs yang relevan untuk depresiasi 3,2843, interval nominal 95% [1,0357; 5,5329], probabilitas nominal 0,005. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 1,09, kuartal keempat 23,99, kuartal ke-24 31,30 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2025Q2, 76 kuartal. Lag level (1,0,1,0). Koefisien kurs yang relevan untuk depresiasi 0,7391, interval nominal 95% [-0,8762; 2,3544], probabilitas nominal 0,365. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; heteroskedasticity; CUSUMSQ instability; ARCH4; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,44, kuartal keempat 6,80, kuartal ke-24 7,04 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2025Q2, 76 kuartal. Lag level (1,0,1,0,0). Koefisien kurs yang relevan untuk depresiasi 0,2357, interval nominal 95% [-2,2351; 2,7064], probabilitas nominal 0,850. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; heteroskedasticity; CUSUMSQ instability; ARCH4; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 1,09, kuartal keempat 2,16, kuartal ke-24 2,25 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 200. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q1, 79 kuartal. Lag level (1,0,0,2). Koefisien kurs yang relevan untuk depresiasi -2,1852, interval nominal 95% [-3,8436; -0,5269], probabilitas nominal 0,011. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -5,75, kuartal keempat -18,72, kuartal ke-24 -20,83 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q1, 79 kuartal. Lag level (1,1,2,0,2). Koefisien kurs yang relevan untuk depresiasi -3,9043, interval nominal 95% [-5,7937; -2,0148], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -11,52, kuartal keempat -35,60, kuartal ke-24 -37,21 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q1, 79 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 2,9046, interval nominal 95% [-2,3043; 8,1135], probabilitas nominal 0,270. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUMSQ instability; ARCH4. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 15,74, kuartal keempat 27,27, kuartal ke-24 27,68 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q1, 79 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 5,5866, interval nominal 95% [-1,7965; 12,9698], probabilitas nominal 0,136. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUMSQ instability; ARCH4; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 30,85, kuartal keempat 52,55, kuartal ke-24 53,25 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 201. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q1, 79 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,4423, interval nominal 95% [-0,0388; 2,9233], probabilitas nominal 0,056. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 8,73, kuartal keempat 13,66, kuartal ke-24 13,75 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q1, 79 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 0,7641, interval nominal 95% [-1,3498; 2,8780], probabilitas nominal 0,474. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 4,67, kuartal keempat 7,24, kuartal ke-24 7,28 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q1, 79 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 0,6171, interval nominal 95% [-0,7379; 1,9721], probabilitas nominal 0,367. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 5,04, kuartal keempat 5,88, kuartal ke-24 5,88 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q1, 79 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 0,9278, interval nominal 95% [-1,0316; 2,8871], probabilitas nominal 0,348. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 7,60, kuartal keempat 8,84, kuartal ke-24 8,84 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 202. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q1, 79 kuartal. Lag level (1,0,1,0). Koefisien kurs yang relevan untuk depresiasi 3,6617, interval nominal 95% [0,3709; 6,9524], probabilitas nominal 0,030. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 18,42, kuartal keempat 34,08, kuartal ke-24 34,90 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q1, 79 kuartal. Lag level (1,0,1,0,0). Koefisien kurs yang relevan untuk depresiasi 4,3683, interval nominal 95% [-0,3253; 9,0619], probabilitas nominal 0,068. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 22,13, kuartal keempat 40,70, kuartal ke-24 41,63 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q1, 79 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,5218, interval nominal 95% [0,2084; 2,8352], probabilitas nominal 0,024. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 9,38, kuartal keempat 14,42, kuartal ke-24 14,50 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q1, 79 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,8753, interval nominal 95% [-0,0018; 3,7524], probabilitas nominal 0,050. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 11,62, kuartal keempat 17,78, kuartal ke-24 17,87 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 203. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q1, 79 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 0,4839, interval nominal 95% [-2,1014; 3,0692], probabilitas nominal 0,710. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: ARCH4. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 1,63, kuartal keempat 4,09, kuartal ke-24 4,61 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q1, 79 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 2,4649, interval nominal 95% [-0,7930; 5,7228], probabilitas nominal 0,136. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: ARCH4. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 9,25, kuartal keempat 21,57, kuartal ke-24 23,49 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,1,0,1). Koefisien kurs yang relevan untuk depresiasi -0,5689, interval nominal 95% [-1,3924; 0,2546], probabilitas nominal 0,173. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 10,64, kuartal keempat -5,40, kuartal ke-24 -5,42 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,1,1,0,1). Koefisien kurs yang relevan untuk depresiasi -1,6430, interval nominal 95% [-2,9387; -0,3472], probabilitas nominal 0,014. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 11,39, kuartal keempat -15,63, kuartal ke-24 -15,66 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 204. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,1,2). Koefisien kurs yang relevan untuk depresiasi 1,0810, interval nominal 95% [-1,0637; 3,2258], probabilitas nominal 0,318. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -18,22, kuartal keempat 10,61, kuartal ke-24 10,30 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,1,2,0). Koefisien kurs yang relevan untuk depresiasi 0,5400, interval nominal 95% [-2,8592; 3,9392], probabilitas nominal 0,752. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; ARCH4; non-normal residuals. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,73, kuartal keempat 5,14, kuartal ke-24 5,15 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,1,1,2). Koefisien kurs yang relevan untuk depresiasi -1,3252, interval nominal 95% [-2,4648; -0,1857], probabilitas nominal 0,023. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; CUSUMSQ instability; ARCH4; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 3,40, kuartal keempat -11,63, kuartal ke-24 -12,63 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,2,2,1,2). Koefisien kurs yang relevan untuk depresiasi -3,0512, interval nominal 95% [-4,6544; -1,4479], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 18,85, kuartal keempat -28,44, kuartal ke-24 -29,08 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 205. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,1,0). Koefisien kurs yang relevan untuk depresiasi 0,2814, interval nominal 95% [-1,7533; 2,3161], probabilitas nominal 0,784. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability; ARCH4; non-normal residuals. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 1,15, kuartal keempat 2,52, kuartal ke-24 2,68 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,2,0,2). Koefisien kurs yang relevan untuk depresiasi -1,7500, interval nominal 95% [-4,3295; 0,8295], probabilitas nominal 0,180. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability; ARCH4. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 4,24, kuartal keempat -18,17, kuartal ke-24 -16,68 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,0,2). Koefisien kurs yang relevan untuk depresiasi -1,3760, interval nominal 95% [-3,2494; 0,4974], probabilitas nominal 0,148. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; CUSUMSQ instability; ARCH4. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -1,21, kuartal keempat -10,84, kuartal ke-24 -13,11 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,0,0,2). Koefisien kurs yang relevan untuk depresiasi -1,9951, interval nominal 95% [-4,5649; 0,5747], probabilitas nominal 0,126. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; CUSUMSQ instability; ARCH4. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 15,45, kuartal keempat -15,61, kuartal ke-24 -19,02 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 206. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,2,0,0). Koefisien kurs yang relevan untuk depresiasi -2,3835, interval nominal 95% [-4,5920; -0,1750], probabilitas nominal 0,035. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -5,13, kuartal keempat -16,40, kuartal ke-24 -22,68 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,2,0,2,2). Koefisien kurs yang relevan untuk depresiasi -5,8039, interval nominal 95% [-8,4750; -3,1328], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -0,19, kuartal keempat -38,45, kuartal ke-24 -55,31 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,2,0,0). Koefisien kurs yang relevan untuk depresiasi 1,2272, interval nominal 95% [-3,9034; 6,3579], probabilitas nominal 0,635. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; RESET; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 1,24, kuartal keempat 4,28, kuartal ke-24 10,40 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,2,0,2,0). Koefisien kurs yang relevan untuk depresiasi 26,0440, interval nominal 95% [-56,4880; 108,5759], probabilitas nominal 0,531. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 10,15, kuartal keempat 37,58, kuartal ke-24 135,50 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 207. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2013Q3 sampai 2026Q1, 51 kuartal. Lag level (1,2,2,1). Koefisien kurs yang relevan untuk depresiasi 1,0835, interval nominal 95% [-9,2375; 11,4044], probabilitas nominal 0,833. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 49,18, kuartal keempat 13,84, kuartal ke-24 10,33 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2013Q3 sampai 2026Q1, 51 kuartal. Lag level (1,1,1,0,1). Koefisien kurs yang relevan untuk depresiasi -3,9697, interval nominal 95% [-11,4815; 3,5421], probabilitas nominal 0,292. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 41,93, kuartal keempat -36,46, kuartal ke-24 -37,84 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2013Q3 sampai 2026Q1, 51 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 5,5809, interval nominal 95% [-8,6786; 19,8404], probabilitas nominal 0,435. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 22,55, kuartal keempat 49,82, kuartal ke-24 53,19 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2013Q3 sampai 2026Q1, 51 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 6,1617, interval nominal 95% [-9,8602; 22,1837], probabilitas nominal 0,443. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 25,07, kuartal keempat 55,10, kuartal ke-24 58,73 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 208. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2013Q3 sampai 2026Q1, 51 kuartal. Lag level (1,0,0,1). Koefisien kurs yang relevan untuk depresiasi 0,7088, interval nominal 95% [-10,1032; 11,5209], probabilitas nominal 0,896. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: non-normal residuals. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 44,68, kuartal keempat 13,54, kuartal ke-24 6,76 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2013Q3 sampai 2026Q1, 51 kuartal. Lag level (1,1,1,0,1). Koefisien kurs yang relevan untuk depresiasi -5,0630, interval nominal 95% [-11,8663; 1,7404], probabilitas nominal 0,141. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: RESET. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 24,16, kuartal keempat -45,10, kuartal ke-24 -48,26 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2013Q3 sampai 2026Q1, 51 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,5994, interval nominal 95% [-10,8779; 9,6791], probabilitas nominal 0,907. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -2,41, kuartal keempat -5,35, kuartal ke-24 -5,71 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2013Q3 sampai 2026Q1, 51 kuartal. Lag level (1,0,1,1,0). Koefisien kurs yang relevan untuk depresiasi -3,2818, interval nominal 95% [-11,8110; 5,2473], probabilitas nominal 0,442. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -17,81, kuartal keempat -30,82, kuartal ke-24 -31,28 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 209. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2013Q3 sampai 2026Q1, 51 kuartal. Lag level (1,0,1,0). Koefisien kurs yang relevan untuk depresiasi 1,2264, interval nominal 95% [-12,2613; 14,7140], probabilitas nominal 0,856. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 4,48, kuartal keempat 10,64, kuartal ke-24 11,69 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2013Q3 sampai 2026Q1, 51 kuartal. Lag level (1,1,1,0,0). Koefisien kurs yang relevan untuk depresiasi -8,1310, interval nominal 95% [-18,1108; 1,8489], probabilitas nominal 0,108. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: RESET. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -43,22, kuartal keempat -76,18, kuartal ke-24 -77,50 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2013Q3 sampai 2026Q1, 51 kuartal. Lag level (1,2,2,2). Koefisien kurs yang relevan untuk depresiasi 2,2311, interval nominal 95% [-8,3406; 12,8028], probabilitas nominal 0,672. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 44,54, kuartal keempat 19,75, kuartal ke-24 21,26 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2013Q3 sampai 2026Q1, 51 kuartal. Lag level (1,2,1,2,1). Koefisien kurs yang relevan untuk depresiasi -3,8810, interval nominal 95% [-10,6035; 2,8414], probabilitas nominal 0,250. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 20,38, kuartal keempat -29,33, kuartal ke-24 -36,99 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 210. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2013Q3 sampai 2026Q1, 51 kuartal. Lag level (2,0,0,1). Koefisien kurs yang relevan untuk depresiasi -2,0900, interval nominal 95% [-8,4652; 4,2852], probabilitas nominal 0,512. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 8,53, kuartal keempat -11,98, kuartal ke-24 -19,89 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2013Q3 sampai 2026Q1, 51 kuartal. Lag level (2,0,2,0,0). Koefisien kurs yang relevan untuk depresiasi -2,6569, interval nominal 95% [-8,2775; 2,9637], probabilitas nominal 0,346. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; RESET; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -9,89, kuartal keempat -21,15, kuartal ke-24 -25,32 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,5978, interval nominal 95% [-1,7339; 0,5383], probabilitas nominal 0,298. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; heteroskedasticity; RESET; CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -2,25, kuartal keempat -5,24, kuartal ke-24 -5,70 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi -2,0178, interval nominal 95% [-3,0902; -0,9454], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; heteroskedasticity; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -10,97, kuartal keempat -18,95, kuartal ke-24 -19,23 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 211. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,0,0,2). Koefisien kurs yang relevan untuk depresiasi -1,9750, interval nominal 95% [-5,7854; 1,8353], probabilitas nominal 0,305. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -19,44, kuartal keempat -12,14, kuartal ke-24 -18,56 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,0,0,1,2). Koefisien kurs yang relevan untuk depresiasi -3,8826, interval nominal 95% [-7,5633; -0,2020], probabilitas nominal 0,039. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -24,98, kuartal keempat -25,97, kuartal ke-24 -36,91 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,2,0). Koefisien kurs yang relevan untuk depresiasi -1,9184, interval nominal 95% [-3,0052; -0,8317], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -10,08, kuartal keempat -17,95, kuartal ke-24 -18,28 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,2,2,0,0). Koefisien kurs yang relevan untuk depresiasi -1,0315, interval nominal 95% [-2,7849; 0,7220], probabilitas nominal 0,245. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -5,22, kuartal keempat -9,61, kuartal ke-24 -9,83 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 212. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,2,1,0). Koefisien kurs yang relevan untuk depresiasi -0,9768, interval nominal 95% [-2,6348; 0,6811], probabilitas nominal 0,244. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,65, kuartal keempat -9,02, kuartal ke-24 -9,31 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,2,1,0,0). Koefisien kurs yang relevan untuk depresiasi -1,6227, interval nominal 95% [-3,9369; 0,6915], probabilitas nominal 0,166. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -8,04, kuartal keempat -15,07, kuartal ke-24 -15,47 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,2,0). Koefisien kurs yang relevan untuk depresiasi -2,2674, interval nominal 95% [-3,6410; -0,8939], probabilitas nominal 0,002. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; RESET; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -12,11, kuartal keempat -21,26, kuartal ke-24 -21,61 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,2,2,0,0). Koefisien kurs yang relevan untuk depresiasi -0,4820, interval nominal 95% [-2,5814; 1,6174], probabilitas nominal 0,648. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -2,58, kuartal keempat -4,52, kuartal ke-24 -4,59 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 213. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,2,1). Koefisien kurs yang relevan untuk depresiasi -2,1523, interval nominal 95% [-3,6081; -0,6964], probabilitas nominal 0,004. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUMSQ instability; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -9,56, kuartal keempat -17,43, kuartal ke-24 -20,51 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,2,0,1). Koefisien kurs yang relevan untuk depresiasi -2,3455, interval nominal 95% [-4,4740; -0,2169], probabilitas nominal 0,031. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -13,87, kuartal keempat -20,06, kuartal ke-24 -22,35 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,2,0,2). Koefisien kurs yang relevan untuk depresiasi -1,4895, interval nominal 95% [-3,6009; 0,6218], probabilitas nominal 0,164. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; RESET; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -6,72, kuartal keempat -7,39, kuartal ke-24 -14,06 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,2,0,0,2). Koefisien kurs yang relevan untuk depresiasi -1,8687, interval nominal 95% [-4,4591; 0,7216], probabilitas nominal 0,155. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; RESET; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -8,70, kuartal keempat -9,30, kuartal ke-24 -17,68 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 214. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,2857, interval nominal 95% [0,1378; 2,4336], probabilitas nominal 0,029. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,69, kuartal keempat 8,84, kuartal ke-24 12,23 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,0,0,0,1). Koefisien kurs yang relevan untuk depresiasi 2,2865, interval nominal 95% [0,5876; 3,9855], probabilitas nominal 0,009. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -5,52, kuartal keempat 15,77, kuartal ke-24 21,79 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,0,0,1). Koefisien kurs yang relevan untuk depresiasi 0,9892, interval nominal 95% [-1,7481; 3,7264], probabilitas nominal 0,474. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -40,02, kuartal keempat 5,13, kuartal ke-24 9,43 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,0,0,0,2). Koefisien kurs yang relevan untuk depresiasi 4,3922, interval nominal 95% [-0,1990; 8,9833], probabilitas nominal 0,060. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; non-normal residuals. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -56,23, kuartal keempat 31,98, kuartal ke-24 41,86 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 215. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,5380, interval nominal 95% [-2,1491; 1,0731], probabilitas nominal 0,508. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -2,60, kuartal keempat -4,98, kuartal ke-24 -5,13 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 2,1580, interval nominal 95% [-0,9520; 5,2681], probabilitas nominal 0,171. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 10,98, kuartal keempat 20,12, kuartal ke-24 20,57 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,0,0,2). Koefisien kurs yang relevan untuk depresiasi 5,6754, interval nominal 95% [-0,0847; 11,4356], probabilitas nominal 0,053. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; RESET; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -4,51, kuartal keempat 17,98, kuartal ke-24 53,56 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 11,7364, interval nominal 95% [-0,3490; 23,8218], probabilitas nominal 0,057. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; RESET; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 24,45, kuartal keempat 72,30, kuartal ke-24 111,14 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 216. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,7157, interval nominal 95% [-2,6766; 1,2452], probabilitas nominal 0,469. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -3,44, kuartal keempat -6,62, kuartal ke-24 -6,82 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 2,6467, interval nominal 95% [-1,2108; 6,5041], probabilitas nominal 0,176. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 13,23, kuartal keempat 24,61, kuartal ke-24 25,23 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,1,1,1). Koefisien kurs yang relevan untuk depresiasi 1,9915, interval nominal 95% [-3,3555; 7,3386], probabilitas nominal 0,460. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 11,68, kuartal keempat 11,69, kuartal ke-24 17,26 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,0,0,2,0). Koefisien kurs yang relevan untuk depresiasi 10,9005, interval nominal 95% [-1,2877; 23,0887], probabilitas nominal 0,079. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 13,04, kuartal keempat 41,09, kuartal ke-24 94,52 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 217. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,1,0,0). Koefisien kurs yang relevan untuk depresiasi 1,7136, interval nominal 95% [0,1600; 3,2671], probabilitas nominal 0,031. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 4,03, kuartal keempat 11,23, kuartal ke-24 16,27 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,1,0,1,1). Koefisien kurs yang relevan untuk depresiasi 3,6237, interval nominal 95% [1,0234; 6,2241], probabilitas nominal 0,007. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -12,72, kuartal keempat 20,31, kuartal ke-24 34,47 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,2,0). Koefisien kurs yang relevan untuk depresiasi -0,0512, interval nominal 95% [-2,2929; 2,1905], probabilitas nominal 0,964. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -0,20, kuartal keempat -0,45, kuartal ke-24 -0,49 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,2,0,0). Koefisien kurs yang relevan untuk depresiasi 3,6651, interval nominal 95% [-0,8414; 8,1716], probabilitas nominal 0,109. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 14,63, kuartal keempat 32,62, kuartal ke-24 34,93 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 218. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,1,0). Koefisien kurs yang relevan untuk depresiasi 0,2073, interval nominal 95% [-0,8805; 1,2951], probabilitas nominal 0,705. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 1,94, kuartal keempat 1,98, kuartal ke-24 1,98 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,1,0,0). Koefisien kurs yang relevan untuk depresiasi 0,5302, interval nominal 95% [-1,5656; 2,6261], probabilitas nominal 0,616. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 5,01, kuartal keempat 5,05, kuartal ke-24 5,05 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi -1,2839, interval nominal 95% [-2,6009; 0,0331], probabilitas nominal 0,056. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -8,15, kuartal keempat -12,19, kuartal ke-24 -12,24 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,2006, interval nominal 95% [-0,9658; 3,3670], probabilitas nominal 0,273. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 8,57, kuartal keempat 11,43, kuartal ke-24 11,44 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 219. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,0,2,0). Koefisien kurs yang relevan untuk depresiasi -1,5332, interval nominal 95% [-5,7902; 2,7239], probabilitas nominal 0,475. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUMSQ instability; ARCH4; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -3,81, kuartal keempat -9,61, kuartal ke-24 -14,52 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,0,2,2,0). Koefisien kurs yang relevan untuk depresiasi 4,6393, interval nominal 95% [0,1390; 9,1395], probabilitas nominal 0,044. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 19,90, kuartal keempat 38,44, kuartal ke-24 44,21 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi -1,2718, interval nominal 95% [-2,9341; 0,3905], probabilitas nominal 0,132. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -7,37, kuartal keempat -12,01, kuartal ke-24 -12,12 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 0,7242, interval nominal 95% [-2,2801; 3,7286], probabilitas nominal 0,632. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 4,42, kuartal keempat 6,86, kuartal ke-24 6,90 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 220. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,2,1). Koefisien kurs yang relevan untuk depresiasi 0,4117, interval nominal 95% [-1,0333; 1,8567], probabilitas nominal 0,572. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 12,97, kuartal keempat 5,19, kuartal ke-24 3,92 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,2,0,1). Koefisien kurs yang relevan untuk depresiasi 1,2854, interval nominal 95% [-1,7161; 4,2869], probabilitas nominal 0,396. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 24,11, kuartal keempat 14,25, kuartal ke-24 12,25 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,0,0,0). Koefisien kurs yang relevan untuk depresiasi 0,1443, interval nominal 95% [-1,8103; 2,0989], probabilitas nominal 0,883. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 0,28, kuartal keempat 0,83, kuartal ke-24 1,36 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,7850, interval nominal 95% [-1,3895; 4,9596], probabilitas nominal 0,266. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 4,11, kuartal keempat 11,48, kuartal ke-24 16,94 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 221. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,0,0,0). Koefisien kurs yang relevan untuk depresiasi 3,0327, interval nominal 95% [-0,6549; 6,7202], probabilitas nominal 0,106. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 6,07, kuartal keempat 17,90, kuartal ke-24 28,63 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 5,3211, interval nominal 95% [0,2814; 10,3608], probabilitas nominal 0,039. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 12,21, kuartal keempat 33,99, kuartal ke-24 50,48 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,4456, interval nominal 95% [-2,5922; 1,7010], probabilitas nominal 0,680. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -2,76, kuartal keempat -4,22, kuartal ke-24 -4,25 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,1,0,2,0). Koefisien kurs yang relevan untuk depresiasi -1,1376, interval nominal 95% [-4,6294; 2,3543], probabilitas nominal 0,518. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -7,19, kuartal keempat -10,80, kuartal ke-24 -10,84 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 222. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,2,0,0). Koefisien kurs yang relevan untuk depresiasi -1,1850, interval nominal 95% [-2,2570; -0,1130], probabilitas nominal 0,031. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -8,31, kuartal keempat -11,28, kuartal ke-24 -11,29 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,2,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,4291, interval nominal 95% [-2,1696; 1,3114], probabilitas nominal 0,625. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -3,08, kuartal keempat -4,09, kuartal ke-24 -4,09 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,0,0,0). Koefisien kurs yang relevan untuk depresiasi 2,7729, interval nominal 95% [-2,7536; 8,2993], probabilitas nominal 0,321. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; RESET; CUSUMSQ instability; ARCH4; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 8,59, kuartal keempat 20,08, kuartal ke-24 26,40 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi -2,6515, interval nominal 95% [-9,7232; 4,4201], probabilitas nominal 0,457. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; RESET; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -10,14, kuartal keempat -21,33, kuartal ke-24 -25,27 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 223. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,2,0,0). Koefisien kurs yang relevan untuk depresiasi -1,3801, interval nominal 95% [-2,5228; -0,2374], probabilitas nominal 0,019. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -10,20, kuartal keempat -13,15, kuartal ke-24 -13,15 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,2,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,5228, interval nominal 95% [-2,3762; 1,3306], probabilitas nominal 0,576. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -3,96, kuartal keempat -4,98, kuartal ke-24 -4,98 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,2,0,0). Koefisien kurs yang relevan untuk depresiasi 0,4000, interval nominal 95% [-1,3533; 2,1533], probabilitas nominal 0,651. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; non-normal residuals. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 1,27, kuartal keempat 3,31, kuartal ke-24 3,81 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,2,1,0,0). Koefisien kurs yang relevan untuk depresiasi -2,1524, interval nominal 95% [-3,9098; -0,3950], probabilitas nominal 0,017. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -10,97, kuartal keempat -20,07, kuartal ke-24 -20,51 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 224. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,2523, interval nominal 95% [-3,0325; 2,5280], probabilitas nominal 0,857. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUMSQ instability; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -0,69, kuartal keempat -1,82, kuartal ke-24 -2,40 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi -1,7412, interval nominal 95% [-5,1228; 1,6405], probabilitas nominal 0,308. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUMSQ instability; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -6,31, kuartal keempat -15,08, kuartal ke-24 -16,59 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,2,0,2). Koefisien kurs yang relevan untuk depresiasi 1,7740, interval nominal 95% [-0,8061; 4,3542], probabilitas nominal 0,175. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 22,63, kuartal keempat 19,83, kuartal ke-24 16,91 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,0,0,0,2). Koefisien kurs yang relevan untuk depresiasi 3,2476, interval nominal 95% [-1,6723; 8,1675], probabilitas nominal 0,192. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 46,15, kuartal keempat 36,24, kuartal ke-24 30,95 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 225. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,2,0,2). Koefisien kurs yang relevan untuk depresiasi -1,9600, interval nominal 95% [-4,3009; 0,3808], probabilitas nominal 0,099. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability; ARCH4; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -41,46, kuartal keempat -18,44, kuartal ke-24 -18,68 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,2,0,0,2). Koefisien kurs yang relevan untuk depresiasi -0,5172, interval nominal 95% [-4,9478; 3,9133], probabilitas nominal 0,817. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET; CUSUMSQ instability; ARCH4; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -51,70, kuartal keempat -4,60, kuartal ke-24 -4,93 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,0,1,0). Koefisien kurs yang relevan untuk depresiasi 1,0084, interval nominal 95% [-0,5748; 2,5917], probabilitas nominal 0,208. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 7,44, kuartal keempat 9,53, kuartal ke-24 9,61 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,0,1,0,0). Koefisien kurs yang relevan untuk depresiasi 0,3766, interval nominal 95% [-2,6116; 3,3648], probabilitas nominal 0,802. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 2,78, kuartal keempat 3,56, kuartal ke-24 3,59 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 226. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 2,4662, interval nominal 95% [0,3087; 4,6236], probabilitas nominal 0,026. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 11,52, kuartal keempat 22,69, kuartal ke-24 23,51 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,0,0,0,1). Koefisien kurs yang relevan untuk depresiasi -0,9629, interval nominal 95% [-6,1979; 4,2721], probabilitas nominal 0,715. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 24,46, kuartal keempat -3,92, kuartal ke-24 -9,18 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,1,0). Koefisien kurs yang relevan untuk depresiasi -0,5606, interval nominal 95% [-1,9206; 0,7994], probabilitas nominal 0,414. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,10, kuartal keempat -5,34, kuartal ke-24 -5,34 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,1,0,1). Koefisien kurs yang relevan untuk depresiasi -0,1399, interval nominal 95% [-2,8813; 2,6014], probabilitas nominal 0,919. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -28,24, kuartal keempat -1,44, kuartal ke-24 -1,33 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 227. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,1,0). Koefisien kurs yang relevan untuk depresiasi 0,9685, interval nominal 95% [-0,2668; 2,2038], probabilitas nominal 0,122. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,97, kuartal keempat 8,68, kuartal ke-24 9,23 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (1,0,1,1,1). Koefisien kurs yang relevan untuk depresiasi -0,1974, interval nominal 95% [-2,4280; 2,0332], probabilitas nominal 0,860. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; RESET; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -16,00, kuartal keempat -3,18, kuartal ke-24 -1,88 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,1,1,2). Koefisien kurs yang relevan untuk depresiasi 0,1907, interval nominal 95% [-1,5615; 1,9429], probabilitas nominal 0,829. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 0,49, kuartal keempat 5,33, kuartal ke-24 1,82 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2026Q2, 80 kuartal. Lag level (2,1,1,0,2). Koefisien kurs yang relevan untuk depresiasi -1,8960, interval nominal 95% [-4,9350; 1,1430], probabilitas nominal 0,217. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET; non-normal residuals; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -4,72, kuartal keempat -9,10, kuartal ke-24 -18,07 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 228. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2025Q3, 77 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi -0,8234, interval nominal 95% [-1,4916; -0,1552], probabilitas nominal 0,016. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -7,28, kuartal keempat -7,85, kuartal ke-24 -7,85 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2025Q3, 77 kuartal. Lag level (1,0,0,2,1). Koefisien kurs yang relevan untuk depresiasi 0,5732, interval nominal 95% [-0,4957; 1,6421], probabilitas nominal 0,288. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -8,98, kuartal keempat 5,46, kuartal ke-24 5,46 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2025Q3, 77 kuartal. Lag level (2,0,0,0). Koefisien kurs yang relevan untuk depresiasi 4,1627, interval nominal 95% [-3,0997; 11,4252], probabilitas nominal 0,257. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 8,36, kuartal keempat 22,44, kuartal ke-24 38,91 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2025Q3, 77 kuartal. Lag level (2,0,0,1,0). Koefisien kurs yang relevan untuk depresiasi 2,7797, interval nominal 95% [-7,6712; 13,2306], probabilitas nominal 0,597. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 6,33, kuartal keempat 16,16, kuartal ke-24 26,18 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 229. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2025Q3, 77 kuartal. Lag level (2,0,2,0). Koefisien kurs yang relevan untuk depresiasi -0,3532, interval nominal 95% [-1,5376; 0,8312], probabilitas nominal 0,554. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -2,13, kuartal keempat -3,22, kuartal ke-24 -3,37 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2025Q3, 77 kuartal. Lag level (1,2,0,2,2). Koefisien kurs yang relevan untuk depresiasi 1,6593, interval nominal 95% [0,1929; 3,1258], probabilitas nominal 0,027. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -12,32, kuartal keempat 15,82, kuartal ke-24 15,82 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2025Q3, 77 kuartal. Lag level (2,1,0,0). Koefisien kurs yang relevan untuk depresiasi 0,8709, interval nominal 95% [-1,8548; 3,5965], probabilitas nominal 0,526. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 2,91, kuartal keempat 6,12, kuartal ke-24 8,28 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2025Q3, 77 kuartal. Lag level (2,1,0,2,2). Koefisien kurs yang relevan untuk depresiasi 5,0435, interval nominal 95% [2,2994; 7,7875], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -4,87, kuartal keempat 47,81, kuartal ke-24 48,07 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 230. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2025Q3, 77 kuartal. Lag level (2,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,9237, interval nominal 95% [-5,5883; 9,4358], probabilitas nominal 0,611. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 4,88, kuartal keempat 11,99, kuartal ke-24 18,21 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2025Q3, 77 kuartal. Lag level (2,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,9769, interval nominal 95% [-10,1482; 14,1020], probabilitas nominal 0,746. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 5,01, kuartal keempat 12,31, kuartal ke-24 18,71 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2025Q3, 77 kuartal. Lag level (2,1,2,0). Koefisien kurs yang relevan untuk depresiasi 0,0799, interval nominal 95% [-1,3884; 1,5482], probabilitas nominal 0,914. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; RESET; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 0,30, kuartal keempat 0,65, kuartal ke-24 0,76 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2025Q3, 77 kuartal. Lag level (1,0,2,1,1). Koefisien kurs yang relevan untuk depresiasi 1,6682, interval nominal 95% [0,1564; 3,1799], probabilitas nominal 0,031. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; RESET. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -8,08, kuartal keempat 15,46, kuartal ke-24 15,90 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 231. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2025Q3, 77 kuartal. Lag level (2,2,2,0). Koefisien kurs yang relevan untuk depresiasi 1,6439, interval nominal 95% [-0,8116; 4,0995], probabilitas nominal 0,186. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 4,82, kuartal keempat 11,71, kuartal ke-24 15,65 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2025Q3, 77 kuartal. Lag level (2,2,2,1,2). Koefisien kurs yang relevan untuk depresiasi 3,4028, interval nominal 95% [-0,5182; 7,3238], probabilitas nominal 0,088. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 5,93, kuartal keempat 20,33, kuartal ke-24 32,42 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2025Q2, 76 kuartal. Lag level (2,0,0,0). Koefisien kurs yang relevan untuk depresiasi 5,9385, interval nominal 95% [1,7808; 10,0961], probabilitas nominal 0,006. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 28,67, kuartal keempat 57,64, kuartal ke-24 56,60 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2025Q2, 76 kuartal. Lag level (2,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 7,6356, interval nominal 95% [1,6809; 13,5902], probabilitas nominal 0,013. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 38,44, kuartal keempat 74,32, kuartal ke-24 72,77 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 232. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2025Q2, 76 kuartal. Lag level (2,0,0,1). Koefisien kurs yang relevan untuk depresiasi 2,7706, interval nominal 95% [-0,7872; 6,3284], probabilitas nominal 0,125. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; RESET; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -15,76, kuartal keempat 21,66, kuartal ke-24 26,41 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2025Q2, 76 kuartal. Lag level (1,0,0,0,1). Koefisien kurs yang relevan untuk depresiasi -0,4773, interval nominal 95% [-4,3239; 3,3694], probabilitas nominal 0,805. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: heteroskedasticity; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -69,94, kuartal keempat -5,21, kuartal ke-24 -4,55 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2025Q2, 76 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 2,2538, interval nominal 95% [-1,4734; 5,9809], probabilitas nominal 0,232. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 11,37, kuartal keempat 20,99, kuartal ke-24 21,48 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2025Q2, 76 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 2,6013, interval nominal 95% [-3,1687; 8,3712], probabilitas nominal 0,372. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 13,23, kuartal keempat 24,24, kuartal ke-24 24,79 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 233. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2025Q2, 76 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 4,0335, interval nominal 95% [1,2080; 6,8589], probabilitas nominal 0,006. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; ARCH4. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 21,69, kuartal keempat 37,84, kuartal ke-24 38,44 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2025Q2, 76 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 4,7708, interval nominal 95% [0,5205; 9,0210], probabilitas nominal 0,028. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; ARCH4. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 26,01, kuartal keempat 44,82, kuartal ke-24 45,47 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2025Q2, 76 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi -3,7817, interval nominal 95% [-7,3754; -0,1879], probabilitas nominal 0,039. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: CUSUMSQ instability; ARCH4; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -30,74, kuartal keempat -36,04, kuartal ke-24 -36,04 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2025Q2, 76 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi -3,5846, interval nominal 95% [-9,1028; 1,9335], probabilitas nominal 0,199. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: RESET; CUSUMSQ instability; ARCH4; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -29,15, kuartal keempat -34,16, kuartal ke-24 -34,17 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 234. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2006Q3 sampai 2025Q2, 76 kuartal. Lag level (1,0,1,0). Koefisien kurs yang relevan untuk depresiasi -0,8559, interval nominal 95% [-2,9496; 1,2378], probabilitas nominal 0,418. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; heteroskedasticity; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -3,47, kuartal keempat -7,65, kuartal ke-24 -8,16 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2025Q2, 76 kuartal. Lag level (2,0,0,2,2). Koefisien kurs yang relevan untuk depresiasi -2,4271, interval nominal 95% [-5,3795; 0,5253], probabilitas nominal 0,105. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: BG4 serial correlation; heteroskedasticity; CUSUMSQ instability; non-normal residuals. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 4,97, kuartal keempat -23,05, kuartal ke-24 -23,13 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2006Q3 sampai 2025Q2, 76 kuartal. Lag level (2,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,3117, interval nominal 95% [-1,5341; 4,1575], probabilitas nominal 0,361. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 3,46, kuartal keempat 9,12, kuartal ke-24 12,48 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2006Q3 sampai 2025Q2, 76 kuartal. Lag level (1,0,0,2,0). Koefisien kurs yang relevan untuk depresiasi -0,8647, interval nominal 95% [-3,6274; 1,8979], probabilitas nominal 0,534. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -3,35, kuartal keempat -7,64, kuartal ke-24 -8,24 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 235. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2010Q3 sampai 2026Q1, 63 kuartal. Lag level (1,0,1,0). Koefisien kurs yang relevan untuk depresiasi -0,2792, interval nominal 95% [-1,5309; 0,9726], probabilitas nominal 0,657. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -1,78, kuartal keempat -2,65, kuartal ke-24 -2,66 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2010Q3 sampai 2026Q1, 63 kuartal. Lag level (1,0,1,0,0). Koefisien kurs yang relevan untuk depresiasi 0,2922, interval nominal 95% [-1,6716; 2,2559], probabilitas nominal 0,767. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 1,87, kuartal keempat 2,77, kuartal ke-24 2,78 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2010Q3 sampai 2026Q1, 63 kuartal. Lag level (1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 0,8770, interval nominal 95% [-1,7775; 3,5314], probabilitas nominal 0,511. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 4,28, kuartal keempat 8,13, kuartal ke-24 8,36 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2010Q3 sampai 2026Q1, 63 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 1,4219, interval nominal 95% [-2,7401; 5,5839], probabilitas nominal 0,497. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: RESET; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 7,04, kuartal keempat 13,20, kuartal ke-24 13,55 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 236. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2010Q3 sampai 2026Q1, 63 kuartal. Lag level (1,2,2,0). Koefisien kurs yang relevan untuk depresiasi -1,5364, interval nominal 95% [-2,2697; -0,8030], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -10,55, kuartal keempat -14,62, kuartal ke-24 -14,64 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2010Q3 sampai 2026Q1, 63 kuartal. Lag level (1,0,0,0,0). Koefisien kurs yang relevan untuk depresiasi 0,6814, interval nominal 95% [-0,5719; 1,9347], probabilitas nominal 0,281. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 4,22, kuartal keempat 6,46, kuartal ke-24 6,49 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2010Q3 sampai 2026Q1, 63 kuartal. Lag level (2,2,0,1). Koefisien kurs yang relevan untuk depresiasi 1,2470, interval nominal 95% [-1,2403; 3,7342], probabilitas nominal 0,319. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: non-normal residuals. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama -9,48, kuartal keempat 5,67, kuartal ke-24 11,85 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2010Q3 sampai 2026Q1, 63 kuartal. Lag level (2,0,0,1,0). Koefisien kurs yang relevan untuk depresiasi 3,4943, interval nominal 95% [-0,0101; 6,9987], probabilitas nominal 0,051. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: non-normal residuals. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 12,10, kuartal keempat 26,45, kuartal ke-24 33,29 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 237. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2010Q3 sampai 2026Q1, 63 kuartal. Lag level (2,2,0,0). Koefisien kurs yang relevan untuk depresiasi -2,2223, interval nominal 95% [-3,1089; -1,3357], probabilitas nominal <0,001. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; catatan diagnostik. Flag lengkap: RESET. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -15,61, kuartal keempat -20,84, kuartal ke-24 -21,18 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2010Q3 sampai 2026Q1, 63 kuartal. Lag level (1,2,0,2,0). Koefisien kurs yang relevan untuk depresiasi -0,7150, interval nominal 95% [-2,0504; 0,6203], probabilitas nominal 0,288. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -6,09, kuartal keempat -6,81, kuartal ke-24 -6,82 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2010Q3 sampai 2026Q1, 63 kuartal. Lag level (1,2,0,1). Koefisien kurs yang relevan untuk depresiasi -1,8864, interval nominal 95% [-3,6596; -0,1132], probabilitas nominal 0,037. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama 1,71, kuartal keempat -12,19, kuartal ke-24 -17,97 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2010Q3 sampai 2026Q1, 63 kuartal. Lag level (1,0,1,0,1). Koefisien kurs yang relevan untuk depresiasi 1,0078, interval nominal 95% [-1,7258; 3,7414], probabilitas nominal 0,463. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: heteroskedasticity; CUSUMSQ instability; CUSUM instability or unavailable. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 15,16, kuartal keempat 11,35, kuartal ke-24 9,61 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 238. Atlas C | Maksimum dua lag level

Atlas C | Maksimum dua lag level

Skenario main.

ARDL: sampel estimasi 2010Q3 sampai 2026Q1, 63 kuartal. Lag level (1,2,0,0). Koefisien kurs yang relevan untuk depresiasi 0,4536, interval nominal 95% [-1,0102; 1,9173], probabilitas nominal 0,537. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 1,31, kuartal keempat 3,61, kuartal ke-24 4,32 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2010Q3 sampai 2026Q1, 63 kuartal. Lag level (1,1,0,0,0). Koefisien kurs yang relevan untuk depresiasi 2,6753, interval nominal 95% [1,0567; 4,2939], probabilitas nominal 0,002. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Level didukung; diagnostik memadai. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 11,71, kuartal keempat 24,32, kuartal ke-24 25,50 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

ARDL: sampel estimasi 2010Q3 sampai 2026Q1, 63 kuartal. Lag level (1,2,0,0). Koefisien kurs yang relevan untuk depresiasi -0,7276, interval nominal 95% [-1,6703; 0,2151], probabilitas nominal 0,128. Dengan definisi kurs penelitian, tanda ini mengarah pada pemburukan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: No rejection in listed tests. Pemeriksaan visual-operasional: Akhir horizon belum membaik. Respons kuartal pertama -2,51, kuartal keempat -6,20, kuartal ke-24 -6,94 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2010Q3 sampai 2026Q1, 63 kuartal. Lag level (2,0,2,0,0). Koefisien kurs yang relevan untuk depresiasi 1,8454, interval nominal 95% [0,0497; 3,6412], probabilitas nominal 0,044. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUMSQ instability. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 6,43, kuartal keempat 14,66, kuartal ke-24 17,59 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 239. Atlas C | Agregat Indonesia 2006+

Atlas C | Agregat Indonesia 2006+

Skenario world_2006_sensitivity.

ARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (2,3,2,3). Koefisien kurs yang relevan untuk depresiasi 1,7167, interval nominal 95% [-2,5272; 5,9606], probabilitas nominal 0,422. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: CUSUM instability or unavailable. Pemeriksaan visual-operasional: Pola J pada estimasi titik. Respons kuartal pertama 1,04, kuartal keempat -0,23, kuartal ke-24 14,02 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

NARDL: sampel estimasi 2007Q1 sampai 2026Q1, 77 kuartal. Lag level (2,3,2,1,3). Koefisien kurs yang relevan untuk depresiasi 6,3205, interval nominal 95% [-5,5919; 18,2330], probabilitas nominal 0,293. Dengan definisi kurs penelitian, tanda ini mengarah pada perbaikan neraca pada depresiasi. Hubungan level belum didukung. Flag lengkap: BG4 serial correlation. Pemeriksaan visual-operasional: Perbaikan tanpa fase awal memburuk. Respons kuartal pertama 10,23, kuartal keempat 17,00, kuartal ke-24 52,80 poin log kali seratus. Perubahan log bukan persentase perubahan surplus dolar. Band bersifat pointwise dan belum mengoreksi pemilihan lag.

SUMBER DAN REPRODUKSI
Sumber: semua model sensitivitas Stata. Band pointwise nominal 95%; skala vertikal dapat berbeda.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.