# Data HS-6 UN Comtrade: cakupan, kualitas, dan penggabungan

Tanggal penyusunan: 17 November 2026. Data baru disimpan terpisah; hasil model dan PPT lama belum dihitung ulang.

## Hasil unduhan

- Permintaan mulai 2006. Data bulanan yang tercantum/terambil pada vintage ini: **201212–202609**, 163 bulan; **6,383,850 baris** produk–mitra–arus–bulan.
- Data tahunan pelengkap: **2006–2025**, **1,232,708 baris**. Data ini tetap tahunan, tidak dibagi menjadi bulan atau kuartal.
- Bulan kosong di tengah cakupan: **2013-09, 2014-11, 2014-12**. Periode 2006 sampai sebelum Desember 2012 tidak tersedia pada unduhan bulanan ini. Oktober 2026 belum tercantum saat diambil.
- Reporter: Indonesia. Sepuluh mitra sesuai penelitian ditambah World (seluruh mitra). World jangan dijumlahkan lagi dengan sepuluh mitra karena akan menghitung perdagangan dua kali.
- India memakai kode Comtrade 699; AS memakai wilayah perdagangan 842 (termasuk Puerto Riko dan US Virgin Islands). Definisi tersimpan di manifest.

## Berat dan kuantitas

Angka berikut memakai perdagangan Indonesia–dunia saja agar tidak menggandakan total dunia dengan bilateral:

- Impor: 94.39% nilai perdagangan mempunyai berat bersih positif; 73.06% baris mempunyai kuantitas dengan kode satuan valid; 13.33% nilai terkait baris dengan flag berat estimasi.
- Ekspor: 96.95% nilai perdagangan mempunyai berat bersih positif; 73.96% baris mempunyai kuantitas dengan kode satuan valid; 11.86% nilai terkait baris dengan flag berat estimasi.

Berat bersih dalam kg tidak sama dengan kuantitas tambahan dalam unit produk. Nilai nol, missing, kode satuan tidak valid dan flag estimasi dipertahankan. Pada file bulanan/tahunan, angka 0 pada Quantity dengan kode satuan -1 bukan observasi volume nol yang valid; gunakan flag Quantity_Usable dan Weight_Usable. Unit value dihitung per produk–mitra–periode dan hanya jika penyebut positif. Ia masih dapat berubah karena kualitas/komposisi dalam HS-6, sehingga bukan indeks harga murni. Menjumlahkan kg dari seluruh jenis produk tidak membentuk ukuran volume ekspor yang sebanding secara ekonomi.

## Lokasi file

- Raw respons API: `input/raw/un_comtrade_hs6_20261117/`; manifest berisi parameter, waktu, jumlah baris dan checksum tanpa API key.
- [Workbook audit](../output/tables/comtrade_hs6/Comtrade_HS6_Data_Audit.xlsx).
- [Panel total kuartalan + makro](../intermediate/comtrade_hs6/Trade_Total_Quarter_Macro.csv).
- [Panel total bulanan + makro](../intermediate/comtrade_hs6/Trade_Total_Month_Macro.csv).
- [Total tahunan](../intermediate/comtrade_hs6/Trade_Total_Annual.csv).
- Panel produk bulanan: `intermediate/comtrade_hs6/monthly/` (CSV.GZ, dipartisi per kuartal).
- Panel produk kuartalan: `intermediate/comtrade_hs6/quarterly/`; format long dan dua arus + GDP/kurs/CPI/harga komoditas.
- Panel produk tahunan: `intermediate/comtrade_hs6/annual/`.
- [Indeks file/checksum](../intermediate/comtrade_hs6/File_Index.csv).
- [Klasifikasi komoditas HS-6 menurut revisi](../intermediate/comtrade_hs6/HS6_Commodity_Classification_By_Edition.csv).
- [Deskripsi produk menurut revisi](../intermediate/comtrade_hs6/HS6_Product_Codebook_By_Edition.csv) dan [kamus variabel](../intermediate/comtrade_hs6/Data_Dictionary.csv).
- Audit rinci: `output/diagnostics/comtrade_hs6/`.

## Aturan pengolahan

1. Data asli tidak diedit; respons JSON/CSV dikompresi lossless. Probe awal tidak masuk manifest produksi dan tidak dipakai untuk panel.
2. Nilai USD dibagi 1.000 hanya pada kolom USDk. Pengecekan dilakukan terhadap TOTAL Comtrade dengan reporter, mitra, arus dan periode yang sama.
3. Kunci menyertakan revisi HS asli. **Belum ada harmonisasi HS antarwaktu**; kode identik antarversi tidak otomatis dianggap produk identik. Ini wajib diperhatikan sebelum model produk jangka panjang.
4. Kelas komoditas memakai korespondensi langsung HS-6–SITC3 per revisi dan definisi UNCTAD A11. Kategori campuran/tidak terklasifikasi dipertahankan, tidak diberi label nonkomoditas secara paksa.
5. Ketidakhadiran baris produk–bulan tidak diubah otomatis menjadi nol. `Observed_*` kuartalan menyimpan jumlah baris yang tersedia; kolom utama kuartalan mensyaratkan tiga baris produk–bulan nyata. Kuantitas tambahan juga mensyaratkan satuan konsisten.
6. GDP hanya digabungkan sebagai variabel kuartalan; tidak diinterpolasi menjadi GDP bulanan. Makro lama tetap mempunyai catatan audit sebelumnya, termasuk CPI/FX yang kosong dan proksi permintaan dunia.
   Arah RER bilateral lama: naik=depresiasi. REER BIS dunia: naik=apresiasi. Transformasi tanda untuk model paper belum dilakukan pada panel data ini.
7. Pengecekan integritas bukan pengesahan semua sumber sudah harmonis. Selisih dengan dataset lama dilaporkan, tidak dihilangkan dengan rescaling.

## Status validasi

- Status: **PASS_WITH_DATA_LIMITATIONS**.
- Maksimum absolut selisih jumlah HS-6 vs TOTAL: **0.00000066%**; 0 baris melebihi ambang review 0,01%.
- Panel penelitian lama: checksum tidak berubah.
- Perbandingan tahunan 2006–2009 menunjukkan Comtrade dekat dengan GEM; ini belum merekonsiliasi selisih historis terhadap WDI pada audit sebelumnya.
- Ekspor–impor HS-6 bulanan lengkap sejak 2006: **belum tersedia** dari unduhan ini. Untuk memperpanjang seri volume, cari sumber pelengkap BPS/TradeMap dengan definisi dan revisi HS yang dapat direkonsiliasi.
- Kelengkapan makro, harmonisasi HS, penyaringan seri dan desain identifikasi masih perlu ditangani sebelum estimasi baru. Tidak ada klaim hipotesis telah diuji dengan data baru.

## Reproduksi

Jalankan skrip 19 (unduh/resume), 20 (panel/audit), 21 (workbook/laporan), serta 22 (kamus deskripsi publik) dari folder `script/`. Key dibaca dari `.env.comtrade` lokal yang diabaikan Git; jangan menaruh key pada argumen command line, log, URL tersimpan atau raw.

Rujukan primer: [API UN Comtrade](https://comtradeplus.un.org/en/api-docs), [metadata kolom](https://comtradeplus.un.org/en/reference-tables?table=dataitem), [kuota](https://comtradeplus.un.org/en/subscriptions), dan [klasifikasi UNSD](https://unstats.un.org/unsd/classifications/Econ).
