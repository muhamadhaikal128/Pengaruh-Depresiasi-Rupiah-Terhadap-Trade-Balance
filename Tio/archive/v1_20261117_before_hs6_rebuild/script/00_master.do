* Stata estimation master. Prepared datasets are in intermediate/.
* Complete Python -> Stata -> reporting workflow: 00_run_oskooee.ps1.
version 19
args project
if `"`project'"'=="" local project "F:/Trade-Balance/Tio"
do "`project'/script/13_run_oskooee_models.do" "`project'"
