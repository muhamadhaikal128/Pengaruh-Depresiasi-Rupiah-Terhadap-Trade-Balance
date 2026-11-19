* =============================================================================
* 11_harga_volume.do : dekomposisi efek depresiasi menjadi HARGA vs VOLUME
*
*   Identitas: ln(X/M) = ln(Px/Pm) + ln(Qx/Qm)
*              rasio nilai = terms of trade (harga) + rasio volume
*   Indeks harga (unit value Fisher) dan volume dari 10_indeks_harga_volume.py (data HS-6 kuantitas,
*   10 mitra). Karena tidak ada data kuantitas Indonesia-dunia, cakupan agregat = jumlah 10 mitra.
*
*   P. LP agregat 10 mitra (shock = d(-ln REER), sama dengan A1_ols di 07):
*        y in {lnxm, lntot, lnqxm, lnpx, lnqx, lnpm, lnqm}; SEMUA regresi memakai kontrol yang sama
*        (lag 1-6 dari d.lnpx d.lnqx d.lnpm d.lnqm), sehingga respons lnxm = lntot + lnqxm persis
*        dan lnxm = lnpx + lnqx - lnpm - lnqm persis (OLS linear).
*   Q. Panel per mitra (kurs riil bilateral, FE mitra + FE bulan, Driscoll-Kraay), y in {lnxm, lntot, lnqxm}
*   R. Per kelompok barang (jumlah 10 mitra, time series seperti P), y in {lnxm, lntot, lnqxm}
*   S. ARDL elastisitas VOLUME: uji Marshall-Lerner yang sebenarnya
*        ln Qx = f(ln REER, IPI mitra, ln BCOM);  ln Qm = f(ln REER, ln PDB Indonesia, ln BCOM)
*        eps_x = efek depresiasi 10% pada Qx / 10;  eps_m = -efek pada Qm / 10;  ML: eps_x + eps_m > 1
*
*   Output: output/2_lp/lp_pv.csv, output/1_ardl/ardl_volume.csv, output/0_deskriptif/pv_series.csv
* =============================================================================
version 19
set more off
tempfile pv lp_pv ardl_vol dm_vol
local H 24

* -----------------------------------------------------------------------------
* 0. Data indeks harga & volume
* -----------------------------------------------------------------------------
import delimited using intermediate/analisis/price_volume.csv, clear varnames(1) stringcols(1 2 4)
rename mdate mdate_s
gen mdate = monthly(mdate_s, "YM")
format mdate %tm
drop mdate_s
gen f = cond(flow == "Export", "x", "m")
keep scope id f mdate pidx vidx
reshape wide pidx vidx, i(scope id mdate) j(f) string
gen lnpx  = ln(pidxx)
gen lnqx  = ln(vidxx)
gen lnpm  = ln(pidxm)
gen lnqm  = ln(vidxm)
gen lntot = lnpx - lnpm
gen lnqxm = lnqx - lnqm
gen lnxm  = lntot + lnqxm
save `pv'
preserve
keep if scope == "AGG10"
keep mdate pidxx vidxx pidxm vidxm
export delimited using output/0_deskriptif/pv_series.csv, replace
restore

tempname P
postfile `P' str10 model str10 id str8 var h b se N using `lp_pv', replace

* -----------------------------------------------------------------------------
* P. LP agregat 10 mitra
* -----------------------------------------------------------------------------
use `pv' if scope == "AGG10", clear
merge 1:1 mdate using intermediate/analisis/lp_aggregate.dta, keepusing(dep lncom yf_avg m2-m12 covid gfc) ///
    keep(match) nogen
tsset mdate
gen sh = D.dep
local CP "L(1/6).D.lnpx L(1/6).D.lnqx L(1/6).D.lnpm L(1/6).D.lnqm L(1/6).sh L(0/6).D.lncom L(0/3).yf_avg m2-m12 covid gfc"
forvalues h = 0/`H' {
    foreach y in lnxm lntot lnqxm lnpx lnqx lnpm lnqm {
        quietly gen lhs = F`h'.`y' - L.`y'
        quietly newey lhs sh `CP', lag(`=`h'+1')
        post `P' ("P_agg") ("AGG10") ("`y'") (`h') (_b[sh]) (_se[sh]) (e(N))
        drop lhs
    }
}
* korelasi harga ekspor komoditas dengan BCOM (cek kewajaran indeks)
corr S12.lnpx S12.lncom

