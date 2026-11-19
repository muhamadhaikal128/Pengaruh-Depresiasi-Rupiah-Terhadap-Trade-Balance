"""
10_indeks_harga_volume.py : indeks harga (unit value) dan indeks volume ekspor-impor dari data HS-6

Tujuan: memecah nilai USD ekspor/impor menjadi HARGA x VOLUME, supaya efek depresiasi bisa dibaca
        per channel: apakah neraca memburuk karena harga (terms of trade) atau karena volume?

Input
  input/raw/trademap_hs6_qty/*.xlsx   kuantitas + satuan per HS-6, Indonesia vs 10 mitra, ekspor & impor,
                                      Jan 2006 - Agu 2026 (ITC Trade Map, diunduh Tio 19 Nov 2026)
  ../Tio/intermediate/hs6/{ISO3}_{Export|Import}_Month.csv.gz   nilai USD ribu per HS-6 (data yang sama
                                      dengan yang dipakai di 02_prep_data.do)
  intermediate/dari_tio/HS6_Classification.csv   keanggotaan 7 kelompok barang

Metode (mengikuti IMF Export and Import Price Index Manual 2009 dan indeks unit value BPS)
  - item = HS-6 x mitra; unit value uv = nilai / kuantitas, hanya bila nilai > 0 dan kuantitas > 0
  - indeks Fisher bulanan dengan basis rata-rata TAHUN SEBELUMNYA (annually chained):
        r_i  = uv_it / uv_i,Y-1                     (uv tahun basis = total nilai / total kuantitas)
        L_t  = sum(w_i,Y-1 * r_i) / sum(w_i,Y-1)    (bobot nilai tahun basis)
        P_t  = sum(V_it) / sum(V_it / r_i)          (bobot nilai bulan berjalan)
        F_t  = sqrt(L_t * P_t)
    lalu dirangkai: I_t = rata-rata I tahun Y-1 x F_t (tahun pertama 2006 berbasis rata-rata 2006 sendiri)
  - item dipakai bila satuannya sama dengan satuan dominan tahun basis dan 1/4 <= r_i <= 4 (buang outlier)
  - indeks volume implisit = indeks nilai total / indeks harga  (nilai total mencakup item tanpa kuantitas)
  - identitas: ln(X/M) = ln(Px/Pm) + ln(Qx/Qm), yaitu terms of trade + rasio volume

Output
  intermediate/analisis/hs6_qty_long.csv.gz   kuantitas long (cache parsing xlsx)
  intermediate/analisis/price_volume.csv      scope, id, flow, mdate, pidx, vidx, val_usdk, cover
  output/0_deskriptif/pv_coverage.csv          cakupan nilai yang punya unit value valid

Jalankan dari folder Haikal/:
  uv run --with pandas --with openpyxl python script/10_indeks_harga_volume.py
"""
import glob
import os
import re

import numpy as np
import pandas as pd
from openpyxl import load_workbook

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(ROOT)
RAW = "input/raw/trademap_hs6_qty"
VAL = os.path.join("..", "Tio", "intermediate", "hs6")
CACHE = "intermediate/analisis/hs6_qty_long.csv.gz"
OUT = "intermediate/analisis/price_volume.csv"
ISO = {"australia": "AUS", "china": "CHN", "india": "IND", "japan": "JPN", "korea-republic-of": "KOR",
       "malaysia": "MYS", "singapore": "SGP", "thailand": "THA", "united-states-of-america": "USA", "viet-nam": "VNM"}
GRP = {"commodity": "comm", "agriculture": "sec1", "energy_mining": "sec2", "manufacturing": "noncomm",
       "consumption": "eu1", "intermediate": "eu2", "capital": "eu3"}
RLO, RHI = 0.25, 4.0


# -----------------------------------------------------------------------------
# 1. Parsing workbook kuantitas -> long (di-cache)
# -----------------------------------------------------------------------------
def parse_book(path):
    m = re.search(r"indonesias-(exports-to|imports-from)-(.+?)-by-product", os.path.basename(path))
    flow = "Export" if m.group(1) == "exports-to" else "Import"
    iso = ISO[m.group(2)]
    ws = load_workbook(path, read_only=True).worksheets[0]
    rows = ws.iter_rows(values_only=True)
    hdr = None
    for r in rows:
        if r and r[0] in ("Exporter", "Importer") and r[4] == "Code":
            hdr = r
            break
    cols = [(j, str(h)) for j, h in enumerate(hdr) if h and re.fullmatch(r"\d{6}", str(h))]
    out = []
    for r in rows:
        code = r[4]
        if code is None or str(code).upper() == "TOTAL":
            continue
        hs6 = str(code).strip().zfill(6)
        for j, ym in cols:
            q = r[j]
            if q is None or q == "" or q == 0:
                continue
            u = r[j + 1] or ""
            out.append((hs6, f"{ym[:4]}-{ym[4:]}", float(q), u))
    df = pd.DataFrame(out, columns=["HS6", "Date", "Qty", "Unit"])
    df["ISO3"], df["Flow"] = iso, flow
    print(f"  {iso} {flow}: {len(df):,} baris kuantitas > 0")
    return df


