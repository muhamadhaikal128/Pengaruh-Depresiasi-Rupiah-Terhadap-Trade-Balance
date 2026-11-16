* =============================================================================
* 02_prep_data.do : bangun dataset analisis dari intermediate/ (output 01_build_panel.py)
*   1. Indeks harga komoditas IMF (FRED)        -> intermediate/commodity_prices.dta
*   2. Panel negara x bulan + variabel log       -> intermediate/ana_partner.dta
*   3. Agregat 10 mitra x bulan                  -> intermediate/ana_aggregate.dta
*   4. Klasifikasi HS-4 (komoditas / end-use)    -> intermediate/hs4_groups.csv
*   5. Perdagangan per kelompok barang x bulan   -> intermediate/ana_group.dta
* Dijalankan dari folder Haikal/ (lihat 00_master.do)
* =============================================================================
version 19
clear
set more off

* -----------------------------------------------------------------------------
* 1. Harga komoditas IMF Primary Commodity Prices (2016=100), sumber FRED
*    PALLFNFINDEXM = all commodities, PNRGINDEXM = energi, PFANDBINDEXM = pangan & minuman
* -----------------------------------------------------------------------------
tempfile com
local first = 1
foreach s in PALLFNFINDEXM PNRGINDEXM PFANDBINDEXM {
    import delimited using "input/raw/fred/`s'.csv", clear varnames(1)
    rename observation_date d
    rename `=lower("`s'")' `s'
    gen mdate = mofd(date(d, "YMD"))
    keep mdate `s'
    if !`first' merge 1:1 mdate using `com', nogen
    save `com', replace
    local first = 0
}
format mdate %tm
gen lncom     = ln(PALLFNFINDEXM)
gen lncom_nrg = ln(PNRGINDEXM)
gen lncom_fd  = ln(PFANDBINDEXM)
label var lncom     "ln harga komoditas IMF (all)"
label var lncom_nrg "ln harga komoditas IMF (energi)"
label var lncom_fd  "ln harga komoditas IMF (pangan)"
save intermediate/commodity_prices.dta, replace

* -----------------------------------------------------------------------------
* 2. Panel negara x bulan
* -----------------------------------------------------------------------------
import delimited using intermediate/Panel_Country_Month.csv, clear encoding(utf8)
gen mdate = monthly(date, "YM")
format mdate %tm
keep if !missing(exports_usdk)                 // perdagangan s.d. 2026m8
merge m:1 mdate using intermediate/commodity_prices.dta, keep(master match) nogen

encode iso3, gen(cid)
xtset cid mdate
gen month   = month(dofm(mdate))
forvalues k = 2/12 {
    gen m`k' = month == `k'                    // dummy musiman (ardl tidak terima i.month)
}
gen lntb    = ln(exports_usdk / imports_usdk)
gen lnx     = ln(exports_usdk)
gen lnm     = ln(imports_usdk)
gen lnreer  = ln(reer_bis_broad)
gen lnjis   = ln(jisdor_avg)
gen covid   = inrange(mdate, tm(2020m3), tm(2020m8))
gen gfc     = inrange(mdate, tm(2008m10), tm(2009m6))

* Permintaan luar negeri: rata-rata IPI YoY mitra tertimbang ekspor (bobot = pangsa ekspor
* rata-rata 2006-2026 di antara negara yang IPI-nya tersedia bulan itu).
bysort cid: egen xw = total(exports_usdk)
gen w_ipi = xw * !missing(ipi_yoy_pct)
bysort mdate: egen sw = total(w_ipi)
bysort mdate: egen yf_avg = total(w_ipi * ipi_yoy_pct / sw)
replace yf_avg = . if sw == 0
* IPI mitra: pakai IPI negara itu sendiri bila tersedia, kalau tidak pakai rata-rata mitra
gen yf = ipi_yoy_pct
gen yf_own = !missing(ipi_yoy_pct)
replace yf = yf_avg if missing(yf)
drop xw w_ipi sw

label var lntb   "ln(Ekspor/Impor)"
label var lnreer "ln REER BIS (naik = apresiasi riil)"
label var lnjis  "ln JISDOR Rp/USD (naik = depresiasi)"
label var yf     "IPI YoY mitra (%)"
label var yf_avg "IPI YoY rata-rata 10 mitra tertimbang ekspor (%)"
save intermediate/ana_partner.dta, replace

