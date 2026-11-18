* =============================================================================
* 00_master.do : jalankan seluruh analisis Haikal dari awal (sekitar 13 menit)
*   Jalankan dari folder Haikal/:   cd ".../Haikal"   lalu   do script/00_master.do
*   Prasyarat: Stata 17+; paket SSC ardl, xtpmg, xtscc (diinstal otomatis)
*   Input : intermediate/dari_tio/ (data panel Tio, dari 01_build_panel.py)
*           input/raw/fred/, input/raw/bis/ (diunduh 16 Nov 2026)
*   Output: intermediate/analisis/ (dataset olahan)
*           output/0_deskriptif/, output/1_ardl/, output/2_lp/
* =============================================================================
version 19
clear all
set more off
foreach d in intermediate/analisis output/0_deskriptif output/1_ardl output/2_lp {
    capture mkdir `d'
}
foreach p in ardl xtpmg xtscc {
    capture which `p'
    if _rc ssc install `p'
}

* --- 1. Data
do script/02_prep_data.do            // dataset analisis + klasifikasi HS-4 ke kelompok barang
do script/03_prep_kurs_bilateral.do  // kurs riil bilateral (BIS) + panel untuk LP

* --- 2. ARDL
do script/helper_ardl.do             // program ardl_post
do script/04_ardl_agregat.do         // RQ1: agregat, robustness, NARDL
do script/05_ardl_mitra.do           // RQ2: per mitra + panel PMG/MG
do script/06_ardl_kelompok.do        // RQ3: per kelompok barang

* --- 3. Local projections
do script/07_local_projections.do    // RQ1-RQ3 dengan LP (~10 menit)
