# Presentasi penelitian HS-6

Utama.pptx berisi pembahasan penelitian. Lengkap.pptx memuat pembahasan yang sama, ditambah seluruh respons 176 model utama dan 340 sensitivitas serta grafik koefisien per pasar.

Cover, foto, master, font dan palet mengikuti template pengguna. Teks dan tabel utama dapat diedit. Rumus dirender dengan pdfLaTeX dan ditanam sebagai SVG dengan PNG fallback; sumber LaTeX, PDF vector dan SVG tersedia dalam equations/. Grafik berasal dari hasil Stata yang telah ada, bukan estimasi baru.

Grafik respons memakai perubahan log rasio ekspor/impor agar nilai positif berarti perbaikan. Ini pembalikan tanda tepat dari outcome model log impor/ekspor. Interval ikut ditransformasi. Guncangan kedua arah simetris dalam log, bukan dalam persen aritmetika. Pola J eksploratif tidak sama dengan uji kausal atau uji simultan.

slide_index.csv memuat daftar isi. model_response_slide_index.csv memetakan setiap model ke halaman atlas. slide_notes.md memuat pembahasan dan sumber setiap slide. assets/ memuat data deskriptif dan grafik PNG/PDF. deck_validation.json memuat checksum, kelengkapan model, pelestarian template dan pemeriksaan render.

Reproduksi: jalankan script/10_build_research_ppt.py, kemudian script/11_render_research_ppt.py. Paket Python mengikuti lingkungan proyek. Tidak ada dataset atau hasil estimasi yang diganti saat membuat deck.

## Cakupan negara pelapor

Seluruh perdagangan adalah milik Indonesia. World/WLD menunjukkan seluruh negara mitra, bukan perdagangan global antarsemua negara. Regresi barang membandingkan tujuh kelompok yang dibentuk dari HS-6; regresi tiap kode HS-6 belum dilakukan. Bukti pemeriksaan metadata dan 5.456 nilai TOTAL bulanan tersedia dalam scope_audit_indonesia.json.
