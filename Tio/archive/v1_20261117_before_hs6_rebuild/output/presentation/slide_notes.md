## 01. Depresiasi Rupiah dan Neraca Perdagangan Indonesia

Depresiasi Rupiah dan Neraca Perdagangan Indonesia

Deck membahas bukti awal dan batas interpretasinya. Identitas visual, foto cover, logo, master, layout dan tema mengikuti benchmark pengguna. Penyusunan isi: proyek Tio; bukan klaim pengesahan institusional.

SUMBER DAN REPRODUKSI
notes/hasil_ardl_nardl_oskooee.md; template PPT benchmark pengguna.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 02. Apakah depresiasi selalu memperbaiki perdagangan Indonesia?

Apakah depresiasi selalu memperbaiki perdagangan Indonesia?

Hipotesis awal pengguna menyangkut ekspor. Estimasi replikasi saat ini menggunakan rasio impor/ekspor, sehingga kesimpulan dibatasi pada trade balance. Kanal input impor dan TiVA ditangguhkan.

SUMBER DAN REPRODUKSI
Hasil estimasi Stata dan pengolahan dataset proyek Tio.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 03. Perdagangan Indonesia meningkat, dengan dinamika ekspor dan impor berbeda

Perdagangan Indonesia meningkat, dengan dinamika ekspor dan impor berbeda

Angka tahunan dijumlahkan hanya bila empat kuartal lengkap. Tahun 2026 tidak ditampilkan sebagai satu tahun penuh. Periode 2006–2009 tidak dipakai dalam grafik utama karena audit ketidakselarasan sumber.

SUMBER DAN REPRODUKSI
Sumber: World Bank GEM; intermediate/Panel_World_Quarter.csv. USD ribu dikonversi menjadi USD miliar.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 04. Sepuluh mitra memiliki skala dan posisi perdagangan yang berbeda

Sepuluh mitra memiliki skala dan posisi perdagangan yang berbeda

Pangsa pada panel kanan menggunakan total ekspor ke sepuluh mitra sebagai penyebut, bukan total ekspor Indonesia ke dunia. Tidak mengklaim pemeringkatan top ten dunia terbaru. Data perdagangan dapat berbeda vintage dengan GEM.

SUMBER DAN REPRODUKSI
Sumber: panel bilateral proyek Tio (Trade Map/CEIC asal); Panel_Country_Quarter.csv.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 05. Komoditas mencakup 49,5% ekspor pada sampel sepuluh mitra tahun 2025

Komoditas mencakup 49,5% ekspor pada sampel sepuluh mitra tahun 2025

Empat kategori dipertahankan dalam penyebut: komoditas, nonkomoditas, mixed, unclassified. Model biner hanya memakai dua kategori pertama. Statistik ini khusus sepuluh mitra pada 2025; bukan dunia dan bukan angka gabungan seluruh tahun.

SUMBER DAN REPRODUKSI
Sumber: HS4_Commodity_Classification.csv dan Panel_CommodityGroup_Country_Quarter.csv; pengolahan Tio.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 06. Variabel utama mengikuti spesifikasi trade balance dalam paper

Variabel utama mengikuti spesifikasi trade balance dalam paper

Perdagangan nominal digunakan sebagai rasio M/X. GDP adalah log indeks level riil, bukan pertumbuhan GDP. Kurs riil bilateral semula naik berarti depresiasi sehingga q dibalik tanda. CPI berfungsi membangun kurs riil; bukan regressor tambahan terpisah.

SUMBER DAN REPRODUKSI
Sumber: Bahmani-Oskooee & Fariditavana (2015/2016), DOI 10.1007/s11079-015-9369-5; skrip 12–13.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 07. Statistik deskriptif memakai sampel estimasi agregat yang sama

Statistik deskriptif memakai sampel estimasi agregat yang sama

Tanggal dipilih dari desain estimasi Stata, lalu dicocokkan dengan panel dunia. Tidak menggunakan seluruh 4.388 baris dataset analisis yang mencakup pengulangan seri/skenario. Indeks PDB berbasis rata-rata 2015; basis REER mengikuti BIS.

SUMBER DAN REPRODUKSI
Sumber: WORLD_NARDL_AIC4_design.dta dan Panel_World_Quarter.csv; simpangan baku sampel (N − 1).

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 08. Ketersediaan data membatasi kesetaraan sampel antarmitra