* -----------------------------------------------------------------------------
* Q. Panel per mitra, kurs riil bilateral
* -----------------------------------------------------------------------------
use `pv' if scope == "PARTNER", clear
rename id iso3
merge 1:1 iso3 mdate using intermediate/analisis/lp_partner.dta, keepusing(cid rer yf) keep(match) nogen
xtset cid mdate
gen sh = D.rer
local CQ "L(1/6).D.lntot L(1/6).D.lnqxm L(1/6).sh L(0/3).yf i.mdate"
levelsof cid, local(cids)
foreach h in 0 6 12 18 24 {
    foreach y in lnxm lntot lnqxm {
        quietly gen lhs = F`h'.`y' - L.`y'
        quietly xtscc lhs sh `CQ', fe lag(`=`h'+1')
        post `P' ("Q_panel") ("PANEL") ("`y'") (`h') (_b[sh]) (_se[sh]) (e(N))
        quietly xtscc lhs ibn.cid#c.sh `CQ', fe lag(`=`h'+1')
        foreach c of local cids {
            local nm : label (cid) `c'
            post `P' ("Q_partner") ("`nm'") ("`y'") (`h') (_b[`c'.cid#c.sh]) (_se[`c'.cid#c.sh]) (e(N))
        }
        drop lhs
    }
}

* -----------------------------------------------------------------------------
* R. Per kelompok barang (jumlah 10 mitra), time series
* -----------------------------------------------------------------------------
use `pv' if scope == "GROUP", clear
merge m:1 mdate using intermediate/analisis/lp_aggregate.dta, keepusing(dep lncom yf_avg m2-m12 covid gfc) ///
    keep(match) nogen
encode id, gen(gid)
xtset gid mdate
gen sh = D.dep
local CR "L(1/6).D.lntot L(1/6).D.lnqxm L(1/6).sh L(0/6).D.lncom L(0/3).yf_avg m2-m12 covid gfc"
levelsof id, local(groups)
foreach g of local groups {
    preserve
    keep if id == "`g'"
    tsset mdate
    forvalues h = 0/`H' {
        foreach y in lnxm lntot lnqxm {
            quietly gen lhs = F`h'.`y' - L.`y'
            quietly newey lhs sh `CR', lag(`=`h'+1')
            post `P' ("R_group") ("`g'") ("`y'") (`h') (_b[sh]) (_se[sh]) (e(N))
            drop lhs
        }
    }
    restore
}
postclose `P'

use `lp_pv', clear
gen eff  = 10 * b
gen lo90 = 10 * (b - 1.645 * se)
gen hi90 = 10 * (b + 1.645 * se)
gen p    = 2 * normal(-abs(b / se))
export delimited using output/2_lp/lp_pv.csv, replace
format eff p %7.2f
list id var eff p if model == "P_agg" & inlist(h, 0, 6, 12, 24), sepby(h) noobs clean
list id var eff p if model != "P_agg" & h == 12, sepby(id) noobs clean

* -----------------------------------------------------------------------------
* S. ARDL elastisitas volume (Marshall-Lerner)
* -----------------------------------------------------------------------------
use `pv' if scope == "AGG10", clear
merge 1:1 mdate using intermediate/analisis/ana_aggregate.dta, ///
    keepusing(lnreer lncom yf_avg lngdp_idn m2-m12 covid gfc) keep(match) nogen
tsset mdate
local EX "m2-m12 covid gfc"
tempname V D
ardl_postfile `V', saving(`ardl_vol')
postfile `D' str20 id str45 label h eff10 using `dm_vol', replace
ardl_post lnqx lnreer yf_avg lncom, exog(`EX') xfocus(lnreer) id("V1_qx") ///
    label("Volume ekspor (10 mitra)") maxlags(6) post(`V') dmpost(`D')
ardl_post lnqm lnreer lngdp_idn lncom, exog(`EX') xfocus(lnreer) id("V2_qm") ///
    label("Volume impor (10 mitra)") maxlags(6) post(`V') dmpost(`D')
ardl_post lnqxm lnreer yf_avg lngdp_idn lncom, exog(`EX') xfocus(lnreer) id("V3_qxm") ///
    label("Rasio volume Qx/Qm") maxlags(6) post(`V') dmpost(`D')
ardl_post lntot lnreer lncom, exog(`EX') xfocus(lnreer) id("V4_tot") ///
    label("Terms of trade Px/Pm") maxlags(6) post(`V') dmpost(`D')
postclose `V'
postclose `D'
use `ardl_vol', clear
export delimited using output/1_ardl/ardl_volume.csv, replace
list id lags N pF pt coint10 lr lr_p eff10_lr eff10_sr0 eff10_m12, clean noobs
use `dm_vol', clear
export delimited using output/1_ardl/dm_volume.csv, replace
