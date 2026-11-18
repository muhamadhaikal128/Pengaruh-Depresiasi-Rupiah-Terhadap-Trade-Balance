version 19
clear all
set more off
capture log close
log using "F:/Trade-Balance/Tio/output/diagnostics/ardl_api_probe.log", text replace
adopath ++ "F:/Trade-Balance/Tio/input/reference/oskooee_replication/stata_ado"
import delimited using "F:/Trade-Balance/Tio/intermediate/Panel_Country_Quarter.csv", clear varnames(1) case(preserve)
keep if ISO3=="CHN"
gen tq=quarterly(Quarter,"YQ")
format tq %tq
tsset tq
gen y=Ln_Imports_Exports
gen yd=ln(IDN_GDP_Real_Index_2015mean100)
unab pg : Partner_GDP_Real_Index*
gen yf=ln(`pg')
gen q=-ln(RER_Bilateral_Index_2015mean100)
keep if tq<=yq(2026,2)
gen dq=D.q
gen pos=sum(cond(missing(dq),0,max(dq,0)))
gen neg=sum(cond(missing(dq),0,min(dq,0)))
ardl y yd yf pos neg, maxlags(2) aic ec1 regstore(ureg)
ereturn list
matrix list e(b)
matrix list e(lags)
estimates store ecmodel
estat ectest
return list
matrix list r(cvmat)
estimates restore ureg
matrix list e(b)
local names : colfullnames e(b)
display "NAMES `names'"
estat bgodfrey, lags(1 4)
return list
estat hettest
return list
estat ovtest
return list
capture noisily estat sbcusum
capture noisily return list
capture noisily estat sbcusum, ols
capture noisily return list
log close
exit, clear