Ketersediaan data membatasi kesetaraan sampel antarmitra

Grafik menunjukkan window tersedia, bukan window estimasi setelah empat lag. India CPI baseline dimulai 2013. AS berhenti 2025Q3 karena CPI Oktober kosong; Vietnam berhenti 2025Q2 karena BIS FX Agustus kosong. Data tidak dirapatkan melewati celah.

SUMBER DAN REPRODUKSI
Sumber: output/diagnostics/oskooee/case_registry.csv; audit_validitas_data_macro.md.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 09. Dua mekanisme memberi arah respons yang perlu diuji

Dua mekanisme memberi arah respons yang perlu diuji

Kanal daya saing dan harga komoditas ditampilkan sebagai hipotesis, bukan mekanisme kausal teridentifikasi. Mengontrol BCOM saja tidak mengidentifikasi penuh pengaruh harga global. Kanal input impor secara eksplisit ditangguhkan.

SUMBER DAN REPRODUKSI
Sumber: kerangka penelitian Tio dan spesifikasi paper replikasi; harga BCOM sebagai kontrol sensitivitas.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 10. ARDL menghubungkan dinamika jangka pendek dan hubungan level

ARDL menghubungkan dinamika jangka pendek dan hubungan level

Persamaan disajikan dalam bentuk UECM. z terdiri dari yd, yf, dan q; untuk sensitivitas harga ditambahkan cp. Batas lag utama empat lag ARDL levels setara maksimum tiga lag first difference ECM. Ini berbeda dari paper yang memiliki sampel lebih panjang dan delapan lag first difference.

SUMBER DAN REPRODUKSI
Sumber: paper replikasi DOI 10.1007/s11079-015-9369-5; 13_run_oskooee_models.do.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 11. NARDL memisahkan apresiasi dan depresiasi secara eksplisit

NARDL memisahkan apresiasi dan depresiasi secara eksplisit

POS_t = jumlah max(Δq,0); NEG_t = jumlah min(Δq,0). Koefisien NEG positif dikalikan depresiasi negatif menurunkan y, sehingga trade balance membaik. Wald menguji LR_POS = LR_NEG, bukan koefisien bertanda berlawanan. Ketika bounds tidak mendukung, Wald signifikan tidak membuktikan asimetri jangka panjang yang mapan.

SUMBER DAN REPRODUKSI
Sumber: paper replikasi; notes/hasil_ardl_nardl_oskooee.md; definisi variabel dalam skrip 12.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 12. Estimasi mencakup 62 model utama dan 112 model sensitivitas

Estimasi mencakup 62 model utama dan 112 model sensitivitas

Model utama: dunia 2, bilateral 20, jenis barang 40. Sensitivitas: cap lag dua sebanyak 62, BCOM 40, GEM FX 6, India WPI 2, dunia 2006+ 2. HS4 hanya disaring; 2.115 dari 12.214 seri memenuhi kriteria awal, bukan telah diestimasi.

SUMBER DAN REPRODUKSI
Sumber: results_primary_models.csv; results_all_models.csv; analysis_validation_report.json.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 13. Hubungan jangka panjang dinilai melalui beberapa tahap pemeriksaan

Hubungan jangka panjang dinilai melalui beberapa tahap pemeriksaan

Bounds case III dengan critical values finite sample, keputusan F dan t bersama. Levels_supported5 juga memeriksa joint-X, akar AR, risiko I(2), residual df. Diagnostic_clean5 merupakan flag gabungan tidak ditolak pada uji yang dicantumkan. Tidak menolak diagnostik bukan bukti model benar.

SUMBER DAN REPRODUKSI
Sumber: ardl 1.0.6; Kripfganz–Schneider; diagnostic_summary.csv; independent_OLS_checks.csv.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 14. Agregat dunia belum mendukung hubungan level pada taraf 5%

Agregat dunia belum mendukung hubungan level pada taraf 5%

ARDL F=2.3606 dan t=-2.1556; NARDL F=3.8237 dan t=-2.7126. Kedua keputusan gabungan F/t adalah No rejection, bukan dukungan levels 5%. Wald asimetri p=0.00718 adalah nominal. NARDL CUSUMSQ p MC=0.0126. Jangan menyimpulkan depresiasi selalu memperbaiki/memperburuk neraca agregat.

