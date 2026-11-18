# Hasil ARDL: depresiasi rupiah dan trade balance (RQ1–RQ3)

Haikal, 16 Nov 2026. Semua angka bisa dibuat ulang dengan `do script/00_master.do` (dijalankan dari folder `Haikal/`). Pembahasan metode ada di [4_litrev_metode.md](4_litrev_metode.md).

## Ringkasan jawaban

1. **RQ1 – Apakah depresiasi memperbaiki trade balance? Tidak ada buktinya.**
   - Depresiasi riil 10% menurunkan rasio ekspor/impor sekitar **7% pada bulan yang sama** (signifikan, p ≈ 0,02).
   - Dalam jangka panjang efeknya tidak signifikan di semua 10 spesifikasi.
   - Tidak ada J-curve: trade balance tidak berbalik membaik.
   - Kondisi Marshall-Lerner tidak terpenuhi untuk total perdagangan dengan 10 mitra.
2. **RQ2 – Per mitra: arahnya berbeda-beda, tetapi tidak ada yang signifikan secara formal.**
   - **Arah membaik** (estimasi titik positif): AS, Thailand, Korea, Malaysia, Vietnam. AS paling kuat (+19%, p = 0,04), tetapi kointegrasinya hanya batas.
   - **Arah memburuk**: China, Australia, Jepang. Jepang −17% di bulan pertama (p < 0,001); China −23% setelah 12 bulan.
   - Panel MG/PMG: efek jangka panjang rata-rata ≈ 0. Hausman menolak PMG, artinya efek antar mitra memang heterogen.
3. **RQ3 – Per kelompok barang: arah komoditas dan manufaktur berlawanan.**
   - **Komoditas:** depresiasi cenderung *memperburuk* rasio X/M (−13% jangka panjang, p = 0,07; energi & tambang −20%).
   - **Manufaktur (non-komoditas):** pola **mirip J-curve**: −5% di bulan pertama, lalu +4,5% setelah 12 bulan dan +10% jangka panjang. Arahnya sesuai teori, tetapi efek jangka panjangnya belum signifikan (p = 0,25).
   - **Barang modal dan bahan baku:** rasio X/M turun tajam di awal (−13% dan −7%, signifikan), karena impornya sulit disubstitusi dan kontraknya dalam USD.

## Data dan spesifikasi

- **Sampel:** bulanan, Jan-2006 s.d. Agu-2026, total perdagangan Indonesia dengan 10 mitra (AUS, CHN, IND, JPN, KOR, MYS, SGP, THA, USA, VNM), sekitar 236 observasi efektif.
- **Variabel dependen:** ln(Ekspor/Impor). Rasio dipakai, bukan selisih, supaya bisa di-log dan bebas satuan (standar Bahmani-Oskooee).
- **Kurs:** ln REER BIS broad (naik = apresiasi riil). Robustness: ln JISDOR nominal (Jun-2013+).
- **Kontrol:**
  - ln indeks harga komoditas IMF (all; khusus pertanian dipakai indeks pangan, khusus tambang indeks energi);
  - IPI YoY mitra (tertimbang ekspor untuk agregat; per negara memakai IPI negara itu, diisi rata-rata mitra bila kosong);
  - dummy bulan, dummy GFC (Okt-2008–Jun-2009) dan COVID (Mar–Agu 2020).
- **Estimasi:** ARDL bentuk error-correction, lag maksimum 12 dipilih AIC, uji bounds Pesaran-Shin-Smith dengan p-value Kripfganz-Schneider. "Terkointegrasi" artinya p(F) dan p(t) untuk batas I(1) keduanya < 0,10.
- **Cara membaca angka:** semua efek ditulis sebagai **perubahan rasio X/M (%) akibat depresiasi riil 10%**. **Positif = depresiasi memperbaiki trade balance.** Efek per horizon dihitung dari dynamic multiplier kumulatif.
- **Uji akar unit** (`output/0_deskriptif/unitroot.csv`): ln(X/M) dan IPI mitra I(0); REER, JISDOR dan harga komoditas I(1). Tidak ada yang I(2), jadi ARDL valid.

## RQ1: agregat 10 mitra

Sumber: `output/1_ardl/ardl_agregat.csv` dan `output/1_ardl/jcurve_agregat.png`.

