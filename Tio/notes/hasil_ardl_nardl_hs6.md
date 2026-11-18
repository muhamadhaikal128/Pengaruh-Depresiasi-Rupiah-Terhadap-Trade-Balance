# Hasil penelitian HS-6: ARDL dan NARDL

Run 17 November 2026. Estimasi dilakukan di Stata; data mentah tidak diedit. Pekerjaan sebelumnya diarsipkan ke `archive/v1_20261117_before_hs6_rebuild/`. Kanal dependensi ekspor terhadap input impor/TiVA dikeluarkan dari run ini.

## Mulai membaca

- [Workbook lengkap](../output/tables/oskooee/Oskooee_Results.xlsx), [ringkasan CSV](../output/tables/oskooee/primary_compact.csv).
- [Master do-file](../script/00_master.do); estimator dibagi menjadi 03 agregat, 04 mitra, 05 kelompok, 06 unit root, dan 07 ekspor. Residual, bounds dan CUSUM berada dalam ardl_helpers.do.
- [Registry sampel](../output/diagnostics/oskooee/case_registry.csv), [diagnostik lengkap](../output/diagnostics/oskooee/diagnostic_summary.csv).
- Tabel koefisien setiap model utama tersedia sebagai PNG/PDF di output/tables/oskooee/. Grafik dinamis, residual dan stabilitas ada di output/figures/oskooee/; versi Stata editable di output/gph/oskooee/.

**176 model utama dan 340 sensitivitas telah diestimasi**, total 516. Model utama: satu agregat dunia, sepuluh bilateral, serta tujuh kelompok untuk dunia dan masing-masing sepuluh mitra; masing-masing ARDL dan NARDL.

## Data dan klasifikasi

Nilai perdagangan bersumber dari 22 workbook Trade Map HS-6 pengguna, Januari 2006–Agustus 2026, satuan USD ribu. Kuartal mensyaratkan tiga bulan lengkap. Kolom TOTAL dipakai untuk agregat/bilateral; kelompok dibentuk dari HS-6. Selisih penjumlahan produk terhadap TOTAL dievaluasi terhadap batas pembulatan per baris, tidak dipaksa nol.

Tujuh kelompok:

| Group | Label | Overlapping |
|---|---|---|
| manufacturing | Non-komoditas (manufaktur) | True |
| consumption | Barang konsumsi | True |
| agriculture | Komoditas pertanian & pangan | True |
| intermediate | Bahan baku/penolong | True |
| capital | Barang modal | True |
| commodity | Komoditas (total) | True |
| energy_mining | Komoditas energi & tambang | True |

Manufaktur nonkomoditas dan kelompok komoditas mengikuti UNCTAD A11 berbasis SITC3. Pertanian/pangan mencakup pangan, minuman, tembakau, minyak nabati serta bahan mentah pertanian; energi/tambang mencakup bahan bakar, mineral/bijih, logam nonferrous dan kategori komoditas mineral terkait pada A11. Barang konsumsi, intermediate dan modal mengikuti dimensi penggunaan SNA pada BEC5. **Kelompok saling tumpang tindih dan tidak boleh dijumlahkan sebagai pangsa total.** Barang modal termasuk ternak pembiakan atau produk investasi lain bila BEC mengklasifikasikannya demikian; bukan hanya mesin.

Workbook tidak menyatakan revisi HS yang digunakan untuk setiap sel. Karena kode lama dan baru muncul dalam satu daftar, klasifikasi utama memakai konsensus konservatif per HS-6 di antara revisi yang relevan pada korespondensi UNSD. Kode yang berubah kelas atau bercampur tetap mixed/unclassified. Ini lebih rinci daripada HS-4, tetapi bukan klaim semua masalah revisi waktu sudah selesai. Lihat output/diagnostics/data/Classification_Coverage.csv. Klasifikasi BEC tidak menunjukkan kandungan input impor eksportir.

## Metode dan interpretasi

Adaptasi Bahmani-Oskooee & Fariditavana, DOI 10.1007/s11079-015-9369-5. Outcome **y=ln(M/X)**, bukan ln(X−M) dan bukan persamaan ekspor tersendiri. X−M tetap dipakai untuk statistik deskriptif. q naik=apresiasi; untuk bilateral tanda log RER dibalik. NARDL memisahkan POS dan NEG. NEG merupakan akumulasi perubahan negatif; koefisien NEG positif menunjukkan arah perbaikan neraca ketika depresiasi.