SUMBER DAN REPRODUKSI
Sumber: results_primary_models.csv, WORLD_ARDL_AIC4 dan WORLD_NARDL_AIC4.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 15. Respons dinamis agregat perlu dibaca bersama batas modelnya

Respons dinamis agregat perlu dibaca bersama batas modelnya

Shock -ln(1.10) merupakan kebalikan dari faktor apresiasi 1.10; bukan persis penurunan indeks 10%. Respons ditampilkan dalam 100 x log-point, bukan persen perubahan ekspor. Model tidak memiliki dukungan levels 5% dan terdapat CUSUMSQ instability, sehingga pola tidak diklaim sebagai bukti J-curve.

SUMBER DAN REPRODUKSI
Sumber: dynamic_multipliers.csv, WORLD_NARDL_AIC4. Interval delta-method, bersyarat pada lag terpilih.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 16. Bukti bilateral bervariasi; dukungan paling jelas muncul pada Australia

Bukti bilateral bervariasi; dukungan paling jelas muncul pada Australia

Interval ditampilkan pula untuk model tanpa dukungan levels agar pelaporan lengkap; koefisien tersebut tidak diartikan sebagai LR mapan. Australia dan Malaysia lolos levels+diagnostik. Malaysia p BH=0.0591; Australia=0.00399. Thailand levels didukung tetapi diagnostik ditolak. Sampel tidak identik.

SUMBER DAN REPRODUKSI
Sumber: results_primary_models.csv. Cokelat = levels + diagnostik; jingga = levels; kosong = levels belum didukung.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 17. Australia menunjukkan arah perbaikan dengan dukungan diagnostik lebih kuat

Australia menunjukkan arah perbaikan dengan dukungan diagnostik lebih kuat

LR NEG=3.3560, interval95 [1.5631,5.1490], p nominal0.000399, p BH0.003990. Lolos levels dan flag diagnostik. Hasil bersyarat sumber GDP/CPI, termasuk interpolasi CPI Australia oleh penyedia. Bukti kasus ini tidak digeneralisasi ke seluruh perdagangan Indonesia.

SUMBER DAN REPRODUKSI
Sumber: BIL_AUS_NARDL_AIC4; results_primary_models.csv dan dynamic_multipliers.csv.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 18. Komoditas: arah koefisien berbeda dan ketidakpastian tetap besar

Komoditas: arah koefisien berbeda dan ketidakpastian tetap besar

Tujuh dari sepuluh model komoditas NARDL mendapat levels supported; hanya AUS, IND, MYS juga lolos diagnostik. Koefisien NEG ketiganya tidak signifikan nominal5%. CHN negatif signifikan tetapi diagnostik ditolak. Tidak menafsirkan koefisien tidak signifikan sebagai nol atau bukti dominasi harga global.

SUMBER DAN REPRODUKSI
Sumber: results_primary_models.csv, TYPE_*_commodity_NARDL_AIC4. Legenda status sama dengan grafik bilateral.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 19. Nonkomoditas belum memperoleh dukungan hubungan level pada 5%

Nonkomoditas belum memperoleh dukungan hubungan level pada 5%

Tidak ada model utama nonkomoditas ARDL/NARDL yang lolos flag levels supported5. Interval nominal yang tidak meliputi nol pada beberapa NARDL tidak mengatasi kegagalan dukungan levels. Tidak signifikan bukan bukti komoditas/nonkomoditas sama, dan beda signifikansi bukan uji beda koefisien antarkelompok.

SUMBER DAN REPRODUKSI
Sumber: results_primary_models.csv, TYPE_*_noncommodity_NARDL_AIC4. Simbol kosong = levels belum didukung.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 20. Penyaringan mempersempit jumlah model yang layak dibaca lebih jauh

Penyaringan mempersempit jumlah model yang layak dibaca lebih jauh

27 menolak no-level relation lewat keputusan F/t5. 18 lolos syarat levels tambahan. 7 juga lolos seluruh flag diagnostik yang tercantum. Tiga dari tujuh memiliki p BH koefisien depresiasi <5%: BIL_AUS_ARDL, BIL_AUS_NARDL, TYPE_AUS_commodity_ARDL. Dua estimator pada seri sama bukan bukti independen.

SUMBER DAN REPRODUKSI
Sumber: results_primary_models.csv. Flag gabungan adalah alat penyaringan, bukan jaminan model benar.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 21. Diagnostik mengingatkan bahwa inferensi OLS perlu kehati-hatian

