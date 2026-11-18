# Deck penelitian ARDL/NARDL

Disusun 17 November 2026. Versi final ada di [PPTX](../output/presentation/Depresiasi_Rupiah_Trade_Balance_Tio_20261117_final.pptx) dan [PDF](../output/presentation/Depresiasi_Rupiah_Trade_Balance_Tio_20261117_final.pdf).

Deck terdiri atas 35 slide: 24 slide utama, 1 divider lampiran, dan 10 slide lampiran. Urutan: pertanyaan umum, perdagangan deskriptif, komposisi mitra/komoditas, definisi variabel dan statistik sampel, cakupan data, metode ARDL/NARDL, hasil dunia/bilateral/jenis barang, diagnostik, sensitivitas, kesimpulan dan agenda lanjut. Sumber serta narasi tersedia pada speaker notes dan `output/presentation/slide_notes.md`.

Template mengikuti benchmark pengguna: cover foto, logo, master, layout, Arial Nova/Arial dan palet cokelat-krem. Seluruh 8 bagian XML master/layout/theme tetap identik secara kanonik dengan acuan. Gambar grafik dibuat ulang dengan matplotlib; teks dan tabel PowerPoint dapat diedit. Font matematika/simbol mengikuti fallback PowerPoint.

Statistik deskriptif agregat memakai tepat 61 kuartal tanggal estimasi 2011Q1?2026Q1. Statistik komposisi memakai tahun lengkap 2025 dan hanya 10 mitra. Pangsa komoditas 2025 sekitar 49,5%, bukan angka gabungan semua periode sekitar 58%. Outcome replikasi tetap ln(M/X), bukan ln(X?M), dan bukan persamaan ekspor tersendiri. Belum ada dukungan levels 5% pada baseline dunia; perbandingan sensitivitas kelompok belum diuji secara formal. Hipotesis input impor tetap ditangguhkan.

Pemeriksaan: 35 slide dirender PowerPoint, PDF 35 halaman dan PNG 35 gambar. Pemeriksaan tinggi teks dan sel tabel tidak menemukan overflow. Seluruh slide diperiksa melalui contact sheets; beberapa slide utama juga pada ukuran penuh. Angka 27/18/7 model tersaring diperiksa ulang. Enam input utama mempunyai checksum sebelum/sesudah identik. Hasil estimasi dan panel penelitian tidak ditulis ulang.

Reproduksi: `script/17_build_research_deck.py`, lalu `script/18_render_research_deck.py`; paket di `requirements_presentation.txt`. Template asli disalin ke `input/reference/presentation_template/`. File tanpa suffix `_final` dalam folder presentasi merupakan draf render awal, bukan versi yang disarankan.
