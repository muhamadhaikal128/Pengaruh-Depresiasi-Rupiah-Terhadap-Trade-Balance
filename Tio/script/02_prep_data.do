* Data built from 22 HS-6 workbooks; no HS-4 trade data used.
import delimited "$OP/intermediate/Oskooee_Quarterly_Analysis.csv", clear varnames(1) case(preserve) encoding(utf8) asdouble
format tq %tq
isid sid tq
assert x>0 & m>0
assert abs(y-ln(m/x))<1e-9
save "$OP/intermediate/oskooee/analysis_quarterly.dta", replace
