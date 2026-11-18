# Tinjauan literatur dan pilihan metode

Haikal, 16 Nov 2026. Hasil estimasinya ada di [2_hasil_ardl.md](2_hasil_ardl.md) dan [3_hasil_lp.md](3_hasil_lp.md).

Isi:
1. Teori
2. Mengapa ARDL dominan
3. Kelemahan ARDL
4. Apakah ARDL terbaik?
5. Local projections
6. Kenapa LP cocok di sini
7. Referensi

## 1. Kerangka teori yang diuji

- **Kondisi Marshall-Lerner:** depresiasi riil memperbaiki trade balance dalam jangka panjang bila jumlah elastisitas harga ekspor dan impor (absolut) > 1.
- **J-curve** (Magee 1973): dalam jangka pendek trade balance justru memburuk. Volume masih terkunci kontrak, sementara harga impor dalam rupiah langsung naik. Setelah volume menyesuaikan, trade balance membaik. Rose & Yellen (1989) dan Bahmani-Oskooee & Ratha (2004) mendefinisikan J-curve secara empiris sebagai **efek jangka pendek negatif yang diikuti efek jangka panjang positif dan signifikan**.
- **Dominant currency paradigm** (Gopinath et al. 2020): bila perdagangan diinvoice dalam USD, depresiasi terhadap USD menaikkan harga impor dalam rupiah, tetapi tidak membuat ekspor Indonesia lebih murah di mata pembeli, karena harganya sudah dalam USD. Akibatnya efek perbaikan lewat ekspor lemah. Ini relevan untuk komoditas Indonesia (batu bara, CPO, nikel) yang harganya ditentukan di pasar dunia dalam USD.

## 2. Mengapa ARDL dominan di literatur J-curve

Sejak Bahmani-Oskooee & Brooks (1999), sebagian besar studi J-curve memakai ARDL / bounds testing (Pesaran, Shin & Smith 2001). Survei Bahmani-Oskooee & Ratha (2004) dan Bahmani-Oskooee & Hegerty (2010) memperlihatkan alasannya:

1. **Variabel campuran I(0)/I(1) bisa dipakai.** Data kita memang campuran. ADF/PP menunjukkan ln(X/M) dan IPI mitra I(0), sedangkan ln REER, ln JISDOR dan harga komoditas I(1). Tidak ada yang I(2) (`output/0_deskriptif/unitroot.csv`). Johansen mensyaratkan semua I(1). Engle-Granger lemah di sampel kecil.
2. **Jangka pendek dan jangka panjang dalam satu persamaan.** Koefisien ΔREER (jangka pendek) dan koefisien LR langsung menguji J-curve.
3. **Sampel terbatas tetap bisa diuji**, dengan nilai kritis finite-sample (Narayan 2005; Kripfganz & Schneider 2020). Paket Stata `ardl` (Kripfganz & Schneider 2023) yang kita pakai sudah menghitung p-value-nya.
4. **Bisa dipecah menjadi NARDL** (Shin, Yu & Greenwood-Nimmo 2014) untuk menguji asimetri depresiasi vs apresiasi. Bahmani-Oskooee & Fariditavana (2016) menunjukkan NARDL lebih sering menemukan J-curve dibanding ARDL linear.

**Studi Indonesia** juga hampir semuanya memakai ARDL/NARDL:
- Bahmani-Oskooee & Harvey (2009): ARDL bilateral untuk 13 mitra. J-curve ditemukan pada 5 mitra.
- Bahmani-Oskooee & Harvey (2019): NARDL bilateral. Asimetri jangka pendek ditemukan di hampir semua mitra, dan asimetri jangka panjang di 5 mitra.
- Rifami & Heriqbaldi (2023): Indonesia–China per industri. J-curve ditemukan di 2 industri dengan ARDL dan 9 industri dengan NARDL.

Pola umumnya: **hasil sangat tergantung mitra dan sektor, dan agregasi menyembunyikan efek** (aggregation bias). Inilah alasan RQ2 dan RQ3.

