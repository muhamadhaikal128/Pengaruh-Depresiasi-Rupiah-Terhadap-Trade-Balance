* Unit-root tests before estimation; residual/stability tests are inside fitcase.
use "$OP/intermediate/oskooee/analysis_quarterly.dta", clear
levelsof sid, local(sids)
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
            if !_rc post $PU (`s') ("`code'") ("`v'") ("`tr'") ("ADF_BIC") (`selected') (r(Zt)) (r(p)) (r(N))
            capture quietly pperron `a', lags(4)
            if !_rc post $PU (`s') ("`code'") ("`v'") ("`tr'") ("PP") (4) (r(Zt)) (r(p)) (r(N))
            if "`tr'"=="level" {
                capture quietly dfuller `a', lags(`selected') trend
                if !_rc post $PU (`s') ("`code'") ("`v'") ("`tr'") ("ADF_trend") (`selected') (r(Zt)) (r(p)) (r(N))
            }
            drop `a' `trend'
        }
    }
    restore
}
