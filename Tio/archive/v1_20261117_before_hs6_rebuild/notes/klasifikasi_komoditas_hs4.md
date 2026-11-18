# Klasifikasi komoditas dan nonkomoditas pada HS-4

> Pembaruan sumber input impor: OECD TiVA Indonesia 1995-2022 dan kamus BEC5 telah diunduh; pemetaan HS-BEC/HS-industri belum digabungkan. Lihat [data_barang_modal_dan_input_impor.md](data_barang_modal_dan_input_impor.md).


Dibangun 17 November 2026 untuk dataset Tio. Daftar berisi 1.264 kode HS-4: **358 commodity, 857 noncommodity, 47 mixed, dan 2 unclassified**. Label ini merupakan hasil olahan dari definisi UNCTAD dan korespondensi resmi UNSD, bukan tabel biner HS-4 yang diterbitkan langsung oleh UNCTAD.

## Definisi dan alasan pemilihan

Dasar utama adalah kelompok **UNCTAD A11**, yaitu komoditas primer beserta batu mulia dan emas nonmoneter. Pada SITC Rev.3 cakupannya adalah `0 + 1 + 2 + 3 + 4 + 68 + 667 + 971`. Kelompok pembanding adalah barang manufaktur, yakni SITC `5 + 6 + 7 + 8`, dengan mengecualikan `68` dan `667`. Transaksi khusus dan kode di luar kedua kelompok tidak otomatis dimasukkan ke nonkomoditas.

Definisi ini memberi dasar yang dapat direplikasi untuk pengujian ketergantungan komoditas. Namun, **komoditas tidak identik dengan barang mentah**, dan label komoditas tidak membuktikan ketidakpekaan terhadap kurs. Beberapa makanan olahan dan produk logam nonferrous termasuk dalam kelompok komoditas menurut definisi ini. Sebaliknya, ferro-alloy HS7202 termasuk manufaktur/nonkomoditas dalam definisi utama, meskipun harganya dapat berhubungan erat dengan pasar global.

Jika pertanyaan difokuskan pada harga yang terbentuk di bursa atau harga acuan global, klasifikasi Rauch (homogen, reference-priced, differentiated) adalah pengayaan yang berbeda. Label Rauch belum dibangun dalam hasil ini dan tidak boleh dianggap sama dengan UNCTAD A11.

## Sumber resmi dan raw

