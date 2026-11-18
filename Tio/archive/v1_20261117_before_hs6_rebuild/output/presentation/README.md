# Deck penelitian: depresiasi rupiah dan trade balance

PPTX mengikuti cover, logo, master, layout, font dan tema benchmark pengguna. Isi merupakan hasil estimasi awal proyek Tio per 17 November 2026, bukan klaim pengesahan institusional.

- `Depresiasi_Rupiah_Trade_Balance_Tio_20261117_final.pptx`: presentasi final editable. File tanpa akhiran `_final` adalah draf render awal.
- PDF dan `slides/`: hasil render PowerPoint jika tersedia.
- `assets/`: grafik PNG/PDF dan CSV statistik deskriptif yang dipakai dalam deck.
- `slide_notes.md`: sumber, definisi, narasi, dan batas interpretasi setiap slide.
- `deck_validation.json`: checksum, pelestarian template, dan pemeriksaan hasil.

Reproduksi: jalankan `script/17_build_research_deck.py`, lalu `script/18_render_research_deck.py`. Set `PYTHONPATH` sesuai paket proyek. Template disimpan pada `input/reference/presentation_template/`. Grafik ilmiah dibangun dengan matplotlib; teks dan tabel utama dalam PPT dapat diedit. Data mentah, panel, dan hasil estimasi tidak diubah.

Sampel: statistik agregat N=61 memakai tanggal desain estimasi 2011Q1–2026Q1. Grafik tahunan dan komposisi 2025 memakai tahun lengkap, dengan penyebut 10 mitra untuk grafik bilateral/jenis barang. Koefisien yang tidak mendapat dukungan levels tetap diperlihatkan dan ditandai. P-value/interval nominal setelah seleksi AIC; BH eksploratif bukan koreksi seleksi model.
