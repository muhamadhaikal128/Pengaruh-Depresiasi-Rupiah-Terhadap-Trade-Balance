## Versi bahasa lebih mudah — 18 November 2026

Mulai dari **Depresiasi_Rupiah_Trade_Balance_Indonesia_HS6_Tio_Bahasa_Mudah.pdf** untuk versi yang lebih natural. Penjelasan diperbarui dan istilah Inggris yang umum dipertahankan. Angka, tabel dan hasil estimasi sama; PDF sebelumnya tetap tersedia sebagai referensi teknis.

# Naskah penelitian elaboratif

Mulai dari Depresiasi_Rupiah_Trade_Balance_Indonesia_HS6_Tio.pdf. Ini naskah kerja berbasis hasil Stata run 17 November 2026, bukan artikel jurnal yang telah melalui peer review.

paper.tex, sections/, numbers.tex dan tables/ adalah sumber LaTeX yang dapat diedit. assets/ memuat grafik PDF vector, PNG dan data tabel. Lampiran mempertahankan 176 model utama dan 340 sensitivitas. Semua perdagangan adalah milik Indonesia; model barang adalah tujuh kategori hasil klasifikasi HS-6.

Reproduksi: jalankan script/12_build_research_paper.py dengan paket Python proyek dan pdfLaTeX lokal. Pertahankan sumber paper.tex serta sections/ di folder ini. Generator menarik angka dari keluaran Stata tanpa mengestimasi ulang model. paper_validation.json mencatat checksum, kelengkapan dan pemeriksaan tata letak.

Untuk belajar: mulai dengan definisi rasio dan orientasi kurs; baca hasil agregat, uraian tiap mitra dan kelompok; lalu bandingkan pola titik dengan diagnostik serta sensitivitas. Seluruh respons 516 model juga tersedia dalam PPT lengkap.
