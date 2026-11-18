version 19
clear all
set more off
capture log close
log using "F:/Trade-Balance/Tio/output/diagnostics/stata_environment_probe.log", text replace
noisily display "STATA_VERSION=" c(stata_version)
noisily display "STATA_FLAVOR=" c(flavor)
capture noisily which ardl
capture noisily which nardl
capture noisily which estat ectest
capture noisily which cusum6
capture noisily which estat sbcusum
capture noisily sysdir
log close
exit, clear
