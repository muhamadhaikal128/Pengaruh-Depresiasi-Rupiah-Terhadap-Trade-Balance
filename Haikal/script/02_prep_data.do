* =============================================================================
* 02_prep_data.do : dataset analisis versi HS-6 (data olahan Tio, 17 Nov 2026)
*
* Input (intermediate/dari_tio/, disalin dari Tio/intermediate/):
*   Trade_Total_Month.csv : ekspor/impor TOTAL per mitra + dunia (WLD), harga komoditas
*                           database DEN (BCOM, batu bara, CPO, ...), PDB riil Indonesia
*   Trade_Goods_Month.csv : ekspor/impor per kelompok barang HS-6 (klasifikasi UNSD HS->SITC3->BEC5)
*   Panel_Country_Month.csv : IPI YoY mitra, REER BIS, JISDOR (panel lama Tio)
*   input/raw/fred/       : indeks harga komoditas IMF (robustness)
*
* Output (intermediate/analisis/):
*   commodity_prices.dta  : ln BCOM, batu bara, CPO, indeks IMF
*   ana_partner.dta       : 10 mitra x bulan
*   ana_aggregate.dta     : Indonesia vs DUNIA x bulan (+ versi 10 mitra: lntb10)
*   ana_group.dta         : 7 kelompok barang, Indonesia vs dunia x bulan
*   trade_group_partner.dta : 7 kelompok x 10 mitra x bulan (panel LP)
*   output/0_deskriptif/group_shares.csv
*
* Kode kelompok (dipertahankan dari versi HS-4 supaya script 04-07 tetap sama):
*   comm = commodity, sec1 = agriculture, sec2 = energy_mining, noncomm = manufacturing,
*   eu1 = consumption, eu2 = intermediate, eu3 = capital
* =============================================================================
version 19
clear
set more off

