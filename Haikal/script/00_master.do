* =============================================================================
* 00_master.do : jalankan seluruh analisis Haikal dari awal
*   Jalankan dari folder Haikal/:   cd ".../Haikal"   lalu   do script/00_master.do
*   Prasyarat: Stata 17+, paket ssc: ardl (Kripfganz & Schneider), xtpmg
*   Data intermediate/ dari script/01_build_panel.py (Tio); harga komoditas dari FRED
*   (input/raw/fred/*.csv, diunduh 16 Nov 2026).
* =============================================================================
version 19
clear all
set more off
capture mkdir output/tables
capture mkdir output/figures
capture mkdir output/diagnostics

foreach p in ardl xtpmg {
    capture which `p'
    if _rc ssc install `p'
}

do script/02_prep_data.do          // dataset analisis + klasifikasi HS-4
do script/ardl_helpers.do          // program ardl_post
do script/03_ardl_agregat.do       // RQ1: agregat, robustness, NARDL, J-curve
do script/04_ardl_mitra.do         // RQ2: per mitra dagang + panel PMG
do script/05_ardl_kelompok.do      // RQ3: per kelompok barang
