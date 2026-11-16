# Tinjauan literatur: apakah ARDL metode terbaik?

Disusun 16 Nov 2026 (Haikal). Dipakai bersama [hasil_rq.md](hasil_rq.md).

## 1. Kerangka teori yang diuji

- **Kondisi Marshall-Lerner:** depresiasi riil memperbaiki trade balance dalam jangka panjang bila jumlah elastisitas harga ekspor dan impor (absolut) > 1.
- **J-curve** (Magee 1973): dalam jangka pendek trade balance justru memburuk. Volume masih terkunci kontrak, sementara harga impor dalam rupiah langsung naik. Setelah volume menyesuaikan, trade balance membaik. Rose & Yellen (1989) dan Bahmani-Oskooee & Ratha (2004) mendefinisikan J-curve secara empiris sebagai **efek jangka pendek negatif yang diikuti efek jangka panjang positif dan signifikan**.
- **Dominant currency paradigm** (Gopinath et al. 2020): bila perdagangan diinvoice dalam USD, depresiasi terhadap USD menaikkan harga impor dalam rupiah, tetapi tidak membuat ekspor Indonesia lebih murah di mata pembeli, karena harganya sudah dalam USD. Akibatnya efek perbaikan lewat ekspor lemah. Ini relevan untuk komoditas Indonesia (batu bara, CPO, nikel) yang harganya ditentukan di pasar dunia dalam USD.

## 2. Mengapa ARDL dominan di literatur J-curve

Sejak Bahmani-Oskooee & Brooks (1999), sebagian besar studi J-curve memakai ARDL / bounds testing (Pesaran, Shin & Smith 2001). Survei Bahmani-Oskooee & Ratha (2004) dan Bahmani-Oskooee & Hegerty (2010) memperlihatkan alasannya:

1. **Variabel campuran I(0)/I(1) bisa dipakai.** Data kita memang campuran. ADF/PP menunjukkan ln(X/M) dan IPI mitra I(0), sedangkan ln REER, ln JISDOR dan harga komoditas I(1). Tidak ada yang I(2) (`output/tables/unitroot.csv`). Johansen mensyaratkan semua I(1). Engle-Granger lemah di sampel kecil.
2. **Jangka pendek dan jangka panjang dalam satu persamaan.** Koefisien ΔREER (jangka pendek) dan koefisien LR langsung menguji J-curve.
3. **Sampel terbatas tetap bisa diuji**, dengan nilai kritis finite-sample (Narayan 2005; Kripfganz & Schneider 2020). Paket Stata `ardl` (Kripfganz & Schneider 2023) yang kita pakai sudah menghitung p-value-nya.
4. **Bisa dipecah menjadi NARDL** (Shin, Yu & Greenwood-Nimmo 2014) untuk menguji asimetri depresiasi vs apresiasi. Bahmani-Oskooee & Fariditavana (2016) menunjukkan NARDL lebih sering menemukan J-curve dibanding ARDL linear.

**Studi Indonesia** juga hampir semuanya memakai ARDL/NARDL:
- Bahmani-Oskooee & Harvey (2009): ARDL bilateral untuk 13 mitra. J-curve ditemukan pada 5 mitra.
- Bahmani-Oskooee & Harvey (2019): NARDL bilateral. Asimetri jangka pendek ditemukan di hampir semua mitra, dan asimetri jangka panjang di 5 mitra.
- Rifami & Heriqbaldi (2023): Indonesia–China per industri. J-curve ditemukan di 2 industri dengan ARDL dan 9 industri dengan NARDL.

Pola umumnya: **hasil sangat tergantung mitra dan sektor, dan agregasi menyembunyikan efek** (aggregation bias). Inilah alasan RQ2 dan RQ3 kita.

## 3. Kelemahan ARDL (dan relevansinya untuk data kita)

| Kelemahan | Relevansi di sini | Alternatif / perbaikan |
|:--|:--|:--|
| Persamaan tunggal: REER diasumsikan eksogen lemah (tidak ada umpan balik TB → kurs) | **Tinggi.** Rupiah dan neraca dagang sama-sama digerakkan siklus komoditas. Rupiah cenderung melemah saat harga komoditas jatuh, sehingga koefisien REER bisa tertular efek komoditas. | VAR/VECM dengan identifikasi struktural; local projections (Jordà 2005) dengan instrumen/kontrol |
| Linear dan simetris | Sedang. Sudah diuji dengan NARDL: simetri tidak ditolak. | NARDL (sudah dijalankan) |
| Hanya satu vektor kointegrasi | Rendah (3 regresor) | Johansen bila semua I(1) |
| Peka terhadap pilihan lag (AIC vs BIC) | Sedang. Pola lag AIC dan BIC berbeda, tetapi kesimpulannya sama. | Laporkan beberapa spesifikasi (sudah: 10 spesifikasi di `ardl_agregat.csv`) |
| Bounds test "degenerate" bila variabel dependen sendiri I(0) | **Tinggi.** ln(X/M) stasioner, sehingga uji t pada ECM hampir otomatis signifikan. | Uji tambahan pada koefisien lag regresor (McNown, Sam & Goh 2018); interpretasi lewat dynamic multiplier, bukan hanya uji kointegrasi |
| Dynamic multiplier tanpa selang kepercayaan | Sedang | Bootstrap; atau local projections yang langsung memberi CI per horizon |
| Panel mitra: REER sama untuk semua mitra, sehingga ada cross-sectional dependence | **Tinggi** untuk RQ2 | Kurs riil **bilateral** + CS-ARDL (Chudik & Pesaran 2015) atau MG; gravity PPML untuk data HS |

