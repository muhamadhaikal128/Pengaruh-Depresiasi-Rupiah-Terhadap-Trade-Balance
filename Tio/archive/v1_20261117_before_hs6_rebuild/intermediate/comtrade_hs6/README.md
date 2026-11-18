# UN Comtrade HS-6 panels

This is a separate data source. Existing Trade Map, GEM, model results and presentation are unchanged.

- `monthly/`: monthly long panels, partitioned by quarter, including monthly macro/price controls.
- `quarterly/*_Long.csv.gz`: strict quarter totals, quantities and coverage flags.
- `quarterly/*_TwoFlow_Macro.csv.gz`: exports/imports joined with quarterly GDP, FX, CPI and commodity controls.
- `annual/`: supplementary annual data beginning 2006. These are never disaggregated to months.
- `HS6_Commodity_Classification_By_Edition.csv`: direct HS6-SITC3 UNCTAD A11 classification.
- `File_Index.csv`: row counts and checksums. All CSV.GZ files can be read by pandas with compression inferred.

Values are current USD; USDk columns divide by 1,000. Reporter is Indonesia; partners include the ten research partners and World. Comtrade India=699; USA trade area=842 includes Puerto Rico and US Virgin Islands. Native HS edition is part of every product key. No temporal HS harmonisation is asserted.

Monthly source absence is not silently treated as zero. Quarter `Observed_*` fields sum available rows; strict `Trade_Value_USD` requires three actual product-month rows. Weight/quantity also require usable source values and consistent units. Missing or zero denominators never yield unit values. Unit values are not pure price indexes; quality/composition can change. No total-weight price index across dissimilar products is constructed.

Quarterly macro availability flags are not estimation eligibility certificates. Unit-root, cointegration, common support, identification and multiple testing require further work. Existing macro audit caveats remain. Annual files are kept annual and have no fabricated quarterly GDP. Diagnostics and provenance are in `output/diagnostics/comtrade_hs6/` and the raw download manifest.
