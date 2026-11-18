# Data harga komoditas dari Database DEN

> Pembaruan klasifikasi HS4 17 November 2026: komoditas/nonkomoditas telah dipisahkan pada `intermediate/hs_classified/`; kode campuran dan khusus disimpan tersendiri. Lihat [klasifikasi_komoditas_hs4.md](klasifikasi_komoditas_hs4.md). Pemetaan BEC dan intensitas input impor masih perlu dilengkapi.


Pembaruan: 17 November 2026. Sumber adalah workbook pengguna `Database DEN_26 October_temp.xlsx`, bukan unduhan baru dari penyedia data. Metadata ticker dan satuan mengikuti sheet `Legend`; autentisitas serta definisi kontrak belum dikonfirmasi langsung kepada penyedia.

## Raw dan jejak sumber

- Salinan asli: `Tio/input/raw/commodity_den_20261117/Database DEN_26 October_temp.xlsx`.
- `source_manifest.json` mencatat lokasi sumber, ukuran, waktu penyalinan, dan SHA-256. Skrip memastikan salinan identik dengan file sumber.
- `baseline_before_commodity_merge/` menyimpan lima CSV tujuan dan Excel gabungan sebelum perubahan pertama ini.
- Ekstraksi menggunakan nilai cache Excel (`data_only=True`). Formula, makro, dan instruksi di workbook tidak dijalankan.

## Seri dan konflik dalam workbook

Ada 20 ticker unik di sheet `Commodities` dan `Sulfur etc.`. Masing-masing memiliki dua blok tanggal/nilai. Blok kiri digunakan sebagai salinan sumber utama; blok kanan hanya untuk perbandingan. Nilai kosong pada blok kiri tidak ditambal dari kanan. Semua perbedaan tercatat di `Commodity_Duplicate_Audit.csv`.

Sebanyak 17 seri masuk sebagai kolom tambahan di panel: WTI, Brent, batubara Newcastle, emas, CPO kontrak depan, nikel kontrak depan, BCOM, SCFI, WCI, dua harga bijih nikel, bijih besi, urea, sulfur, grafit, metanol, dan jet kerosene. SCFI/WCI adalah indikator pengiriman, bukan harga komoditas.

Tiga seri tetap tersedia di tabel tersendiri, tetapi dikecualikan dari panel utama:

| Series | Alasan |
|---|---|
| CPO_Active | Banyak tanggal memiliki angka berbeda di kedua blok; perlu penjelasan pemilik workbook/penyedia. |
| DOW_Unverified | Identitas instrumen dan satuan dalam Legend belum cukup jelas. |
| Nickel_3M_UnverifiedUnit | Legend menulis `6 metric tons price quote`; satuannya perlu dikonfirmasi. |

Beberapa seri lain juga memiliki konflik pada tanggal tertentu. **Seluruh bulan yang mengandung konflik angka dikecualikan dari `Mean` yang masuk panel**, tanpa memilih salah satu angka. Data mentah blok kiri tetap tersedia pada `Value`/`Observed_Mean`, ditambah penanda konflik. Dengan demikian nilai mentah yang tersimpan tidak sama dengan sertifikasi kelayakan estimasi.

## Tabel intermediate

| File | Isi |
|---|---|
| `Commodity_Daily.csv` | Semua observasi numerik blok kiri, ticker, tanggal dan penanda konflik. |
| `Commodity_Monthly.csv` | Format panjang: rata-rata teramati, nilai akhir teramati, jumlah observasi, tanggal awal/akhir, konflik, bulan parsial, serta Mean/EOP yang lolos aturan periode. |
| `Commodity_Quarterly.csv` | Format panjang: Mean adalah rata-rata tiga Mean bulanan yang lengkap, dengan jumlah bulan dan status kelengkapan. |
| `Commodity_Monthly_Wide.csv` | Kolom CMD_ untuk 17 seri yang memenuhi syarat metadata; untuk merge pada Date. |
| `Commodity_Quarterly_Wide.csv` | Kolom CMD_ untuk merge pada Quarter. |
| `Commodity_Data_Dictionary.csv` | Ticker, nama dan satuan menurut Legend, kolom asal, jenis seri, status kelayakan merge dan catatan. |
| `Commodity_Data_Coverage.csv` | Cakupan tanggal, jumlah observasi, bulan/kuartal yang tersedia, serta bulan berkonflik. |
| `Commodity_Duplicate_Audit.csv` | Perbedaan nilai dan missing/error antarblok, termasuk nilai kedua blok. |
| `Commodity_Validation_Report.json` | Hasil pemeriksaan ekstraksi, integritas dan penggabungan. |

Data telah dihubungkan dengan lima dataset berikut, tanpa menambah baris atau mengubah nilai kolom lama:

- `Macro_Monthly.csv`, `Panel_Country_Month.csv`, dan `Trade_World_Monthly.csv`: berdasarkan `Date` berbentuk YYYY-MM.
- `Panel_Country_Quarter.csv` dan `Panel_World_Quarter.csv`: berdasarkan `Quarter` berbentuk YYYYQn.

Excel `Panel_Gabungan_Indonesia.xlsx` memuat tambahan yang sama di sheet tujuan serta sheet `Commodity_Monthly`, `Commodity_Quarterly`, `Commodity_Dictionary`, dan `Commodity_Coverage`. Sheet lookup/catatan lama dipertahankan.

