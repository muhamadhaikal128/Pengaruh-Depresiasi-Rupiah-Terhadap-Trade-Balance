# Hasil local projections (LP): depresiasi rupiah dan trade balance (RQ1–RQ3)

Haikal, 16 Nov 2026. Melengkapi [2_hasil_ardl.md](2_hasil_ardl.md). Alasan memakai LP dan literaturnya ada di [4_litrev_metode.md](4_litrev_metode.md) §5–6.

- **Script:** `script/03_prep_kurs_bilateral.do` (data) dan `script/07_local_projections.do` (estimasi).
- **Output:** `output/2_lp/`:
  - `lp_summary.csv`: efek dan p-value di horizon 0/3/6/12/18/24;
  - `lp_irf.csv`: semua horizon 0–24;
  - grafik `lp_*.png`.

## Spesifikasi

Untuk setiap horizon h = 0..24 bulan:

> y_{t+h} − y_{t−1} = a_h + b_h · guncangan_t + lag(1..12) Δy + lag(1..12) guncangan + kontrol + e

| | RQ1 Agregat | RQ2 Panel mitra | RQ3 Panel mitra × kelompok |
|:--|:--|:--|:--|
| Unit | 10 mitra dijumlah, bulanan | mitra × bulan (10 × 248) | (mitra, kelompok) × bulan, per kelompok |
| y | ln(X/M) | ln(X_i/M_i) | ln(X_ig/M_ig) |
| Guncangan | Δ(−ln REER) | Δ kurs riil bilateral | Δ kurs riil bilateral |
| Kontrol | lag 1–12 Δy dan guncangan; Δln harga komoditas (lag 0–12); IPI mitra (lag 0–3); musiman; GFC, COVID | lag 1–12 Δy dan guncangan; IPI mitra (lag 0–3); **FE mitra + FE bulan** | sama dengan RQ2 |
| SE | Newey-West (lag h+1) | Driscoll-Kraay (lag h+1) | Driscoll-Kraay (lag h+1) |

**Data dan definisi:**
- **Kurs riil bilateral:** ln(Rp per mata uang mitra) + ln CPI mitra − ln CPI Indonesia. Naik = rupiah melemah riil. Sumber: BIS. Detail ada di [catatan_data.md](catatan_data.md).
- **Korelasi dengan REER:** perubahan RER bilateral berkorelasi 0,54–0,94 dengan REER. Sisa variasinya yang khusus per mitra adalah sumber identifikasi panel.
- **Cara membaca angka:** semua efek = perubahan rasio X/M (%) akibat depresiasi riil 10% (= 10 × b_h). Positif = membaik.
- **Persistensi guncangan:** depresiasi 10% bertahan sekitar 9–11% sampai 24 bulan. Jadi respons di horizon panjang adalah efek dari depresiasi yang permanen.

**Penting – "missing intercept":** FE waktu di panel menyerap efek agregat. Panel hanya mengukur efek **relatif**: apakah neraca dengan mitra *i* membaik dibanding mitra lain ketika rupiah melemah *khusus* terhadap mata uang *i*. Jawaban RQ1 (efek agregat) tetap dari LP time series.

## RQ1: agregat (`lp_agregat.png`)

| Horizon (bulan) | 0 | 6 | 12 | 24 |
|:--|--:|--:|--:|--:|
| LP OLS, efek (%) | **−5,7** | **−8,8** | **−10,2** | −5,2 |
| p | 0,05 | 0,09 | 0,05 | 0,16 |

- **LP mengonfirmasi ARDL.** Depresiasi langsung menurunkan rasio X/M (ARDL: −7%), memburuk sampai sekitar −10% di bulan 12, dan **tidak berbalik positif** dalam 24 bulan. Tidak ada J-curve.
- **LP-IV gagal dan tidak dipakai.** Indeks dolar AS broad sebagai instrumen terlalu lemah (F first stage = 0,14, p = 0,71). Ketika USD menguat global, mata uang mitra juga melemah terhadap USD, sehingga REER rupiah hampir tidak bergerak. Kandidat instrumen lain: kejutan kebijakan moneter AS (high-frequency FOMC surprises).

## RQ2: panel mitra (`lp_panel.png`, `lp_mitra.png`)

| | Bln 0 (p) | 6 | 12 (p) | 24 |
|:--|--:|--:|--:|--:|
| **Rata-rata 10 mitra** | −1,8 (0,58) | +0,1 | −5,7 (0,19) | +0,2 |
| Tanpa Vietnam | −2,8 (0,42) | +0,2 | −6,4 (0,12) | −0,6 |
| China | **−11,1 (0,02)** | +0,1 | **−18,4 (0,06)** | −10,3 |
| Jepang | **−9,7 (0,01)** | −3,1 | **−11,7 (0,00)** | −9,1 |
| Thailand | −4,3 (0,50) | +7,8 | **−15,2 (0,04)** | −1,8 |
| Malaysia | −0,9 | +14,0 | −10,4 (0,25) | −4,9 |
| AS | +0,4 | −3,4 | −6,4 (0,26) | +1,7 |
| India, Korea, Singapura, Australia, Vietnam | tidak signifikan di semua horizon | | | |

- **Rata-rata:** tidak ada efek relatif.
- **China dan Jepang:** neraca bilateral memburuk signifikan, konsisten dengan ARDL. Indonesia mengimpor banyak barang modal dan bahan baku dari kedua negara ini, dan impor itu sulit disubstitusi.
- **AS:** hasil ARDL (+19% jangka panjang) **tidak terkonfirmasi** setelah guncangan bersama dikontrol.

## RQ3: panel per kelompok barang (`lp_kelompok.png`)

| Kelompok | Bln 0 (p) | 6 | 12 (p) | 24 (p) |
|:--|--:|--:|--:|--:|
| Komoditas energi & tambang | 0,0 | −15,8 | **−22,2 (0,02)** | −10,2 (0,25) |
| Bahan baku/penolong | −3,1 (0,42) | −3,9 | **−9,8 (0,01)** | +0,3 |
| Barang modal | −8,4 (0,21) | +4,1 | −3,8 | +0,4 |
| Komoditas (total) | −0,4 | −3,0 | −7,4 (0,28) | +7,3 (0,19) |
| Non-komoditas (manufaktur) | −2,8 (0,35) | −0,4 | +0,2 | −4,4 (0,41) |
| Barang konsumsi | −2,6 (0,53) | +6,3 | +3,6 | +9,1 (0,10) |
| Komoditas pertanian & pangan | +1,7 | +6,7 | +9,3 (0,15) | **+22,0 (0,00)** |

**Interpretasi:**
- **Energi & tambang dan bahan baku** memburuk sekitar 12 bulan setelah depresiasi, konsisten dengan ARDL.
- **Pertanian & pangan** adalah satu-satunya yang membaik signifikan, tapi baru setelah sekitar 2 tahun. Barang konsumsi cenderung membaik.
- **Pola J-curve manufaktur di ARDL tidak terkonfirmasi:** responsnya sekitar nol.

## Yang masih kurang

- Instrumen yang kuat untuk LP-IV agregat.
- Koreksi bias LP di sampel kecil atau bootstrap.
- Data volume/harga untuk memisahkan efek harga dari efek volume.
