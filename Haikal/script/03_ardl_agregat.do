* =============================================================================
* 03_ardl_agregat.do : RQ1 - apakah depresiasi rupiah memperbaiki trade balance?
*   Data: total perdagangan Indonesia dengan 10 mitra utama, bulanan 2006m1-2026m8
*   Model: ln(X/M) = f(ln REER, ln harga komoditas, IPI mitra) + musiman + dummy krisis
*   Output: output/tables/unitroot.csv, ardl_agregat.csv, nardl_agregat.csv,
*           output/figures/jcurve_agregat.png, tb_reer_series.png, output/diagnostics/cusum_*.png
* =============================================================================
version 19
set more off
local EX "m2-m12 covid gfc"

use intermediate/ana_aggregate.dta, clear
tsset mdate

* -----------------------------------------------------------------------------
* 0. Grafik deskriptif
* -----------------------------------------------------------------------------
twoway (line lntb mdate, yaxis(1) lcolor(navy)) ///
       (line lnreer mdate, yaxis(2) lcolor(maroon) lpattern(dash)), ///
       ytitle("ln(Ekspor/Impor)", axis(1)) ytitle("ln REER (naik = apresiasi)", axis(2)) ///
       xtitle("") legend(order(1 "ln(X/M) 10 mitra" 2 "ln REER BIS") pos(6) rows(1)) ///
       title("Trade balance vs REER, 2006-2026") scheme(s2color)
graph export output/figures/tb_reer_series.png, replace width(1600)

