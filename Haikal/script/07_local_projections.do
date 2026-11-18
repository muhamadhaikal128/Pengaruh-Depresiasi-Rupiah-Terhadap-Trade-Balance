* =============================================================================
* 07_local_projections.do : RQ1-RQ3 dengan local projections (Jorda 2005)
*
*   Persamaan per horizon h = 0..24 bulan:
*     y_{t+h} - y_{t-1} = a_h + b_h * shock_t + lag(1..12) dy, lag(1..12) shock + kontrol + e
*   y = ln(X/M); shock = perubahan bulanan kurs (NAIK = depresiasi). Lag augmentation
*   mengikuti Montiel Olea & Plagborg-Moller (2021).
*   Efek depresiasi 10% (dalam % rasio X/M) = 10 * b_h. Positif = trade balance membaik.
*
*   A. Agregat (RQ1), time series, SE Newey-West (lag h+1):
*      A1 OLS: shock = d(-ln REER), kontrol: harga komoditas, IPI mitra, musiman, dummy krisis
*      A2 LP-IV: d(-ln REER) diinstrumen d ln indeks USD broad (Fed). Rupiah melemah saat
*         USD menguat secara global, sebuah guncangan yang bukan berasal dari neraca dagang Indonesia.
*      A3 respons REER itu sendiri (persistensi guncangan)
*   B. Panel mitra x bulan (RQ2), kurs riil BILATERAL, FE mitra + FE waktu (bulan),
*      SE Driscoll-Kraay (lag h+1). FE waktu menyerap semua guncangan bersama:
*      siklus komoditas, permintaan domestik Indonesia, pelemahan rupiah yang umum.
*      B1 efek rata-rata, B2 efek per mitra (interaksi), B3 tanpa Vietnam (CPI pendekatan)
*   C. Panel mitra x kelompok barang (RQ3), sama dengan B1, per kelompok.
*
*   Output: output/2_lp/lp_irf.csv, lp_summary.csv, output/2_lp/lp_*.png
* =============================================================================
version 19
set more off
tempfile lp_irf
local H 24

tempname P
postfile `P' str12 model str20 id str45 label h b se N F1 using `lp_irf', replace

* -----------------------------------------------------------------------------
* A. Agregat
* -----------------------------------------------------------------------------
use intermediate/analisis/lp_aggregate.dta, clear
tsset mdate
gen sh   = D.dep
gen z    = D.lnusd
local CA "L(1/12).D.lntb L(1/12).sh L(0/12).D.lncom L(0/3).yf_avg m2-m12 covid gfc"
forvalues h = 0/`H' {
    quietly gen lhs = F`h'.lntb - L.lntb
    quietly gen lhx = F`h'.dep - L.dep
    * A1 OLS
    quietly newey lhs sh `CA', lag(`=`h'+1')
    post `P' ("A1_ols") ("AGG") ("Agregat, OLS") (`h') (_b[sh]) (_se[sh]) (e(N)) (.)
    * A2 LP-IV
    quietly ivregress 2sls lhs `CA' L(1/12).z (sh = z), vce(hac bartlett `=`h'+1')
    local b = _b[sh]
    local s = _se[sh]
    local n = e(N)
    quietly estat firststage
    local F = r(mineig)
    post `P' ("A2_iv") ("AGG") ("Agregat, LP-IV (instrumen: indeks USD)") (`h') (`b') (`s') (`n') (`F')
    * A3 respons kurs sendiri
    quietly newey lhx sh `CA', lag(`=`h'+1')
    post `P' ("A3_dep") ("AGG") ("Respons -ln REER") (`h') (_b[sh]) (_se[sh]) (e(N)) (.)
    drop lhs lhx
}
* first stage di h = 0 untuk dilaporkan
gen lhs = lntb - L.lntb
ivregress 2sls lhs `CA' L(1/12).z (sh = z), vce(hac bartlett 1) first
estat firststage
drop lhs

* -----------------------------------------------------------------------------
* B. Panel mitra x bulan, RER bilateral
* -----------------------------------------------------------------------------
use intermediate/analisis/lp_partner.dta, clear
xtset cid mdate
gen sh = D.rer
local CP "L(1/12).D.lntb L(1/12).sh L(0/3).yf i.mdate"
levelsof cid, local(cids)
forvalues h = 0/`H' {
    quietly gen lhs = F`h'.lntb - L.lntb
    * B1 efek rata-rata
    quietly xtscc lhs sh `CP', fe lag(`=`h'+1')
    post `P' ("B1_panel") ("PANEL") ("Panel 10 mitra, FE mitra+waktu") (`h') (_b[sh]) (_se[sh]) (e(N)) (.)
    * B3 tanpa Vietnam
    quietly xtscc lhs sh `CP' if iso3 != "VNM", fe lag(`=`h'+1')
    post `P' ("B3_novnm") ("PANEL") ("Panel tanpa Vietnam") (`h') (_b[sh]) (_se[sh]) (e(N)) (.)
    * B2 efek per mitra
    quietly xtscc lhs ibn.cid#c.sh `CP', fe lag(`=`h'+1')
    foreach c of local cids {
        local nm : label (cid) `c'
        post `P' ("B2_partner") ("`nm'") ("`nm'") (`h') (_b[`c'.cid#c.sh]) (_se[`c'.cid#c.sh]) (e(N)) (.)
    }
    drop lhs
}