* -----------------------------------------------------------------------------
* 1. Harga komoditas (database DEN via Tio; IMF/FRED sebagai pembanding)
* -----------------------------------------------------------------------------
tempfile imf
local first = 1
foreach s in PALLFNFINDEXM PNRGINDEXM PFANDBINDEXM {
    import delimited using "input/raw/fred/`s'.csv", clear varnames(1)
    rename observation_date d
    rename `=lower("`s'")' `s'
    gen mdate = mofd(date(d, "YMD"))
    keep mdate `s'
    if !`first' merge 1:1 mdate using `imf', nogen
    save `imf', replace
    local first = 0
}

import delimited using intermediate/dari_tio/Trade_Total_Month.csv, clear encoding(utf8)
keep if iso3 == "WLD"
gen mdate = monthly(date, "YM")
keep mdate cmd_bcom_mean cmd_coal_newcastle_mean cmd_cpo_front_mean cmd_nickel_front_mean ///
     cmd_brent_mean idn_gdp_real_index_2015mean100
merge 1:1 mdate using `imf', keep(master match) nogen
format mdate %tm
tsset mdate
gen lncom      = ln(cmd_bcom_mean)                 // utama: Bloomberg Commodity Index
gen lncom_nrg  = ln(cmd_coal_newcastle_mean)       // energi & tambang: batu bara Newcastle (2009+)
gen lncom_fd   = ln(cmd_cpo_front_mean)            // pertanian & pangan: CPO
gen lncom_imf  = ln(PALLFNFINDEXM)                 // robustness: indeks IMF all commodities
* PDB riil Indonesia: kuartalan (bulan akhir kuartal) -> bulanan, interpolasi log-linear
gen lngdp_q = ln(idn_gdp_real_index_2015mean100)
ipolate lngdp_q mdate, gen(lngdp_idn)
label var lncom     "ln BCOM (database DEN)"
label var lncom_nrg "ln harga batu bara Newcastle"
label var lncom_fd  "ln harga CPO"
label var lncom_imf "ln indeks komoditas IMF (all)"
label var lngdp_idn "ln PDB riil Indonesia (interpolasi bulanan)"
keep mdate lncom lncom_nrg lncom_fd lncom_imf lngdp_idn
save intermediate/analisis/commodity_prices.dta, replace

* -----------------------------------------------------------------------------
* 2. Panel 10 mitra x bulan
*    nilai perdagangan dari baris TOTAL Trade_Total_Month (HS-6, Trade Map);
*    IPI, REER, JISDOR dari Panel_Country_Month
* -----------------------------------------------------------------------------
import delimited using intermediate/dari_tio/Trade_Total_Month.csv, clear encoding(utf8)
keep iso3 date exports_usdk imports_usdk
rename (exports_usdk imports_usdk) (x m)
tempfile tot
save `tot'

import delimited using intermediate/dari_tio/Panel_Country_Month.csv, clear encoding(utf8)
drop exports_usdk imports_usdk trade_balance_usdk total_trade_usdk
merge 1:1 iso3 date using `tot', keep(match) nogen
rename (x m) (exports_usdk imports_usdk)
gen mdate = monthly(date, "YM")
format mdate %tm
keep if !missing(exports_usdk) & !missing(imports_usdk)
merge m:1 mdate using intermediate/analisis/commodity_prices.dta, keep(master match) nogen

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

* Permintaan luar negeri: IPI YoY mitra tertimbang ekspor (bobot = pangsa ekspor 2006-2026
* di antara negara yang IPI-nya tersedia bulan itu)
bysort cid: egen xw = total(exports_usdk)
gen w_ipi = xw * !missing(ipi_yoy_pct)
bysort mdate: egen sw = total(w_ipi)
bysort mdate: egen yf_avg = total(w_ipi * ipi_yoy_pct / sw)
replace yf_avg = . if sw == 0
gen yf = ipi_yoy_pct
gen yf_own = !missing(ipi_yoy_pct)
replace yf = yf_avg if missing(yf)
drop xw w_ipi sw

label var lntb   "ln(Ekspor/Impor)"
label var lnreer "ln REER BIS (naik = apresiasi riil)"
label var lnjis  "ln JISDOR Rp/USD (naik = depresiasi)"
label var yf     "IPI YoY mitra (%)"
label var yf_avg "IPI YoY rata-rata 10 mitra tertimbang ekspor (%)"
save intermediate/analisis/ana_partner.dta, replace

* -----------------------------------------------------------------------------
* 3. Agregat: Indonesia vs DUNIA (utama) + jumlah 10 mitra (robustness)
* -----------------------------------------------------------------------------
collapse (sum) x_10m = exports_usdk m_10m = imports_usdk ///
         (first) reer_bis_broad jisdor_avg yf_avg month m2-m12 covid gfc, by(mdate)
tempfile ag10
save `ag10'
use `tot', clear
keep if iso3 == "WLD"
gen mdate = monthly(date, "YM")
rename (x m) (exports_usdk imports_usdk)
keep mdate exports_usdk imports_usdk
merge 1:1 mdate using `ag10', keep(match) nogen
merge 1:1 mdate using intermediate/analisis/commodity_prices.dta, keep(master match) nogen
format mdate %tm
tsset mdate
gen lntb   = ln(exports_usdk / imports_usdk)
gen lntb10 = ln(x_10m / m_10m)
gen lnx    = ln(exports_usdk)
gen lnm    = ln(imports_usdk)
gen lnreer = ln(reer_bis_broad)
gen lnjis  = ln(jisdor_avg)
gen t      = _n
label var lntb   "ln(Ekspor/Impor), Indonesia vs dunia"
label var lntb10 "ln(Ekspor/Impor), jumlah 10 mitra"
label var lnreer "ln REER BIS (naik = apresiasi riil)"
label var lnjis  "ln JISDOR Rp/USD (naik = depresiasi)"
label var yf_avg "IPI YoY mitra tertimbang (%)"
save intermediate/analisis/ana_aggregate.dta, replace

* -----------------------------------------------------------------------------
* 4. Kelompok barang HS-6 (Trade_Goods_Month, klasifikasi Tio)
* -----------------------------------------------------------------------------
import delimited using intermediate/dari_tio/Trade_Goods_Month.csv, clear encoding(utf8)
keep iso3 group date exports_usdk imports_usdk
rename (exports_usdk imports_usdk) (x m)
gen mdate = monthly(date, "YM")
format mdate %tm
gen str8 grp = ""
replace grp = "comm"    if group == "commodity"
replace grp = "sec1"    if group == "agriculture"
replace grp = "sec2"    if group == "energy_mining"
replace grp = "noncomm" if group == "manufacturing"
replace grp = "eu1"     if group == "consumption"
replace grp = "eu2"     if group == "intermediate"
replace grp = "eu3"     if group == "capital"
assert grp != ""
gen str40 grp_label = ""
replace grp_label = "Komoditas (total)"            if grp == "comm"
replace grp_label = "Non-komoditas (manufaktur)"   if grp == "noncomm"
replace grp_label = "Komoditas pertanian & pangan" if grp == "sec1"
replace grp_label = "Komoditas energi & tambang"   if grp == "sec2"
replace grp_label = "Barang konsumsi"              if grp == "eu1"
replace grp_label = "Bahan baku/penolong"          if grp == "eu2"
replace grp_label = "Barang modal"                 if grp == "eu3"
keep iso3 grp grp_label mdate x m

* panel mitra x kelompok (dipakai 03 dan 07)
preserve
    drop if iso3 == "WLD"
    save intermediate/analisis/trade_group_partner.dta, replace
restore

* Indonesia vs dunia per kelompok
keep if iso3 == "WLD"
drop iso3
merge m:1 mdate using intermediate/analisis/ana_aggregate.dta, keep(match) ///
    keepusing(lnreer lnjis lncom lncom_nrg lncom_fd lncom_imf lngdp_idn yf_avg month m2-m12 covid gfc t) nogen
gen lntb = ln(x / m)
encode grp, gen(gid)
xtset gid mdate
save intermediate/analisis/ana_group.dta, replace

* ringkasan pangsa per kelompok (dunia, kumulatif seluruh periode)
preserve
use intermediate/analisis/ana_aggregate.dta, clear
quietly summarize exports_usdk
local X = r(sum)
quietly summarize imports_usdk
local M = r(sum)
restore
collapse (sum) x m, by(grp grp_label)
gen share_x = 100 * x / `X'
gen share_m = 100 * m / `M'
gen tb_usdbn = (x - m) / 1e6
keep grp grp_label share_x share_m tb_usdbn
list, clean noobs
export delimited using output/0_deskriptif/group_shares.csv, replace
