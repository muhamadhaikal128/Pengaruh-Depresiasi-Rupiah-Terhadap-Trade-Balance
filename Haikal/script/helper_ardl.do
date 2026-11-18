* =============================================================================
* helper_ardl.do : program bantu ardl_post, di-load oleh 00_master.do sebelum 04-06
*
* ardl_post depvar xvars [if], exog() xfocus() id() label() post() [dmpost() ic() maxlags() trend()]
*   - estimasi ARDL bentuk EC (Kripfganz & Schneider, paket -ardl-), lag dipilih AIC/BIC
*   - uji bounds PSS (2001) dengan p-value Kripfganz & Schneider (2020)
*   - diagnostik: Breusch-Godfrey LM(12), ARCH(12), Ramsey RESET
*   - dynamic multiplier kumulatif untuk xfocus (bentuk level, lag sama)
*   - kirim satu baris hasil ke postfile `post', dan jalur multiplier ke `dmpost'
*
* Konvensi tanda: xfocus = ln REER (naik = apresiasi riil). Kolom "eff10_*" sudah dibalik
* menjadi efek DEPRESIASI riil 10% terhadap rasio X/M dalam persen:
*   eff10 = -0.10 * koefisien * 100  (positif = depresiasi memperbaiki trade balance)
* =============================================================================

