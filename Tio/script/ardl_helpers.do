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

