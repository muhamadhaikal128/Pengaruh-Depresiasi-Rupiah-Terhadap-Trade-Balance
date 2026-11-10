# Pengaruh Depresiasi Rupiah terhadap Trade Balance

> Status: struktur proyek disiapkan (10 Nov 2026). Isi model, data, dan hasil menyusul.

## Pertanyaan riset
Seberapa besar dan seberapa cepat depresiasi Rupiah memengaruhi neraca perdagangan (trade balance)
Indonesia? (Termasuk cek efek J-curve / kondisi Marshall-Lerner.)

## Struktur folder

| Folder | Isi |
|:--|:--|
| `input/raw/` | Data mentah apa adanya dari sumber (BPS, BI, SEKI, Bloomberg, dll.). Jangan diedit. |
| `input/reference/` | Paper, manual, catatan metodologi, kode referensi. |
| `intermediate/` | Dataset hasil olahan (`.dta`, `.csv`) yang dibuat script. Bisa dibuat ulang. |
| `script/` | Script analisis, diberi nomor sesuai urutan jalan (`00_master.do`, `01_import.do`, ...). |
| `output/tables/` | Tabel hasil (CSV/XLSX). |
| `output/figures/` | Grafik final (PNG/PDF). |
| `output/gph/` | Grafik Stata `.gph` (editable). |
| `output/diagnostics/` | Uji diagnostik: unit root, kointegrasi, residual, stabilitas. |
| `archive/` | Versi lama script/hasil yang sudah tidak dipakai, per subfolder versi (`v1_.../`). |
| `notes/` | Catatan kerja, draft narasi, to-do. |
| `CHANGELOG.md` | Riwayat perubahan per versi. |

## Cara menjalankan
Jalankan `script/00_master.do` dari root proyek (akan ditambahkan).