1. [UNCTAD product groups and composition, SITC Rev.3, April 2025](https://unctadstat.unctad.org/EN/Classifications/DimSitcRev3Products_DsibSpecialGroupings_Hierarchy.pdf): definisi kelompok A11 dan manufaktur.
2. [UNSD classifications and correspondence tables](https://unstats.un.org/unsd/classifications/Econ/): tabel langsung HS1992/1996/2002/2007/2012/2017/2022 ke SITC Rev.3, baik correlation maupun conversion.
3. [UNSD conversion methodology, 2022](https://unstats.un.org/unsd/classifications/Econ/corr-notes/HS2022%20conversion%20to%20earlier%20HS%20versions%20and%20other%20classifications%20%20-%20v.1.0.pdf): menjelaskan hubungan banyak-ke-banyak dan keterbatasan konversi.
4. [Federal Reserve, Appendix A: Rauch Classification](https://www.federalreserve.gov/econres/notes/feds-notes/assessing-the-extent-of-trade-fragmentation-20231103.html): penjelasan klasifikasi alternatif berdasarkan diferensiasi pasar.

Salinan sumber tersimpan pada `Tio/input/raw/hs_commodity_classification_20261117/`. `source_manifest.json` mencatat URL, waktu unduh, ukuran, dan SHA-256. Permintaan sumber dengan checksum tersimpan pula di `Tio/script/hs_classification_source_requests.json`. Semua 12 file sumber diperiksa sebelum klasifikasi.

Tabel lengkap HS-SITC-BEC digunakan untuk menentukan himpunan kode HS6 yang harus tercakup pada setiap revisi. **Pemetaan SITC untuk klasifikasi memakai tabel korelasi langsung per revisi**, bukan menarik hubungan transitif melalui seluruh kolom revisi HS dalam tabel lengkap.

## Cara menangani HS-4 dan revisi

1. Baca relasi resmi HS6 ke SITC3 pada setiap revisi HS, pertahankan semua kemungkinan relasi dan nol di depan.
2. Klasifikasikan setiap SITC3 menurut definisi di atas. HS6 yang tidak memiliki pasangan SITC tetap ditandai unclassified; tidak dipaksakan menjadi manufaktur.
3. Naikkan ke HS4: suatu heading hanya menjadi komoditas murni atau nonkomoditas murni bila semua subheading/pasangan terkait berada pada kelompok yang sama.
4. Dataset sumber tidak mencatat revisi HS secara eksplisit. Karena itu label utama memakai **konsensus seluruh revisi yang tersedia**. Jika ada campuran dalam satu revisi atau perbedaan antarrevisi, heading masuk mixed. Hasil per revisi dan hasil tabel conversion juga disimpan untuk peninjauan/robustness.

`Commodity_Flag` bernilai 1 untuk commodity, 0 untuk noncommodity, dan kosong untuk mixed/unclassified. Jangan mengubah kosong menjadi 0. `Binary_Sample=True` hanya untuk kedua kelompok murni.

Contoh:

| HS4 | Produk | Kelompok utama |
|---|---|---|
| 0901 | Kopi | commodity |
| 1511 | Minyak sawit | commodity |
| 2701 | Batubara | commodity |
| 2709 | Minyak bumi mentah | commodity |
| 7502 | Nikel tidak ditempa | commodity |
| 7202 | Ferro-alloys | noncommodity menurut UNCTAD A11 |
| 8703 | Mobil penumpang | noncommodity |
| 7108 | Emas | mixed: heading juga mencakup emas moneter yang berada di luar SITC |
| 7118 | Koin | unclassified untuk pembagian utama ini |
| 9999 | Barang tidak dirinci | unclassified |

Jika metadata perdagangan menegaskan bahwa HS7108 hanya memuat emas nonmoneter, pembatasan emas dapat ditinjau dengan bukti tersebut/HS6. Saat ini angka pada HS4 tidak dibagi secara arbitrer. Hal yang sama berlaku untuk kode campuran lain. Jumlah subheading tidak digunakan sebagai bobot nilai perdagangan.

**Konsensus kategori tidak mengharmonisasikan sejarah produk.** Kode/nama dari revisi berbeda masih dapat berubah cakupannya dalam deret 2006-2026. Label yang stabil membantu pemisahan, tetapi analisis deret per produk tetap perlu pemeriksaan revisi/structural break terhadap sumber awal.

## File klasifikasi

| File intermediate | Fungsi |
|---|---|
| `HS4_Commodity_Classification.csv` | Master lookup HS_Code, Product, kelas, flag, subgroup, edisi, dan penanda ambiguitas. |
| `HS4_Commodity_Classification.xlsx` | Versi Excel dengan ringkasan, klasifikasi per edisi, dan daftar kode untuk ditinjau. |
| `HS4_Classification_By_Edition.csv` | Hasil per HS4 per revisi, termasuk pembanding berbasis tabel conversion. |
| `HS6_SITC3_Commodity_Crosswalk.csv` | Jejak detail HS6-SITC3, kelas, file/sheet/baris sumber. |
| `HS4_Commodity_Classification_Summary.csv` | Jumlah kode pada setiap kelompok. |
| `HS4_Classification_Validation_Report.json` | Pemeriksaan cakupan, checksum, dan contoh produk. |

## Panel terpisah yang dapat digunakan

Lokasi utama: `Tio/intermediate/hs_classified/`.

```text
hs_classified/
  commodity/
    HS4_List.csv
    HS4_CHN_Month.csv
    HS4_CHN_Quarter.csv
    ... AUS, IND, JPN, KOR, MYS, SGP, THA, USA, VNM
  noncommodity/
    HS4_List.csv
    HS4_CHN_Month.csv
    HS4_CHN_Quarter.csv
    ...
  mixed/
    HS4_List.csv
    ... panel per mitra
  unclassified/
    HS4_List.csv
    ... panel per mitra
```

Panel bulanan berkunci `ISO3 + HS_Code + Date`, panel kuartalan berkunci `ISO3 + HS_Code + Quarter`. Ekspor dan impor sudah berada dalam satu baris. Nilai tetap dalam USD ribu. Baris sumber dan file `hs_panel/` awal tidak diubah.

Variabel utama: `Exports_USDk`, `Imports_USDk`, `Trade_Balance_USDk=X-M`, `Total_Trade_USDk=X+M`, `Ln_Exports_Imports=ln(X/M)`, dan `Ln_Imports_Exports=ln(M/X)`. Kedua rasio log hanya dihitung jika ekspor dan impor positif. Perbaikan trade balance berarti ln(X/M) naik atau ln(M/X) turun; tentukan orientasi sebelum membaca koefisien.

**Nol perdagangan tetap nol** untuk analisis yang membutuhkannya, termasuk PPML. Nilai kosong tidak diganti nol. `Exports_Source_Row_Present`/`Imports_Source_Row_Present` membedakan keberadaan baris sumber pada panel bulanan. Kode yang ada hanya pada satu arus perdagangan tidak diberi nilai nol untuk arus satunya.

Kuartal dijumlahkan dari tiga bulan, dengan `NMonths_Exports`, `NMonths_Imports`, dan `Complete_Both_Flows`. Jika salah satu bulan hilang, total arus terkait tidak diisi. Grid mencakup periode makro sampai 2026Q4, tetapi perdagangan HS sumber baru tersedia sampai Agustus 2026. September-Oktober dan kuartal akhir yang belum lengkap tetap kosong.

## Panel kelompok dengan makro

- `Panel_CommodityGroup_Country_Month.csv`: empat kelompok x sepuluh mitra x bulan, dengan kurs, CPI, GDP yang tersedia, serta kolom CMD_ dari tahap sebelumnya.
- `Panel_CommodityGroup_Country_Quarter.csv`: jumlah perdagangan tiga bulan per kelompok, GDP riil kuartalan dan kurs riil bilateral, serta harga komoditas kuartalan.
- `HS4_Classified_File_Manifest.csv`: lokasi, jumlah baris/kode dan ketersediaan trade positif setiap file terpisah.
- `HS4_Classified_Source_Coverage.csv`: cakupan dan nol perdagangan pada 20 file sumber.
- `HS4_Classified_Reconciliation.csv`: rekonsiliasi pemisahan terhadap jumlah HS awal, serta perbandingan dengan perdagangan total mitra pada panel awal.
- `HS4_Commodity_Trade_Shares.csv` dan `HS4_Commodity_Trade_Summary.csv`: pangsa nominal berdasarkan nilai teramati dalam sepuluh mitra ini; bukan pangsa seluruh ekspor Indonesia.
- `HS4_Classified_Validation_Report.json`: hasil pemeriksaan konservasi nilai, nol perdagangan, kuartal, dan integritas sumber.

Pada panel kelompok, `Observed_Exports_USDk`/`Observed_Imports_USDk` adalah subtotal tersedia. Kolom `Exports_USDk`/`Imports_USDk` hanya diisi bila seluruh kode dalam himpunan sumber arus/mitra/kelompok tersebut tersedia pada bulan itu. Himpunan kode yang dilaporkan sumber dapat berbeda antar mitra/arus; jumlahnya tercantum pada kolom N_HS4. Perbandingan dengan total mitra disajikan sebagai diagnosis, tanpa menskalakan nilai HS agar sama dengan total resmi.

Kelompok mixed dan unclassified ikut dalam rekonsiliasi agar tidak ada nilai perdagangan yang hilang. Namun, keduanya dikeluarkan dari perbandingan biner utama. Pangsa komoditas murni tidak mengalokasikan bagian komoditas yang mungkin terdapat di heading mixed.

`Ready_NARDL_CPI_Group` hanya menunjukkan ketersediaan trade positif, GDP riil Indonesia/mitra, serta RER berbasis CPI. `Ready_NARDL_CPI_Group_With_BCOM` juga memerlukan BCOM. `Ready_NARDL_PriceProxy_Group` menyediakan pemeriksaan alternatif RER dengan penanda WPI; penggunaan proksi tersebut harus dijelaskan. Flag ini bukan uji stasioneritas, kointegrasi, panjang sampel, kontinuitas, atau validitas kausal. Semua catatan audit makro dan konflik komoditas pada tahap sebelumnya tetap berlaku.

## Menyiapkan satu HS4 untuk estimasi

Jalankan dari direktori proyek dengan Python yang memiliki paket dalam `requirements_hs_classification.txt`:

```powershell
python Tio/script/07_classify_hs4_commodity.py
python Tio/script/08_build_hs_commodity_panels.py
python Tio/script/09_prepare_hs4_estimation.py --hs 1511 --partner CHN
```

Tahap 07 berjalan offline dari raw dan memeriksa checksum. Untuk memulihkan sumber yang belum ada, gunakan `--download`; sumber yang sudah tersedia tidak diunduh ulang atau diganti diam-diam. Tahap 08 memerlukan panel makro/komoditas yang sudah dibangun. Urutan rebuild lengkap setelah makro: **03 -> 06 -> 04 -> 07 -> 08 -> 09**. Jika 03/06 diulang, ulangi 08/09 agar snapshot kolom makro pada panel kelompok/contoh tetap terbaru.

Perintah contoh 09 menghasilkan `Tio/intermediate/hs_classified/examples/Estimation_HS4_1511_CHN_Quarter.csv`: satu produk x China, ekspor-impor, trade balance, GDP, RER, BCOM dan log yang relevan. Ubah HS dan partner sesuai kebutuhan. Skrip tidak mengestimasi model atau menghapus kuartal yang kosong.

Untuk membaca HS di Python, pertahankan nol di depan:

```python
from pathlib import Path
import pandas as pd
base = Path('Tio/intermediate')
d = pd.read_csv(base / 'hs_classified/commodity/HS4_CHN_Quarter.csv',
                dtype={'HS_Code': str})
d = d.loc[d['HS_Code'].eq('1511')].copy()
```

Untuk NARDL per produk, mulai dari seri kuartalan dan cek kecukupan observasi positif serta celah kalender. Jangan merapatkan kuartal dengan menghapus baris kosong sebelum membuat lag. Untuk PPML ekspor, pakai nilai ekspor dalam level dengan nol yang teramati; log trade balance bukan variabel dependen PPML.

Data ini menyiapkan pengujian perbedaan respons depresiasi. Hasil klasifikasi sendiri belum menguji apakah depresiasi menguntungkan ekspor. Untuk kanal input impor, pemetaan BEC dan intensitas input impor dari IO/TiVA tetap merupakan kebutuhan terpisah.

## Pemeriksaan hasil yang dijalankan

- Klasifikasi mencakup semua 1.264 kode lookup. Semua 12 sumber raw lolos SHA-256.
- Pemisahan menghasilkan 80 file panel HS4 (10 mitra x 4 kelompok x 2 frekuensi), 3.053.500 baris bulanan dan 1.025.976 baris kuartalan. Grid bulanan tambahan tidak mengisi perdagangan yang hilang.
- Sebanyak 5.974.568 baris flow sumber direkonstruksi tanpa mengubah nilainya; 3.273.254 observasi nol dipertahankan. Seluruh file sumber HS, lookup dan panel makro tidak berubah.
- Jumlah nilai empat kelompok sama dengan jumlah HS sumber, per negara-bulan-arus. Selisih maksimum jumlah HS terhadap total mitra pada panel awal adalah sekitar 0,022764%; selisih sumber ini dilaporkan, bukan ditutup dengan penskalaan.
- Kolom makro pada panel kelompok kuartalan yang tersimpan diperiksa kembali terhadap panel makro asli, termasuk metadata teks dan nilai kosong.
- Dua contoh HS1511 (komoditas) dan HS8703 (nonkomoditas) untuk China berhasil dibuat. Contoh hanya menunjukkan struktur dan ketersediaan variabel; baris kalender tetap lengkap dan kuartal dengan arus nol tidak dipaksakan memiliki rasio log.

**Kontinuitas pada contoh:** HS1511-China memiliki 39 kuartal dengan variabel tersedia, tetapi rentang terpanjang tanpa celah hanya 13 kuartal. Untuk HS8703-China, angkanya 45 dan 10 kuartal. Angka total observasi tersebut tidak boleh diperlakukan sebagai satu deret berurutan untuk membuat lag. File `.availability.json` menyimpan panjang/rentang berurutan terpanjang. Contoh per produk ini memerlukan evaluasi kelayakan sebelum NARDL; panel kelompok agregat atau model ekspor dalam level dapat menjadi jalur analisis yang berbeda, sesuai pertanyaan penelitian.