## 3. Kelemahan ARDL (dan relevansinya untuk data kita)

| Kelemahan | Relevansi di sini | Alternatif / perbaikan |
|:--|:--|:--|
| Persamaan tunggal: REER diasumsikan eksogen lemah (tidak ada umpan balik TB → kurs) | **Tinggi.** Rupiah dan neraca dagang sama-sama digerakkan siklus komoditas. Rupiah cenderung melemah saat harga komoditas jatuh, sehingga koefisien REER bisa tertular efek komoditas. | LP panel dengan FE waktu (sudah, §5); VAR struktural; LP-IV |
| Linear dan simetris | Sedang. Sudah diuji dengan NARDL: simetri tidak ditolak. | NARDL (sudah) |
| Hanya satu vektor kointegrasi | Rendah (3 regresor) | Johansen bila semua I(1) |
| Peka terhadap pilihan lag (AIC vs BIC) | Sedang. Pola lag AIC dan BIC berbeda, tetapi kesimpulannya sama. | 10 spesifikasi dilaporkan (`output/1_ardl/ardl_agregat.csv`) |
| Bounds test "degenerate" bila variabel dependen sendiri I(0) | **Tinggi.** ln(X/M) stasioner, sehingga uji t pada ECM hampir otomatis signifikan. | McNown, Sam & Goh (2018); baca lewat dynamic multiplier / LP |
| Dynamic multiplier tanpa selang kepercayaan | Sedang | LP memberi CI per horizon (sudah) |
| Panel mitra: REER sama untuk semua mitra, sehingga ada cross-sectional dependence | **Tinggi** untuk RQ2 | Kurs riil bilateral + FE waktu (sudah, LP); CS-ARDL (Chudik & Pesaran 2015) |

## 4. Apakah ARDL metode terbaik?

**ARDL bukan satu-satunya metode yang benar, tetapi pilihan baseline yang tepat** untuk pertanyaan ini. Alasannya: ARDL standar literatur J-curve (jadi hasil kita sebanding dengan studi Indonesia sebelumnya), cocok untuk campuran I(0)/I(1), dan langsung memisahkan efek jangka pendek dari jangka panjang.

Supaya kesimpulannya kuat, ARDL perlu dilengkapi:
- NARDL untuk asimetri (sudah);
- panel MG/PMG (sudah; Hausman menolak PMG);
- **local projections dengan kurs riil bilateral** sebagai cek endogenitas (sudah, §5–6).

Perbaikan data yang tersisa:
- pendapatan domestik Indonesia untuk model agregat;
- harga komoditas spesifik (batu bara, CPO, nikel);
- data volume ekspor/impor.

## 5. Local projections (LP)

**Apa itu LP.** Jordà (2005) memperkenalkan cara mengestimasi impulse response secara langsung: untuk setiap horizon *h*, regresikan y_{t+h} − y_{t−1} pada guncangan di *t* plus kontrol. Koefisiennya langsung menjadi respons di bulan ke-*h*. Berbeda dengan ARDL/VAR, respons ini tidak diturunkan dari satu model dinamis yang lalu diekstrapolasi.

**LP vs VAR/ARDL.**
- Secara populasi, LP dan VAR mengestimasi impulse response yang sama (Plagborg-Møller & Wolf 2021). Perbedaannya ada di sifat sampel terbatas: LP bias lebih kecil tapi varians lebih besar.
- Simulasi Li, Plagborg-Møller & Wolf (2024) menemukan LP unggul soal bias, sedangkan VAR unggul soal presisi. Herbst & Johannsen (2024) menunjukkan LP bisa bias di sampel kecil.
- Konsekuensinya: LP dipakai **bersama** ARDL, tidak menggantikannya. Kalau keduanya sepakat, kesimpulannya kuat.