## 4. Kesimpulan: ARDL "terbaik"?

**ARDL bukan satu-satunya metode yang benar, tetapi pilihan baseline yang tepat** untuk pertanyaan ini. Alasannya: ARDL standar literatur J-curve (jadi hasil kita sebanding dengan studi Indonesia sebelumnya), cocok untuk campuran I(0)/I(1), dan langsung memisahkan efek jangka pendek dari jangka panjang.

Yang perlu ditambahkan supaya kesimpulannya kuat:

1. **NARDL** untuk asimetri. Sudah dijalankan, dan hasilnya simetri tidak ditolak.
2. **Panel MG/PMG** untuk RQ2. Sudah dijalankan; Hausman menolak PMG, jadi MG yang dipakai. Idealnya diganti CS-ARDL dengan kurs riil bilateral.
3. **Local projections atau VAR** sebagai cek endogenitas kurs–komoditas. Ini cek paling penting yang **belum** dikerjakan.
4. Perbaikan **data** lebih penting daripada ganti metode:
   - kurs riil bilateral (kurs nominal + CPI tiap mitra);
   - pendapatan domestik Indonesia (IPI/PDB bulanan) untuk persamaan impor;
   - harga komoditas spesifik (batu bara, CPO, nikel) untuk kelompok komoditas.

## Referensi

- Backus, D.K., Kehoe, P.J., & Kydland, F.E. (1994). Dynamics of the trade balance and the terms of trade: the J-curve? *American Economic Review*, 84(1), 84–103.
- Bahmani-Oskooee, M., & Brooks, T.J. (1999). Bilateral J-curve between US and her trading partners. *Weltwirtschaftliches Archiv*, 135(1), 156–165.
- Bahmani-Oskooee, M., & Fariditavana, H. (2016). Nonlinear ARDL approach and the J-curve phenomenon. *Open Economies Review*, 27(1), 51–70.
- Bahmani-Oskooee, M., & Harvey, H. (2009). The J-curve: Indonesia vs. her major trading partners. *Journal of Economic Integration*, 24(4), 765–777.
- Bahmani-Oskooee, M., & Harvey, H. (2019). The J-curve and bilateral trade balances of Indonesia with its major partners: are there asymmetric effects? *New Zealand Economic Papers*, 53(1), 63–76.
- Bahmani-Oskooee, M., & Hegerty, S.W. (2010). The J- and S-curves: a survey of the recent literature. *Journal of Economic Studies*, 37(6), 580–596.
- Bahmani-Oskooee, M., & Ratha, A. (2004). The J-curve: a literature review. *Applied Economics*, 36(13), 1377–1398.
- Chudik, A., & Pesaran, M.H. (2015). Common correlated effects estimation of heterogeneous dynamic panel data models with weakly exogenous regressors. *Journal of Econometrics*, 188(2), 393–420.
- Gopinath, G., Boz, E., Casas, C., Díez, F.J., Gourinchas, P.-O., & Plagborg-Møller, M. (2020). Dominant currency paradigm. *American Economic Review*, 110(3), 677–719.
- Jordà, Ò. (2005). Estimation and inference of impulse responses by local projections. *American Economic Review*, 95(1), 161–182.
- Kripfganz, S., & Schneider, D.C. (2020). Response surface regressions for critical value bounds and approximate p-values in equilibrium correction models. *Oxford Bulletin of Economics and Statistics*, 82(6), 1456–1481.
- Kripfganz, S., & Schneider, D.C. (2023). ardl: Estimating autoregressive distributed lag and equilibrium correction models. *Stata Journal*, 23(4), 983–1019.
- Magee, S.P. (1973). Currency contracts, pass-through, and devaluation. *Brookings Papers on Economic Activity*, 1973(1), 303–325.
- McNown, R., Sam, C.Y., & Goh, S.K. (2018). Bootstrapping the autoregressive distributed lag test for cointegration. *Applied Economics*, 50(13), 1509–1521.
- Narayan, P.K. (2005). The saving and investment nexus for China: evidence from cointegration tests. *Applied Economics*, 37(17), 1979–1990.
- Pesaran, M.H., Shin, Y., & Smith, R.P. (1999). Pooled mean group estimation of dynamic heterogeneous panels. *Journal of the American Statistical Association*, 94(446), 621–634.
- Pesaran, M.H., Shin, Y., & Smith, R.J. (2001). Bounds testing approaches to the analysis of level relationships. *Journal of Applied Econometrics*, 16(3), 289–326.
- Rifami, & Heriqbaldi, U. (2023). Exchange rate and Indonesia-China bilateral industry trade flows: J-curve and asymmetric effects. *Iranian Economic Review*. (cek volume/halaman sebelum dikutip)
- Rose, A.K., & Yellen, J.L. (1989). Is there a J-curve? *Journal of Monetary Economics*, 24(1), 53–68.
- Shin, Y., Yu, B., & Greenwood-Nimmo, M. (2014). Modelling asymmetric cointegration and dynamic multipliers in a nonlinear ARDL framework. Dalam R. Sickles & W. Horrace (Eds.), *Festschrift in Honor of Peter Schmidt* (pp. 281–314). Springer.

Catatan verifikasi: referensi Indonesia (Bahmani-Oskooee & Harvey 2009, 2019; Rifami & Heriqbaldi 2023) dicek lewat RePEc/EconBiz pada 16 Nov 2026, tetapi baru dari abstraknya, bukan teks lengkap. Referensi lain adalah karya standar; tetap cek ulang halaman dan volume sebelum masuk draft final.