capture program drop ardl_post
program define ardl_post
    version 19
    syntax varlist(ts min=2) [if], exog(string) xfocus(name) id(string) label(string) post(name) ///
        [dmpost(name) ic(string) MAXLags(numlist) trend(string) H(integer 36)]

    if "`ic'" == ""      local ic aic
    if "`maxlags'" == "" local maxlags 12
    gettoken y xs : varlist
    local trendopt
    if "`trend'" != "" local trendopt trendvar(`trend')

    * ---- 1. EC form, lag selection
    capture noisily ardl `varlist' `if', exog(`exog') maxlags(`maxlags') `ic' ec `trendopt'
    if _rc {
        post `post' ("`id'") ("`label'") ("`ic'") (.) ("gagal") (.) (.) (.) (.) (.) (.) (.) (.) (.) ///
            (.) (.) (.) (.) (.) (.) (.) (.) (.) (.) (.) (.)
        exit
    }
    tempname L
    matrix `L' = e(lags)
    local N = e(N)
    local lagstr ""
    forvalues j = 1/`=colsof(`L')' {
        local lagstr "`lagstr'`=cond(`j'>1, ",", "")'`=`L'[1,`j']'"
    }
    local lagstr "(`lagstr')"
    local adj   = _b[ADJ:L.`y']
    local adjse = _se[ADJ:L.`y']
    local lr    = _b[LR:`xfocus']
    local lrse  = _se[LR:`xfocus']
    local lrp   = 2 * ttail(e(df_r), abs(`lr' / `lrse'))
    * dampak jangka pendek (bulan ke-0) dan jumlah koefisien SR
    capture local sr0 = _b[SR:D.`xfocus']
    if _rc local sr0 = .
    capture local sr0se = _se[SR:D.`xfocus']
    if _rc local sr0se = .
    local sr0p = cond(missing(`sr0'), ., 2 * ttail(e(df_r), abs(`sr0' / `sr0se')))

    * ---- 2. bounds test
    quietly estat ectest
    tempname cv
    matrix `cv' = r(cvmat)
    local F  = r(F_pss)
    local t  = r(t_pss)
    local pF = `cv'[1, 8]            // p-value batas I(1)
    local pt = `cv'[2, 8]
    local co10 = (`pF' < .10) & (`pt' < .10)
    local co05 = (`pF' < .05) & (`pt' < .05)

    * ---- 3. diagnostik residual
    quietly estat bgodfrey, lags(12)
    local p_bg = el(r(p), 1, 1)
    quietly estat archlm, lags(12)
    local p_arch = el(r(p), 1, 1)
    capture quietly estat ovtest
    local p_reset = cond(_rc, ., r(p))

    * ---- 4. dynamic multiplier (bentuk level, lag sama)
    local lagnum ""
    forvalues j = 1/`=colsof(`L')' {
        local lagnum "`lagnum' `=`L'[1,`j']'"
    }
    quietly ardl `varlist' `if', exog(`exog') lags(`lagnum') `trendopt'
    local p = `L'[1, 1]
    local xpos : list posof "`xfocus'" in varlist
    local q = `L'[1, `xpos']
    * respons impuls d_s = beta_s + sum_i phi_i d_{s-i}, lalu kumulatif (Mata: ardl_dm)
    tempname B Phi
    matrix `B'   = J(1, `q' + 1, 0)
    forvalues s = 0/`q' {
        if `s' == 0 matrix `B'[1, 1] = _b[`xfocus']
        else        matrix `B'[1, `s' + 1] = _b[L`s'.`xfocus']
    }
    matrix `Phi' = J(1, max(`p', 1), 0)
    forvalues i = 1/`p' {
        matrix `Phi'[1, `i'] = _b[L`i'.`y']
    }
    mata: _dm = ardl_dm(st_matrix("`B'"), st_matrix("`Phi'"), `p', `h')
    mata: st_local("dm0",  strofreal(_dm[1],  "%21.0g"))
    mata: st_local("dm3",  strofreal(_dm[4],  "%21.0g"))
    mata: st_local("dm6",  strofreal(_dm[7],  "%21.0g"))
    mata: st_local("dm12", strofreal(_dm[13], "%21.0g"))
    mata: st_local("dm24", strofreal(_dm[25], "%21.0g"))
    mata: st_local("dmmax6", strofreal(max(_dm[1..7]), "%21.0g"))
    if "`dmpost'" != "" {
        forvalues s = 0/`h' {
            mata: st_local("v", strofreal(_dm[`s' + 1], "%21.0g"))
            post `dmpost' ("`id'") ("`label'") (`s') (-10 * `v')
        }
    }

    * J-curve (Rose-Yellen / Bahmani-Oskooee): depresiasi awalnya memperburuk TB
    * (multiplier REER > 0 dalam 6 bulan pertama) lalu memperbaiki dalam jangka panjang
    * (koefisien LR < 0 dan signifikan 10%, dengan kointegrasi).
    local jc = (`dmmax6' > 0) & (`lr' < 0) & (`lrp' < .10) & `co10'

    post `post' ("`id'") ("`label'") ("`ic'") (`N') ("`lagstr'") (`F') (`t') (`pF') (`pt') (`co10') (`co05') ///
        (`adj') (`adjse') (`lr') (`lrse') (`lrp') (`sr0') (`sr0p') ///
        (-10 * `lr') (-10 * `sr0') (-10 * `dm6') (-10 * `dm12') (-10 * `dm24') (`p_bg') (`p_arch') (`jc')
end

* postfile header yang cocok dengan ardl_post
capture program drop ardl_postfile
program define ardl_postfile
    syntax name, saving(string)
    postfile `namelist' str20 id str45 label str4 ic N str40 lags F t pF pt coint10 coint05 ///
        adj adj_se lr lr_se lr_p sr0 sr0_p eff10_lr eff10_sr0 eff10_m6 eff10_m12 eff10_m24 ///
        p_lm12 p_arch12 jcurve using `saving', replace
end

mata:
// cumulative dynamic multipliers m_h = sum_{j<=h} d_j, with impulse responses
// d_s = beta_s + sum_i phi_i d_{s-i}
real colvector ardl_dm(real rowvector B, real rowvector Phi, real scalar p, real scalar h)
{
    real colvector d, m
    real scalar s, i
    d = J(h + 1, 1, 0)
    for (s = 0; s <= h; s++) {
        d[s + 1] = (s + 1 <= cols(B) ? B[s + 1] : 0)
        for (i = 1; i <= p; i++) {
            if (s - i >= 0) d[s + 1] = d[s + 1] + Phi[i] * d[s - i + 1]
        }
    }
    m = runningsum(d)
    return(m)
}
end