Diagnostik mengingatkan bahwa inferensi OLS perlu kehati-hatian

BG4=12, BP=14, RESET=11, JB=12, ARCH4=5, CUSUMSQ=19. Penolakan diagnostik bukan kepastian salah model, namun p-value OLS klasik tidak boleh diperlakukan kuat. Tidak ada model utama ditandai I2 belum disingkirkan; daya uji sampel pendek tetap terbatas.

SUMBER DAN REPRODUKSI
Sumber: diagnostic_summary.csv. CUSUMSQ menggunakan 19.999 simulasi referensi Gaussian dengan seed tetap.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 22. Hasil peka terhadap panjang lag dan kontrol harga komoditas

Hasil peka terhadap panjang lag dan kontrol harga komoditas

Tabulasi menggunakan jumlah Levels_supported5 dan gabungan dengan Diagnostic_clean5, bukan clean saja. Model PRICE_IND_commodity_NARDL_AIC4 N49/K25 tidak memiliki critical values finite-sample, sehingga ditandai unavailable. Kesamaan jumlah dukungan tidak berarti koefisien identik atau mekanisme harga teridentifikasi.

SUMBER DAN REPRODUKSI
Sumber: results_all_models.csv. AIC antarcap memiliki N efektif berbeda; tidak dibandingkan secara langsung.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 23. Kesimpulan awal: manfaat depresiasi belum dapat digeneralisasi

Kesimpulan awal: manfaat depresiasi belum dapat digeneralisasi

Hindari klaim hipotesis terbukti, efek nol, efek kausal ekspor, atau komoditas pasti kurang sensitif. Bukti terkuat tersaring terdapat pada Australia; agregat belum didukung. Bukti negatif yang tidak signifikan bukan bukti kerugian. Model bilateral bersampel berbeda.

SUMBER DAN REPRODUKSI
Sumber: sintesis 62 model utama, 112 sensitivitas dan catatan audit data Tio.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 24. Prioritas lanjutan: perkuat data dan uji perbedaan secara langsung

Prioritas lanjutan: perkuat data dan uji perbedaan secara langsung

Usulan ini merupakan agenda, belum dilaksanakan dalam run saat ini. Hipotesis input impor/TiVA tetap on hold. HS4 pre-eligible bukan jaminan dapat diestimasi. Ekspor nominal dan volume membutuhkan pembedaan serta deflator yang tepat.

SUMBER DAN REPRODUKSI
Sumber: notes/hasil_ardl_nardl_oskooee.md; audit_validitas_data_macro.md; kelayakan awal HS-4.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 25. Lampiran

Lampiran

Rincian untuk pemeriksaan dan reproduksi hasil.

SUMBER DAN REPRODUKSI
Output model dan manifest sumber di proyek Tio.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 26. Lampiran | NARDL bilateral: koefisien dan status interpretasi

Lampiran | NARDL bilateral: koefisien dan status interpretasi

Status levels supported memasukkan bounds F/t dan syarat tambahan, bukan F saja. Diagnostic flag tidak ditolak bukan jaminan model benar. Koefisien tanpa levels support belum diartikan sebagai hubungan LR mapan.

SUMBER DAN REPRODUKSI
Sumber: results_primary_models.csv. ✓ = terpenuhi / tidak ditolak; — = belum. Interval dan p-value nominal.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 27. Lampiran | NARDL komoditas: koefisien dan status interpretasi

Lampiran | NARDL komoditas: koefisien dan status interpretasi

Perbandingan dua tabel kelompok bukan uji statistik beda koefisien antarkelompok. Koefisien tanpa levels support belum layak diartikan sebagai hubungan LR mapan.

SUMBER DAN REPRODUKSI
Sumber: results_primary_models.csv. ✓ = terpenuhi / tidak ditolak; — = belum; p-value setelah seleksi AIC.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 28. Lampiran | NARDL nonkomoditas: koefisien dan status interpretasi

Lampiran | NARDL nonkomoditas: koefisien dan status interpretasi

Perbandingan dua tabel kelompok bukan uji statistik beda koefisien antarkelompok. Koefisien tanpa levels support belum layak diartikan sebagai hubungan LR mapan.

SUMBER DAN REPRODUKSI
Sumber: results_primary_models.csv. ✓ = terpenuhi / tidak ditolak; — = belum; p-value setelah seleksi AIC.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 29. Lampiran | ARDL linear melengkapi pembacaan model nonlinear