* -----------------------------------------------------------------------------
* C. Panel mitra x kelompok barang
* -----------------------------------------------------------------------------
use intermediate/analisis/lp_group_partner.dta, clear
xtset pg mdate
gen sh = D.rer
local CG "L(1/12).D.lntb L(1/12).sh L(0/3).yf i.mdate"
levelsof grp, local(groups)
foreach g of local groups {
    forvalues h = 0/`H' {
        quietly gen lhs = F`h'.lntb - L.lntb
        quietly xtscc lhs sh `CG' if grp == "`g'", fe lag(`=`h'+1')
        post `P' ("C_group") ("`g'") ("`g'") (`h') (_b[sh]) (_se[sh]) (e(N)) (.)
        drop lhs
    }
}
postclose `P'

* -----------------------------------------------------------------------------
* Tabel & grafik
* -----------------------------------------------------------------------------
use `lp_irf', clear
* label kelompok
replace label = "Komoditas (total)"            if id == "comm"
replace label = "Non-komoditas (manufaktur)"   if id == "noncomm"
replace label = "Komoditas pertanian & pangan" if id == "sec1"
replace label = "Komoditas energi & tambang"   if id == "sec2"
replace label = "Barang konsumsi"              if id == "eu1"
replace label = "Bahan baku/penolong"          if id == "eu2"
replace label = "Barang modal"                 if id == "eu3"
* efek depresiasi 10% (%), kecuali respons kurs sendiri (dalam % depresiasi juga)
gen eff = 10 * b
gen lo90 = 10 * (b - 1.645 * se)
gen hi90 = 10 * (b + 1.645 * se)
gen lo95 = 10 * (b - 1.96 * se)
gen hi95 = 10 * (b + 1.96 * se)
gen p = 2 * normal(-abs(b / se))
save `lp_irf', replace
export delimited using output/2_lp/lp_irf.csv, replace

* ringkasan horizon 0, 3, 6, 12, 18, 24
preserve
keep if inlist(h, 0, 3, 6, 12, 18, 24)
keep model id label h eff p F1
reshape wide eff p F1, i(model id label) j(h)
drop F13 F16 F112 F118 F124
format eff* %7.2f
format p* %6.3f
list model id eff0 p0 eff6 p6 eff12 p12 eff24 p24, clean noobs
export delimited using output/2_lp/lp_summary.csv, replace
restore

* A. Agregat: OLS vs IV
local opts "yline(0, lcolor(gs10)) xlabel(0(6)24) xtitle(Bulan setelah depresiasi) scheme(s2color)"
twoway (rarea lo90 hi90 h if model == "A1_ols", color(navy%20) lwidth(none)) ///
       (line eff h if model == "A1_ols", lcolor(navy) lwidth(medthick)) ///
       (line eff h if model == "A2_iv", lcolor(maroon) lpattern(dash)) ///
       (line lo90 h if model == "A2_iv", lcolor(maroon%50) lpattern(shortdash)) ///
       (line hi90 h if model == "A2_iv", lcolor(maroon%50) lpattern(shortdash)), ///
       `opts' ytitle("Perubahan rasio X/M (%)") ///
       title("LP agregat: respons trade balance terhadap depresiasi riil 10%", size(medium)) ///
       legend(order(2 "OLS (90% CI arsir)" 3 "LP-IV, instrumen indeks USD (90% CI putus-putus)") ///
           pos(6) rows(2) size(small)) xsize(9) ysize(6)
graph export output/2_lp/lp_agregat.png, replace width(1600)

* B. Panel: rata-rata
twoway (rarea lo95 hi95 h if model == "B1_panel", color(navy%12) lwidth(none)) ///
       (rarea lo90 hi90 h if model == "B1_panel", color(navy%25) lwidth(none)) ///
       (line eff h if model == "B1_panel", lcolor(navy) lwidth(medthick)) ///
       (line eff h if model == "B3_novnm", lcolor(maroon) lpattern(dash)), ///
       `opts' ytitle("Perubahan rasio X/M (%)") ///
       title("Panel LP: depresiasi riil bilateral 10%", size(medium)) ///
       subtitle("FE mitra + FE bulan, SE Driscoll-Kraay", size(small)) ///
       legend(order(3 "10 mitra (90/95% CI)" 4 "Tanpa Vietnam") pos(6) rows(1) size(small)) xsize(9) ysize(6)
graph export output/2_lp/lp_panel.png, replace width(1600)

* B2: per mitra
twoway (rarea lo90 hi90 h, color(navy%20) lwidth(none)) (line eff h, lcolor(navy)) if model == "B2_partner", ///
       by(id, note("Arsir = 90% CI. FE mitra + FE bulan, SE Driscoll-Kraay.", size(vsmall)) ///
          title("Panel LP per mitra: depresiasi riil bilateral 10%", size(medium)) legend(off) cols(5) yrescale) ///
       `opts' ytitle("%") xtitle("Bulan") xsize(10) ysize(5)
graph export output/2_lp/lp_mitra.png, replace width(1800)

* C: per kelompok
twoway (rarea lo90 hi90 h, color(navy%20) lwidth(none)) (line eff h, lcolor(navy)) if model == "C_group", ///
       by(label, note("Arsir = 90% CI. Panel mitra, FE mitra + FE bulan, SE Driscoll-Kraay.", size(vsmall)) ///
          title("Panel LP per kelompok barang: depresiasi riil bilateral 10%", size(medium)) legend(off) cols(4)) ///
       `opts' ytitle("%") xtitle("Bulan") xsize(10) ysize(5.5)
graph export output/2_lp/lp_kelompok.png, replace width(1800)
