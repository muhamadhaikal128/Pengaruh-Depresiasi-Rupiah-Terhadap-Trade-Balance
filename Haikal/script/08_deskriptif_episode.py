"""
08_deskriptif_episode.py : statistik deskriptif per episode depresiasi rupiah

Jalankan dari folder Haikal/ setelah 00_master.do:
    uv run --with pandas --with matplotlib python script/08_deskriptif_episode.py

Episode depresiasi (aturan zigzag, IDR/USD rata-rata bulanan BIS):
    mulai  = titik terendah IDR/USD sebelum rupiah melemah >= 10%
    selesai = puncak IDR/USD sebelum rupiah menguat kembali >= 5%
Perubahan diukur dari awal episode (t0) ke 12 bulan kemudian (t0+12), memakai rata-rata
3 bulan (t0-2..t0 vs t0+10..t0+12) supaya pola musiman saling meniadakan.

Output (output/0_deskriptif/):
    episodes.csv            daftar episode + perubahan kurs, ekspor, impor, X/M, BCOM, IPI mitra
    episode_mitra.csv       perubahan X/M bilateral per episode
    episode_kelompok.csv    perubahan X/M per kelompok barang per episode
    driver_r2.csv           R^2 bivariat perubahan 12 bulan ln(X/M) terhadap kurs, BCOM, IPI mitra
    summary_stats.csv       statistik deskriptif variabel model
    event_xm.csv            jalur X/M (indeks t0 = 100) per episode, bulan -6..24
"""
import os

import numpy as np
import pandas as pd

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(ROOT)
OUT = "output/0_deskriptif"

# ---- data
fx = pd.read_csv("input/raw/bis/bis_xru_monthly.csv")
fx = fx[fx.REF_AREA == "ID"][["TIME_PERIOD", "OBS_VALUE"]]
fx = fx.rename(columns={"TIME_PERIOD": "mdate", "OBS_VALUE": "idr"})
fx["mdate"] = pd.to_datetime(fx.mdate)
fx = fx.set_index("mdate").idr

agg = pd.read_stata("intermediate/analisis/ana_aggregate.dta").set_index("mdate")
agg["idr"] = fx
part = pd.read_stata("intermediate/analisis/ana_partner.dta")
grp = pd.read_stata("intermediate/analisis/ana_group.dta")


# ---- 1. episode
def zigzag(s, up=0.10, down=0.05):
    eps, tr, i_tr, inrise, pk, i_pk = [], s.iloc[0], s.index[0], False, None, None
    for d, v in s.items():
        if not inrise:
            if v < tr:
                tr, i_tr = v, d
            elif v / tr - 1 >= up:
                inrise, pk, i_pk = True, v, d
        else:
            if v > pk:
                pk, i_pk = v, d
            elif v / pk - 1 <= -down:
                eps.append((i_tr, i_pk, tr, pk))
                inrise, tr, i_tr = False, v, d
    if inrise:
        eps.append((i_tr, i_pk, tr, pk))
    return eps


NAMES = {2007: "Krisis global 2008", 2011: "Taper tantrum 2013", 2014: "Komoditas jatuh 2015",
         2016: "Normalisasi Fed 2018", 2020: "COVID 2020", 2021: "Pengetatan Fed 2022",
         2023: "2023–24", 2024: "2024–26"}
start_trade = agg.index[agg.exports_usdk.notna()].min()
eps = [e for e in zigzag(fx) if e[0] >= start_trade - pd.DateOffset(months=2)]


def m3(s, t, lo, hi):
    """rata-rata s pada bulan t+lo .. t+hi (butuh data lengkap)"""
    idx = [t + pd.DateOffset(months=k) for k in range(lo, hi + 1)]
    v = s.reindex(idx)
    return v.mean() if v.notna().all() else np.nan


def chg(s, t, log=True):
    a, b = m3(s, t, -2, 0), m3(s, t, 10, 12)
    return (np.log(b / a) * 100) if log else (b - a)


agg["xm"] = agg.exports_usdk / agg.imports_usdk
agg["reer"] = np.exp(agg.lnreer)
agg["bcom"] = np.exp(agg.lncom)
rows = []
for t0, t1, lo, hi in eps:
    r = {"episode": NAMES.get(t0.year, str(t0.year)), "mulai": t0.strftime("%b %Y"), "puncak": t1.strftime("%b %Y"),
         "bulan": (t1.year - t0.year) * 12 + t1.month - t0.month,
         "dep_idr_usd": (hi / lo - 1) * 100,
         "dep_reer_12m": -chg(agg.reer, t0), "d_xm_12m": chg(agg.xm, t0),
         "d_x_12m": chg(agg.exports_usdk, t0), "d_m_12m": chg(agg.imports_usdk, t0),
         "d_bcom_12m": chg(agg.bcom, t0), "d_ipi_12m": chg(agg.yf_avg, t0, log=False),
         "t0": t0}
    rows.append(r)