* -----------------------------------------------------------------------------
* 3. Agregat 10 mitra
* -----------------------------------------------------------------------------
collapse (sum) exports_usdk imports_usdk (first) reer_bis_broad jisdor_avg lncom lncom_nrg lncom_fd ///
         yf_avg month m2-m12 covid gfc, by(mdate)
tsset mdate
gen lntb   = ln(exports_usdk / imports_usdk)
gen lnx    = ln(exports_usdk)
gen lnm    = ln(imports_usdk)
gen lnreer = ln(reer_bis_broad)
gen lnjis  = ln(jisdor_avg)
gen t      = _n
label var lntb   "ln(Ekspor/Impor), 10 mitra"
label var lnreer "ln REER BIS (naik = apresiasi riil)"
label var lnjis  "ln JISDOR Rp/USD (naik = depresiasi)"
label var yf_avg "IPI YoY mitra tertimbang (%)"
save intermediate/ana_aggregate.dta, replace

* -----------------------------------------------------------------------------
* 4. Klasifikasi HS-4
*    sector : 1 Komoditas pertanian/pangan, 2 Komoditas energi & tambang, 3 Manufaktur
*             (komoditas ~ definisi UNCTAD: SITC 0,1,2,3,4,68,667,971; dipetakan ke HS-4,
*              ditambah 7202 ferroalloy/feronikel karena relevan untuk hilirisasi nikel)
*    enduse : 1 Barang konsumsi, 2 Bahan baku/penolong, 3 Barang modal
*             (pendekatan BEC / klasifikasi impor BPS, aturan per bab + pengecualian HS-4)
* -----------------------------------------------------------------------------
import delimited using intermediate/HS_Lookup.csv, clear stringcols(1) encoding(utf8)
rename hs_code hs4
replace hs4 = substr("0000" + hs4, -4, 4)
gen ch = real(substr(hs4, 1, 2))
gen h  = real(hs4)

* --- sektor / komoditas
gen sector = 3
replace sector = 1 if inrange(ch, 1, 24)
replace sector = 1 if h == 4001 | inrange(h, 4101, 4103) | inrange(h, 4401, 4407) | inrange(h, 4701, 4707)
replace sector = 1 if inrange(h, 5001, 5003) | inrange(h, 5101, 5105) | inrange(h, 5201, 5203) | inrange(h, 5301, 5305)
replace sector = 2 if inrange(ch, 25, 27)
replace sector = 2 if inrange(h, 7101, 7112)                       // mutiara, batu mulia, emas/perak mentah
replace sector = 2 if inlist(h, 7202, 7401, 7402, 7403, 7501, 7502, 7601, 7801, 7901) | h == 8001
replace sector = 2 if inrange(h, 8101, 8112)
gen commodity = sector < 3

* --- end use (BEC-like)
gen enduse = 2                                                      // default: bahan baku/penolong
* konsumsi, per bab
replace enduse = 1 if inlist(ch, 2, 3, 4, 7, 8, 9, 16, 19, 20, 21, 22, 30, 33, 42, 43, 49)
replace enduse = 1 if inrange(ch, 61, 67) | inlist(ch, 91, 92, 93, 94, 95, 96, 97)
* pengecualian pangan
replace enduse = 1 if inlist(h, 1006, 1704, 1806, 2402, 2403, 3401)  // beras, permen, cokelat, rokok, sabun
replace enduse = 1 if inrange(h, 7113, 7118)                        // perhiasan
replace enduse = 2 if inrange(h, 1801, 1805)                        // kakao (bahan)
* mesin & listrik
replace enduse = 3 if ch == 84
replace enduse = 2 if inlist(h, 8409, 8473, 8481, 8482, 8483, 8484, 8487)                  // suku cadang
replace enduse = 1 if inlist(h, 8418, 8450)                                                // kulkas, mesin cuci
replace enduse = 3 if inlist(h, 8501, 8502, 8504, 8514, 8515, 8517, 8525, 8526) | inlist(h, 8530, 8531, 8543)
replace enduse = 1 if inlist(h, 8508, 8509, 8510, 8516, 8519, 8527, 8528)                  // elektronik rumah tangga
* kendaraan, pesawat, kapal, instrumen
replace enduse = 3 if inlist(ch, 86, 88, 89)
replace enduse = 3 if inlist(h, 8701, 8702, 8704, 8705, 8709, 8716)
replace enduse = 1 if inlist(h, 8703, 8711, 8712, 8713)
replace enduse = 2 if inlist(h, 8706, 8707, 8708, 8714)
replace enduse = 3 if ch == 90
replace enduse = 2 if inlist(h, 9001, 9002)
replace enduse = 1 if inlist(h, 9003, 9004)
replace enduse = 2 if ch == 99 | ch == 98

