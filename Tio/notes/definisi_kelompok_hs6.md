# Definisi tujuh kelompok HS-6 dan keterbatasannya

Sumber klasifikasi: tabel korespondensi resmi UNSD HS/SITC/BEC (2022), korelasi langsung HS/SITC3, dan manual BEC5. Data perdagangan: 22 workbook pengguna, Januari 2006 sampai Agustus 2026, USD ribu. Ini analisis nilai perdagangan, bukan kandungan input impor.

| Kelompok | Aturan |
|---|---|
| Non-komoditas (manufaktur) | Kategori nonkomoditas pada definisi UNCTAD A11; SITC3 bagian 5, 6, 7, 8 dengan pengecualian komoditas mineral/logam A11 |
| Barang konsumsi | BEC5, SNA end use=final consumption |
| Komoditas pertanian & pangan | A11 pangan/minuman/tembakau/minyak serta bahan mentah pertanian |
| Bahan baku/penolong | BEC5, SNA end use=intermediate consumption; bukan ukuran input asing dalam ekspor |
| Barang modal | BEC5, SNA end use=gross fixed capital formation |
| Komoditas (total) | UNCTAD A11: SITC3 bagian 0+1+2+3+4 serta divisi 68 dan grup 667, 971 |
| Komoditas energi & tambang | A11 bahan bakar, bijih/mineral, logam nonferrous, batu mulia dan emas nonmoneter terkait |

**Ketujuh kelompok tidak eksklusif.** Konsumsi/intermediate/modal berada pada sumbu penggunaan; komoditas/nonkomoditas berada pada sumbu karakter barang. Pertanian dan energi/tambang merupakan rincian dari total komoditas. Menjumlahkan ketujuh nilai akan menghitung sebagian perdagangan lebih dari sekali.

Workbook tidak menyatakan revisi HS per sel. Daftar produk memuat kode lama dan baru. Untuk menghindari penetapan revisi tanpa bukti, klasifikasi utama memakai konsensus per kode HS-6 dari korespondensi lintas revisi. Konsensus berbeda tidak dipaksa menjadi salah satu kelas; mixed/unclassified dipertahankan dan dikeluarkan dari kelompok yang belum dapat dipastikan. Daftar lengkap dan kemungkinan kode BEC ada pada intermediate/HS6_Classification.csv.

Cakupan klasifikasi dihitung menurut nilai dan jumlah kode per negara/arus di output/diagnostics/data/Classification_Coverage.csv. Pangsa seluruh periode tidak boleh dilabel sebagai pangsa tahun tertentu. Total dunia tidak boleh dijumlahkan kembali dengan nilai sepuluh mitra.

Nol eksplisit pada workbook tetap nol; blank tidak diubah nol. Kuartal utama mensyaratkan tiga bulan. Juli-Agustus 2026 belum menjadi kuartal III lengkap. Agregat dan bilateral memakai baris TOTAL agar tidak terpengaruh akumulasi pembulatan setiap HS-6; kelompok memakai jumlah kode yang diklasifikasikan. Selisih HS6 vs TOTAL ditampilkan dan dibandingkan batas pembulatan 0,5 ribu USD per baris.

Model memakai ln(M/X), PDB riil Indonesia/mitra, dan q dengan arah naik=apresiasi. Analisis ini tidak mengidentifikasi efek ekspor secara terpisah atau efek volatilitas kurs. Kanal input impor/TiVA dikeluarkan. Sampel mengikuti jendela lengkap berurutan dan tidak dirapatkan melewati celah. Perbandingan signifikansi kelompok yang berbeda bukan uji beda koefisien.

Baca notes/hasil_ardl_nardl_hs6.md setelah run selesai. Audit makro historis ada di input/reference/audit_validitas_data_macro.md; keterbatasan CPI, FX dan vintage GDP masih berlaku.

Sumber primer: https://unstats.un.org/unsd/classifications/Econ/ dan input/reference/classification_sources/unsd_bec5_manual.pdf.