**Inferensi.** Montiel Olea & Plagborg-Møller (2021) menunjukkan bahwa dengan *lag augmentation* (menambahkan lag variabel ke regresi), inferensi LP valid untuk data stasioner maupun persisten dan di horizon panjang. Kita tetap memakai SE Newey-West/Driscoll-Kraay (Driscoll & Kraay 1998; Hoechle 2007) supaya konservatif.

**LP-IV.** Stock & Watson (2018) membahas LP dengan instrumen eksternal untuk efek kausal dinamis. Ramey (2016) mengulas literatur guncangan makro dan propagasinya.

**Aplikasi kurs dan perdagangan.**
- IMF (2015, WEO Okt-2015 Bab 3) memakai LP dalam analisis episode depresiasi besar. Temuannya: depresiasi riil efektif 10% rata-rata menaikkan ekspor neto riil sekitar 1,5% PDB.
- Kami belum menemukan studi LP panel yang khusus menguji J-curve untuk Indonesia. Ini bisa jadi kontribusi.

## 6. Kenapa LP cocok di sini

- **Respons per horizon lengkap dengan CI.** J-curve pada dasarnya bentuk impulse response, dan LP memberi selang kepercayaan di setiap bulan.
- **Tidak memaksa satu hubungan jangka panjang.** Ini penting karena ln(X/M) stasioner.
- **Bisa dibawa ke panel dengan FE waktu.** Dengan kurs riil **bilateral**, FE waktu menyerap siklus komoditas, permintaan domestik, dan pelemahan rupiah yang umum. Ini mengatasi kelemahan utama ARDL di §3.
- **Batasnya ("missing intercept"):** panel dengan FE waktu hanya mengidentifikasi efek **relatif** antar mitra, bukan efek agregat. Karena itu RQ1 tetap dijawab dengan LP time series.

## 7. Referensi

