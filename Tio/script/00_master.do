* HS-6 rebuild: actual Stata ARDL and NARDL estimation.
version 19
clear all
set more off
set type double
set linesize 180
set seed 20261117
args project
if `"`project'"'=="" local project "F:/Trade-Balance/Tio"
cd "`project'"
global OP "`project'"
adopath ++ "$OP/input/reference/oskooee_replication/stata_ado"
foreach folder in tables figures gph diagnostics {
    capture mkdir "$OP/output/`folder'/oskooee"
}
capture mkdir "$OP/output/diagnostics/oskooee/models"
capture mkdir "$OP/intermediate/oskooee"
capture log close
log using "$OP/output/diagnostics/oskooee/estimation.log", text replace
tempname PS PC PL PV PU PF
postfile `PS' str80 model_id str50 series_id str10 estimator str30 scope str30 scenario int cap double N df_r r2a AIC BIC F_pss t_pss F_pI0 F_pI1 t_pI0 t_pI1 F_lo5 F_hi5 t_lo5 t_hi5 F_lo10 F_hi10 lr_asym_p sr_asym_p lr_x_p bg1_p bg4_p hetero_p reset_p cusum cusum_cv5 level_RSS_diff rank_full using "$OP/output/tables/oskooee/model_summary.dta", replace
postfile `PC' str80 model_id str60 term double b se t p lo95 hi95 using "$OP/output/tables/oskooee/coefficients_ecm.dta", replace
postfile `PL' str80 model_id int idx str60 term double b se using "$OP/output/tables/oskooee/coefficients_levels.dta", replace
postfile `PV' str80 model_id int i j double covariance using "$OP/output/tables/oskooee/covariance_levels.dta", replace
postfile `PU' int sid str50 series_id str12 variable str12 transform str12 test int lag double statistic p N using "$OP/output/diagnostics/oskooee/unit_root_tests.dta", replace
postfile `PF' str80 model_id str30 stage int rc using "$OP/output/diagnostics/oskooee/model_failures.dta", replace
global PS `PS'
global PC `PC'
global PL `PL'
global PV `PV'
global PF `PF'

global PU `PU'

do "$OP/script/ardl_helpers.do"
do "$OP/script/02_prep_data.do"
do "$OP/script/06_diagnostics.do"
do "$OP/script/03_ardl_agregat.do"
do "$OP/script/04_ardl_mitra.do"
do "$OP/script/05_ardl_kelompok.do"
do "$OP/script/07_export.do" coefficients
noisily display "OSKOOEE_ESTIMATION_COMPLETED"
log close
exit, clear