AIC maksimum 4 lag levels, cap 2 sebagai sensitivitas; intercept tanpa tren, ECM t−1. World baseline mulai 2010 untuk mempertahankan pembandingan dengan run sebelumnya; 2006+ sebagai sensitivitas. GDP dalam log indeks level riil, bukan pertumbuhan. Permintaan dunia adalah proksi PDB 10 mitra berbobot ekspor 2006–2008 yang dihitung ulang dari workbook baru, bukan PDB global.

Bounds finite-sample menggunakan F dan t; levels_supported5 juga memeriksa joint-X, akar dinamis, risiko I(2) serta minimal 15 derajat bebas residual. ADF/PP memeriksa level dan first difference. Diagnostik meliputi BG, BP, RESET, JB, ARCH, CUSUM dan CUSUMSQ. CUSUMSQ menggunakan band simultan referensi Gaussian 19.999 simulasi, seed tetap, aproksimasi. Pemeriksaan prediksi OLS independen dan ekuivalensi ECM–levels dilakukan untuk setiap model.

P-value/CI nominal setelah pemilihan AIC. BH merupakan koreksi eksploratif dalam keluarga scope-estimator; bukan koreksi seleksi lag. Model kelompok bertumpang tindih, sehingga tidak menjadi bukti independen. Signifikan pada satu kelompok dan tidak signifikan pada kelompok lain bukan uji beda koefisien.

## Ringkasan hasil

Untuk agregat dunia, ARDL dan NARDL utama belum memenuhi syarat hubungan level pada taraf 5%. Karena itu, tanda atau signifikansi koefisien LR saja belum menjadi kesimpulan jangka panjang.

Pada NARDL bilateral, Australia dan Malaysia lolos penyaringan hubungan level serta diagnostik utama dan mempunyai koefisien NEG positif. Hubungan ini mengarah pada perbaikan neraca saat depresiasi, dengan syarat model yang digunakan. Signifikansi nominal tetap perlu dibaca bersama kolom BH dan hasil sensitivitas; bukan bukti kausal.

Pada tujuh kelompok dunia, tidak ada NARDL yang sekaligus lolos syarat level dan seluruh penyaringan diagnostik. Kelompok konsumsi dan energi/tambang mempunyai dukungan level, tetapi juga catatan diagnostik. Hasil ini belum cukup untuk menyimpulkan bahwa komoditas secara umum tidak sensitif terhadap kurs.

Pada ARDL linier dunia, komoditas total (q = -1,3546) dan energi/tambang (q = -2,0399) lolos penyaringan level serta diagnostik dan mempunyai koefisien q negatif. Dengan q naik berarti apresiasi, tanda ini mengarah pada memburuknya rasio neraca saat depresiasi. Arah negatif bertahan pada cap dua dan kontrol BCOM, tetapi beberapa sensitivitas mempunyai masalah diagnostik. Pada NARDL, koefisien NEG terkait belum signifikan secara nominal dan dukungan model berubah menurut lag. Temuan ini bergantung pada spesifikasi, bukan bukti kausal yang sudah mapan.

Koefisien tidak signifikan tidak membuktikan efek nol. Perbedaan signifikansi antara manufaktur dan komoditas juga bukan uji langsung perbedaan sensitivitas kedua kelompok. Model di sini menguji rasio impor/ekspor, sehingga tidak memisahkan respons ekspor dari respons impor.

| scope | estimator | Models | Levels_supported5 | Diagnostics_clean5 |
|---|---|---|---|---|
| aggregate | ARDL | 1 | 0 | 1 |
| aggregate | NARDL | 1 | 0 | 0 |
| bilateral | ARDL | 10 | 3 | 2 |
| bilateral | NARDL | 10 | 3 | 3 |
| goods | ARDL | 77 | 23 | 27 |
| goods | NARDL | 77 | 33 | 30 |

F/t bounds 5% menolak no-level relation pada **95/176** model; **62/176** lolos syarat tambahan levels; **28/176** juga tidak ditolak dalam flag diagnostik gabungan. Ini penyaringan, bukan sertifikat kebenaran atau identifikasi kausal.

