* =============================================================================
* 06_ardl_kelompok.do : RQ3 - efek depresiasi per kelompok barang
*   Dua cara pengelompokan HS-4 (lihat 02_prep_data.do bagian 4):
*     - Komoditas vs non-komoditas; komoditas dipecah pertanian/pangan vs energi/tambang
*     - End use (BEC / klasifikasi BPS): konsumsi, bahan baku/penolong, barang modal
*   Model per kelompok g: ln(X_g/M_g) = f(ln REER, ln harga komoditas relevan, IPI mitra)
*     + dua persamaan terpisah ln X_g dan ln M_g untuk melihat sumber efeknya
*   Output: output/1_ardl/ardl_kelompok.csv, output/1_ardl/kelompok_lr.png, jcurve_kelompok.png
* =============================================================================
version 19
set more off
tempfile ardl_kelompok dm_kelompok
local EX "m2-m12 covid gfc"

use intermediate/analisis/ana_group.dta, clear
gen lnx = ln(x)
gen lnm = ln(m)
* indeks harga komoditas yang paling relevan per kelompok
gen pcom = lncom
replace pcom = lncom_fd  if grp == "sec1"
replace pcom = lncom_nrg if grp == "sec2"
label var pcom "ln harga komoditas (sesuai kelompok)"

tempname P D
ardl_postfile `P', saving(`ardl_kelompok')
postfile `D' str20 id str45 label h eff10 using `dm_kelompok', replace
levelsof grp, local(groups)
foreach g of local groups {
    preserve
    keep if grp == "`g'"
    tsset mdate
    local nm = grp_label[1]
    * batu bara baru tersedia 2009 -> sampel energi mulai 2010, dummy GFC selalu nol
    local EXg = cond("`g'" == "sec2", "m2-m12 covid", "`EX'")
    ardl_post lntb lnreer pcom yf_avg, exog(`EXg') xfocus(lnreer) id("`g'") label("`nm'") ///
        post(`P') dmpost(`D')
    ardl_post lnx lnreer pcom yf_avg, exog(`EXg') xfocus(lnreer) id("`g'_X") label("`nm': ekspor") post(`P')
    ardl_post lnm lnreer pcom yf_avg, exog(`EXg') xfocus(lnreer) id("`g'_M") label("`nm': impor") post(`P')
    restore
}
postclose `P'
postclose `D'

use `ardl_kelompok', clear
gen eq = cond(strpos(id, "_X"), "X", cond(strpos(id, "_M"), "M", "TB"))
format F t pF pt adj adj_se lr lr_se lr_p sr0 sr0_p eff10_* p_* %9.3f
sort eq id
list id lags N pF pt coint10 adj lr lr_p eff10_lr eff10_sr0 eff10_m12 p_lm12 jcurve, clean noobs sepby(eq)
export delimited using output/1_ardl/ardl_kelompok.csv, replace

* grafik efek jangka panjang (persamaan rasio X/M)
keep if eq == "TB"
gen lo = eff10_lr - 1.96 * 10 * lr_se
gen hi = eff10_lr + 1.96 * 10 * lr_se
gen sig = lr_p < .10 & coint10
sort eff10_lr
gen pos = _n
forvalues i = 1/`=_N' {
    label define pos `i' "`=label[`i']'", add
}
label values pos pos
twoway (rcap lo hi pos, horizontal lcolor(gs9)) ///
       (scatter pos eff10_lr if sig,  mcolor(navy) msymbol(D)) ///
       (scatter pos eff10_lr if !sig, mcolor(gs8) msymbol(Oh)), ///
       ylabel(1/`=_N', valuelabel angle(0) labsize(small)) xline(0, lcolor(maroon)) ///
       xtitle("Perubahan jangka panjang rasio X/M (%) akibat depresiasi riil 10%", size(small)) ytitle("") ///
       title("Efek jangka panjang depresiasi per kelompok barang", size(medium)) ///
       legend(order(2 "Signifikan 10% & terkointegrasi" 3 "Tidak signifikan / tanpa kointegrasi") ///
           pos(6) rows(2) size(small)) ///
       note("Batang = 95% CI. Positif = depresiasi memperbaiki trade balance.", size(vsmall)) ///
       xsize(9) ysize(6) scheme(s2color)
graph export output/1_ardl/kelompok_lr.png, replace width(1600)

use `dm_kelompok', clear
export delimited using output/1_ardl/dm_kelompok.csv, replace
twoway (line eff10 h, lcolor(navy)) if h <= 24, by(label, note("") cols(4) ///
       title("Respons kumulatif rasio X/M terhadap depresiasi riil 10%") yrescale) ///
       yline(0, lcolor(gs10)) xtitle("Bulan") ytitle("%") xlabel(0(6)24) scheme(s2color)
graph export output/1_ardl/jcurve_kelompok.png, replace width(1800)
