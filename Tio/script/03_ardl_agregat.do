use "$OP/intermediate/oskooee/analysis_quarterly.dta", clear
levelsof sid if scope=="aggregate", local(sids)
foreach s of local sids {
    preserve
    keep if sid==`s'
    local scen=scenario[1]
    restore
    foreach estimator in ARDL NARDL {
        noisily display "RUNNING SID `s': `estimator' AIC4"
        capture noisily fitcase `s' `estimator' 4
        if _rc post $PF ("SID`s'_`estimator'_4") ("unhandled") (_rc)
        if "`scen'"=="main" {
            noisily display "RUNNING SID `s': `estimator' AIC2"
            capture noisily fitcase `s' `estimator' 2
            if _rc post $PF ("SID`s'_`estimator'_2") ("unhandled") (_rc)
        }
    }
}
