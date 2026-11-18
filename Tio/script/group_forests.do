* Seven overlapping groups; one editable forest per partner and estimator.
import delimited "$OP/output/tables/oskooee/Forest_Goods_Data.csv", clear varnames(1) case(preserve) encoding(utf8) asdouble
levelsof ISO3, local(partners)
foreach iso of local partners {
    foreach est in ARDL NARDL {
        preserve
        keep if ISO3=="`iso'" & estimator=="`est'"
        gen byte axis=8-Order
        label define goods_axis 7 "Non-komoditas (manufaktur)" 6 "Barang konsumsi" 5 "Komoditas pertanian & pangan" 4 "Bahan baku/penolong" 3 "Barang modal" 2 "Komoditas (total)" 1 "Komoditas energi & tambang", replace
        label values axis goods_axis
        local term "q"
        if "`est'"=="NARDL" local term "NEG"
        twoway (rcap Lo95 Hi95 axis, horizontal lcolor(gs9)) (scatter axis Estimate if Supported==1 & Clean==1, msymbol(O) mcolor("165 100 78")) (scatter axis Estimate if Supported==1 & Clean==0, msymbol(O) mcolor("193 117 41")) (scatter axis Estimate if Supported==0, msymbol(Oh) mcolor(gs7)), xline(0,lcolor(maroon)) ylabel(1(1)7,valuelabel angle(0) labsize(small)) yscale(range(.5 7.5)) ytitle("") xtitle("Koefisien jangka panjang `term' (CI nominal 95%)",size(small)) title("Efek jangka panjang per kelompok: `iso'") subtitle("`est' | y = ln(M/X); q naik = apresiasi",size(small)) note("Positif: arah perbaikan neraca saat depresiasi. Kelompok saling tumpang tindih." "Koefisien tanpa dukungan levels belum layak ditafsirkan sebagai hubungan LR mapan.",size(vsmall)) legend(order(2 "Levels + diagnostik" 3 "Levels; caveat diagnostik" 4 "Levels belum didukung") rows(1) size(vsmall)) graphregion(color(white)) plotregion(color(white)) xsize(12) ysize(7) name(groupforest,replace) nodraw
        graph save groupforest "$OP/output/gph/oskooee/forest_`iso'_`est'_goods.gph", replace
        * PNG/PDF use the identical coefficient data through the reporting script;
        * batch Stata retains the native editable GPH without requiring a Graph window.
        graph drop groupforest
        restore
    }
}