E = pd.DataFrame(rows)
# pembanding: rata-rata perubahan 12 bulan di bulan yang bukan awal episode
dxm = (np.log(agg.xm.rolling(3).mean()).diff(12) * 100)
E.attrs["benchmark"] = dxm.mean()
E.drop(columns="t0").to_csv(f"{OUT}/episodes.csv", index=False)

# ---- 2. event study X/M dunia, indeks t0 = 100 (rata-rata 3 bulan)
xm3 = agg.xm.rolling(3, center=True).mean()
ev = []
for _, r in E.iterrows():
    base = xm3.get(r.t0)
    for k in range(-6, 25):
        t = r.t0 + pd.DateOffset(months=k)
        v = xm3.get(t, np.nan)
        ev.append({"episode": r.episode, "k": k, "xm_idx": v / base * 100 if base else np.nan})
pd.DataFrame(ev).to_csv(f"{OUT}/event_xm.csv", index=False)

# ---- 3. per mitra dan per kelompok
part["mdate"] = pd.to_datetime(part.mdate)
pm = []
for iso, g in part.groupby("iso3"):
    s = (g.set_index("mdate").exports_usdk / g.set_index("mdate").imports_usdk)
    for _, r in E.iterrows():
        pm.append({"iso3": iso, "episode": r.episode, "d_xm_12m": chg(s, r.t0)})
pd.DataFrame(pm).to_csv(f"{OUT}/episode_mitra.csv", index=False)

grp["mdate"] = pd.to_datetime(grp.mdate)
gk = []
for g_, g in grp.groupby("grp"):
    s = g.set_index("mdate")
    xm = s.x / s.m
    for _, r in E.iterrows():
        gk.append({"grp": g_, "episode": r.episode, "d_xm_12m": chg(xm, r.t0),
                   "d_x_12m": chg(s.x, r.t0), "d_m_12m": chg(s.m, r.t0)})
pd.DataFrame(gk).to_csv(f"{OUT}/episode_kelompok.csv", index=False)

# ---- 4. driver: R^2 bivariat perubahan 12 bulan (seluruh sampel)
#     dipisah untuk ekspor, impor, dan rasio X/M: harga komoditas bisa menggerakkan ekspor DAN
#     impor sekaligus, sehingga efeknya saling meniadakan di rasio
d = pd.DataFrame({"d_x": np.log(agg.exports_usdk).diff(12) * 100,
                  "d_m": np.log(agg.imports_usdk).diff(12) * 100,
                  "d_xm": np.log(agg.xm).diff(12) * 100,
                  "d_dep": -agg.lnreer.diff(12) * 100,
                  "d_bcom": agg.lncom.diff(12) * 100,
                  "ipi": agg.yf_avg,
                  "d_gdp": agg.lngdp_idn.diff(12) * 100}).dropna()
dr = []
for y, ylab in [("d_x", "Ekspor"), ("d_m", "Impor"), ("d_xm", "Rasio X/M")]:
    for v, lab in [("d_dep", "Depresiasi riil (REER)"), ("d_bcom", "Harga komoditas (BCOM)"),
                   ("ipi", "Permintaan mitra (IPI)"), ("d_gdp", "PDB riil Indonesia")]:
        c = d[y].corr(d[v])
        dr.append({"y": ylab, "driver": lab, "var": v, "corr": c, "r2": c ** 2,
                   "slope": np.polyfit(d[v], d[y], 1)[0], "n": len(d)})
pd.DataFrame(dr).to_csv(f"{OUT}/driver_r2.csv", index=False)
d.to_csv(f"{OUT}/driver_scatter.csv")

# ---- 5. statistik deskriptif variabel model (bulanan, Indonesia-dunia)
ss = pd.DataFrame({
    "Rasio ekspor/impor (X/M)": agg.xm,
    "Ekspor (USD miliar)": agg.exports_usdk / 1e6,
    "Impor (USD miliar)": agg.imports_usdk / 1e6,
    "REER (2020=100)": agg.reer,
    "IDR per USD": agg.idr,
    "BCOM (indeks)": agg.bcom,
    "IPI mitra (% yoy)": agg.yf_avg,
})
ss = ss[(ss.index >= start_trade) & (ss.index <= "2026-08-01")]
st = ss.describe().T[["count", "mean", "std", "min", "max"]]
st["periode"] = [f"{ss[c].first_valid_index():%b %Y}–{ss[c].last_valid_index():%b %Y}" for c in ss]
st.to_csv(f"{OUT}/summary_stats.csv")

# ---- ringkasan ke layar
pd.set_option("display.width", 200)
print(E.drop(columns="t0").round(1).to_string(index=False))
print("benchmark rata-rata perubahan 12 bulan X/M (semua bulan):", round(E.attrs["benchmark"], 2))
print(pd.DataFrame(dr).round(3).to_string(index=False))
print(st.round(2).to_string())