### Indonesia–dunia

| estimator | N | lag_order | lr_q_b | lr_pos_b | lr_neg_b | lr_asym_p | Bounds5 | Diagnostic_Flags |
|---|---|---|---|---|---|---|---|---|
| ARDL | 61 | (2,3,0,4) | 0.4292 |  |  |  | No rejection | No rejection in listed tests |
| NARDL | 61 | (2,0,3,0,4) |  | -2.1422 | 2.5724 | 0.0060 | Inconclusive | CUSUMSQ instability |

### Model dengan dukungan levels dan flag diagnostik lebih mendukung

| model_id | N | lr_q_b | lr_neg_b | Dep_LR_p | Dep_LR_p_BH |
|---|---|---|---|---|---|
| BIL_AUS_ARDL_AIC4 | 77 | 2.0835 |  | 0.0021 | 0.0209 |
| BIL_AUS_NARDL_AIC4 | 77 |  | 3.3560 | 0.0004 | 0.0040 |
| BIL_MYS_NARDL_AIC4 | 78 |  | 1.3461 | 0.0236 | 0.0591 |
| TYPE_AUS_commodity_ARDL_AIC4 | 77 | 1.7010 |  | 0.0082 | 0.1031 |
| TYPE_AUS_commodity_NARDL_AIC4 | 77 |  | 1.3791 | 0.1422 | 0.3318 |
| TYPE_AUS_intermediate_NARDL_AIC4 | 77 |  | 2.5180 | 0.0103 | 0.0527 |
| TYPE_CHN_agriculture_ARDL_AIC4 | 78 | -0.8091 |  | 0.1192 | 0.3072 |
| TYPE_CHN_agriculture_NARDL_AIC4 | 78 |  | -2.0365 | 0.0016 | 0.0148 |
| TYPE_CHN_consumption_NARDL_AIC4 | 78 |  | -2.7105 | 0.0309 | 0.1081 |
| TYPE_IND_commodity_NARDL_AIC4 | 49 |  | -4.5686 | 0.3200 | 0.5029 |
| TYPE_IND_energy_mining_NARDL_AIC4 | 49 |  | -4.5058 | 0.3458 | 0.5257 |
| TYPE_JPN_commodity_NARDL_AIC4 | 78 |  | -0.7102 | 0.4930 | 0.6123 |
| TYPE_JPN_energy_mining_NARDL_AIC4 | 78 |  | -0.1602 | 0.8935 | 0.9453 |
| TYPE_KOR_capital_NARDL_AIC4 | 78 |  | 7.1469 | 0.0271 | 0.1042 |
| TYPE_MYS_capital_ARDL_AIC4 | 78 | 0.1775 |  | 0.7511 | 0.9037 |
| TYPE_MYS_capital_NARDL_AIC4 | 78 |  | 0.7838 | 0.4683 | 0.6102 |
| TYPE_MYS_commodity_ARDL_AIC4 | 78 | -1.2903 |  | 0.0878 | 0.2703 |
| TYPE_MYS_commodity_NARDL_AIC4 | 78 |  | 1.4444 | 0.2577 | 0.4615 |
| TYPE_MYS_energy_mining_ARDL_AIC4 | 78 | -1.3762 |  | 0.1158 | 0.3072 |
| TYPE_MYS_energy_mining_NARDL_AIC4 | 78 |  | 1.1172 | 0.4833 | 0.6102 |
| TYPE_THA_intermediate_ARDL_AIC4 | 78 | 1.0630 |  | 0.0307 | 0.1244 |
| TYPE_THA_intermediate_NARDL_AIC4 | 78 |  | -1.5678 | 0.1245 | 0.3091 |
| TYPE_USA_agriculture_ARDL_AIC4 | 75 | -0.8364 |  | 0.0171 | 0.1194 |
| TYPE_USA_agriculture_NARDL_AIC4 | 75 |  | 0.6216 | 0.2780 | 0.4866 |
| TYPE_USA_consumption_NARDL_AIC4 | 75 |  | 5.8605 | 0.0000 | 0.0027 |
| TYPE_WLD_commodity_ARDL_AIC4 | 61 | -1.3546 |  | 0.0001 | 0.0037 |
| TYPE_WLD_consumption_ARDL_AIC4 | 61 | 2.0258 |  | 0.0305 | 0.1244 |
| TYPE_WLD_energy_mining_ARDL_AIC4 | 61 | -2.0399 |  | 0.0000 | 0.0000 |

