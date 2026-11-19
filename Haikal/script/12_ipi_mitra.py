"""
12_ipi_mitra.py : IPI (Index of Industrial Production) 10 mitra dagang dan rata-rata tertimbangnya

Input
  intermediate/dari_tio/Panel_Country_Month.csv   IPI yoy (%) per mitra (CEIC) dan ekspor/impor Indonesia per mitra
  input/raw/worldbank/gdp_usd_wb.json             PDB nominal USD 2006-2025 (World Bank, NY.GDP.MKTP.CD)

Tiga skema bobot (tetap sepanjang sampel; dinormalkan ulang tiap bulan ke mitra yang datanya tersedia):
  1. pangsa ekspor Indonesia 2006-2026   (dipakai di model dan deck: ukuran pasar mitra bagi ekspor Indonesia)
  2. pangsa total perdagangan 2006-2026
  3. pangsa PDB rata-rata 2006-2025      (ukuran ekonomi mitra)

Output
  output/0_deskriptif/ipi_mitra_10.xlsx   workbook dengan formula hidup (bobot dan rata-rata bisa diubah)
  output/0_deskriptif/ipi_mitra.csv       seri yang sama untuk deck (dihitung di Python, dicek sama dengan Excel)

Jalankan dari folder Haikal/:
  uv run --with pandas --with openpyxl python script/12_ipi_mitra.py
"""
import json
import os

import numpy as np
import pandas as pd
from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(ROOT)
OUTX, OUTC = "output/0_deskriptif/ipi_mitra_10.xlsx", "output/0_deskriptif/ipi_mitra.csv"
ISO = ["AUS", "CHN", "IND", "JPN", "KOR", "MYS", "SGP", "THA", "USA", "VNM"]
NM = {"AUS": "Australia", "CHN": "China", "IND": "India", "JPN": "Jepang", "KOR": "Korea Selatan", "MYS": "Malaysia",
      "SGP": "Singapura", "THA": "Thailand", "USA": "Amerika Serikat", "VNM": "Vietnam"}

# -----------------------------------------------------------------------------
# Data
# -----------------------------------------------------------------------------
d = pd.read_csv("intermediate/dari_tio/Panel_Country_Month.csv")
ipi = d.pivot(index="Date", columns="ISO3", values="IPI_YoY_pct")[ISO].sort_index()
tr = d.groupby("ISO3")[["Exports_USDk", "Imports_USDk"]].sum().loc[ISO] / 1e3          # USD juta
wb = json.load(open("input/raw/worldbank/gdp_usd_wb.json", encoding="utf-8"))[1]
gdp = pd.DataFrame([(r["countryiso3code"], int(r["date"]), r["value"]) for r in wb], columns=["iso", "year", "gdp"])
gdp = gdp.pivot(index="year", columns="iso", values="gdp")[ISO].sort_index() / 1e9     # USD miliar

w = pd.DataFrame({"ekspor": tr.Exports_USDk, "perdagangan": tr.Exports_USDk + tr.Imports_USDk, "pdb": gdp.mean()})
w = w / w.sum()


def wavg(wt):
    a = ipi.notna()
    return (ipi.fillna(0) * wt).sum(axis=1) / (a * wt).sum(axis=1).replace(0, np.nan)


out = pd.DataFrame({"ipi_sederhana": ipi.mean(axis=1), "ipi_w_ekspor": wavg(w.ekspor),
                    "ipi_w_perdagangan": wavg(w.perdagangan), "ipi_w_pdb": wavg(w.pdb),
                    "n_mitra": ipi.notna().sum(axis=1)})
out["ipi_w_ekspor_3b"] = out.ipi_w_ekspor.rolling(3).mean()
out.index.name = "mdate"
out.round(4).to_csv(OUTC)

# -----------------------------------------------------------------------------
# Workbook
# -----------------------------------------------------------------------------
F = "Arial"
f_title, f_head, f_in, f_txt = Font(name=F, bold=True, size=12), Font(name=F, bold=True, size=10), \
    Font(name=F, size=10, color="0000FF"), Font(name=F, size=10)
f_link = Font(name=F, size=10, color="008000")
fill_h, fill_key = PatternFill("solid", fgColor="F3E9E3"), PatternFill("solid", fgColor="FFF2CC")
thin = Border(bottom=Side(style="thin", color="999999"))
wbk = Workbook()

