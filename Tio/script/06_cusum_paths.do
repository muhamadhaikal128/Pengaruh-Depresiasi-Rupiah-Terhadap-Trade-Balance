* Export official Stata recursive CUSUM paths from fixed selected UECM fits.
* No lag reselection: selected levels lags and exact estimation dates are restored.
version 19
clear all
set more off
set type double
set linesize 180
args project
if `"`project'"'=="" local project "F:/Trade-Balance/Tio"
global OP "`project'"
cd "$OP"
adopath ++ "$OP/input/reference/oskooee_replication/stata_ado"
capture log close
log using "$OP/output/diagnostics/oskooee/cusum_paths.log", text replace
import delimited "$OP/output/diagnostics/oskooee/case_registry.csv", clear case(preserve)
keep series_id scope scenario sid
tempfile registry summaries
save `registry'
use "$OP/output/tables/oskooee/model_summary.dta", clear
merge m:1 series_id scope scenario using `registry', keep(match) nogen
keep if scenario=="main" & cap==4
save `summaries'
levelsof model_id, local(models)
tempname PATHS
postfile `PATHS' str80 model_id double tq CUSUM cusum_lower cusum_upper cusum_expected official_stat using "$OP/output/diagnostics/oskooee/stata_cusum_paths.dta", replace
foreach id of local models {
    use `summaries', clear
    keep if model_id=="`id'"
    local sid=sid[1]
    local estimator=estimator[1]
    local expected_stat=cusum[1]
    local expected_N=N[1]
    estimates use "$OP/output/diagnostics/oskooee/models/`id'.ster"
    local terms : colnames e(b)
    local xx "yd yf q"
    if "`estimator'"=="NARDL" local xx "yd yf pos neg"
    local lags ""
    foreach v in y `xx' {
        local mx=0
        foreach term of local terms {
            if "`term'"=="L.`v'" local mx=max(`mx',1)
            if regexm("`term'","^L([0-9]+)[.]`v'$") local mx=max(`mx',real(regexs(1)))
        }
        local lags "`lags' `mx'"
    }
    use "$OP/output/diagnostics/oskooee/models/`id'_design.dta", clear
    quietly summarize tq
    local first=r(min)
    local last=r(max)
    use "$OP/intermediate/oskooee/analysis_quarterly.dta", clear
    keep if sid==`sid'
    tsset tq
    gen double dq=D.q
    gen double pos=sum(cond(missing(dq),0,max(dq,0)))
    gen double neg=sum(cond(missing(dq),0,min(dq,0)))
    quietly ardl y `xx' if inrange(tq,`first',`last'), lags(`lags') ec1 regstore(uecm)
    assert e(N)==`expected_N'
    estimates restore uecm
    local kk=e(rank)
    gen byte es=e(sample)
    quietly estat sbcusum, nograph generate(official, ci)
    local official_stat=r(cusum)
    assert abs(`official_stat'-`expected_stat')<1e-7
    keep if es
    gen double tau=(_n-`kk')/(_N-`kk')
    forvalues i=1/`=_N' {
        if !missing(official[`i']) post `PATHS' ("`id'") (tq[`i']) (official[`i']) (official_lb[`i']) (official_ub[`i']) (tau[`i']) (`official_stat')
    }
}
postclose `PATHS'
use "$OP/output/diagnostics/oskooee/stata_cusum_paths.dta", clear
export delimited "$OP/output/diagnostics/oskooee/stata_cusum_paths.csv", replace
display "STATA_CUSUM_PATHS_COMPLETED"
log close
exit, clear