Seluruh model tetap dilaporkan, termasuk yang tidak mendukung kointegrasi atau mempunyai masalah diagnostik. Grafik LR untuk model tanpa dukungan levels tidak boleh dipakai sebagai kesimpulan LR yang mapan. Grafik respons tidak otomatis membuktikan J-curve.

## Batas data yang tetap berlaku

- India baseline CPI mulai 2013; WPI hanya sensitivitas terpisah. CPI Australia bulanan berasal dari interpolasi penyedia.
- AS CPI Oktober 2025 dan Vietnam FX Agustus 2025 kosong. Sampel mengikuti rentang lengkap terpanjang; celah tidak dirapatkan.
- GDP sebagian mitra berakhir 2026Q1; proksi permintaan dunia mengikuti batas tersebut. Perbedaan window memengaruhi perbandingan antarmitra.
- Historis GDP Indonesia/India/Vietnam dan konsep FX Thailand/Vietnam mempunyai catatan vintage/sumber. Data Trade Map baru belum direkonsiliasi penuh dengan seri nasional independen; rekonsiliasi HS6 terhadap TOTAL adalah pemeriksaan internal.
- Harga BCOM merupakan kontrol sensitivitas, bukan identifikasi kausal pengaruh harga global.
- File baru berisi nilai perdagangan; run ini tidak menguji ekspor volume atau dependensi input impor.
- Referensi audit lama dipertahankan di input/reference/ dan seluruh keluaran sebelumnya ada di archive/.

## Pemeriksaan CUSUM

Kurva CUSUM utama diekspor langsung melalui opsi generate() pada estat sbcusum, dari UECM dengan lag dan sampel terpilih. Maksimum kurva harus mereproduksi statistik Stata untuk seluruh 176 model utama. [Dokumentasi resmi Stata](https://www.stata.com/manuals/tsestatsbcusum.pdf).

Matriks awal TYPE_AUS_capital_NARDL_AIC4 dan TYPE_AUS_consumption_NARDL_AIC4 belum full rank. Perhitungan independen Python menunda inisialisasi sampai full rank sehingga statistiknya berbeda. Kurva resmi Stata dipertahankan, perbedaan dicatat dalam CUSUM_cross_implementation_check.csv, dan kedua model diberi caveat serta tidak diberi label diagnostik bersih. Pada model dengan matriks awal full rank, kesesuaian independen tetap diwajibkan dengan toleransi numerik.

Run neraca perdagangan ini tidak dengan sendirinya membuktikan hipotesis tentang ekspor saja. Seluruh hasil merupakan asosiasi kondisional; belum mengidentifikasi efek kausal depresiasi.

## Reproduksi

`script/00_run.ps1` menjalankan 01_build_panel.py -> 00_master.do (Stata) -> 06_cusum_paths.do -> 08_report_results.py -> 07_export.do graphs -> 09_validate_results.py. Do-file Stata utama berada langsung di script/; helper Python berada di script/python/. Raw workbook dipertahankan identik dengan file pengguna.

## Bounds finite-sample yang tidak tersedia

Koefisien tetap diestimasi, tetapi critical values bounds finite-sample tidak tersedia pada sensitivitas berikut karena N terlalu kecil relatif terhadap jumlah parameter. Statusnya Unavailable; hasil ini tidak dipakai sebagai dukungan hubungan level.

| Model | N | Parameter | Lag |
|---|---:|---:|---|
| PRICE_IND_commodity_NARDL_AIC4 | 49 | 25 | (4,1,4,2,4,4) |
| PRICE_IND_energy_mining_NARDL_AIC4 | 49 | 27 | (3,3,4,4,4,3) |
| PRICE_IND_intermediate_NARDL_AIC4 | 49 | 25 | (4,4,1,3,3,4) |

Perdagangan bernilai nominal dan belum disesuaikan musiman. Run ini menguji arah/level kurs; tidak ada variabel volatilitas kurs terpisah.