# --- Catatan
ws = wbk.active
ws.title = "Catatan"
notes = [
    ("IPI 10 mitra dagang Indonesia: rata-rata sederhana dan tertimbang", f_title),
    ("", f_txt),
    ("Isi workbook", f_head),
    ("Bobot: ukuran tiap mitra (ekspor Indonesia, total perdagangan, PDB) dan bobotnya. Sel biru = input yang bisa diubah.", f_txt),
    ("IPI_yoy: pertumbuhan IPI yoy (%) per mitra per bulan, lalu rata-rata sederhana dan tiga rata-rata tertimbang (formula).", f_txt),
    ("PDB_WB: PDB nominal USD miliar 2006-2025 per mitra (World Bank); rata-ratanya menjadi ukuran ekonomi di sheet Bobot.", f_txt),
    ("", f_txt),
    ("Metode", f_head),
    ("Rata-rata tertimbang bulan t = SUMPRODUCT(IPI_t, bobot) / SUMPRODUCT(bobot mitra yang IPI-nya tersedia di bulan t).", f_txt),
    ("Bobot dinormalkan ulang setiap bulan karena cakupan IPI berbeda: Australia s.d. Jan 2021, Malaysia sejak 2016, "
     "Vietnam sejak 2018, China tanpa Januari-Februari di beberapa tahun.", f_txt),
    ("Seri yang dipakai di model dan deck: tertimbang pangsa ekspor Indonesia (ukuran pasar mitra bagi ekspor Indonesia).", f_txt),
    ("", f_txt),
    ("Sumber", f_head),
    ("IPI yoy: CEIC (data panel mitra, intermediate/dari_tio/Panel_Country_Month.csv).", f_txt),
    ("Ekspor dan impor Indonesia per mitra: ITC Trade Map, Jan 2006 - Okt 2026, USD juta.", f_txt),
    ("PDB: World Bank WDI, NY.GDP.MKTP.CD (GDP, current US$), diakses 19 Nov 2026.", f_txt),
    ("Dibuat oleh script/12_ipi_mitra.py.", f_txt),
]
for i, (t, f) in enumerate(notes, 1):
    ws.cell(i, 1, t).font = f
ws.column_dimensions["A"].width = 130

# --- PDB_WB
wp = wbk.create_sheet("PDB_WB")
wp["A1"] = "PDB nominal (USD miliar), World Bank NY.GDP.MKTP.CD"
wp["A1"].font = f_title
wp.cell(3, 1, "Tahun").font = f_head
for j, c in enumerate(ISO, 2):
    wp.cell(3, j, NM[c]).font = f_head
for i, (yr, row) in enumerate(gdp.iterrows(), 4):
    wp.cell(i, 1, str(yr)).font = f_txt
    for j, c in enumerate(ISO, 2):
        cell = wp.cell(i, j, None if pd.isna(row[c]) else round(float(row[c]), 2))
        cell.font, cell.number_format = f_in, "#,##0.0"
last_p = 3 + len(gdp)
wp.cell(last_p + 1, 1, "Rata-rata").font = f_head
for j in range(2, 12):
    col = get_column_letter(j)
    cell = wp.cell(last_p + 1, j, f"=AVERAGE({col}4:{col}{last_p})")
    cell.font, cell.number_format = Font(name=F, size=10, bold=True), "#,##0.0"
wp.column_dimensions["A"].width = 12
for j in range(2, 12):
    wp.column_dimensions[get_column_letter(j)].width = 14

# --- Bobot
wbw = wbk.create_sheet("Bobot", 1)
wbw["A1"] = "Ukuran mitra dan bobot"
wbw["A1"].font = f_title
hdr = ["ISO3", "Mitra", "Ekspor Indonesia 2006-2026 (USD juta)", "Total perdagangan 2006-2026 (USD juta)",
       "PDB rata-rata 2006-2025 (USD miliar)", "Bobot ekspor", "Bobot perdagangan", "Bobot PDB"]
for j, h in enumerate(hdr, 1):
    c = wbw.cell(3, j, h)
    c.font, c.fill, c.alignment = f_head, fill_h, Alignment(wrap_text=True, vertical="center")
for i, c in enumerate(ISO, 4):
    wbw.cell(i, 1, c).font = f_txt
    wbw.cell(i, 2, NM[c]).font = f_txt
    x = wbw.cell(i, 3, round(float(tr.loc[c, "Exports_USDk"]), 1)); x.font, x.number_format = f_in, "#,##0"
    t = wbw.cell(i, 4, round(float(tr.loc[c, "Exports_USDk"] + tr.loc[c, "Imports_USDk"]), 1))
    t.font, t.number_format = f_in, "#,##0"
    g = wbw.cell(i, 5, f"=PDB_WB!{get_column_letter(ISO.index(c) + 2)}{last_p + 1}")
    g.font, g.number_format = f_link, "#,##0.0"
    for k, src in enumerate("CDE"):
        cc = wbw.cell(i, 6 + k, f"={src}{i}/SUM({src}$4:{src}$13)")
        cc.font, cc.number_format = f_txt, "0.0%"