label define sector 1 "Komoditas pertanian & pangan" 2 "Komoditas energi & tambang" 3 "Manufaktur"
label define enduse 1 "Barang konsumsi" 2 "Bahan baku/penolong" 3 "Barang modal"
label values sector sector
label values enduse enduse
keep hs4 product sector commodity enduse
export delimited using intermediate/hs4_groups.csv, replace
save intermediate/hs4_groups.dta, replace

* -----------------------------------------------------------------------------
* 5. Perdagangan per kelompok (semua 10 mitra dijumlah) x bulan
* -----------------------------------------------------------------------------
local isos AUS CHN IND JPN KOR MYS SGP THA USA VNM
tempfile acc
local first = 1
foreach fl in Export Import {
    foreach c of local isos {
        import delimited using "intermediate/hs_panel/`fl'_`c'.csv", clear ///
            stringcols(3) encoding(utf8) colrange(:5)
        rename hs_code hs4
        replace hs4 = substr("0000" + hs4, -4, 4)
        merge m:1 hs4 using intermediate/hs4_groups.dta, keep(master match) keepusing(sector enduse)
        quietly count if _merge == 1
        if r(N) > 0 di as error "`fl' `c': `r(N)' baris HS tanpa klasifikasi -> diberi manufaktur/bahan baku"
        replace sector = 3 if _merge == 1
        replace enduse = 2 if _merge == 1
        drop _merge
        gen mdate = monthly(date, "YM")
        * simpan dua dimensi: sektor dan end use
        preserve
            collapse (sum) v = value_usdk, by(mdate sector)
            gen str20 grp = "sec" + string(sector)
            drop sector
            tempfile s
            save `s'
        restore
        collapse (sum) v = value_usdk, by(mdate enduse)
        gen str20 grp = "eu" + string(enduse)
        drop enduse
        append using `s'
        gen str6 flow = "`fl'"
        gen str3 iso3 = "`c'"
        if !`first' append using `acc'
        save `acc', replace
        local first = 0
    }
}
* total per kelompok (10 mitra), plus komoditas vs non-komoditas
collapse (sum) v, by(flow grp mdate)
reshape wide v, i(grp mdate) j(flow) string
rename (vExport vImport) (x m)
tempfile g
save `g'
keep if inlist(grp, "sec1", "sec2")
collapse (sum) x m, by(mdate)
gen grp = "comm"
append using `g'
* non-komoditas = manufaktur
expand 2 if grp == "sec3", gen(dup)
replace grp = "noncomm" if dup
drop dup

gen str40 grp_label = ""
replace grp_label = "Komoditas (total)"            if grp == "comm"
replace grp_label = "Non-komoditas (manufaktur)"   if grp == "noncomm"
replace grp_label = "Komoditas pertanian & pangan" if grp == "sec1"
replace grp_label = "Komoditas energi & tambang"   if grp == "sec2"
replace grp_label = "Manufaktur"                   if grp == "sec3"
replace grp_label = "Barang konsumsi"              if grp == "eu1"
replace grp_label = "Bahan baku/penolong"          if grp == "eu2"
replace grp_label = "Barang modal"                 if grp == "eu3"
drop if grp == "sec3"                                  // sama dengan noncomm

format mdate %tm
merge m:1 mdate using intermediate/ana_aggregate.dta, keep(match) ///
    keepusing(lnreer lnjis lncom lncom_nrg lncom_fd yf_avg month m2-m12 covid gfc t) nogen
gen lntb = ln(x / m)
encode grp, gen(gid)
xtset gid mdate
save intermediate/ana_group.dta, replace

* ringkasan pangsa per kelompok
preserve
collapse (sum) x m, by(grp grp_label)
egen X = total(x * inlist(grp, "comm", "noncomm"))
egen M = total(m * inlist(grp, "comm", "noncomm"))
gen share_x = 100 * x / X
gen share_m = 100 * m / M
gen tb_usdbn = (x - m) / 1e6
keep grp grp_label share_x share_m tb_usdbn
list, clean noobs
export delimited using output/tables/group_shares.csv, replace
restore
