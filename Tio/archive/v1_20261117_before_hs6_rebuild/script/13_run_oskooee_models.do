* ARDL/NARDL replication: paper outcome ln(M/X), q up = appreciation.
* Run from Tio, or: do script/13_run_oskooee_models.do F:/Trade-Balance/Tio
version 19
clear all
set more off
set linesize 180
set seed 20261117
args project pilotsid
if `"`project'"'=="" local project "F:/Trade-Balance/Tio"
cd "`project'"
global OP "`project'"
adopath ++ "$OP/input/reference/oskooee_replication/stata_ado"
capture mkdir "$OP/output/tables/oskooee"
capture mkdir "$OP/output/figures/oskooee"
capture mkdir "$OP/output/gph/oskooee"
capture mkdir "$OP/output/diagnostics/oskooee/models"
capture mkdir "$OP/intermediate/oskooee"
capture log close
log using "$OP/output/diagnostics/oskooee/estimation.log", text replace
import delimited "$OP/intermediate/Oskooee_Quarterly_Analysis.csv", clear varnames(1) case(preserve) encoding(utf8)
format tq %tq
save "$OP/intermediate/oskooee/analysis_quarterly.dta", replace
levelsof sid, local(sids)
if "`pilotsid'"!="" local sids "`pilotsid'"
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
capture program drop fitcase
program define fitcase
    args sid est cap
    preserve
    use "$OP/intermediate/oskooee/analysis_quarterly.dta", clear
    keep if sid==`sid'
    tsset tq
    local code=series_id[1]
    local scope=scope[1]
    local scen=scenario[1]
    local price=price_control[1]
    local id "`code'_`est'_AIC`cap'"
    local xx "yd yf q"
    gen double dq=D.q
    gen double pos=sum(cond(missing(dq),0,max(dq,0)))
    gen double neg=sum(cond(missing(dq),0,min(dq,0)))
    if "`est'"=="NARDL" local xx "yd yf pos neg"
    if `price' local xx "`xx' cp"
    quietly summarize tq
    local fixedstart=r(min)+`cap'
    * The same maximum-lag holdback is used for ARDL and NARDL within a cap.
    capture noisily ardl y `xx', maxlags(`cap') aic ec1 regstore(uecm)
    if _rc {
        post $PF ("`id'") ("ardl_estimation") (_rc)
        restore
        exit
    }
    estimates store ecmodel
    gen byte es=e(sample)
    local NN=e(N)
    local df=e(df_r)
    local rsqa=e(r2_a)
    local rss=e(rss)
    local Fstat=e(F_pss)
    local tstat=e(t_pss)
    matrix LAG=e(lags)
    matrix EB=e(b)
    matrix EV=e(V)
    local terms : colfullnames EB
    local kk=colsof(EB)
    local j=0
    foreach term of local terms {
        local ++j
        local bb=EB[1,`j']
        local ss=sqrt(max(0,EV[`j',`j']))
        local tt=cond(`ss'>0,`bb'/`ss',.)
        local pp=cond(`ss'>0,2*ttail(`df',abs(`tt')) ,.)
        local cv=invttail(`df',.025)
        post $PC ("`id'") ("`term'") (`bb') (`ss') (`tt') (`pp') (`bb'-`cv'*`ss') (`bb'+`cv'*`ss')
    }
    foreach s in Fp0 Fp1 tp0 tp1 Flo Fhi tlo thi Flo10 Fhi10 lap sap xp bg1 bg4 het reset cus ccv {
        local `s'=.
    }
    capture noisily estat ectest
    if !_rc {
        matrix CV=r(cvmat)
        local Fp0=CV[1,7]
        local Fp1=CV[1,8]
        local tp0=CV[2,7]
        local tp1=CV[2,8]
        local Flo=CV[1,3]
        local Fhi=CV[1,4]
        local tlo=CV[2,3]
        local thi=CV[2,4]
        local Flo10=CV[1,1]
        local Fhi10=CV[1,2]
    }
    else post $PF ("`id'") ("bounds_test") (_rc)
    if "`est'"=="NARDL" {
        capture noisily test [LR]L.pos = [LR]L.neg
        if !_rc local lap=r(p)
        local pe "0"
        local ne "0"
        foreach term of local terms {
            if substr("`term'",1,3)=="SR:" & strpos("`term'",".pos") local pe "`pe' + _b[`term']"
            if substr("`term'",1,3)=="SR:" & strpos("`term'",".neg") local ne "`ne' + _b[`term']"
        }
        capture noisily testnl (`pe' = `ne')
        if !_rc local sap=r(p)
    }
    estimates restore uecm
    local rnames : colnames e(b)
    local rvars : subinstr local rnames "_cons" "", all
    local rdep "`e(depvar)'"
    local K=e(rank)
    local ai=`NN'*ln(e(rss)/`NN')+2*`K'
    local bi=`NN'*ln(e(rss)/`NN')+ln(`NN')*`K'
    * Extra lagged-X levels restriction, with q=0 current-X equivalents.
    local levelx ""
    foreach x of local xx {
        local found=0
        foreach n of local rnames {
            if "`n'"=="L.`x'" | "`n'"=="L1.`x'" {
                local levelx "`levelx' `n'"
                local found=1
            }
        }
        if !`found' local levelx "`levelx' `x'"
    }
    capture noisily test `levelx'
    if !_rc local xp=r(p)
    capture noisily estat bgodfrey, lags(1 4)
    if !_rc {
        matrix BP=r(p)
        local bg1=BP[1,1]
        local bg4=BP[1,2]
    }
    capture noisily estat hettest
    if !_rc local het=r(p)
    * RESET with one squared fitted-value term, on the estimated UECM.
    predict double uf if es, xb
    gen double uf2=uf^2
    capture quietly regress `rdep' `rvars' uf2 if es
    if !_rc {
        quietly test uf2
        local reset=r(p)
    }
    estimates restore uecm
    capture noisily estat sbcusum, name(cs,replace) nodraw title("`id': recursive CUSUM")
    if !_rc {
        local cus=r(cusum)
        matrix CC=r(cvalues)
        local ccv=CC[1,2]
        if "`scen'"=="main" & `cap'==4 {
            graph save "$OP/output/gph/oskooee/`id'_cusum.gph", replace
        }
    }
    else post $PF ("`id'") ("recursive_cusum") (_rc)
    capture graph drop _all
    * Refit the algebraically identical ARDL levels equation on EXACT same sample.
    local py=LAG[1,1]
    local vars "L(1/`py').y"
    local j=1
    foreach x of local xx {
        local ++j
        local qx=LAG[1,`j']
        local vars "`vars' L(0/`qx').`x'"
    }
    quietly regress y `vars' if es
    local rd=abs(e(rss)-`rss')
    local full=(e(rank)==colsof(e(b)))
    if `rd'>1e-7*max(1,`rss') | e(N)!=`NN' {
        post $PF ("`id'") ("levels_ECM_equivalence") (459)
    }
    matrix LB=e(b)
    matrix LV=e(V)
    local lterms : colnames LB
    local lk=colsof(LB)
    local j=0
    foreach term of local lterms {
        local ++j
        post $PL ("`id'") (`j') ("`term'") (LB[1,`j']) (sqrt(max(0,LV[`j',`j'])))
        forvalues h=1/`lk' {
            post $PV ("`id'") (`j') (`h') (LV[`j',`h'])
        }
    }
    predict double residual if es, residuals
    predict double fitted if es, xb
    fvrevar `vars'
    local generated "`r(varlist)'"
    local j=0
    foreach v of local generated {
        local ++j
        gen double X`j'=`v'
    }
    local ++j
    gen double X`j'=1
    if `j'!=`lk' post $PF ("`id'") ("design_column_count") (459)
    estimates save "$OP/output/diagnostics/oskooee/models/`id'.ster", replace
    post $PS ("`id'") ("`code'") ("`est'") ("`scope'") ("`scen'") (`cap') (`NN') (`df') (`rsqa') (`ai') (`bi') (`Fstat') (`tstat') (`Fp0') (`Fp1') (`tp0') (`tp1') (`Flo') (`Fhi') (`tlo') (`thi') (`Flo10') (`Fhi10') (`lap') (`sap') (`xp') (`bg1') (`bg4') (`het') (`reset') (`cus') (`ccv') (`rd') (`full')
    keep if es
    keep tq y yd yf q pos neg cp residual fitted X*
    save "$OP/output/diagnostics/oskooee/models/`id'_design.dta", replace
    export delimited using "$OP/output/diagnostics/oskooee/models/`id'_design.csv", replace
    restore
end

foreach s of local sids {
    preserve
    keep if sid==`s'
    local code=series_id[1]
    local scen=scenario[1]
    tsset tq
    gen double deltaq=D.q
    gen double pos=sum(cond(missing(deltaq),0,max(deltaq,0)))
    gen double neg=sum(cond(missing(deltaq),0,min(deltaq,0)))
    foreach v in y yd yf q pos neg cp {
        quietly count if !missing(`v')
        if r(N)<40 continue
        foreach tr in level diff {
            tempvar a trend
            if "`tr'"=="level" gen double `a'=`v'
            else gen double `a'=D.`v'
            gen double `trend'=tq
            * BIC selection on a common maximum-four-lag ADF sample.
            quietly summarize tq
            local cutoff=r(min)+6
            local best=.
            local selected=0
            forvalues l=0/4 {
                local dl ""
                if `l'>0 local dl "L(1/`l').D.`a'"
                quietly regress D.`a' L.`a' `dl' if tq>=`cutoff'
                local crit=e(N)*ln(e(rss)/e(N))+e(rank)*ln(e(N))
                if `crit'<`best' {
                    local best=`crit'
                    local selected=`l'
                }
            }
            capture quietly dfuller `a', lags(`selected')
            if !_rc post `PU' (`s') ("`code'") ("`v'") ("`tr'") ("ADF_BIC") (`selected') (r(Zt)) (r(p)) (r(N))
            capture quietly pperron `a', lags(4)
            if !_rc post `PU' (`s') ("`code'") ("`v'") ("`tr'") ("PP") (4) (r(Zt)) (r(p)) (r(N))
            if "`tr'"=="level" {
                capture quietly dfuller `a', lags(`selected') trend
                if !_rc post `PU' (`s') ("`code'") ("`v'") ("`tr'") ("ADF_trend") (`selected') (r(Zt)) (r(p)) (r(N))
            }
            drop `a' `trend'
        }
    }
    restore
    foreach estimator in ARDL NARDL {
        noisily display "RUNNING SID `s': `estimator' AIC4"
        capture noisily fitcase `s' `estimator' 4
        if _rc post `PF' ("SID`s'_`estimator'_4") ("unhandled") (_rc)
        if "`scen'"=="main" {
            noisily display "RUNNING SID `s': `estimator' AIC2"
            capture noisily fitcase `s' `estimator' 2
            if _rc post `PF' ("SID`s'_`estimator'_2") ("unhandled") (_rc)
        }
    }
}
foreach h in PS PC PL PV PU PF {
    postclose ``h''
}
foreach file in model_summary coefficients_ecm coefficients_levels covariance_levels {
    use "$OP/output/tables/oskooee/`file'.dta", clear
    export delimited "$OP/output/tables/oskooee/`file'.csv", replace
}
foreach file in unit_root_tests model_failures {
    use "$OP/output/diagnostics/oskooee/`file'.dta", clear
    export delimited "$OP/output/diagnostics/oskooee/`file'.csv", replace
}
noisily display "OSKOOEE_ESTIMATION_COMPLETED"
log close
exit, clear
