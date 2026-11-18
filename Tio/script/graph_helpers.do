* Native editable Stata graphs from the exact numerical plotting data.
* PNG/PDF are rendered by 14_report_oskooee_results.py (batch needs no Graph window).
version 19
clear all
set more off
args project
if `"`project'"'=="" local project "F:/Trade-Balance/Tio"
cd "`project'"
global OP "`project'"
capture log close
log using "$OP/output/diagnostics/oskooee/native_graphs.log", text replace
import delimited "$OP/output/tables/oskooee/results_primary_models.csv", clear varnames(1) case(preserve) encoding(utf8)
levelsof model_id, local(models)
foreach id of local models {
    import delimited "$OP/output/diagnostics/oskooee/dynamic_multipliers.csv", clear varnames(1) case(preserve)
    keep if model_id=="`id'"
    twoway (rarea lower95_logpoints upper95_logpoints horizon_quarters if direction=="depreciation", color(navy%15) lwidth(none)) (line effect_logpoints horizon_quarters if direction=="depreciation", lcolor(navy)) (rarea lower95_logpoints upper95_logpoints horizon_quarters if direction=="appreciation", color(orange%15) lwidth(none)) (line effect_logpoints horizon_quarters if direction=="appreciation", lcolor(orange)), yline(0) title("`id'") subtitle("Dynamic response to +/-ln(1.10) q shock") xtitle("Quarter") ytitle("100 x change in ln(M/X)") legend(order(2 "Depreciation" 4 "Appreciation")) name(dm,replace) nodraw
    graph save dm "$OP/output/gph/oskooee/`id'_multipliers.gph", replace
    import delimited "$OP/output/diagnostics/oskooee/stability_paths.csv", clear varnames(1) case(preserve)
    keep if model_id=="`id'"
    format tq %tq
    if _N>0 {
        twoway (rarea lower upper tq, color(navy%15) lwidth(none)) (line CUSUMSQ tq, lcolor(navy)) (line expected tq, lpattern(dash) lcolor(gs8)), title("`id': CUSUMSQ") subtitle("Gaussian-reference MC 95% band; 19,999 draws") legend(order(2 "CUSUMSQ" 3 "Expected path")) name(sq,replace) nodraw
        graph save sq "$OP/output/gph/oskooee/`id'_cusumsq.gph", replace
    }
    use "$OP/output/diagnostics/oskooee/models/`id'_design.dta", clear
    format tq %tq
    twoway line residual tq, yline(0) title("`id': residuals") name(re,replace) nodraw
    graph save re "$OP/output/gph/oskooee/`id'_residuals.gph", replace
    capture graph drop _all
}
do "$OP/script/group_forests.do"
display "OSKOOEE_NATIVE_GRAPHS_COMPLETED"
log close
exit, clear