wbw.cell(14, 2, "Jumlah").font = f_head
for j in range(3, 9):
    col = get_column_letter(j)
    c = wbw.cell(14, j, f"=SUM({col}4:{col}13)")
    c.font, c.number_format = f_head, "0.0%" if j >= 6 else "#,##0"
wbw.cell(16, 1, "Sel biru = input (ITC Trade Map, World Bank); sel hijau = tautan ke sheet PDB_WB; hitam = formula.").font = f_txt
wbw["C3"].comment = Comment("Sumber: ITC Trade Map, ekspor Indonesia ke mitra, Jan 2006 - Okt 2026.", "script 12")
wbw["E3"].comment = Comment("Sumber: World Bank WDI NY.GDP.MKTP.CD, rata-rata 2006-2025 (sheet PDB_WB).", "script 12")
wbw.column_dimensions["A"].width = 7
wbw.column_dimensions["B"].width = 17
for col in "CDE":
    wbw.column_dimensions[col].width = 20
for col in "FGH":
    wbw.column_dimensions[col].width = 13
wbw.row_dimensions[3].height = 42

# --- IPI_yoy
wi = wbk.create_sheet("IPI_yoy", 1)
wi["A1"] = "IPI yoy (%) 10 mitra dan rata-ratanya"
wi["A1"].font = f_title
labels = ["Bobot ekspor", "Bobot perdagangan", "Bobot PDB"]
for r, (lb, bc) in enumerate(zip(labels, "FGH"), 3):
    wi.cell(r, 1, lb).font = f_head
    for j, c in enumerate(ISO, 2):
        cell = wi.cell(r, j, f"=Bobot!{bc}{ISO.index(c) + 4}")
        cell.font, cell.number_format = f_link, "0.0%"
H = 7
cols = ["Bulan"] + [NM[c] for c in ISO] + ["Jumlah mitra", "Rata-rata sederhana", "Tertimbang ekspor",
                                            "Tertimbang perdagangan", "Tertimbang PDB", "Tertimbang ekspor, rata-rata 3 bulan"]
for j, h in enumerate(cols, 1):
    c = wi.cell(H, j, h)
    c.font, c.fill, c.alignment, c.border = f_head, fill_h, Alignment(wrap_text=True, vertical="center"), thin
for i, (dt, row) in enumerate(ipi.iterrows(), H + 1):
    wi.cell(i, 1, dt).font = f_txt
    for j, c in enumerate(ISO, 2):
        v = row[c]
        cell = wi.cell(i, j, None if pd.isna(v) else float(v))
        cell.font, cell.number_format = f_in, "0.0"
    rng = f"B{i}:K{i}"
    wi.cell(i, 12, f"=COUNT({rng})").font = f_txt
    wi.cell(i, 13, f'=IF(L{i}=0,"",AVERAGE({rng}))')
    for k, wr in enumerate((3, 4, 5)):
        wi.cell(i, 14 + k, f'=IF(L{i}=0,"",SUMPRODUCT({rng},$B${wr}:$K${wr})/SUMPRODUCT(--ISNUMBER({rng}),$B${wr}:$K${wr}))')
    if i >= H + 3:
        wi.cell(i, 18, f'=IF(COUNT(N{i - 2}:N{i})<3,"",AVERAGE(N{i - 2}:N{i}))')
    for j in range(13, 19):
        wi.cell(i, j).number_format = "0.00"
        wi.cell(i, j).font = f_txt
for i in range(H + 1, H + 1 + len(ipi)):
    wi.cell(i, 14).fill = fill_key
wi.cell(H, 14).comment = Comment("Seri yang dipakai di model (yf_avg) dan di deck.", "script 12")
wi.freeze_panes = wi.cell(H + 1, 2)
wi.column_dimensions["A"].width = 10
for j in range(2, 19):
    wi.column_dimensions[get_column_letter(j)].width = 11
wi.row_dimensions[H].height = 44
wi.cell(5 + 1, 1, "Kuning = seri yang dipakai di model dan deck.").font = Font(name=F, size=9, italic=True)

wbk.save(OUTX)
print("tersimpan:", OUTX, "dan", OUTC)
print(w.round(3))
print(out.describe().round(2).T[["count", "mean", "min", "max"]])
