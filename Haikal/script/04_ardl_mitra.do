* =============================================================================
* 04_ardl_mitra.do : RQ2 - efek depresiasi per negara mitra dagang
*   (a) ARDL per negara: ln(X_i/M_i) = f(ln REER, ln harga komoditas, IPI mitra i)
*   (b) Panel ARDL: Pooled Mean Group (PMG) vs Mean Group (MG), uji Hausman
*   Catatan: REER yang dipakai adalah REER multilateral Indonesia (BIS), bukan kurs riil
*   bilateral (data CPI & kurs mitra belum ada) -> lihat notes/hasil_dan_metode.md
*   Output: output/tables/ardl_mitra.csv, pmg_mitra.csv, output/figures/mitra_lr.png, jcurve_mitra.png
* =============================================================================
version 19
set more off
local EX "m2-m12 covid gfc"

use intermediate/ana_partner.dta, clear
xtset cid mdate

* -----------------------------------------------------------------------------
* (a) ARDL per negara
* -----------------------------------------------------------------------------
tempname P D
ardl_postfile `P', saving(output/tables/ardl_mitra.dta)
postfile `D' str20 id str45 label h eff10 using output/tables/dm_mitra.dta, replace
levelsof iso3, local(isos)
foreach c of local isos {
    preserve
    keep if iso3 == "`c'"
    tsset mdate
    local nm = country[1]
    quietly count if yf_own
    local own = r(N)
    ardl_post lntb lnreer lncom yf, exog(`EX') xfocus(lnreer) id("`c'") ///
        label("`nm' (IPI sendiri `own' bln)") post(`P') dmpost(`D')
    restore
}
postclose `P'
postclose `D'

use output/tables/ardl_mitra.dta, clear
format F t pF pt adj adj_se lr lr_se lr_p sr0 sr0_p eff10_* p_* %9.3f
gsort -eff10_lr
list id lags N pF pt coint10 adj lr lr_p eff10_lr eff10_sr0 eff10_m12 p_lm12 jcurve, clean noobs
export delimited using output/tables/ardl_mitra.csv, replace

* grafik: efek jangka panjang depresiasi riil 10% per mitra (95% CI)
gen lo = eff10_lr - 1.96 * 10 * lr_se
gen hi = eff10_lr + 1.96 * 10 * lr_se
gen sig = lr_p < .10 & coint10
sort eff10_lr
gen pos = _n
forvalues i = 1/`=_N' {
    label define pos `i' "`=id[`i']'", add
}
label values pos pos
twoway (rcap lo hi pos, horizontal lcolor(gs9)) ///
       (scatter pos eff10_lr if sig,  mcolor(navy) msymbol(D)) ///
       (scatter pos eff10_lr if !sig, mcolor(gs8) msymbol(Oh)), ///
       ylabel(1/`=_N', valuelabel angle(0)) xline(0, lcolor(maroon)) ///
       xtitle("Perubahan jangka panjang rasio X/M (%) akibat depresiasi riil 10%", size(small)) ytitle("") ///
       title("Efek jangka panjang depresiasi per mitra dagang", size(medium)) ///
       legend(order(2 "Signifikan 10% & terkointegrasi" 3 "Tidak signifikan / tanpa kointegrasi") ///
           pos(6) rows(2) size(small)) ///
       note("Batang = 95% CI. Positif = depresiasi memperbaiki trade balance.", size(vsmall)) ///
       xsize(9) ysize(6) scheme(s2color)
graph export output/figures/mitra_lr.png, replace width(1600)

use output/tables/dm_mitra.dta, clear
twoway (line eff10 h, lcolor(navy)) if h <= 24, by(id, note("") title("Respons kumulatif rasio X/M terhadap depresiasi riil 10%") ///
       yrescale) yline(0, lcolor(gs10)) xtitle("Bulan") ytitle("%") xlabel(0(6)24) scheme(s2color)
graph export output/figures/jcurve_mitra.png, replace width(1800)

* -----------------------------------------------------------------------------
* (b) Panel PMG / MG (Pesaran, Shin & Smith 1999)
*     long run dipaksa sama antar negara (PMG) vs bebas (MG); Hausman memilih
* -----------------------------------------------------------------------------
use intermediate/ana_partner.dta, clear
xtset cid mdate
local SR "d.lnreer ld.lnreer d.lncom d.yf ld.lntb m2-m12 covid gfc"
xtpmg d.lntb `SR', lr(l.lntb lnreer lncom yf) ec(ec) replace pmg
estimates store pmg
local pmg_b  = _b[ec:lnreer]
local pmg_se = _se[ec:lnreer]
local pmg_ec = _b[SR:ec]
local pmg_ecse = _se[SR:ec]
local pmg_com = _b[ec:lncom]
local pmg_comse = _se[ec:lncom]
xtpmg d.lntb `SR', lr(l.lntb lnreer lncom yf) ec(ec) replace mg
estimates store mg
local mg_b  = _b[ec:lnreer]
local mg_se = _se[ec:lnreer]
local mg_ec = _b[SR:ec]
local mg_ecse = _se[SR:ec]
local mg_com = _b[ec:lncom]
local mg_comse = _se[ec:lncom]
capture noisily hausman mg pmg, sigmamore
local hp = cond(_rc, ., r(p))
local hchi = cond(_rc, ., r(chi2))

tempname H
postfile `H' str6 est lr_reer lr_reer_se lr_reer_p eff10_lr lr_com lr_com_se ec ec_se hausman_chi2 hausman_p ///
    using output/tables/pmg_mitra.dta, replace
post `H' ("PMG") (`pmg_b') (`pmg_se') (2 * normal(-abs(`pmg_b' / `pmg_se'))) (-10 * `pmg_b') ///
    (`pmg_com') (`pmg_comse') (`pmg_ec') (`pmg_ecse') (`hchi') (`hp')
post `H' ("MG") (`mg_b') (`mg_se') (2 * normal(-abs(`mg_b' / `mg_se'))) (-10 * `mg_b') ///
    (`mg_com') (`mg_comse') (`mg_ec') (`mg_ecse') (`hchi') (`hp')
postclose `H'
use output/tables/pmg_mitra.dta, clear
format lr_reer-hausman_p %9.3f
list, clean noobs
export delimited using output/tables/pmg_mitra.csv, replace