Lampiran | ARDL linear melengkapi pembacaan model nonlinear

ARDL linear memaksakan respons simetris. Tabel memungkinkan pembaca menilai apakah pembacaan berbeda dengan NARDL. Perbedaan estimator pada sampel sama bukan observasi independen.

SUMBER DAN REPRODUKSI
Sumber: results_primary_models.csv, BIL_*_ARDL_AIC4. p BH dalam 10 model ARDL bilateral.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 30. Lampiran | Statistik variabel hasil transformasi pada sampel agregat

Lampiran | Statistik variabel hasil transformasi pada sampel agregat

Mean dan SD adalah statistik sampel hasil transformasi yang benar-benar masuk model. NEG tidak diubah menjadi besaran positif. Konstanta dapat menyerap perubahan basis indeks atau titik awal kumulatif; slope tetap dibaca sesuai definisi q.

SUMBER DAN REPRODUKSI
Sumber: output/diagnostics/oskooee/models/WORLD_NARDL_AIC4_design.dta.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 31. Lampiran | Stabilitas dunia dan Australia memberi hasil berbeda

Lampiran | Stabilitas dunia dan Australia memberi hasil berbeda

Dunia NARDL p MC=0.0126. Australia NARDL tidak menolak stabilitas dalam flag gabungan. CUSUM memakai implementasi resmi Stata dan telah dicocokkan dengan konstruksi independen; CUSUMSQ dihitung melalui simulasi referensi dengan seed tetap.

SUMBER DAN REPRODUKSI
Sumber: stability_paths.csv; diagnostic_summary.csv. Band Monte Carlo aproksimasi, bukan tabel persis paper.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 32. Lampiran | Catatan data yang memengaruhi pembacaan hasil

Lampiran | Catatan data yang memengaruhi pembacaan hasil

Selisih impor GEM vs WDI 2006 maksimum24.283%. World start2010. CPI Australia interpolasi penyedia. India CPI mulai2013; WPI sensitivity terpisah. USA CPI October2025 missing dan VNM FX August2025 missing. Raw perdagangan asal CEIC/ITC tidak berada di Tio; checksum memastikan tidak berubah, bukan validasi penuh ke sumber asal.

SUMBER DAN REPRODUKSI
Sumber: audit_validitas_data_macro.md; sumber_data_macro_dan_merge.md; hasil_ardl_nardl_oskooee.md.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 33. Lampiran | Peta sumber dan konstruksi variabel

Lampiran | Peta sumber dan konstruksi variabel

Investing.com tidak berhasil diunduh (403); kurs yang dipakai berasal dari BIS, dengan GEM sebagai sensitivitas terpisah. Tidak ada klaim menggunakan data Investing. Data harga BCOM berasal dari workbook pengguna; transformasi dan audit dicatat dalam data_komoditas_den.md.

SUMBER DAN REPRODUKSI
Sumber: Macro_Source_Manifest.csv; download_manifest.json; catatan audit; klasifikasi HS-4; workbook harga pengguna.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 34. Lampiran | Hasil dapat dilacak ke data, kode, dan diagnostik

Lampiran | Hasil dapat dilacak ke data, kode, dan diagnostik

Deck dibangun dari keluaran penelitian yang sudah divalidasi, tanpa mengestimasi ulang. CSV deskriptif dan grafik deck tersimpan di output/presentation/assets. Slide notes menyimpan sumber dan batas interpretasi. PPTX dapat diedit, PDF dan PNG dipakai untuk pemeriksaan visual.

SUMBER DAN REPRODUKSI
Sumber: struktur proyek; master do-file dan wrapper pipeline; delivery_validation.json.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.

## 35. Lampiran | Referensi metodologi utama

Lampiran | Referensi metodologi utama

Paper Bahmani-Oskooee online2015 dan volume jurnal2016. Implementasi ardl dan bounds Kripfganz–Schneider bukan klaim reproduksi persis critical values historis paper. CUSUMSQ aproksimasi MC ditandai. Dokumen audit sumber lokal memuat URL provenance masing-masing respons sumber.

SUMBER DAN REPRODUKSI
Sumber: paper pengguna dan referensi implementasi yang disimpan di input/reference/oskooee_replication/.

Versi hasil: 17 November 2026. Angka berasal dari hasil estimasi yang sudah ada; deck tidak menjalankan ulang model.