## Arti kolom CMD_

- Bulanan: `CMD_BCOM_Mean`, `CMD_BCOM_NObs`, `CMD_BCOM_NConflictDays`, dan pola nama yang sama untuk seri lain.
- Kuartalan: `CMD_BCOM_Mean`, `CMD_BCOM_NMonths`, dan pola yang sama untuk seri lain.
- `Mean` bulanan adalah rata-rata nilai numerik tersedia dalam **satuan asli**. Tidak ada interpolasi atau rebasing otomatis. `Mean` kosong jika bulan awal/akhir parsial atau ada konflik angka antarblok.
- Bulan pertama diperlakukan secara konservatif sebagai parsial bila observasi dimulai setelah tanggal 1. Bulan terakhir parsial jika tanggal terakhir mendahului hari kerja terakhir bulan tersebut; ini pemeriksaan jendela kalender, bukan kalender bursa.
- Kuartalan hanya diisi bila ketiga Mean bulanan tersedia; setiap bulan berbobot sama. Ini bukan rata-rata langsung semua observasi harian dalam kuartal.
- Workbook memiliki observasi sampai **2 November 2026**. November dikecualikan dari Mean panel karena parsial. Grid bulanan utama berakhir Oktober 2026.
- `NObs` menghitung sel numerik pada tanggal yang tersedia; bukan jaminan jumlah transaksi atau kutipan harga baru. Nilai berulang tidak dihapus dan tidak otomatis dianggap pergerakan harga aktual.
- Tidak dilakukan pengisian bulan sebelum suatu seri tersedia, penggabungan kontrak berbeda, atau pembuatan harga masa depan.
- CPO menurut Legend menggunakan **MYR per ton**, bukan USD. Jangan menyamakannya langsung dengan harga USD; jika diperlukan, buat seri konversi yang terpisah menggunakan kurs MYR/USD terverifikasi.
- WTI memiliki nilai harian nonpositif pada sumber. Nilai tersebut dipertahankan; jangan mengambil log seluruh seri harian tanpa pemeriksaan.

`Use_In_Panel` pada format panjang menunjukkan kelengkapan periode dan tidak adanya konflik angka, sedangkan `Merge_Eligible` menunjukkan keputusan metadata tingkat seri. Kedua syarat harus dipertimbangkan. Lolos pemeriksaan integritas tidak membuktikan validitas ekonomi, ketepatan harga benchmark untuk setiap HS, atau hubungan sebab-akibat. Batasan audit makro sebelumnya tetap berlaku.

## Menjalankan ulang

Gunakan Python dengan pandas, numpy, dan openpyxl:

```powershell
python Tio/script/06_merge_commodity_den.py
python Tio/script/04_validate_macro_external.py
```

Skrip pertama berjalan offline dari salinan raw setelah impor pertama, memeriksa SHA-256, mengganti hanya kolom miliknya yang berawalan `CMD_`, dan menguji bahwa nilai kolom lama tetap sama. File keluaran disiapkan di drive proyek sebelum mengganti file tujuan. Jalankan dari direktori proyek atau gunakan lokasi absolut skrip.

**Urutan bila membangun ulang makro:** `03_merge_macro_external.py` -> `06_merge_commodity_den.py` -> `04_validate_macro_external.py`. Skrip 03 membangun dari baseline makro dan tidak membawa kolom komoditas, sehingga langkah 06 wajib dijalankan setelahnya. Skrip ini tidak mengubah jutaan baris file HS; saat analisis HS, hubungkan kolom yang dipilih melalui Date atau Quarter.

## Data penelitian yang masih diprioritaskan

1. Pemetaan HS dan revisinya ke komoditas/nonkomoditas serta harga benchmark yang sesuai. BCOM adalah kontrol harga global luas, bukan harga tiap produk ekspor Indonesia.
2. Pemetaan HS-BEC untuk penggunaan barang, dengan menangani korespondensi banyak-ke-banyak. BEC tidak mengukur kandungan input impor dalam ekspor.
3. Tabel input-output yang memisahkan input impor atau OECD ICIO/TiVA, serta pemetaan industri-HS, untuk mengukur ketergantungan ekspor terhadap input impor.
4. Volume/berat perdagangan per HS untuk memisahkan kanal harga dan kuantitas; ini pengayaan mekanisme, bukan syarat wajib replikasi nominal trade balance dasar.
5. Perdagangan HS dengan dunia bila cakupan pengujian hendak mewakili seluruh ekspor Indonesia, bukan hanya sepuluh mitra.
6. Jika menguji volatilitas: seri kurs berfrekuensi lebih tinggi dengan definisi dan penanganan hari tanpa perdagangan yang jelas. Depresiasi dan volatilitas harus dipisahkan dalam spesifikasi.

Rujukan definisi: [BEC UNSD](https://unstats.un.org/unsd/trade/classifications/bec.asp), [korespondensi HS/BEC](https://uncomtrade.org/docs/hs-sitc-bec-conversion-and-correspondence-tables/), [OECD TiVA](https://www.oecd.org/en/topics/sub-issues/trade-in-value-added.html). Lihat juga `audit_validitas_data_macro.md` untuk perbedaan sumber makro yang masih perlu ditinjau.