- Backus, D.K., Kehoe, P.J., & Kydland, F.E. (1994). Dynamics of the trade balance and the terms of trade: the J-curve? *American Economic Review*, 84(1), 84–103.
- Bahmani-Oskooee, M., & Brooks, T.J. (1999). Bilateral J-curve between US and her trading partners. *Weltwirtschaftliches Archiv*, 135(1), 156–165.
- Bahmani-Oskooee, M., & Fariditavana, H. (2016). Nonlinear ARDL approach and the J-curve phenomenon. *Open Economies Review*, 27(1), 51–70.
- Bahmani-Oskooee, M., & Harvey, H. (2009). The J-curve: Indonesia vs. her major trading partners. *Journal of Economic Integration*, 24(4), 765–777.
- Bahmani-Oskooee, M., & Harvey, H. (2019). The J-curve and bilateral trade balances of Indonesia with its major partners: are there asymmetric effects? *New Zealand Economic Papers*, 53(1), 63–76.
- Bahmani-Oskooee, M., & Hegerty, S.W. (2010). The J- and S-curves: a survey of the recent literature. *Journal of Economic Studies*, 37(6), 580–596.
- Bahmani-Oskooee, M., & Ratha, A. (2004). The J-curve: a literature review. *Applied Economics*, 36(13), 1377–1398.
- Chudik, A., & Pesaran, M.H. (2015). Common correlated effects estimation of heterogeneous dynamic panel data models with weakly exogenous regressors. *Journal of Econometrics*, 188(2), 393–420.
- Driscoll, J.C., & Kraay, A.C. (1998). Consistent covariance matrix estimation with spatially dependent panel data. *Review of Economics and Statistics*, 80(4), 549–560.
- Gopinath, G., Boz, E., Casas, C., Díez, F.J., Gourinchas, P.-O., & Plagborg-Møller, M. (2020). Dominant currency paradigm. *American Economic Review*, 110(3), 677–719.
- Herbst, E.P., & Johannsen, B.K. (2024). Bias in local projections. *Journal of Econometrics*, 240(1), 105655.
- Hoechle, D. (2007). Robust standard errors for panel regressions with cross-sectional dependence. *Stata Journal*, 7(3), 281–312.
- IMF (2015). Exchange rates and trade flows: disconnected? *World Economic Outlook*, Oktober 2015, Bab 3 (Leigh et al.).
- Jordà, Ò. (2005). Estimation and inference of impulse responses by local projections. *American Economic Review*, 95(1), 161–182.
- Kripfganz, S., & Schneider, D.C. (2020). Response surface regressions for critical value bounds and approximate p-values in equilibrium correction models. *Oxford Bulletin of Economics and Statistics*, 82(6), 1456–1481.
- Kripfganz, S., & Schneider, D.C. (2023). ardl: Estimating autoregressive distributed lag and equilibrium correction models. *Stata Journal*, 23(4), 983–1019.
- Li, D., Plagborg-Møller, M., & Wolf, C.K. (2024). Local projections vs. VARs: lessons from thousands of DGPs. *Journal of Econometrics*, 244(2), 105722.
- Magee, S.P. (1973). Currency contracts, pass-through, and devaluation. *Brookings Papers on Economic Activity*, 1973(1), 303–325.
- McNown, R., Sam, C.Y., & Goh, S.K. (2018). Bootstrapping the autoregressive distributed lag test for cointegration. *Applied Economics*, 50(13), 1509–1521.
- Montiel Olea, J.L., & Plagborg-Møller, M. (2021). Local projection inference is simpler and more robust than you think. *Econometrica*, 89(4), 1789–1823.
- Narayan, P.K. (2005). The saving and investment nexus for China: evidence from cointegration tests. *Applied Economics*, 37(17), 1979–1990.
- Pesaran, M.H., Shin, Y., & Smith, R.P. (1999). Pooled mean group estimation of dynamic heterogeneous panels. *Journal of the American Statistical Association*, 94(446), 621–634.
- Pesaran, M.H., Shin, Y., & Smith, R.J. (2001). Bounds testing approaches to the analysis of level relationships. *Journal of Applied Econometrics*, 16(3), 289–326.
- Plagborg-Møller, M., & Wolf, C.K. (2021). Local projections and VARs estimate the same impulse responses. *Econometrica*, 89(2), 955–980.
- Ramey, V.A. (2016). Macroeconomic shocks and their propagation. Dalam *Handbook of Macroeconomics*, Vol. 2A, 71–162. Elsevier.
- Rifami, & Heriqbaldi, U. (2023). Exchange rate and Indonesia-China bilateral industry trade flows: J-curve and asymmetric effects. *Iranian Economic Review*. (cek volume/halaman sebelum dikutip)
- Rose, A.K., & Yellen, J.L. (1989). Is there a J-curve? *Journal of Monetary Economics*, 24(1), 53–68.
- Shin, Y., Yu, B., & Greenwood-Nimmo, M. (2014). Modelling asymmetric cointegration and dynamic multipliers in a nonlinear ARDL framework. Dalam R. Sickles & W. Horrace (Eds.), *Festschrift in Honor of Peter Schmidt* (pp. 281–314). Springer.
- Stock, J.H., & Watson, M.W. (2018). Identification and estimation of dynamic causal effects in macroeconomics using external instruments. *Economic Journal*, 128(610), 917–948.

**Catatan verifikasi** (16 Nov 2026):
- Sudah dicek lewat RePEc, EconBiz atau situs penerbit: Bahmani-Oskooee & Harvey (2009, 2019), Rifami & Heriqbaldi (2023), Bahmani-Oskooee & Hegerty (2010), Montiel Olea & Plagborg-Møller (2021), Plagborg-Møller & Wolf (2021), IMF WEO 2015 Bab 3. Studi Indonesia baru dicek dari abstraknya, bukan teks lengkap.
- Perlu dicek ulang volume/halamannya sebelum masuk draft: Rifami & Heriqbaldi (2023), Li et al. (2024), Herbst & Johannsen (2024). Referensi lainnya adalah karya standar, tapi tetap cek sebelum dikutip.