if os.path.exists(CACHE):
    qty = pd.read_csv(CACHE, dtype={"HS6": str})
else:
    print("parsing workbook kuantitas ...")
    qty = pd.concat([parse_book(p) for p in sorted(glob.glob(f"{RAW}/*.xlsx"))], ignore_index=True)
    qty.to_csv(CACHE, index=False, compression="gzip")
print("kuantitas:", f"{len(qty):,}", "baris; satuan:", qty.Unit.value_counts().head(8).to_dict())

# -----------------------------------------------------------------------------
# 2. Gabung dengan nilai USD
# -----------------------------------------------------------------------------
vals = []
for iso in sorted(qty.ISO3.unique()):
    for fl in ("Export", "Import"):
        v = pd.read_csv(f"{VAL}/{iso}_{fl}_Month.csv.gz", dtype={"HS6": str})
        v["HS6"] = v.HS6.str.zfill(6)
        vals.append(v[v.Value_USDk > 0])
val = pd.concat(vals, ignore_index=True)
d = val.merge(qty, on=["ISO3", "Flow", "HS6", "Date"], how="left")
d["Unit"] = d.Unit.fillna("")
d["mdate"] = pd.to_datetime(d.Date)
d["Y"] = d.mdate.dt.year
d["item"] = d.ISO3 + "_" + d.HS6
d["has_q"] = (d.Qty > 0) & (d.Unit != "")

cls = pd.read_csv("intermediate/dari_tio/HS6_Classification.csv", dtype={"HS6": str})
cls["HS6"] = cls.HS6.str.zfill(6)
d = d.merge(cls[["HS6"] + list(GRP)], on="HS6", how="left")
for g in GRP:
    d[g] = d[g].fillna(0).astype(int)


# -----------------------------------------------------------------------------
# 3. Indeks Fisher berantai tahunan
# -----------------------------------------------------------------------------
def fisher_index(x):
    """x: baris item-bulan untuk satu scope & flow. Hasil: DataFrame per bulan (pidx, vidx, val, cover)."""
    tot = x.groupby("mdate").Value_USDk.sum()
    q = x[x.has_q]
    # unit value tahunan per item, satuan dominan (nilai terbesar)
    yu = q.groupby(["item", "Y", "Unit"]).agg(V=("Value_USDk", "sum"), Q=("Qty", "sum")).reset_index()
    yu = yu.sort_values("V").groupby(["item", "Y"]).tail(1)
    yu["uvb"] = yu.V / yu.Q
    base = yu.rename(columns={"Unit": "Ub", "V": "Vb"})[["item", "Y", "Ub", "Vb", "uvb"]]
    years = sorted(x.Y.unique())
    res, level = [], {}
    for Y in years:
        by = Y - 1 if Y > years[0] else Y
        m = q[q.Y == Y].merge(base[base.Y == by].drop(columns="Y"), on="item")
        m = m[m.Unit == m.Ub]
        m["r"] = (m.Value_USDk / m.Qty) / m.uvb
        m = m[(m.r >= RLO) & (m.r <= RHI)]
        link = 100.0 if Y == years[0] else level[by]
        for t, g in m.groupby("mdate"):
            L = (g.Vb * g.r).sum() / g.Vb.sum()
            P = g.Value_USDk.sum() / (g.Value_USDk / g.r).sum()
            res.append((t, link * np.sqrt(L * P), g.Value_USDk.sum()))
        if res:
            yr = [p for (t, p, _) in res if t.year == Y]
            level[Y] = np.mean(yr) if yr else link
    r = pd.DataFrame(res, columns=["mdate", "pidx", "vmatch"]).set_index("mdate")
    r["val_usdk"] = tot
    r["cover"] = r.vmatch / r.val_usdk * 100
    v0 = r.val_usdk[r.index.year == years[0]].mean()
    r["vidx"] = 100 * (r.val_usdk / v0) / (r.pidx / 100)
    return r.drop(columns="vmatch").reset_index()


out = []
for fl in ("Export", "Import"):
    f = d[d.Flow == fl]
    jobs = [("AGG10", "AGG10", f)] + [("PARTNER", iso, f[f.ISO3 == iso]) for iso in sorted(f.ISO3.unique())] + \
           [("GROUP", GRP[g], f[f[g] == 1]) for g in GRP]
    for scope, id_, x in jobs:
        r = fisher_index(x)
        r.insert(0, "flow", fl)
        r.insert(0, "id", id_)
        r.insert(0, "scope", scope)
        out.append(r)
        print(f"  {fl:6s} {scope:7s} {id_:6s} cakupan rata-rata {r.cover.mean():5.1f}%  "
              f"harga 2006->akhir {r.pidx.iloc[0]:6.1f}->{r.pidx.iloc[-1]:6.1f}  volume ->{r.vidx.iloc[-1]:6.1f}")
pv = pd.concat(out, ignore_index=True)
pv["mdate"] = pv.mdate.dt.strftime("%Y-%m")
pv.to_csv(OUT, index=False)
cov = pv.groupby(["scope", "id", "flow"]).cover.agg(["mean", "min"]).round(1).reset_index()
cov.to_csv("output/0_deskriptif/pv_coverage.csv", index=False)
print("tersimpan:", OUT, len(pv), "baris")
