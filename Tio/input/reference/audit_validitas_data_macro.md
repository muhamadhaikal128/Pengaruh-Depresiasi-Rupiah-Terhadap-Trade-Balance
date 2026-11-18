> Referensi historis sebelum rebuild HS-6. Dataset dan tabel yang dirujuk berada di archive/v1_20261117_before_hs6_rebuild/. Audit data baru berada di output/diagnostics/data/.

# Audit Validitas Data Makro

Tanggal: 17 November 2026. Dataset: `Tio/intermediate`. Audit ini memperluas pemeriksaan merge sebelumnya dengan perbandingan sumber dan pemeriksaan definisi ekonomi.

## Kesimpulan

**Integritas penggabungan: lulus. Validitas substantif: bersyarat, belum dapat dinyatakan seluruhnya terverifikasi tanpa pengecualian.** Sumber resmi dan file yang sesuai sumber tidak menjamin semua seri mempunyai definisi, cakupan atau vintage yang sama.

Pemeriksaan sebelumnya berstatus PASS hanya untuk struktur, aritmetika dan ketersediaan data. Kini `Macro_Validation_Report.json` membedakan `integrity_status=PASS` dari `substantive_validity=CONDITIONAL_REVIEW_REQUIRED`.

## Yang diperiksa dan dapat dipastikan

- URL, seri dan checksum sumber utama dapat ditelusuri. Checksum membuktikan byte tidak berubah, bukan membuktikan kebenaran statistik sumber.
- Seluruh 18 kolom panel awal tetap sama setelah merge, termasuk missing. Panel masih 2.500 baris, kunci ISO3–Date unik.
- Konversi USD juta ke ribu, identitas X−M, arah kurs silang dan log rasio diperiksa.
- GDP dibaca sebagai level kuartalan; indeks diubah ke rata-rata 2015=100. Tidak ada interpolasi GDP bulanan.
- Kuartal yang kurang dari tiga observasi bulanan tidak dianggap lengkap. Grid waktu tidak dipampatkan.
- India sebelum 2013 tidak diberi label CPI murni; WPI ditandai dan hanya masuk alternatif PriceProxy.
- Pemeriksaan file Excel dan CSV selesai setelah koreksi audit.

## Pembanding tambahan

Sumber audit disimpan di `input/raw/macro_external_20261117/audit_cross_sources/` dengan manifest unduhan terpisah. Data utama tidak diganti hanya agar sama dengan pembanding.

1. CPI BIS dibandingkan dengan CPI World Bank GEM setelah basis disamakan.
2. Kurs BIS dibandingkan dengan kurs period-average GEM sebelum kurs silang dihitung.
3. GDP kuartalan GEM dibandingkan dengan GDP SA IMF/FRED untuk Indonesia, Jepang dan AS.
4. Rata-rata empat kuartal GDP dibandingkan dengan GDP riil tahunan WDI untuk 11 negara; basis waktu India dan Australia disesuaikan ke tahun fiskal.
5. Perdagangan total dibandingkan dengan IMF/FRED serta WDI/WTO tahunan dari tahap sebelumnya.

Pembanding dapat memakai sumber nasional awal yang sama sehingga **tidak seluruhnya independen**. CPI Vietnam berasal dari GEM dalam dataset utama dan pembanding: kesamaan nilainya hanya pemeriksaan ekstraksi, bukan validasi independen. CPI Australia tidak memiliki observasi pembanding bulanan/kuartalan nonmissing pada respons GEM yang diperoleh; statusnya `NOT_COMPARED_REFERENCE_UNAVAILABLE`.

Hasil lengkap ada di [ringkasan](../../archive/v1_20261117_before_hs6_rebuild/intermediate/Macro_Audit_CrossSource_Summary.csv) dan [observasi pembanding](../../archive/v1_20261117_before_hs6_rebuild/intermediate/Macro_Audit_CrossSource_Detail.csv). Ambang 1% hanyalah aturan penyaringan untuk memprioritaskan review, bukan batas universal data benar/salah.

## Temuan utama

| Kelompok | Hasil perbandingan | Penilaian |
|---|---|---|
| CPI Jepang, Korea, Singapura, AS | Selisih maksimum setelah rebase kurang dari 0,000001% pada overlap | Sangat konsisten antarcompiler; sumber awal dapat sama |
| CPI Tiongkok, Malaysia, Thailand | Selisih maksimum sekitar 0,23%; 0,10%; 0,60% | Dekat, tetapi bukan identik |
| CPI Indonesia | Maksimum 1,565%, Juni 2007 | Perlu pemeriksaan seri historis/vintage; belum diputuskan bahwa salah satu salah |
| CPI Australia | Seri BIS adalah interpolasi dari kuartalan; pembanding GEM tidak tersedia | Jangan diperlakukan sebagai observasi harga bulanan yang dikumpulkan terpisah |
| Kurs Thailand | Maksimum 10,107%, Desember 2007 | Tidak boleh dianggap beda pembulatan; konsep pasar/quotation perlu diverifikasi sebelum memilih baseline |
| Kurs Vietnam | Maksimum 4,799%, Mei 2024 | Konsep kurs kedua compiler tidak boleh diasumsikan sama |
| Kurs Korea | Maksimum 1,268%, Desember 2008 | Periksa perbedaan fixing/observasi saat krisis; tidak dihapus sebagai outlier |
| GDP SA kuartalan Jepang dan AS | Maksimum sekitar 0,000035% dan 0,001764% | Sangat dekat setelah rebase |
| GDP SA kuartalan Indonesia | Maksimum 1,576%, 2007Q3 | Historis perlu review; tidak dibenarkan “memperbaiki” level dengan faktor arbitrer |
| GDP tahunan Australia | Selisih maksimum setelah penyelarasan fiskal sekitar 0,028% | Perbedaan awal sebagian besar karena salah basis tahun pembanding, bukan GDP utama yang salah |
| GDP tahunan India dan Vietnam | Selisih maksimum sekitar 6,093% dan 3,900% | Masih perlu pemeriksaan vintage/base-year/seri historis; penyelarasan fiskal saja tidak menghilangkan seluruh perbedaan India |
| Perdagangan dunia 2006–2009 | Selisih impor GEM–WDI mencapai 24,283% pada 2006 | Belum harmonis. Perlu rekonsiliasi dengan sumber nasional sebelum menjadikan periode ini baseline agregat utama |

