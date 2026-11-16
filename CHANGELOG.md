# Changelog: Pengaruh Depresiasi Rupiah terhadap Trade Balance

## v0 — 10 Nov 2026: struktur proyek
- Folder `input/`, `intermediate/`, `script/`, `output/`, `archive/`, `notes/` dibuat
  mengikuti struktur proyek Simulasi-Rupiah.
## v0.1 — 15 Nov 2026: panel gabungan perdagangan, IPI/GDP, REER, JISDOR
- Panel 10 mitra dagang utama (Jan 2006 – Okt 2026): ekspor/impor total, IPI YoY, GDP YoY, REER BIS (broad, real), JISDOR (rata-rata dan akhir bulan), disimpan di `intermediate/Panel_Country_Month.csv` dan `intermediate/Panel_Gabungan_Indonesia.xlsx`.
- Data perdagangan HS-4 per mitra (nilai dan YoY) di `intermediate/hs_panel/`.
- Script `01_build_panel.py` untuk membuat ulang semua dataset di atas.
- Catatan data (definisi variabel dan keterbatasan seri) di `notes/catatan_data_panel.md`.
## v0.2 — 16 Nov 2026: folder kerja per orang
- Repo dibagi jadi `Haikal/` dan `Tio/` supaya tidak conflict. Masing-masing hanya mengedit folder sendiri.
- Isi lama (`input/`, `intermediate/`, `script/`, `output/`, `archive/`, `notes/`) disalin ke kedua folder. Root sekarang hanya berisi README, CHANGELOG, `.gitignore`.