| Spesifikasi | Lag | Kointegrasi | Efek bln 0 (p) | 12 bln | Jangka panjang (p) |
|:--|:--|:--:|--:|--:|--:|
| **Utama: REER, AIC** | (6,9,2,7) | ya | **−7,1 (0,02)** | −7,3 | −4,9 (0,60) |
| BIC | (3,1,0,0) | ya | −6,7 (0,02) | −4,6 | −3,9 (0,59) |
| Dengan tren linear | (6,2,4,6) | tidak | −6,7 (0,02) | −8,2 | −15,2 (0,21) |
| Maxlag 6 | (6,1,4,0) | tidak | −7,0 (0,02) | −3,4 | −4,1 (0,71) |
| Tanpa harga komoditas | (6,1,1) | ya | −6,8 (0,02) | −4,7 | −6,0 (0,49) |
| Sampel 2006–2019 | (3,2,0,6) | tidak | −2,8 (0,40) | −12,3 | −21,7 (0,19) |
| JISDOR nominal, 2013+ | (12,12,0,12) | tidak | −8,5 (0,03) | −11,3 | −9,6 (0,42) |
| REER, 2013+ | (3,1,0,10) | ya | −7,0 (0,05) | −7,4 | −7,5 (0,11) |

- **Diagnostik spesifikasi utama:** tidak ada autokorelasi (LM(12) p = 0,41), tidak ada ARCH (p = 0,33), dan parameter stabil (CUSUM 0,33 < nilai kritis 5% 0,95; lihat `output/1_ardl/`). Kecepatan penyesuaian −0,145 per bulan, kira-kira separuh deviasi hilang dalam 4–5 bulan.
- **NARDL** (`nardl_agregat.csv`): koefisien jangka panjang apresiasi 3,60 dan depresiasi 3,26 (keduanya p ≈ 0,05). Wald simetri jangka panjang p = 0,12 dan jangka pendek p = 0,17. **Tidak ada bukti asimetri.** Uji bounds NARDL juga tidak meyakinkan (p(t) = 0,29).
- **Persamaan ekspor dan impor terpisah:** keduanya tidak terkointegrasi, dan persamaan impor gagal uji autokorelasi. Ini wajar karena pendapatan domestik Indonesia belum masuk model. Anggap indikatif saja.

**Interpretasi.** Hasil ini konsisten di semua spesifikasi: depresiasi langsung memperburuk rasio X/M, dan perbaikannya tidak pernah muncul. Ada catatan penting soal stasioneritas. ln(X/M) sendiri stasioner, sedangkan REER I(1). Kalau depresiasi punya efek permanen pada rasio X/M, rasio itu seharusnya ikut I(1). Jadi stasioneritas ln(X/M) sudah merupakan petunjuk bahwa efek permanennya kecil.

## RQ2: per mitra dagang

Sumber: `output/1_ardl/ardl_mitra.csv`, `pmg_mitra.csv`, `output/1_ardl/mitra_lr.png` dan `jcurve_mitra.png`.

| Mitra | Kointegrasi | Efek bln 0 (p) | 6 bln | 12 bln | Jangka panjang (p) |
|:--|:--:|--:|--:|--:|--:|
| AS (USA) | batas (p(t) = 0,10) | – | +8,1 | +11,7 | **+19,3 (0,04)** |
| Thailand | ya | – | +4,9 | +6,6 | +10,4 (0,21) |
| Korea Selatan | tidak | – | +5,7 | +7,6 | +13,9 (0,50) |
| Malaysia | tidak | – | +4,0 | +5,3 | +22,3 (0,50) |
| Vietnam | tidak | – | +21,5 | +30,7 | +112 (0,35)* |
| India | ya | +5,6 (0,49) | −3,8 | −7,5 | +4,1 (0,76) |
| Singapura | ya | +13,8 (0,03) | −6,0 | −7,3 | −6,6 (0,28) |
| Jepang | tidak | **−17,4 (0,00)** | −0,7 | −15,4 | +6,0 (0,83)* |
| China | tidak | −8,4 (0,12) | −13,4 | −23,0 | −84,9 (0,13)* |
| Australia | tidak | −0,7 (0,94) | −8,8 | −8,7 | −128 (0,35)* |

"–" berarti AIC memilih lag 0 untuk ΔREER, sehingga dampak bulan pertama sudah tercakup di kolom 6 bulan. Tanda * berarti kecepatan penyesuaian sangat lambat (|ADJ| < 0,1), jadi koefisien jangka panjangnya tidak presisi. Vietnam juga gagal uji autokorelasi.

**Panel** (10 mitra, efek jangka panjang depresiasi 10%):

| Estimator | Efek | p |
|:--|--:|--:|
| PMG | +1,1% | 0,75 |
| MG | −2,5% | 0,63 |

Hausman χ² = 13,6 (p = 0,003): asumsi PMG (efek jangka panjang sama untuk semua mitra) ditolak, sehingga MG yang dipakai. Rata-rata efeknya nol karena arah antar mitra saling meniadakan.