* -----------------------------------------------------------------------------
* 1. Uji akar unit: ADF (4 lag) dan Phillips-Perron, level dan first difference
*    ARDL bounds test butuh semua variabel I(0) atau I(1), tidak boleh I(2)
* -----------------------------------------------------------------------------
tempname ur
postfile `ur' str10 var str6 form adf_stat adf_p pp_stat pp_p using output/tables/unitroot.dta, replace
foreach v in lntb lnreer lnjis lncom lncom_nrg lncom_fd yf_avg {
    quietly dfuller `v', lags(4)
    local a = r(Zt)
    local ap = r(p)
    quietly pperron `v'
    post `ur' ("`v'") ("level") (`a') (`ap') (r(Zt)) (r(pval))
    quietly dfuller D.`v', lags(4)
    local a = r(Zt)
    local ap = r(p)
    quietly pperron D.`v'
    post `ur' ("`v'") ("diff") (`a') (`ap') (r(Zt)) (r(pval))
}
postclose `ur'
preserve
use output/tables/unitroot.dta, clear
list, clean noobs
export delimited using output/tables/unitroot.csv, replace
restore

* -----------------------------------------------------------------------------
* 2. ARDL agregat: spesifikasi utama + robustness
* -----------------------------------------------------------------------------
tempname P D
ardl_postfile `P', saving(output/tables/ardl_agregat.dta)
postfile `D' str20 id str45 label h eff10 using output/tables/dm_agregat.dta, replace

* (a) utama: REER, AIC, maxlag 12
ardl_post lntb lnreer lncom yf_avg, exog(`EX') xfocus(lnreer) id("A1_main") ///
    label("Utama: REER, AIC") post(`P') dmpost(`D')
* diagnostik stabilitas spesifikasi utama (CUSUM)
quietly ardl lntb lnreer lncom yf_avg, exog(`EX') maxlags(12) aic ec
estat sbcusum
graph export output/diagnostics/cusum_agregat.png, replace width(1400)
estat sbcusum, ols
graph export output/diagnostics/cusum_ols_agregat.png, replace width(1400)

* (b) BIC (lag lebih hemat)
ardl_post lntb lnreer lncom yf_avg, exog(`EX') xfocus(lnreer) id("A2_bic") ///
    label("BIC") ic(bic) post(`P') dmpost(`D')
* (c) dengan tren deterministik (case 5)
ardl_post lntb lnreer lncom yf_avg, exog(`EX') xfocus(lnreer) id("A3_trend") ///
    label("Dengan tren linear") trend(t) post(`P')
* (d) maxlag 6
ardl_post lntb lnreer lncom yf_avg, exog(`EX') xfocus(lnreer) id("A4_lag6") ///
    label("Maxlag 6") maxlags(6) post(`P')
* (e) tanpa harga komoditas
ardl_post lntb lnreer yf_avg, exog(`EX') xfocus(lnreer) id("A5_nocom") ///
    label("Tanpa harga komoditas") post(`P')
* (f) sampel sebelum COVID
ardl_post lntb lnreer lncom yf_avg if mdate <= tm(2019m12), exog(m2-m12 gfc) xfocus(lnreer) ///
    id("A6_pre2020") label("Sampel 2006-2019") post(`P')
* (g) kurs nominal JISDOR (Rp/USD, naik = depresiasi), 2013m6+ ; tanda dibalik supaya
*     konvensinya sama (xfocus = -ln JISDOR, naik = apresiasi)
gen neg_lnjis = -lnjis
ardl_post lntb neg_lnjis lncom yf_avg if !missing(lnjis), exog(m2-m12 covid) xfocus(neg_lnjis) ///
    id("A7_jisdor") label("Kurs nominal JISDOR (2013-2026)") post(`P') dmpost(`D')
* pembanding: REER pada sampel yang sama dengan JISDOR
ardl_post lntb lnreer lncom yf_avg if !missing(lnjis), exog(m2-m12 covid) xfocus(lnreer) ///
    id("A7b_reer2013") label("REER, sampel 2013-2026") post(`P')
* (h) ekspor dan impor terpisah (elastisitas)
ardl_post lnx lnreer lncom yf_avg, exog(`EX') xfocus(lnreer) id("A8_exports") ///
    label("ln Ekspor (bukan rasio)") post(`P')
ardl_post lnm lnreer lncom yf_avg, exog(`EX') xfocus(lnreer) id("A9_imports") ///
    label("ln Impor (bukan rasio)") post(`P')
postclose `P'
postclose `D'

use output/tables/ardl_agregat.dta, clear
format F t pF pt adj adj_se lr lr_se lr_p sr0 sr0_p eff10_* p_* %9.3f
list id lags N F pF pt coint10 adj lr lr_p eff10_lr eff10_sr0 eff10_m12 p_lm12 jcurve, clean noobs
export delimited using output/tables/ardl_agregat.csv, replace

* -----------------------------------------------------------------------------
* 3. NARDL (Shin, Yu & Greenwood-Nimmo 2014): apakah depresiasi dan apresiasi
*    berpengaruh asimetris? (Bahmani-Oskooee & Fariditavana 2016)
* -----------------------------------------------------------------------------
use intermediate/ana_aggregate.dta, clear
tsset mdate
gen dr = D.lnreer
replace dr = 0 if missing(dr)
gen reer_app = sum(max(dr, 0))           // partial sum apresiasi
gen reer_dep = sum(min(dr, 0))           // partial sum depresiasi (nilai negatif)
ardl lntb reer_app reer_dep lncom yf_avg, exog(`EX') maxlags(12) aic ec maxcombs(400000)
estat ectest
local pF = r(cvmat)[1, 8]
local pt = r(cvmat)[2, 8]
local N = e(N)
local adj = _b[ADJ:L.lntb]
tempname NL
postfile `NL' str25 term b se p using output/tables/nardl_agregat.dta, replace
foreach v in reer_app reer_dep lncom yf_avg {
    post `NL' ("LR:`v'") (_b[LR:`v']) (_se[LR:`v']) (2 * ttail(e(df_r), abs(_b[LR:`v'] / _se[LR:`v'])))
}
test [LR]reer_app = [LR]reer_dep
post `NL' ("Wald LR simetri (F)") (r(F)) (.) (r(p))
test [SR]D.reer_app = [SR]D.reer_dep
post `NL' ("Wald SR dampak simetri (F)") (r(F)) (.) (r(p))
post `NL' ("ADJ") (`adj') (_se[ADJ:L.lntb]) (.)
post `NL' ("Bounds p(F, I1)") (`pF') (.) (.)
post `NL' ("Bounds p(t, I1)") (`pt') (.) (.)
post `NL' ("N") (`N') (.) (.)
postclose `NL'
use output/tables/nardl_agregat.dta, clear
list, clean noobs
export delimited using output/tables/nardl_agregat.csv, replace

* -----------------------------------------------------------------------------
* 4. Grafik J-curve: efek kumulatif depresiasi riil 10% terhadap rasio X/M
* -----------------------------------------------------------------------------
use output/tables/dm_agregat.dta, clear
twoway (line eff10 h if id == "A1_main", lcolor(navy) lwidth(medthick)) ///
       (line eff10 h if id == "A2_bic", lcolor(maroon) lpattern(dash)) ///
       (line eff10 h if id == "A7_jisdor", lcolor(forest_green) lpattern(shortdash)), ///
       yline(0, lcolor(gs10)) xlabel(0(6)36) ///
       xtitle("Bulan setelah depresiasi") ytitle("Perubahan rasio X/M (%)") ///
       title("Respons trade balance terhadap depresiasi riil 10%") ///
       subtitle("Dynamic multiplier kumulatif ARDL, 10 mitra dagang") ///
       legend(order(1 "REER, AIC (utama)" 2 "REER, BIC" 3 "JISDOR nominal") pos(6) rows(1)) ///
       scheme(s2color)
graph export output/figures/jcurve_agregat.png, replace width(1600)
