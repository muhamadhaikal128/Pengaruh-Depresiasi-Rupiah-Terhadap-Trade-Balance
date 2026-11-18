# HS4 commodity/noncommodity panels

UNCTAD A11 with conservative HS4 consensus across official direct UNSD HS1992-2022 correlations.

- commodity/: 358 codes; HS4_<ISO3>_Month.csv and HS4_<ISO3>_Quarter.csv.
- noncommodity/: 857 codes; same layout.
- mixed/: 47 codes retained separately; not binary noncommodity.
- unclassified/: 2 special codes retained separately.
- Each folder has HS4_List.csv. Every trade panel contains both exports and imports.
- examples/: two single-product China panels with macro variables, GDP/RER logs and availability flags.

Read [the full methodology and usage guide](../../notes/klasifikasi_komoditas_hs4.md).
Master classification: [HS4_Commodity_Classification.csv](../HS4_Commodity_Classification.csv).
Macro-joined group panel: [Panel_CommodityGroup_Country_Quarter.csv](../Panel_CommodityGroup_Country_Quarter.csv).

Keep HS_Code as text; keep observed zero trade as zero. Unknown values are not zeros.
Quarterly flows require three observed months. Log(X/M) and log(M/X) require both flows > 0.
The stable category label does not assert full historical HS harmonisation.
