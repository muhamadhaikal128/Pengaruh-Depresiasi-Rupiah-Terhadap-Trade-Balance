# Ringkasan hasil

Haikal, 16 Nov 2026. Baca ini dulu; detailnya ada di:
- [2_hasil_ardl.md](2_hasil_ardl.md)
- [3_hasil_lp.md](3_hasil_lp.md)
- [4_litrev_metode.md](4_litrev_metode.md)

**Cara membaca angka:** semua efek = perubahan rasio **ekspor/impor** (%) akibat depresiasi riil rupiah 10%. **Positif = trade balance membaik**, negatif = memburuk. Angka tebal signifikan di level 10%.

## Kesimpulan utama

**Depresiasi rupiah tidak memperbaiki trade balance Indonesia; dalam jangka pendek–menengah justru memperburuk.** Kesimpulan ini konsisten di dua metode (ARDL dan local projections) dan di semua uji ketahanan.

## RQ1: apakah depresiasi meningkatkan trade balance?

**Tidak.**

| | Bulan 0 | Bulan 6 | Bulan 12 | Bulan 24 | Jangka panjang |
|:--|--:|--:|--:|--:|--:|
| ARDL | **−7,1** | −8,3 | −7,3 | −6,5 | −4,9 (tidak signifikan) |
| LP | **−5,7** | **−8,8** | **−10,2** | −5,2 | – |

- **Tidak ada J-curve:** trade balance tidak pernah berbalik membaik.
- **Marshall-Lerner tidak terpenuhi:** efek jangka panjang tidak signifikan di semua 10 spesifikasi ARDL.
- **NARDL:** efek depresiasi dan apresiasi simetris.

## RQ2: per negara mitra

| Mitra | ARDL | LP (kurs riil bilateral, FE mitra + bulan) | Kesimpulan |
|:--|:--|:--|:--|
| **China** | memburuk (−23% di bln 12) | **−11% bln 0, −18% bln 12** | **Paling terdampak** |
| **Jepang** | **−17% bln 0** | **−10% bln 0, −12% bln 12** | **Paling terdampak** |
| Thailand | membaik, tidak signifikan | **−15% bln 12** | Tidak konsisten |
| AS | membaik (+19%, kointegrasi batas) | ≈ 0 | **Tidak robust** |
| Australia, India, Korea, Malaysia, Singapura, Vietnam | tidak signifikan | tidak signifikan | Tidak ada efek jelas |
| Rata-rata | PMG/MG ≈ 0 | ≈ 0 | – |

Indonesia mengimpor barang modal dan bahan baku dari China dan Jepang. Impor itu sulit diganti, jadi saat rupiah melemah, nilai impornya membengkak.

## RQ3: per kelompok barang

| Kelompok | Pangsa ekspor | ARDL | LP | Kesimpulan |
|:--|--:|:--|:--|:--|
| **Energi & tambang** | 42% | −20% (tidak signifikan) | **−22% bln 12** | **Memburuk** |
| **Bahan baku/penolong** | 79%* | **−7% bln 0** | **−10% bln 12** | **Memburuk** |
| Barang modal | 5% | **−13% bln 0** | −8% bln 0 (tidak signifikan) | Memburuk di awal |
| Komoditas (total) | 61% | −13% jangka panjang (p = 0,07) | tidak signifikan | Cenderung memburuk |
| **Pertanian & pangan** | 19% | ≈ 0 | **+22% bln 24** | **Satu-satunya yang membaik** (butuh sekitar 2 tahun) |
| Barang konsumsi | 16% | membaik, tidak signifikan | +9% bln 24 (p = 0,10) | Cenderung membaik |
| Manufaktur | 39% | pola mirip J-curve, tidak signifikan | ≈ 0 | J-curve tidak terkonfirmasi |

\*Batu bara, CPO dan nikel ikut terhitung sebagai bahan baku di klasifikasi end-use. Dua pengelompokan (komoditas vs non-komoditas, dan end-use) saling tumpang tindih, jadi pangsanya tidak dijumlahkan.

Komoditas dihargai dalam USD di pasar dunia dan volumenya ditentukan sisi suplai, sehingga rupiah murah tidak menambah ekspor. Sebaliknya, impor bahan baku dan barang modal langsung lebih mahal. Hanya produk yang sensitif harga (pangan olahan, barang konsumsi) yang perlahan diuntungkan.

## Metode, singkat

- **ARDL** dipakai sebagai baseline, karena standar di literatur J-curve dan studi Indonesia. Kelemahannya: rawan endogenitas, karena rupiah dan neraca sama-sama digerakkan siklus komoditas.
- **Local projections dengan kurs riil bilateral dan FE waktu** lebih kredibel, karena guncangan bersama ikut terserap.
  - Hasil yang **bertahan** di kedua metode: China, Jepang, energi/tambang, bahan baku.
  - Hasil yang **hilang** di LP: AS membaik, dan J-curve manufaktur.
- **LP-IV** dengan indeks dolar AS gagal (instrumen lemah, F = 0,14), jadi tidak dipakai.

## Keterbatasan

1. Pendapatan domestik Indonesia belum masuk model agregat. Di panel LP, faktor ini sudah terserap FE waktu.
2. CPI Vietnam masih pendekatan dari inflasi tahunan; hasil tanpa Vietnam tetap sama.
3. Data dalam nilai USD, jadi efek harga dan volume belum dipisah.
4. Cakupannya hanya 10 mitra, dengan data sampai Agu-2026.
