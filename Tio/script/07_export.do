args phase project
if `"`project'"'!="" global OP "`project'"
if "$OP"=="" global OP "F:/Trade-Balance/Tio"
if "`phase'"=="graphs" {
    do "$OP/script/graph_helpers.do" "$OP"
    exit
}
postclose $PS
postclose $PC
postclose $PL
postclose $PV
postclose $PU
postclose $PF
foreach file in model_summary coefficients_ecm coefficients_levels covariance_levels {
    use "$OP/output/tables/oskooee/`file'.dta", clear
    export delimited "$OP/output/tables/oskooee/`file'.csv", replace
}
foreach file in unit_root_tests model_failures {
    use "$OP/output/diagnostics/oskooee/`file'.dta", clear
    export delimited "$OP/output/diagnostics/oskooee/`file'.csv", replace
}
