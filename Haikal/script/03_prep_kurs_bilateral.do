* =============================================================================
* 03_prep_kurs_bilateral.do : kurs riil bilateral + data panel untuk local projections (07)
*   1. Kurs riil bilateral rupiah vs 10 mitra (BIS kurs & CPI)  -> intermediate/analisis/rer_bilateral.dta
*   2. Panel mitra x bulan + RER bilateral                        -> intermediate/analisis/lp_partner.dta
*   3. Panel mitra x kelompok barang x bulan + RER bilateral      -> intermediate/analisis/lp_group_partner.dta
*   4. Agregat + indeks dolar AS broad (instrumen LP-IV)          -> intermediate/analisis/lp_aggregate.dta
*
* Definisi: rer_i = ln(Rp per mata uang i) + ln CPI_i - ln CPI_Indonesia
*           NAIK = rupiah terdepresiasi secara riil terhadap mitra i
* Sumber: BIS WS_XRU (kurs per USD, rata-rata bulanan), BIS WS_LONG_CPI (indeks),
*         diunduh 16 Nov 2026. CPI Vietnam tidak ada di BIS -> dibentuk dari inflasi
*         tahunan World Bank (FRED FPCPITOTLZGVNM), dibagi rata per bulan; 2026 = laju 2025.
* =============================================================================
version 19
set more off

* ---- kurs per USD
import delimited using input/raw/bis/bis_xru_monthly.csv, clear
keep ref_area time_period obs_value
rename (ref_area obs_value) (iso2 e_usd)
gen mdate = monthly(time_period, "YM")
drop time_period
tempfile fx
save `fx'

* ---- CPI
import delimited using input/raw/bis/bis_cpi_monthly.csv, clear
keep ref_area time_period obs_value
rename (ref_area obs_value) (iso2 cpi)
gen mdate = monthly(time_period, "YM")
drop time_period
* Vietnam dari inflasi tahunan
preserve
    import delimited using input/raw/fred/FPCPITOTLZGVNM.csv, clear
    gen year = year(date(observation_date, "YMD"))
    rename fpcpitotlzgvnm infl
    keep if year >= 2004
    tsset year
    tsappend, add(1)                                  // 2026: pakai laju 2025
    replace infl = L.infl if missing(infl)
    expand 12
    bysort year: gen mon = _n
    gen mdate = ym(year, mon)
    sort mdate
    gen dlp = ln(1 + infl / 100) / 12
    gen cpi = 100 * exp(sum(dlp))
    gen iso2 = "VN"
    keep iso2 mdate cpi
    tempfile vn
    save `vn'
restore
append using `vn'
merge 1:1 iso2 mdate using `fx', nogen
* Amerika: USD per USD = 1 (baris AS dibentuk ulang dari kalender Indonesia, CPI AS di-merge)
drop if iso2 == "US"
expand 2 if iso2 == "ID", gen(us)
replace iso2 = "US" if us
replace e_usd = 1 if us
replace cpi = . if us
drop us
preserve
    import delimited using input/raw/bis/bis_cpi_monthly.csv, clear
    keep if ref_area == "US"
    gen mdate = monthly(time_period, "YM")
    keep mdate obs_value
    rename obs_value cpi_us
    tempfile us
    save `us'
restore
merge m:1 mdate using `us', nogen
replace cpi = cpi_us if iso2 == "US"
drop cpi_us
drop if iso2 == "US" & missing(mdate)
* celah internal di sumber: CPI AS Okt-2025 tidak dirilis BLS (government shutdown),
* kurs VND Agu-2025 kosong di BIS -> interpolasi linear (hanya celah di tengah, bukan ujung)
encode iso2, gen(c2)
xtset c2 mdate
tsfill
bysort c2 (mdate): replace iso2 = iso2[_n-1] if missing(iso2)
foreach v in cpi e_usd {
    bysort c2: ipolate `v' mdate, gen(`v'_i)
    quietly count if missing(`v') & !missing(`v'_i)
    di "`v': " r(N) " observasi diinterpolasi"
    replace `v' = `v'_i
    drop `v'_i
}
drop c2

* ---- RER bilateral vs Indonesia
preserve
    keep if iso2 == "ID"
    keep mdate e_usd cpi
    rename (e_usd cpi) (e_id cpi_id)
    tempfile id
    save `id'
restore
drop if iso2 == "ID"
merge m:1 mdate using `id', keep(match) nogen
gen ner = ln(e_id / e_usd)                      // ln Rp per unit mata uang mitra
gen rer = ner + ln(cpi) - ln(cpi_id)
gen str3 iso3 = ""
local pairs AU AUS CN CHN IN IND JP JPN KR KOR MY MYS SG SGP TH THA US USA VN VNM
while "`pairs'" != "" {
    gettoken a pairs : pairs
    gettoken b pairs : pairs
    replace iso3 = "`b'" if iso2 == "`a'"
}
format mdate %tm
keep iso3 mdate ner rer cpi
label var ner "ln kurs nominal Rp per mata uang mitra (naik = depresiasi)"
label var rer "ln kurs riil bilateral (naik = depresiasi riil rupiah)"
drop if missing(rer)
save intermediate/analisis/rer_bilateral.dta, replace

* ---- panel mitra x bulan
use intermediate/analisis/ana_partner.dta, clear
merge 1:1 iso3 mdate using intermediate/analisis/rer_bilateral.dta, keep(master match) nogen
xtset cid mdate
gen dep = -lnreer                               // naik = depresiasi riil efektif
save intermediate/analisis/lp_partner.dta, replace

* ---- panel mitra x kelompok x bulan
use intermediate/analisis/trade_group_partner.dta, clear
drop if x <= 0 | m <= 0
gen lntb = ln(x / m)
merge m:1 iso3 mdate using intermediate/analisis/rer_bilateral.dta, keep(match) nogen
merge m:1 iso3 mdate using intermediate/analisis/ana_partner.dta, keep(match) nogen ///
    keepusing(yf lncom lncom_nrg lncom_fd m2-m12 covid gfc cid)
egen pg = group(iso3 grp)
xtset pg mdate
save intermediate/analisis/lp_group_partner.dta, replace

* ---- agregat + indeks USD broad (Fed, DTWEXBGS) rata-rata bulanan
import delimited using input/raw/fred/DTWEXBGS.csv, clear
gen mdate = mofd(date(observation_date, "YMD"))
collapse (mean) usd = dtwexbgs, by(mdate)
gen lnusd = ln(usd)
label var lnusd "ln indeks dolar AS broad (naik = USD menguat)"
tempfile u
save `u'
use intermediate/analisis/ana_aggregate.dta, clear
merge 1:1 mdate using `u', keep(master match) nogen
tsset mdate
gen dep = -lnreer
gen depn = lnjis
label var dep "-ln REER (naik = depresiasi riil)"
save intermediate/analisis/lp_aggregate.dta, replace

* ringkasan korelasi RER bilateral vs REER
use intermediate/analisis/lp_partner.dta, clear
bysort iso3: egen n_rer = count(rer)
xtset cid mdate
gen d_rer = D.rer
gen d_dep = D.dep
tabstat d_rer d_dep n_rer, by(iso3) stat(sd max) format(%6.3f)
bysort iso3: corr d_rer d_dep