Angka perbandingan adalah selisih relatif absolut pada indeks/satuan yang disamakan, bukan standard error atau probabilitas data salah. Perbedaan riil antara seri yang sah tidak otomatis berarti error unduhan.

### Koreksi nyata: penyambungan kurs Vietnam

Versi sebelumnya memasukkan satu observasi GEM pada Agustus 2025 untuk mengisi lubang BIS. Setelah diketahui kedua keluarga seri berbeda material, penyambungan tersebut **dihapus**. Nilai utama BIS pada bulan itu kembali missing. CSV panel, workbook dan coverage dibangun ulang.

Seri GEM penuh kini disimpan terpisah di [FX_Bilateral_WBGEM_Alternative.csv](../../archive/v1_20261117_before_hs6_rebuild/intermediate/FX_Bilateral_WBGEM_Alternative.csv). Jika memakai alternatif ini, pilih keluarga sumber yang konsisten untuk seluruh periode, bukan mencampurkan satu bulan. Ini konsekuensi audit, bukan bukti bahwa seluruh BIS atau GEM salah.

### Penyelarasan tahun fiskal untuk audit GDP

WDI tidak selalu memakai tahun kalender. Untuk pembanding, India tahun y disusun dari April y–Maret y+1; Australia tahun y dari Juli y−1–Juni y. Basis indeks pembanding 2015 juga dihitung untuk periode fiskal yang sama. Label kuartal pada dataset utama tidak dipindahkan. [Penjelasan World Bank](https://datahelpdesk.worldbank.org/knowledgebase/articles/201203-are-all-wdi-series-on-a-calendar-year-reporting-pe).

### Lonjakan bukan otomatis data salah

Penyaringan perubahan bulanan lebih dari 10% menghasilkan 22 baris pada panel. Sebagian besar adalah dua perubahan IDR/USD yang diulang di sepuluh mitra, ditambah perubahan AUD dan KRW saat krisis. Tidak dilakukan winsorization atau penghapusan otomatis. Rinciannya ada di [Macro_Audit_Large_Monthly_Changes.csv](../../archive/v1_20261117_before_hs6_rebuild/intermediate/Macro_Audit_Large_Monthly_Changes.csv).

## Keputusan penggunaan untuk penelitian

1. **CPI:** gunakan `CPI_Index_2015mean100`/`Partner_CPI_Index_2015mean100` untuk spesifikasi CPI. `Price_Index_2015mean100` dapat memuat WPI India; jangan tertukar.
2. **Kurs:** hitungan NER/RER lulus pemeriksaan aritmetika. Untuk Thailand dan Vietnam, lakukan sensitivitas antarseri penuh BIS dan GEM dan verifikasi konsep quotation terhadap bank sentral; belum ada dasar menyatakan keduanya interchangeable.
3. **GDP:** gunakan indeks, bukan menjumlahkan native LCU antarnegara. GDP awal Indonesia, India dan Vietnam memerlukan uji sensitivitas vintage/periode. Verifikasi semua kuartal terhadap statistik nasional belum dilakukan.
4. **Trade balance agregat:** seri GEM customs adalah pilihan yang didokumentasikan, tetapi periode 2006–2009 belum lolos rekonsiliasi konsep lintas sumber. Jangan memilih sumber berdasarkan koefisien yang mendukung hipotesis.
5. **Kekosongan:** CPI AS Oktober 2025 dan kurs Vietnam Agustus 2025 tetap missing di keluarga utama. Jangan drop kuartal lalu menganggap jaraknya tetap satu kuartal saat membentuk lag NARDL.
6. **Data awal user:** source mentah CEIC/ITC asli tidak tersedia di folder Tio. Audit memastikan nilainya tidak berubah, tetapi tidak mengesahkan seluruh observasi awal terhadap file sumber berlisensi.

`Ready_NARDL_*` hanya indikator variabel tersedia. Itu bukan sertifikat kelayakan model, tidak menggantikan uji I(2), kointegrasi, structural break, kecukupan sampel atau validitas kausal.

## Reproduksi

```powershell
python Tio/script/03_merge_macro_external.py
python Tio/script/04_validate_macro_external.py
python Tio/script/05_audit_macro_sources.py
```

Untuk mengunduh pembanding yang belum ada, tambahkan `--download` pada skrip 05. Skrip 05 tidak mengganti observasi penelitian utama; ia menghasilkan tabel audit dan alternatif kurs.

Dokumentasi primer pendukung: [BIS consumer prices](https://www.bis.org/pages/statistics/cp-long-series-documentation.pdf), [BIS USD exchange rates](https://www.bis.org/pages/statistics/xrusd-documentation.pdf), [WDI annual periods](https://datahelpdesk.worldbank.org/knowledgebase/articles/201203-are-all-wdi-series-on-a-calendar-year-reporting-pe). Dokumentasi BIS menjelaskan proksi harga dan asal kurs; penyebab setiap selisih compiler yang ditemukan belum semuanya teridentifikasi.