**Interpretasi** (hipotesis, perlu dicek dengan komposisi barang per mitra):
- **Ekspor ke AS** didominasi manufaktur padat karya (pakaian, alas kaki, furnitur, elektronik) yang sensitif harga, sehingga depresiasi membantu. Ini cocok dengan hasil RQ3 untuk manufaktur.
- **Impor dari China dan Jepang** adalah barang modal dan bahan baku. Ekspor ke China dan Australia didominasi komoditas berharga USD. Dua hal ini memberi arah memburuk.

## RQ3: per kelompok barang

Sumber: `output/1_ardl/ardl_kelompok.csv`, `output/0_deskriptif/group_shares.csv`, `output/1_ardl/kelompok_lr.png` dan `jcurve_kelompok.png`. Klasifikasi HS-4 ada di `intermediate/analisis/hs4_groups.csv`; aturannya di `script/02_prep_data.do` bagian 4.

**Pengelompokan:**
- **Komoditas vs non-komoditas:** mengikuti definisi UNCTAD (SITC 0–4, 68, 667, 971) yang dipetakan ke HS-4, ditambah HS 7202 (feronikel). Komoditas dipecah lagi menjadi pertanian/pangan dan energi/tambang.
- **End use:** mengikuti BEC / klasifikasi impor BPS: konsumsi, bahan baku/penolong, barang modal.

| Kelompok | Pangsa X | Pangsa M | Kointegrasi | Bln 0 (p) | 12 bln | 24 bln | Jangka panjang (p) |
|:--|--:|--:|:--:|--:|--:|--:|--:|
| Komoditas (total) | 61% | 29% | tidak | −4,2 (0,34) | −9,1 | −11,4 | **−13,1 (0,07)** |
| – energi & tambang | 42% | 19% | tidak | −5,9 (0,31) | −10,0 | −13,9 | −20,4 (0,21) |
| – pertanian & pangan | 19% | 10% | ya | – | −0,9 | −0,9 | −0,8 (0,85) |
| Non-komoditas (manufaktur) | 39% | 71% | ya | −5,4 (0,10) | **+4,5** | **+7,9** | +9,9 (0,25) |
| Barang konsumsi | 16% | 9% | ya | +2,8 (0,53) | +6,0 | +5,8 | +5,7 (0,39) |
| Bahan baku/penolong | 79% | 68% | batas | **−7,2 (0,04)** | −10,4 | −7,9 | −6,4 (0,53) |
| Barang modal | 5% | 23% | ya | **−12,8 (0,05)** | −7,1 | −7,4 | −8,3 (0,58) |

Pangsa dihitung dari kumulatif 2006–Agu 2026, untuk 10 mitra.

**Interpretasi:**
- **Komoditas:** harga ditentukan di pasar dunia dalam USD dan volumenya ditentukan sisi suplai. Akibatnya depresiasi tidak menaikkan ekspor, sedangkan impor yang berharga USD jadi lebih mahal dalam rupiah. Ada juga kemungkinan kausalitas terbalik: rupiah melemah *karena* harga komoditas jatuh. Ini belum sepenuhnya tertangkap oleh kontrol indeks harga komoditas IMF.
- **Manufaktur:** satu-satunya kelompok dengan pola J-curve (memburuk dulu, lalu membaik). Barang konsumsi juga cenderung membaik. Dua kelompok ini adalah kanal tempat depresiasi bisa membantu, tetapi pangsanya di ekspor kecil.
- **Barang modal dan bahan baku:** depresiasi langsung memperburuk rasio X/M karena impor bahan baku dan barang modal inelastis dalam jangka pendek. Ini sesuai dengan cerita ketergantungan impor input industri.

## Keterbatasan dan langkah berikut

1. **Kurs riil bilateral belum ada.** RQ2 masih memakai REER multilateral yang sama untuk semua mitra. Prioritas: data kurs nominal dan CPI 10 mitra (IMF IFS / CEIC).
2. **Pendapatan domestik Indonesia belum masuk** (IPI Indonesia tidak tersedia di FRED). Ini membuat persamaan impor lemah. Bisa pakai IPI/PDB bulanan BPS/CEIC atau Indeks Keyakinan Konsumen.
3. **Endogenitas kurs dan komoditas.** Sudah dicek dengan local projections + kurs riil bilateral + FE waktu; lihat [3_hasil_lp.md](3_hasil_lp.md).
4. **Dynamic multiplier belum punya selang kepercayaan.** Perlu bootstrap.
5. **Klasifikasi end use masih pendekatan per bab HS** dengan pengecualian. Bisa diganti konkordansi resmi HS–BEC Rev.5 (UN Stats) bila tersedia.
6. **Cakupan:** hanya 10 mitra (bukan total ekspor/impor Indonesia), dan data perdagangan baru sampai Agu-2026.
