"""
09_build_ppt.py : deck hasil riset (template DEN, mengikuti deck Banking Stress Test)

Urutan: ringkasan eksekutif -> alur -> 01 teori & literatur (+RQ) -> 02 data -> 03 fakta awal
        -> 04 metodologi -> 05 hasil (+mengapa negatif) -> 06 diagnostik & robustness -> kesimpulan -> lampiran
Konvensi warna grafik/tabel: cokelat = neraca memburuk, oranye = membaik, pucat/hitam = tidak signifikan.

Jalankan dari folder Haikal/ setelah 00_master.do dan 08_deskriptif_episode.py:
    uv run --with python-pptx --with pandas --with matplotlib python script/09_build_ppt.py
Output: output/3_ppt/Depresiasi_Rupiah_Trade_Balance.pptx (+ grafik di output/3_ppt/grafik/)

Konvensi teks: ~kata~ dicetak miring (istilah asing seperti ~channel~).
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Patch
import numpy as np
import pandas as pd
from lxml import etree
from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Pt

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(ROOT)
OUT, FIG = "output/3_ppt", "output/3_ppt/grafik"
os.makedirs(FIG, exist_ok=True)
TEMPLATE = "input/reference/template_DEN.pptx"
SRC_DECK = os.path.join(ROOT, "..", "..", "banking-stress-test", "Banking Stress Test (Solvency).pptx")
LPIV_F = 0.35   # F first stage LP-IV (00_master.log, 07_local_projections.do)

ORANGE, BROWN, MUTED, DARKOR = "F0A22E", "A5644E", "B58B80", "C17529"
GREY, TXT, CREAM, LINE, SECNUM = "595959", "262626", "F3E9E3", "BFBFBF", "C3986D"
rgb = RGBColor.from_string
L, R = PP_ALIGN.LEFT, PP_ALIGN.RIGHT
X1, W1, X2, W2 = 34, 430, 492, 428

# =============================================================================
# Data
# =============================================================================
D0, D1, D2, DT = "output/0_deskriptif", "output/1_ardl", "output/2_lp", "intermediate/dari_tio"
ardl_ag = pd.read_csv(f"{D1}/ardl_agregat.csv")
ardl_mi = pd.read_csv(f"{D1}/ardl_mitra.csv")
ardl_kg = pd.read_csv(f"{D1}/ardl_kelompok.csv")
dm_ag = pd.read_csv(f"{D1}/dm_agregat.csv")
nardl = pd.read_csv(f"{D1}/nardl_agregat.csv").set_index("term")
pmg = pd.read_csv(f"{D1}/pmg_mitra.csv").set_index("est")
lp = pd.read_csv(f"{D2}/lp_irf.csv")
shares = pd.read_csv(f"{D0}/group_shares.csv")
unitroot = pd.read_csv(f"{D0}/unitroot.csv")
eps = pd.read_csv(f"{D0}/episodes.csv")
ev = pd.read_csv(f"{D0}/event_xm.csv")
ep_m = pd.read_csv(f"{D0}/episode_mitra.csv")
ep_g = pd.read_csv(f"{D0}/episode_kelompok.csv")
drv = pd.read_csv(f"{D0}/driver_r2.csv")
sct = pd.read_csv(f"{D0}/driver_scatter.csv")
sst = pd.read_csv(f"{D0}/summary_stats.csv", index_col=0)
agg = pd.read_stata("intermediate/analisis/ana_aggregate.dta")
fx = pd.read_csv("input/raw/bis/bis_xru_monthly.csv")
fx = fx[fx.REF_AREA == "ID"].assign(mdate=lambda d: pd.to_datetime(d.TIME_PERIOD)).set_index("mdate").OBS_VALUE
tot = pd.read_csv(f"{DT}/Trade_Total_Month.csv", usecols=["ISO3", "Exports_USDk", "Imports_USDk"])
cov = pd.read_csv(f"{DT}/Classification_Coverage.csv")
# harga vs volume (10_indeks_harga_volume.py, 11_harga_volume.do)
pvx = pd.read_csv("intermediate/analisis/price_volume.csv")
lpq = pd.read_csv(f"{D2}/lp_pv.csv")
avol = pd.read_csv(f"{D1}/ardl_volume.csv").set_index("id")
pvcov = pd.read_csv(f"{D0}/pv_coverage.csv")

GRP = {"comm": "Komoditas (total)", "sec2": "Komoditas energi & tambang", "sec1": "Komoditas pertanian & pangan",
       "noncomm": "Non-komoditas (manufaktur)", "eu1": "Barang konsumsi", "eu2": "Bahan baku/penolong",
       "eu3": "Barang modal"}
GRP_S = {"comm": "Komoditas", "sec2": "Energi & tambang", "sec1": "Pertanian & pangan", "noncomm": "Manufaktur",
         "eu1": "Konsumsi", "eu2": "Bahan baku", "eu3": "Barang modal"}
CTRY = {"AUS": "Australia", "CHN": "China", "IND": "India", "JPN": "Jepang", "KOR": "Korea Selatan",
        "MYS": "Malaysia", "SGP": "Singapura", "THA": "Thailand", "USA": "Amerika Serikat", "VNM": "Vietnam"}
EP_SHORT = {r.episode: s for r, s in zip(eps.itertuples(), ["GFC 08", "Taper 13", "Komod. 15", "Fed 18",
                                                              "COVID 20", "Fed 22", "2023–24", "2024–26"])}
MON = {"May": "Mei", "Aug": "Agu", "Oct": "Okt", "Dec": "Des"}


def idn(x, d=1, sign=False):
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "–"
    s = f"{x:+.{d}f}" if sign else f"{x:.{d}f}"
    return s.replace("-", "−").replace(".", ",")


def bln(s):
    for a, b in MON.items():
        s = s.replace(a, b)
    return s


def lpv(model, id_, h, col="eff"):
    r = lp[(lp.model == model) & (lp.id == id_) & (lp.h == h)]
    return float(r[col].iloc[0]) if len(r) else np.nan


def star(p):
    return "*" if (p is not None and not np.isnan(p) and p < 0.10) else ""


def is_sig(p):
    return p is not None and not np.isnan(p) and p < 0.10


def sig(e, p):
    """angka + bintang; signifikan diwarnai menurut arah: cokelat = memburuk, oranye = membaik"""
    if e is None or (isinstance(e, float) and np.isnan(e)):
        return "–"
    return (idn(e) + star(p), (BROWN if e < 0 else DARKOR) if is_sig(p) else "000000")


PALE = {BROWN: "DCC6BD", ORANGE: "F8DDB0"}


def dcol(e, p):
    """warna batang: arah (cokelat memburuk, oranye membaik), pucat bila tidak signifikan"""
    base = BROWN if e < 0 else ORANGE
    return "#" + (base if is_sig(p) else PALE[base])


# =============================================================================
# Grafik
# =============================================================================
plt.rcParams.update({"font.family": "Calibri", "font.size": 11, "axes.spines.top": False,
                     "axes.spines.right": False, "axes.edgecolor": "#7F7F7F", "axes.linewidth": 0.8,
                     "xtick.color": "#404040", "ytick.color": "#404040", "axes.grid": True,
                     "grid.color": "#E0E0E0", "grid.linewidth": 0.6, "axes.axisbelow": True})
C = lambda h: "#" + h
CMAP = LinearSegmentedColormap.from_list("den", ["#" + BROWN, "#FFFFFF", "#" + ORANGE])


def save(fig, name):
    p = f"{FIG}/{name}.png"
    fig.savefig(p, dpi=250, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return p


def fig_jcurve_theory():
    t = np.linspace(0, 10, 200)
    y = -1.2 * np.exp(-((t - 1.8) ** 2) / 1.2) + 1.6 / (1 + np.exp(-(t - 5)))
    y -= y[0]
    fig, ax = plt.subplots(figsize=(4.3, 2.8))
    ax.axvspan(0.15, 3.2, color=C(BROWN), alpha=0.08, lw=0)
    ax.axvspan(3.2, 10, color=C(ORANGE), alpha=0.08, lw=0)
    ax.plot(t, y, color=C(ORANGE), lw=3)
    ax.axhline(0, color="#404040", lw=0.9)
    ax.text(1.65, 1.35, "Fase 1\nharga bergerak,\nvolume belum", ha="center", fontsize=9.5, color="#404040")
    ax.text(6.6, -0.95, "Fase 2\nvolume menyesuaikan", ha="center", fontsize=9.5, color="#404040")
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlabel("Waktu setelah depresiasi"); ax.set_ylabel("Neraca perdagangan")
    ax.grid(False)
    return save(fig, "teori_jcurve")


def fig_partners():
    s = tot.groupby("ISO3")[["Exports_USDk", "Imports_USDk"]].sum()
    w = s.loc["WLD"]
    p = s.drop("WLD")
    sh = pd.DataFrame({"x": p.Exports_USDk / w.Exports_USDk * 100, "m": p.Imports_USDk / w.Imports_USDk * 100,
                       "t": (p.Exports_USDk + p.Imports_USDk) / (w.Exports_USDk + w.Imports_USDk) * 100})
    sh = sh.sort_values("t")
    fig, ax = plt.subplots(figsize=(4.4, 3.9))
    y = np.arange(len(sh))
    ax.barh(y + 0.19, sh.x, height=0.36, color=C(ORANGE), label="Ekspor")
    ax.barh(y - 0.19, sh.m, height=0.36, color=C(BROWN), label="Impor")
    ax.set_yticks(y); ax.set_yticklabels([CTRY[i] for i in sh.index])
    ax.grid(axis="y", visible=False)
    ax.set_xlabel("% dari total ekspor / impor Indonesia, 2006–2026")
    ax.legend(frameon=False, fontsize=9, loc="lower right")
    tot_x = p.Exports_USDk.sum() / w.Exports_USDk * 100
    tot_m = p.Imports_USDk.sum() / w.Imports_USDk * 100
    tot_t = (p.Exports_USDk.sum() + p.Imports_USDk.sum()) / (w.Exports_USDk + w.Imports_USDk) * 100
    return save(fig, "pangsa_mitra"), sh, tot_x, tot_m, tot_t


def fig_timeline():
    s = fx[(fx.index >= "2006-01-01")]
    a = agg.set_index("mdate")
    tb = ((a.exports_usdk - a.imports_usdk) / 1e6).rolling(12).mean()
    bcom = np.exp(a.lncom)
    fig, (ax, bx, cx) = plt.subplots(3, 1, figsize=(6.4, 5.4), sharex=True, gridspec_kw={"height_ratios": [1, 1, 1]})
    for k, r in enumerate(eps.itertuples()):
        st, en = pd.to_datetime(r.mulai, format="%b %Y"), pd.to_datetime(r.puncak, format="%b %Y")
        st = max(st, s.index[0])
        for x in (ax, bx, cx):
            x.axvspan(st, en, color=C(ORANGE), alpha=0.18, lw=0)
        ax.text(st + (en - st) / 2, s.max() * (1.03 if k % 2 == 0 else 1.13), EP_SHORT[r.episode], ha="center",
                va="bottom", fontsize=7.5, color="#404040")
    ax.plot(s.index, s.values, color=C(BROWN), lw=1.8)
    ax.set_ylim(s.min() * 0.92, s.max() * 1.24)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:,.0f}".replace(",", ".")))
    bx.axhline(0, color="#404040", lw=0.9)
    bx.fill_between(tb.index, tb.values, 0, where=tb.values >= 0, color=C(ORANGE), alpha=0.55, lw=0)
    bx.fill_between(tb.index, tb.values, 0, where=tb.values < 0, color=C(BROWN), alpha=0.7, lw=0)
    bx.plot(tb.index, tb.values, color="#404040", lw=0.8)
    bx.set_ylim(tb.min() * 1.6, tb.max() * 1.35)
    cx.plot(bcom.index, bcom.values, color=C(BROWN), lw=1.8)
    cx.set_ylim(bcom.min() * 0.85, bcom.max() * 1.15)
    for x, t in [(ax, "A · Kurs Rp per USD (garis naik = rupiah melemah)"),
                 (bx, "B · Neraca perdagangan, USD miliar/bulan (oranye = surplus, cokelat = defisit)"),
                 (cx, "C · Harga komoditas dunia, indeks BCOM")]:
        x.text(0.005, 0.97, t, transform=x.transAxes, ha="left", va="top", fontsize=9, fontweight="bold",
               color="#262626", bbox=dict(facecolor="white", edgecolor="none", alpha=0.8, pad=1))
        x.tick_params(labelsize=8.5)
    fig.tight_layout(h_pad=0.5)
    return save(fig, "episode_timeline")


def shade_episodes(axes):
    for r in eps.itertuples():
        st, en = pd.to_datetime(r.mulai, format="%b %Y"), pd.to_datetime(r.puncak, format="%b %Y")
        for x in axes:
            x.axvspan(st, en, color=C(ORANGE), alpha=0.18, lw=0)


def fig_timeline_macro():
    """episode depresiasi dibandingkan dengan ekspor-impor, permintaan mitra, dan PDB Indonesia"""
    a = agg.set_index("mdate")
    a = a[a.index >= "2006-01-01"]
    fig, axs = plt.subplots(4, 1, figsize=(6.4, 5.6), sharex=True)
    shade_episodes(axs)
    ax, bx, cx, dx = axs
    for v, c, lb in [("exports_usdk", ORANGE, "ekspor"), ("imports_usdk", BROWN, "impor")]:
        s = (a[v] / 1e6).rolling(12).mean()
        ax.plot(s.index, s.values, color=C(c), lw=1.7)
        ax.text(s.index[-1] + pd.Timedelta(days=50), s.iloc[-1], lb, color=C(c), fontsize=8,
                va="bottom" if lb == "ekspor" else "top", fontweight="bold")
    ip = a.yf_avg.rolling(3).mean()
    gd = a.lngdp_idn.diff(12) * 100
    rr = a.reer_bis_broad
    for x, s, c in [(bx, ip, BROWN), (cx, gd, BROWN)]:
        x.axhline(0, color="#404040", lw=0.8)
        x.plot(s.index, s.values, color=C(c), lw=1.6)
    dx.plot(rr.index, rr.values, color=C(BROWN), lw=1.6)
    for x, t in [(ax, "A · Ekspor dan impor, USD miliar/bulan (rata-rata 12 bulan)"),
                 (bx, "B · Permintaan mitra: IPI 10 mitra, % yoy (rata-rata 3 bulan)"),
                 (cx, "C · PDB riil Indonesia, % yoy"),
                 (dx, "D · REER, 2020 = 100 (turun = rupiah melemah riil)")]:
        x.text(0.005, 0.97, t, transform=x.transAxes, ha="left", va="top", fontsize=8.5, fontweight="bold",
               color="#262626", bbox=dict(facecolor="white", edgecolor="none", alpha=0.8, pad=1))
        x.tick_params(labelsize=8)
        lo, hi = x.get_ylim()
        x.set_ylim(lo, hi + (hi - lo) * 0.3)
    ax.set_xlim(pd.Timestamp("2006-01-01"), pd.Timestamp("2027-09-01"))
    fig.tight_layout(h_pad=0.4)
    return save(fig, "episode_makro")


def fig_lp_intuition():
    """ilustrasi local projections: satu regresi per horizon, koefisien dirangkai menjadi impulse response"""
    s = lp[(lp.model == "A1_ols") & (lp.id == "AGG")].sort_values("h")
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(4.4, 4.2), gridspec_kw={"height_ratios": [0.8, 1.4]})
    # panel atas: garis waktu
    ax.set_xlim(-3, 26.5); ax.set_ylim(-0.3, 4.6); ax.axis("off")
    ax.plot([-2, 25], [0.4, 0.4], color="#7F7F7F", lw=1)
    ax.plot([0], [0.4], "o", color=C(BROWN), ms=9, zorder=5)
    ax.text(0, -0.25, "bulan t:\nrupiah melemah", ha="center", va="top", fontsize=8, color=C(BROWN), fontweight="bold")
    for k, (h, yy) in enumerate([(0, 1.1), (6, 1.75), (12, 2.4), (24, 3.05)]):
        ax.plot([0, 0, h, h], [0.55, yy, yy, 0.55], color=C(ORANGE), lw=1.3)
        ax.plot([h], [0.55], marker="v", color=C(ORANGE), ms=5)
        ax.text(h + 0.4 if h < 24 else h - 0.4, yy + 0.08, f"regresi {k + 1}: h = {h}", fontsize=8,
                ha="left" if h < 24 else "right", va="bottom", color="#404040")
        if h > 0:
            ax.text(h, 0.05, f"t+{h}", ha="center", va="top", fontsize=7.5, color="#595959")
    ax.text(-2.8, 4.55, "1 · Untuk setiap h, satu regresi: perubahan rasio X/M dari t−1 ke t+h", fontsize=8.5,
            fontweight="bold", color="#262626", va="top")
    # panel bawah: hasilnya
    bx.fill_between(s.h, s.lo90, s.hi90, color=C(BROWN), alpha=0.15, lw=0)
    bx.plot(s.h, s.eff, color=C(BROWN), lw=1.6)
    for h in (0, 6, 12, 24):
        r = s[s.h == h].iloc[0]
        bx.plot([h], [r.eff], "o", color=C(ORANGE), ms=6, zorder=5, mec="white")
    r12 = s[s.h == 12].iloc[0]
    bx.annotate(f"koefisien regresi h = 12:\n{r12.eff:.1f}%".replace(".", ",").replace("-", "−"), (12, r12.eff),
                xytext=(14.5, -19.5), fontsize=8, color="#262626", arrowprops=dict(arrowstyle="-", color="#404040", lw=0.7))
    bx.axhline(0, color="#404040", lw=0.9)
    bx.set_ylim(-25, 12); bx.set_xlim(-0.5, 25)
    bx.set_xticks(range(0, 25, 6)); bx.set_xlabel("Bulan setelah rupiah melemah (h)", fontsize=9)
    bx.set_ylabel("% rasio X/M", fontsize=9); bx.tick_params(labelsize=8)
    bx.set_title("2 · Koefisien dari 25 regresi dirangkai menjadi impulse response", fontsize=8.5, fontweight="bold",
                 loc="left", color="#262626")
    fig.tight_layout(h_pad=0.6)
    return save(fig, "lp_intuisi")


def fig_pretrend():
    """rasio X/M sebelum dan sesudah awal episode: sudah turun sebelum rupiah melemah"""
    g = ev[(ev.k >= -6) & (ev.k <= 12)].groupby("k").xm_idx
    m, lo_, hi_ = g.mean(), g.quantile(0.25), g.quantile(0.75)
    fig, ax = plt.subplots(figsize=(4.3, 2.9))
    ax.fill_between(lo_.index, lo_.values, hi_.values, color=C(MUTED), alpha=0.3, lw=0)
    ax.axvspan(-6, 0, color=C(BROWN), alpha=0.07, lw=0)
    ax.plot(m.index, m.values, color=C(BROWN), lw=2.6)
    ax.axhline(100, color="#404040", lw=0.9); ax.axvline(0, color="#7F7F7F", lw=0.9, ls="--")
    ax.annotate(f"{m.loc[-6]:.1f} → 100:\nsudah turun sebelum\nrupiah melemah".replace(".", ","),
                (-3, m.loc[-3]), xytext=(-5.8, 82), fontsize=8.5, color=C(BROWN), fontweight="bold",
                arrowprops=dict(arrowstyle="-", color=C(BROWN), lw=0.7))
    ax.text(0.4, 113.5, "rupiah mulai melemah →", fontsize=8, color="#595959", va="top")
    ax.set_ylim(80, 114); ax.set_xlim(-6, 12); ax.set_xticks(range(-6, 13, 3))
    ax.set_xlabel("Bulan sejak awal episode depresiasi", fontsize=9); ax.set_ylabel("Rasio X/M (awal episode = 100)", fontsize=9)
    ax.tick_params(labelsize=8.5)
    return save(fig, "pretrend")


def fig_corr_dep():
    """korelasi depresiasi riil dengan variabel lain (perubahan 12 bulan)"""
    lab = [("d_x", "Ekspor"), ("ipi", "IPI mitra"), ("d_xm", "Rasio X/M"), ("d_bcom", "Harga komoditas"),
           ("d_m", "Impor"), ("d_gdp", "PDB Indonesia")]
    v = pd.Series({nm: sct["d_dep"].corr(sct[c]) for c, nm in lab}).sort_values()
    fig, ax = plt.subplots(figsize=(4.3, 2.9))
    ax.barh(v.index, v.values, color=[C(BROWN) if x < -0.15 else "#" + PALE[BROWN] for x in v.values], height=0.6)
    for i, x in enumerate(v.values):
        ax.text(x - 0.01, i, f"{x:.2f}".replace(".", ",").replace("-", "−"), va="center", ha="right", fontsize=9)
    ax.axvline(0, color="#404040", lw=0.9); ax.grid(axis="y", visible=False)
    ax.set_xlim(-0.4, 0.1); ax.tick_params(labelsize=9)
    ax.set_xlabel("← turun saat rupiah melemah     korelasi     naik →", fontsize=9)
    return save(fig, "korelasi_depresiasi"), v


def zones(ax, lo, hi, base=0.0, up="Di atas 0: neraca membaik", dn="Di bawah 0: neraca memburuk"):
    """arsir zona membaik (oranye) dan memburuk (cokelat) supaya arah grafik langsung terbaca"""
    ax.axhspan(base, hi, color=C(ORANGE), alpha=0.07, lw=0)
    ax.axhspan(lo, base, color=C(BROWN), alpha=0.07, lw=0)
    ax.axhline(base, color="#404040", lw=1)
    ax.set_ylim(lo, hi)
    ax.text(0.015, 0.97, up, transform=ax.transAxes, ha="left", va="top", fontsize=8.5, color=C(DARKOR),
            fontweight="bold")
    ax.text(0.015, 0.03, dn, transform=ax.transAxes, ha="left", va="bottom", fontsize=8.5, color=C(BROWN),
            fontweight="bold")


def fig_event(bench):
    fig, ax = plt.subplots(figsize=(4.3, 3.0))
    g = ev.groupby("k").xm_idx
    lo_, hi_, m = g.quantile(0.25), g.quantile(0.75), g.mean()
    ax.axhspan(100, 125, color=C(ORANGE), alpha=0.07, lw=0)
    ax.axhspan(70, 100, color=C(BROWN), alpha=0.07, lw=0)
    ax.axhline(100, color="#404040", lw=1)
    ax.set_ylim(70, 125)
    ax.text(0.985, 0.97, "Di atas 100: membaik", transform=ax.transAxes, ha="right", va="top", fontsize=8.5,
            color=C(DARKOR), fontweight="bold")
    ax.text(0.985, 0.03, "Di bawah 100: memburuk", transform=ax.transAxes, ha="right", va="bottom", fontsize=8.5,
            color=C(BROWN), fontweight="bold")
    ax.fill_between(lo_.index, lo_.values, hi_.values, color=C(MUTED), alpha=0.35, lw=0,
                    label="interquartile range (separuh episode di dalamnya)")
    ax.plot(m.index, m.values, color=C(BROWN), lw=2.8, label="rata-rata 8 episode")
    ax.axvline(0, color="#7F7F7F", lw=0.9, ls="--")
    ax.text(-5.6, 122, "← sebelum", fontsize=8, color="#595959", va="top")
    ax.text(0.5, 122, "rupiah mulai melemah →", fontsize=8, color="#595959", va="top")
    bm = 100 * np.exp(bench / 100)
    ax.plot([12], [m.loc[12]], "o", color=C(BROWN), ms=6, zorder=5)
    ax.plot([12], [bm], "D", color="#404040", ms=5, zorder=5)
    ax.annotate(f"bulan ke-12: {m.loc[12]:.1f}".replace(".", ","), (12, m.loc[12]), xytext=(14, 86),
                fontsize=8.5, color=C(BROWN), fontweight="bold", arrowprops=dict(arrowstyle="-", color=C(BROWN), lw=0.7))
    ax.annotate(f"pembanding bulan biasa: {bm:.1f}".replace(".", ","), (12, bm), xytext=(6.5, 110),
                fontsize=8.5, color="#404040", arrowprops=dict(arrowstyle="-", color="#404040", lw=0.7))
    ax.set_xticks(range(-6, 25, 6))
    ax.set_xlabel("Bulan sejak awal episode depresiasi")
    ax.legend(frameon=False, fontsize=8.5, loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=2)
    return save(fig, "episode_event")


def fig_drivers():
    order = ["Depresiasi riil (REER)", "Harga komoditas (BCOM)", "Permintaan mitra (IPI)", "PDB riil Indonesia"]
    lab = ["Depresiasi riil", "Harga komoditas", "Permintaan mitra", "PDB Indonesia"]
    fig, axs = plt.subplots(1, 3, figsize=(4.5, 2.9), sharey=True)
    yy = np.arange(4)[::-1]
    for ax, y in zip(axs, ["Ekspor", "Impor", "Rasio X/M"]):
        v = drv[drv.y == y].set_index("driver").loc[order].r2 * 100
        ax.barh(yy, v, color=[C(ORANGE)] + ["#C9B2A9"] * 3, height=0.62)
        for yi, vi in zip(yy, v):
            ax.text(vi + 3, yi, f"{vi:.0f}%", va="center", fontsize=8.5, color="#262626")
        ax.set_title(y, fontsize=10.5, color="#262626", fontweight="bold")
        ax.set_xlim(0, 100); ax.set_xticks([]); ax.grid(False)
        ax.spines["bottom"].set_visible(False)
        ax.tick_params(length=0)
    axs[0].set_yticks(yy); axs[0].set_yticklabels(lab, fontsize=9.5)
    fig.tight_layout(w_pad=0.4)
    return save(fig, "driver_r2")


def fig_scatter():
    fig, axs = plt.subplots(1, 2, figsize=(4.4, 3.0))
    for ax, (xv, yv, xl, yl, c, t) in zip(axs, [
            ("d_bcom", "d_x", "Δ harga komoditas (%)", "Δ ekspor (%)", ORANGE, "Erat"),
            ("d_dep", "d_xm", "Δ depresiasi riil (%)", "Δ rasio X/M (%)", BROWN, "Hampir tak berpola")]):
        ax.scatter(sct[xv], sct[yv], s=9, color=C(c), alpha=0.7, lw=0)
        b = np.polyfit(sct[xv], sct[yv], 1)
        xx = np.linspace(sct[xv].min(), sct[xv].max(), 10)
        ax.plot(xx, np.polyval(b, xx), color="#404040", lw=1.2)
        ax.set_title(f"{t} (r = {sct[xv].corr(sct[yv]):.2f})".replace(".", ","), fontsize=9.5, color="#262626",
                     fontweight="bold")
        ax.set_xlabel(xl, fontsize=9); ax.set_ylabel(yl, fontsize=9)
        ax.tick_params(labelsize=8.5)
    fig.tight_layout(w_pad=1.2)
    return save(fig, "driver_scatter")


def fig_heat(df, rows, rowlab, name, figsize):
    piv = df.pivot(index=df.columns[0], columns="episode", values="d_xm_12m").loc[rows, list(eps.episode)]
    piv.columns = [EP_SHORT[c] for c in piv.columns]
    piv["Rata-rata"] = piv.mean(axis=1)
    piv = piv.sort_values("Rata-rata")
    rows = list(piv.index)
    fig, ax = plt.subplots(figsize=figsize)
    v = piv.values.astype(float)
    im = ax.imshow(np.clip(v, -50, 50), cmap=CMAP, vmin=-50, vmax=50, aspect="auto")
    cb = fig.colorbar(im, ax=ax, orientation="horizontal", fraction=0.045, pad=0.15, aspect=40)
    cb.set_ticks([-50, -25, 0, 25, 50])
    cb.set_ticklabels(["≤ −50\nmemburuk", "−25", "0", "+25", "≥ +50\nmembaik"])
    cb.ax.tick_params(labelsize=8, length=0)
    cb.outline.set_visible(False)
    for i in range(v.shape[0]):
        for j in range(v.shape[1]):
            if not np.isnan(v[i, j]):
                ax.text(j, i, f"{v[i, j]:.0f}".replace("-", "−"), ha="center", va="center", fontsize=8.5,
                        fontweight="bold" if j == v.shape[1] - 1 else "normal", color="#262626")
    # label dua baris supaya nama episode tidak bertabrakan
    xl = [c.replace(" ", "\n") if c != "Rata-rata" else "Rata-\nrata" for c in piv.columns]
    xl = [c.replace("–", "–\n") if "\n" not in c else c for c in xl]
    ax.set_xticks(range(v.shape[1])); ax.set_xticklabels(xl, fontsize=8.5, linespacing=0.95)
    ax.set_yticks(range(v.shape[0])); ax.set_yticklabels([rowlab[r] for r in rows], fontsize=9.5)
    ax.axvline(v.shape[1] - 1.5, color="#404040", lw=1)
    ax.grid(False)
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.tick_params(length=0)
    return save(fig, name), piv


def fig_avg_bar(series, labels, name):
    d = series.sort_values()
    fig, ax = plt.subplots(figsize=(3.2, 2.3))
    ax.barh([labels[i] for i in d.index], d.values, color=[C(ORANGE) if v > 0 else C(BROWN) for v in d.values],
            height=0.6)
    ax.axvline(0, color="#404040", lw=0.9); ax.grid(axis="y", visible=False)
    ax.tick_params(labelsize=9)
    ax.set_xlabel("Rata-rata 8 episode (%)", fontsize=9)
    return save(fig, name)


def fig_stats_ts():
    a = agg.copy()
    a["xm12"] = np.exp(a.lntb).rolling(12).mean()
    fig, axs = plt.subplots(1, 3, figsize=(9.4, 1.9))
    for ax, (v, t, c) in zip(axs, [("xm12", "Rasio X/M (rata-rata 12 bulan)", ORANGE),
                                    ("reer", "REER (2020=100)", BROWN), ("bcom", "BCOM (indeks)", BROWN)]):
        y = a.xm12 if v == "xm12" else np.exp(a.lnreer if v == "reer" else a.lncom)
        ax.plot(a.mdate, y, color=C(c), lw=1.8)
        ax.set_title(t, fontsize=10, color="#262626")
        ax.tick_params(labelsize=8.5)
    fig.tight_layout(w_pad=1.5)
    return save(fig, "stat_ts")


def fig_shares():
    d = shares.assign(lab=shares.grp.map(GRP)).sort_values("share_x")
    fig, ax = plt.subplots(figsize=(4.3, 2.8))
    y = np.arange(len(d))
    ax.barh(y + 0.19, d.share_x, height=0.36, color=C(ORANGE), label="Ekspor")
    ax.barh(y - 0.19, d.share_m, height=0.36, color=C(BROWN), label="Impor")
    ax.set_yticks(y); ax.set_yticklabels(d.lab)
    ax.grid(axis="y", visible=False)
    ax.set_xlabel("% dari total ekspor / impor ke dunia, 2006–2026")
    ax.legend(frameon=False, fontsize=9, loc="lower right")
    return save(fig, "pangsa_kelompok")


YLIM_RQ1 = (-25, 15)
XLAB_DIR = "← memburuk        % perubahan rasio X/M        membaik →"
SIG_LEGEND = [Patch(color=C(BROWN), label="memburuk, signifikan 10%"), Patch(color=C(ORANGE), label="membaik, signifikan 10%"),
              Patch(color="#" + PALE[BROWN], label="tidak signifikan")]


def fig_ardl_jcurve():
    fig, ax = plt.subplots(figsize=(4.3, 2.9))
    zones(ax, *YLIM_RQ1)
    d = dm_ag[dm_ag.h <= 24]
    for id_, c, ls, lab in [("A2_bic", MUTED, "--", "lag BIC"), ("A10_10mitra", MUTED, ":", "10 mitra"),
                            ("A1_main", BROWN, "-", "utama")]:
        s = d[d.id == id_]
        ax.plot(s.h, s.eff10, color=C(c), ls=ls, lw=2.6 if id_ == "A1_main" else 1.4)
        ax.text(24.6, s.eff10.iloc[-1], lab, fontsize=8.5, color=C(c), va="center",
                fontweight="bold" if id_ == "A1_main" else "normal")
    ax.set_xlim(0, 30)
    ax.set_xticks(range(0, 25, 6)); ax.set_xlabel("Bulan setelah rupiah melemah")
    ax.set_ylabel("% rasio X/M")
    return save(fig, "ardl_jcurve")


def fig_lp_line():
    s = lp[(lp.model == "A1_ols") & (lp.id == "AGG")].sort_values("h")
    fig, ax = plt.subplots(figsize=(4.3, 2.9))
    zones(ax, *YLIM_RQ1)
    ax.fill_between(s.h, s.lo90, s.hi90, color=C(BROWN), alpha=0.18, lw=0)
    ax.plot(s.h, s.eff, color=C(BROWN), lw=2.6)
    ax.text(24.6, s.eff.iloc[-1], "estimasi", fontsize=8.5, color=C(BROWN), va="center", fontweight="bold")
    ax.text(24.6, s.hi90.iloc[-1] + 1.5, "90% CI", fontsize=8.5, color="#7F7F7F", va="center")
    ax.set_xlim(0, 30)
    ax.set_xticks(range(0, 25, 6)); ax.set_xlabel("Bulan setelah rupiah melemah")
    ax.set_ylabel("% rasio X/M")
    return save(fig, "lp_agregat")


def fig_bar_partner():
    d = lp[(lp.model == "B2_partner") & (lp.h == 12)].copy()
    d["lab"] = d.id.map(CTRY)
    d = d.sort_values("eff", ascending=False)
    fig, ax = plt.subplots(figsize=(4.3, 3.3))
    ax.barh(d.lab, d.eff, color=[dcol(e, p) for e, p in zip(d.eff, d.p)], height=0.62)
    ax.errorbar(d.eff, d.lab, xerr=[d.eff - d.lo90, d.hi90 - d.eff], fmt="none", ecolor="#7F7F7F",
                elinewidth=0.8, capsize=2)
    ax.axvline(0, color="#404040", lw=0.9); ax.grid(axis="y", visible=False)
    ax.set_xlabel(XLAB_DIR, fontsize=9.5)
    ax.legend(handles=SIG_LEGEND, frameon=False, fontsize=8, loc="upper center", bbox_to_anchor=(0.42, -0.17), ncol=3,
              handlelength=1.2, columnspacing=0.8)
    return save(fig, "lp_mitra12")


def fig_group_two():
    d = lp[(lp.model == "C_group") & (lp.h.isin([12, 24]))].copy()
    d["lab"] = d.id.map(GRP_S)
    order = d[d.h == 12].sort_values("eff", ascending=False).lab.tolist()
    fig, axs = plt.subplots(1, 2, figsize=(4.5, 3.2), sharey=True)
    y = np.arange(len(order))
    for ax, h in zip(axs, (12, 24)):
        s = d[d.h == h].set_index("lab").loc[order]
        ax.barh(y, s.eff, color=[dcol(e, p) for e, p in zip(s.eff, s.p)], height=0.62)
        for yi, e, p in zip(y, s.eff, s.p):
            ax.text(e + (1.2 if e >= 0 else -1.2), yi, f"{e:.0f}{star(p)}".replace("-", "−"), va="center",
                    ha="left" if e >= 0 else "right", fontsize=8, color="#262626")
        ax.axvline(0, color="#404040", lw=0.9); ax.grid(axis="y", visible=False)
        ax.set_xlim(-38, 38); ax.set_xticks([-20, 0, 20])
        ax.set_title(f"Bulan ke-{h}", fontsize=10.5, fontweight="bold", color="#262626")
        ax.tick_params(labelsize=8.5)
    axs[0].set_yticks(y); axs[0].set_yticklabels(order, fontsize=9)
    fig.tight_layout(w_pad=0.6, rect=(0, 0.06, 1, 1))
    fig.text(0.6, 0.02, "← memburuk     % rasio X/M     membaik →", fontsize=9.5, ha="center")
    return save(fig, "lp_kelompok")


# ---- harga vs volume -------------------------------------------------------------
def pvv(model, id_, var, h, col="eff"):
    r = lpq[(lpq.model == model) & (lpq.id == id_) & (lpq["var"] == var) & (lpq.h == h)]
    return float(r[col].iloc[0]) if len(r) else np.nan


def pvs(model, id_, var, h):
    return sig(pvv(model, id_, var, h), pvv(model, id_, var, h, "p"))


def fig_pv_series():
    d = pvx[pvx.scope == "AGG10"].assign(mdate=lambda x: pd.to_datetime(x.mdate))
    fig, (ax, bx) = plt.subplots(2, 1, figsize=(4.5, 3.9), sharex=True)
    for fl, c, lb in [("Export", ORANGE, "ekspor"), ("Import", BROWN, "impor")]:
        s = d[d.flow == fl].set_index("mdate")
        ax.plot(s.index, s.pidx, color=C(c), lw=1.6)
        ax.text(s.index[-1] + pd.Timedelta(days=60), s.pidx.iloc[-1], lb, color=C(c), fontsize=8.5, va="center",
                fontweight="bold")
        v = s.vidx.rolling(12).mean()
        bx.plot(v.index, v, color=C(c), lw=1.6)
        bx.text(s.index[-1] + pd.Timedelta(days=60), v.iloc[-1], lb, color=C(c), fontsize=8.5, va="center",
                fontweight="bold")
    for x, t in [(ax, "A · Indeks harga (unit value Fisher, 2006 = 100)"),
                 (bx, "B · Indeks volume (rata-rata 12 bulan, 2006 = 100)")]:
        x.text(0.01, 0.97, t, transform=x.transAxes, ha="left", va="top", fontsize=9, fontweight="bold",
               color="#262626")
        x.tick_params(labelsize=8.5)
        x.set_xlim(pd.Timestamp("2006-01-01"), pd.Timestamp("2028-06-01"))
    ax.set_ylim(60, 320); bx.set_ylim(60, 260)
    fig.tight_layout(h_pad=0.4)
    return save(fig, "pv_series")


def fig_decomp_lines():
    d = lpq[(lpq.model == "P_agg")]
    fig, ax = plt.subplots(figsize=(4.4, 3.0))
    zones(ax, -25, 15)
    x = d[d["var"] == "lnxm"].sort_values("h")
    ax.fill_between(x.h, x.lo90, x.hi90, color=C(BROWN), alpha=0.13, lw=0)
    for v, c, ls, lw, lb in [("lnxm", BROWN, "-", 2.6, "rasio X/M"), ("lntot", ORANGE, "--", 1.8, "harga (ToT)"),
                             ("lnqxm", "#7F7F7F", ":", 2.0, "volume")]:
        s = d[d["var"] == v].sort_values("h")
        ax.plot(s.h, s.eff, color=C(c) if c[0] != "#" else c, ls=ls, lw=lw)
        ax.text(24.6, s.eff.iloc[-1], lb, fontsize=8.5, va="center", color=C(c) if c[0] != "#" else c,
                fontweight="bold")
    ax.set_xlim(0, 32); ax.set_xticks(range(0, 25, 6))
    ax.set_xlabel("Bulan setelah rupiah melemah"); ax.set_ylabel("% (depresiasi riil 10%)")
    return save(fig, "pv_decomp")


def fig_waterfall(h=12):
    comp = [("Harga ekspor", "lnpx", 1), ("Volume ekspor", "lnqx", 1), ("Harga impor", "lnpm", -1),
            ("Volume impor", "lnqm", -1), ("Rasio X/M", "lnxm", 1)]
    lab, val, col = [], [], []
    for nm, v, sg in comp:
        e, p = sg * pvv("P_agg", "AGG10", v, h), pvv("P_agg", "AGG10", v, h, "p")
        lab.append(nm); val.append(e); col.append(dcol(e, p) if v != "lnxm" else (C(BROWN) if e < 0 else C(ORANGE)))
    fig, ax = plt.subplots(figsize=(4.4, 3.0))
    y = np.arange(len(lab))[::-1]
    ax.barh(y, val, color=col, height=0.62, edgecolor=["none"] * 4 + ["#262626"], linewidth=1)
    for yi, e, (nm, v, sg) in zip(y, val, comp):
        p = pvv("P_agg", "AGG10", v, h, "p")
        ax.text(e + (0.5 if e >= 0 else -0.5), yi, f"{e:+.1f}{star(p)}".replace("-", "−").replace(".", ","),
                va="center", ha="left" if e >= 0 else "right", fontsize=9, color="#262626")
    ax.axhline(0.5, color="#BFBFBF", lw=0.8, ls="--")
    ax.set_yticks(y); ax.set_yticklabels(lab, fontsize=9.5)
    ax.axvline(0, color="#404040", lw=0.9); ax.grid(axis="y", visible=False)
    ax.set_xlim(-16, 8)
    ax.set_xlabel("← memburuk   kontribusi ke rasio X/M (%)   membaik →", fontsize=9)
    return save(fig, f"pv_waterfall{h}")


def fig_vol_lines():
    d = lpq[(lpq.model == "P_agg")]
    fig, ax = plt.subplots(figsize=(4.4, 2.35))
    for v, c, lb in [("lnqx", BROWN, "volume ekspor"), ("lnqm", "#7F7F7F", "volume impor")]:
        x = d[d["var"] == v].sort_values("h")
        cc = C(c) if c[0] != "#" else c
        ax.fill_between(x.h, x.lo90, x.hi90, color=cc, alpha=0.12, lw=0)
        ax.plot(x.h, x.eff, color=cc, lw=2.2)
        ax.text(24.6, x.eff.iloc[-1], lb, fontsize=8.5, va="center", color=cc, fontweight="bold")
    ax.axhline(0, color="#404040", lw=1)
    ax.text(0.3, 13.5, "Teori: volume ekspor naik (di atas 0), volume impor turun (di bawah 0)", fontsize=8.5,
            color=C(DARKOR), fontweight="bold", va="top")
    ax.set_ylim(-25, 15); ax.set_xlim(0, 33); ax.set_xticks(range(0, 25, 6))
    ax.set_xlabel("Bulan setelah rupiah melemah", fontsize=9); ax.set_ylabel("% volume", fontsize=9)
    ax.tick_params(labelsize=8.5)
    return save(fig, "pv_volume_lp")


def fig_two_channel(model, ids, labels, h, name):
    """dua panel: channel harga (ToT) dan channel volume, per mitra/kelompok; urut dari total paling buruk"""
    tot_ = {i: pvv(model, i, "lnxm", h) for i in ids}
    order = sorted(ids, key=lambda i: -tot_[i])
    fig, axs = plt.subplots(1, 2, figsize=(4.5, 3.3), sharey=True)
    y = np.arange(len(order))
    for ax, (v, t) in zip(axs, [("lntot", "Channel harga (ToT)"), ("lnqxm", "Channel volume")]):
        e = [pvv(model, i, v, h) for i in order]
        p = [pvv(model, i, v, h, "p") for i in order]
        ax.barh(y, e, color=[dcol(a, b) for a, b in zip(e, p)], height=0.62)
        for yi, a, b in zip(y, e, p):
            ax.text(a + (1 if a >= 0 else -1), yi, f"{a:.0f}{star(b)}".replace("-", "−"), va="center",
                    ha="left" if a >= 0 else "right", fontsize=8, color="#262626")
        ax.axvline(0, color="#404040", lw=0.9); ax.grid(axis="y", visible=False)
        lim = 32 if model == "Q_partner" else 48
        ax.set_xlim(-lim, lim)
        ax.set_title(t, fontsize=10.5, fontweight="bold", color="#262626")
        ax.tick_params(labelsize=8.5)
    axs[0].set_yticks(y); axs[0].set_yticklabels([labels[i] for i in order], fontsize=9)
    fig.tight_layout(w_pad=0.6, rect=(0, 0.06, 1, 1))
    fig.text(0.6, 0.02, "← memburuk     % rasio X/M     membaik →", fontsize=9.5, ha="center")
    return save(fig, name)


# =============================================================================
# Helper slide
# =============================================================================
def layout(prs, name):
    return next(l for l in prs.slide_layouts if l.name == name)


def _runs(par, runs, size, color, bold=False):
    """runs: str atau list (teks, bold, warna). ~teks~ = miring."""
    if isinstance(runs, str):
        runs = [(runs, bold, color)]
    for t, b, c in runs:
        for k, seg in enumerate(t.split("~")):
            if not seg:
                continue
            r = par.add_run()
            r.text = seg
            r.font.size = Pt(size)
            if b is not None:
                r.font.bold = bool(b)
            r.font.italic = (k % 2 == 1)
            if c:
                r.font.color.rgb = rgb(c)


def tbox(slide, x, y, w, h, paras, size=13, color=TXT, align=L, bold=False, fill=None, inset=None,
         bullets=False, space=5, anchor=MSO_ANCHOR.TOP):
    sh = slide.shapes.add_textbox(Pt(x), Pt(y), Pt(w), Pt(h))
    tf = sh.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    if inset is not None:
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = Pt(inset)
    if fill:
        sh.fill.solid()
        sh.fill.fore_color.rgb = rgb(fill)
    if isinstance(paras, (str, tuple)):
        paras = [paras]
    for i, p in enumerate(paras):
        par = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        par.alignment = align
        psize, pbold, prun, pb = size, bold, p, bullets
        if isinstance(p, dict):
            psize, pbold, prun, pb = p.get("size", size), p.get("bold", bold), p["runs"], p.get("bullet", bullets)
        _runs(par, prun, psize, color, pbold)
        if pb:
            pPr = par._p.get_or_add_pPr()
            pPr.set("marL", "171450"); pPr.set("indent", "-171450")
            etree.SubElement(pPr, qn("a:buFont")).set("typeface", "Arial")
            etree.SubElement(pPr, qn("a:buChar")).set("char", "•")
        if i > 0:
            par.space_before = Pt(space)
    return sh


def pointers(slide, items, x=44, y=400, w=872, h=None, head="Poin utama", size=12):
    """kotak krem berisi judul tebal + butir naratif; tinggi diperkirakan dari panjang teks"""
    paras = [{"runs": [(head, True, "000000")], "size": size + 1, "bullet": False}] if head else []
    est = 24 + ((size + 1) * 1.25 + 3 if head else 0)
    chars_per_line = (w - 18 - 14) / (size * 0.43)
    for it in items:
        runs = it if isinstance(it, list) else [(it, False, None)]
        paras.append({"runs": runs, "bullet": True})
        n = len("".join(t for t, _, _ in runs).replace("~", ""))
        est += -(-n // chars_per_line) * size * 1.2 + 3
    hh = est if h is None else min(h, est)
    return tbox(slide, x, y, w, hh, paras, size=size, fill=CREAM, inset=9, space=3)


def title(slide, text):
    tf = slide.shapes.title.text_frame
    tf.text = ""
    _runs(tf.paragraphs[0], [(text, None, None)], 20, None)


def hline(slide, x, y, w, color=LINE, weight=0.75):
    ln = slide.shapes.add_connector(1, Pt(x), Pt(y), Pt(x + w), Pt(y))
    ln.line.color.rgb = rgb(color)
    ln.line.width = Pt(weight)


def source(slide, text):
    tbox(slide, 400, 516, 532, 20, [[("Sumber", True, GREY), (": " + text, False, GREY)]], size=10.5, align=R)


def note(slide, text, y, h=30, x=44, w=872):
    tbox(slide, x, y, w, h, text, size=10.5, color=GREY)


def plabel(slide, x, y, w, l1, l2):
    tbox(slide, x, y, w, 38, [{"runs": l1, "bold": True}, {"runs": l2}], size=13, color="000000",
         align=PP_ALIGN.CENTER, space=0)


def pic(slide, path, x, y, w, h):
    """gambar dimuat sebesar mungkin di dalam kotak (x, y, w, h), rata tengah horizontal"""
    iw, ih = Image.open(path).size
    s = min(w / iw, h / ih)
    pw, ph = iw * s, ih * s
    slide.shapes.add_picture(path, Pt(x + (w - pw) / 2), Pt(y), width=Pt(pw), height=Pt(ph))


def numbered(slide, items, y0=92, step=70, x=44, w=872, desc=12.5, head=14.5):
    hline(slide, x, y0, w)
    for i, (hd, ds) in enumerate(items):
        y = y0 + 6 + i * step
        tbox(slide, x, y, 50, 50, f"{i + 1:02d}", size=24, color=BROWN, bold=True)
        tbox(slide, x + 58, y + 1, w - 58, step - 10,
             [{"runs": [(hd, True, "000000")], "size": head}, {"runs": ds, "size": desc}], color=TXT, space=2)
        hline(slide, x, y0 + (i + 1) * step, w)


def table(slide, x, y, w, data, col_w, align=None, size=11.5, row_h=20, hl_rows=()):
    nr, nc = len(data), len(data[0])
    gf = slide.shapes.add_table(nr, nc, Pt(x), Pt(y), Pt(w), Pt(row_h * nr))
    tbl = gf.table
    tblPr = tbl._tbl.tblPr
    tblPr.set("firstRow", "1"); tblPr.set("bandRow", "0")
    st = tblPr.find(qn("a:tableStyleId"))
    if st is not None:
        tblPr.remove(st)
    for j, cw in enumerate(col_w):
        tbl.columns[j].width = Pt(w * cw / sum(col_w))
    for i in range(nr):
        tbl.rows[i].height = Pt(row_h)
        for j in range(nc):
            c = tbl.cell(i, j)
            c.margin_left = c.margin_right = Pt(5)
            c.margin_top = c.margin_bottom = Pt(2)
            c.vertical_anchor = MSO_ANCHOR.MIDDLE
            par = c.text_frame.paragraphs[0]
            c.text_frame.word_wrap = True
            par.alignment = align[j] if align else (L if j == 0 else R)
            txt, colr = data[i][j], "000000"
            if isinstance(txt, tuple):
                txt, colr = txt
            for k, seg in enumerate(str(txt).split("~")):
                if not seg:
                    continue
                r = par.add_run()
                r.text = seg
                r.font.size = Pt(size)
                r.font.bold = (i == 0) or (i in hl_rows)
                r.font.italic = (k % 2 == 1)
                r.font.color.rgb = rgb(colr)
                r.font.name = "Arial"
            tcPr = c._tc.get_or_add_tcPr()
            for tag in ("a:lnL", "a:lnR", "a:lnT", "a:lnB"):
                ln = etree.SubElement(tcPr, qn(tag))
                if tag == "a:lnB":
                    ln.set("w", "12700" if i == 0 else "6350")
                    etree.SubElement(etree.SubElement(ln, qn("a:solidFill")), qn("a:srgbClr")).set(
                        "val", "000000" if i == 0 else "E0E0E0")
                else:
                    ln.set("w", "0")
                    etree.SubElement(ln, qn("a:noFill"))
            etree.SubElement(tcPr, qn("a:noFill"))
    return gf


def box(slide, x, y, w, h, head, desc, num, fill=CREAM, accent=BROWN, dy=76, dsize=11):
    """kartu tahap: nomor, judul tebal, deskripsi"""
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Pt(x), Pt(y), Pt(w), Pt(h))
    sh.fill.solid(); sh.fill.fore_color.rgb = rgb(fill)
    sh.line.fill.background()
    sh.shadow.inherit = False
    tbox(slide, x + 6, y + 4, w - 12, 30, num, size=20, color=accent, bold=True)
    tbox(slide, x + 6, y + 34, w - 12, 40, [{"runs": [(head, True, "000000")]}], size=12.5)
    tbox(slide, x + 6, y + dy, w - 12, h - dy - 4, desc, size=dsize, color=TXT)


def section(prs, num, text, sub=None):
    """pembatas bagian; sub = pertanyaan pemandu yang dijawab bagian ini"""
    s = prs.slides.add_slide(layout(prs, "SubTitle_DEN_bhs"))
    ph = s.placeholders[1]
    ph.text_frame.text = text
    for r in ph.text_frame.paragraphs[0].runs:
        r.font.size = Pt(26); r.font.bold = True
    if num:
        tbox(s, 45, 180, 200, 76, num, size=60, color=SECNUM, bold=True)
    if sub:
        hline(s, 47, 326, 60, color=SECNUM, weight=2)
        tbox(s, 45, 334, 360, 80, sub, size=15, color=CREAM)


def content(prs, ttl, notes=None):
    s = prs.slides.add_slide(layout(prs, "Content_DEN_bhs"))
    title(s, ttl)
    if notes:
        s.notes_slide.notes_text_frame.text = notes.replace("~", "")
    return s


def make_template():
    if os.path.exists(TEMPLATE):
        return
    prs = Presentation(SRC_DECK)
    lst = prs.slides._sldIdLst
    for sid in list(lst):
        prs.part.drop_rel(sid.rId); lst.remove(sid)
    prs.save(TEMPLATE)


# =============================================================================
# Deck
# =============================================================================
def build():
    make_template()
    prs = Presentation(TEMPLATE)
    A = ardl_ag.set_index("id")
    A1 = A.loc["A1_main"]
    am, ak = ardl_mi.set_index("id"), ardl_kg.set_index("id")
    sh = shares.set_index("grp")
    E = eps.copy()
    bench = (np.log((agg.exports_usdk / agg.imports_usdk).rolling(3).mean()).diff(12) * 100).mean()
    ep_mean = E.d_xm_12m.mean()
    dr = drv.set_index(["y", "driver"]).r2 * 100
    lp6, lp12 = lpv("A1_ols", "AGG", 6), lpv("A1_ols", "AGG", 12)

    # ---- cover
    s = prs.slides.add_slide(layout(prs, "1_Title_Garuda"))
    ph = list(s.placeholders)
    tf = ph[0].text_frame
    tf.text = "Depresiasi Rupiah dan Neraca Perdagangan"
    tf.add_paragraph().text = "ARDL dan Local Projections, Data HS-6"
    for p in tf.paragraphs:
        for r in p.runs:
            r.font.size = Pt(26); r.font.color.rgb = rgb("FFFFFF")
    ph[1].text_frame.text = "Indonesia–dunia & 10 mitra   |  Data s.d. Jun 2026   |  November 2026"


    # ---- ringkasan eksekutif
    s = content(prs, "Ringkasan: pelemahan rupiah tidak memperbaiki neraca perdagangan Indonesia",
                notes="Slide ini adalah jawaban singkat seluruh riset. Empat angka di atas merangkum bukti utamanya: model "
                      "ekonometrika, perbandingan episode depresiasi, peran harga komoditas, dan mitra yang paling terdampak. "
                      "Empat butir di bawah menjawab tiga pertanyaan penelitian dan implikasinya. Bagian-bagian berikutnya "
                      "menjelaskan dari mana angka-angka ini berasal.")
    kpis = [(f"{idn(lp12, 0)}%", f"Rasio ekspor/impor 12 bulan setelah rupiah melemah riil 10% (local projections; ARDL "
                                 f"{idn(A1.eff10_m12, 0)}%)", BROWN),
            (f"{idn(ep_mean)}%", f"Rata-rata perubahan rasio X/M 12 bulan setelah 8 episode depresiasi; bulan biasa "
                                 f"{idn(bench)}%", BROWN),
            (f"{idn(dr[('Ekspor', 'Harga komoditas (BCOM)')], 0)}% vs {idn(dr[('Ekspor', 'Depresiasi riil (REER)')], 0)}%",
             "Variasi ekspor yang sejalan dengan harga komoditas, dibanding yang sejalan dengan depresiasi", DARKOR),
            (f"{idn(pvv('P_agg', 'AGG10', 'lnqx', 12), 0)}%",
             "Volume ekspor ke 10 mitra 12 bulan setelah depresiasi riil 10%: volume tidak naik, justru turun", BROWN)]
    for i, (big, ds, colr) in enumerate(kpis):
        x = 44 + i * 222
        hline(s, x, 94, 206, color=colr, weight=2.5)
        tbox(s, x, 98, 206, 36, big, size=24, bold=True, color=colr)
        tbox(s, x, 136, 206, 60, ds, size=10.5, color=TXT)
    numbered(s, [
        ("RQ1 · Neraca agregat memburuk dan tidak pulih; tidak ada J-curve",
         "Rasio ekspor/impor turun sekitar 10% dalam 6–12 bulan. Dua pertiganya karena volume ekspor turun, sisanya karena "
         "terms of trade. Elastisitas volume tidak signifikan dan jumlahnya di bawah 1: Marshall-Lerner tidak terpenuhi."),
        ("RQ2 · Memburuk dengan China (lewat harga) dan Jepang (lewat harga dan volume)",
         "Tidak ada mitra yang membaik secara signifikan, termasuk AS sebagai tujuan ekspor manufaktur."),
        ("RQ3 · Komoditas memburuk lewat harga; barang konsumsi membaik lewat volume",
         "Barang konsumsi satu-satunya kelompok yang bereaksi sesuai teori: volume ekspor-impornya bergeser sehingga rasionya "
         "membaik signifikan setelah 1–2 tahun. Energi & tambang dan barang modal memburuk."),
        ("Implikasi · rupiah yang lebih lemah bukan alat untuk memperbaiki neraca",
         "Neraca lebih ditentukan harga komoditas dan struktur impor. Substitusi impor input dan diversifikasi ekspor ke "
         "barang yang sensitif harga lebih relevan daripada mengandalkan pelemahan kurs."),
    ], y0=206, step=64, desc=11.5, head=13)
    note(s, "Catatan: hasil konsisten antar metode, tetapi kemungkinan ~reverse causality~ belum sepenuhnya tertangani; lihat slide "
            "“Mengapa depresiasi tidak memperbaiki neraca?” dan keterbatasan di kesimpulan.", y=470, h=30)
    source(s, "Estimasi penulis; ITC Trade Map, BIS, Bloomberg")

    # ---- alur presentasi
    s = content(prs, "Alur presentasi: enam pertanyaan berurutan, dari teori sampai ~robustness check~",
                notes="Setiap bagian presentasi menjawab satu pertanyaan, dan jawabannya menjadi bahan bagian berikutnya. "
                      "Teori memberi prediksi, data dan fakta awal menunjukkan pola tanpa model, metode memisahkan efek kurs "
                      "dari faktor lain, hasil menjawab tiga pertanyaan penelitian, dan diagnostik memastikan hasilnya tidak "
                      "bergantung pada satu pilihan model.")
    flow = [("01", "Teori dan literatur", "Apa yang seharusnya terjadi?",
             "Marshall-Lerner, J-curve, bukti global dan Indonesia, research gap, tiga RQ."),
            ("02", "Data", "Apa yang diukur?",
             "10 mitra; 6.883 kode HS-6 menjadi 7 kelompok; indeks harga dan volume; statistik deskriptif."),
            ("03", "Fakta awal", "Apa kata data sebelum model?",
             "8 episode depresiasi, neraca sebelum-sesudah, faktor penggerak neraca, pola per mitra dan kelompok."),
            ("04", "Metodologi", "Cara memisahkan efek kurs?",
             "Tahapan analisis, ARDL vs local projections, daftar 14 variabel, model specification, interpretasi koefisien."),
            ("05", "Hasil", "Apa jawabannya?",
             "RQ1–RQ3, masing-masing dibedah menjadi harga vs volume; uji Marshall-Lerner; mengapa tidak membaik."),
            ("06", "Diagnostik", "Seberapa yakin?",
             "~Unit root test~, ~cointegration~, uji ~residual~, CUSUM, 11 spesifikasi alternatif, NARDL, panel.")]
    cw_ = 139
    for i, (n, nm, q, ds) in enumerate(flow):
        x = 44 + i * (cw_ + 7.6)
        sh_ = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Pt(x), Pt(94), Pt(cw_), Pt(206))
        sh_.fill.solid(); sh_.fill.fore_color.rgb = rgb(CREAM); sh_.line.fill.background(); sh_.shadow.inherit = False
        tbox(s, x + 6, 98, cw_ - 12, 34, n, size=24, bold=True, color=DARKOR if n == "05" else BROWN)
        tbox(s, x + 6, 132, cw_ - 12, 22, nm, size=13.5, bold=True, color="000000")
        tbox(s, x + 6, 154, cw_ - 12, 40, q, size=12.5, bold=True, color=DARKOR)
        tbox(s, x + 6, 196, cw_ - 12, 104, ds, size=11.5, color=TXT)
    pointers(s, [
        [("Dua metode, satu pertanyaan: ", True, None),
         ("ARDL adalah standar literatur J-curve, sehingga hasil bisa dibandingkan dengan studi Indonesia sebelumnya. Local "
          "projections dipakai sebagai pemeriksa independen karena tidak memaksa satu hubungan ~long-run~ dan bisa menyerap "
          "~global shock~ lewat ~fixed effects~.", False, None)],
        [("Fakta awal sebelum model: ", True, None),
         ("kalau pola di data mentah dan hasil model sejalan, kesimpulannya lebih meyakinkan.", False, None)],
        [("Setelah bagian 06: ", True, None), ("kesimpulan dan implikasi. Lampiran A1–A4 berisi glosarium istilah umum dan "
                                               "ekonometrika; lampiran B–E berisi tabel estimasi lengkap.", False, None)],
    ], y=312)
    # legenda warna yang berlaku di seluruh deck
    tbox(s, 44, 440, 300, 20, [[("Konvensi warna di seluruh grafik dan tabel", True, "000000")]], size=12)
    for k, (colr, lb) in enumerate([(BROWN, "neraca memburuk (signifikan)"), (ORANGE, "neraca membaik (signifikan)"),
                                    (PALE[BROWN], "tidak signifikan")]):
        x = 44 + k * 230
        sw = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Pt(x), Pt(466), Pt(26), Pt(14))
        sw.fill.solid(); sw.fill.fore_color.rgb = rgb(colr); sw.line.fill.background(); sw.shadow.inherit = False
        tbox(s, x + 32, 461, 196, 22, lb, size=11.5, color=TXT)
    tbox(s, 44, 486, 872, 20, "Semua angka hasil = % perubahan rasio ekspor/impor bila rupiah melemah riil 10%; * = signifikan "
                              "pada 10%.", size=11, color=GREY)


    # =========================================================================
    section(prs, "01", "Teori dan literatur",
            "Apa yang seharusnya terjadi ketika rupiah melemah, dan apa kata studi sebelumnya?")

    s = content(prs, "Marshall-Lerner: depresiasi hanya memperbaiki neraca bila volume ekspor-impor cukup responsif",
                notes="Inti Marshall-Lerner: depresiasi punya dua efek yang berlawanan. Efek harga langsung memperburuk neraca "
                      "karena setiap unit impor jadi lebih mahal dalam rupiah. Efek volume memperbaiki neraca karena ekspor "
                      "lebih laku dan impor berkurang. Neraca membaik hanya jika efek volume lebih besar, yaitu bila jumlah "
                      "elastisitas lebih dari satu. Contoh di kanan menunjukkan dua kasus dengan depresiasi yang sama tetapi "
                      "hasil berlawanan.")
    tbox(s, 44, 94, 430, 118, [
        {"runs": [("Rumus", True, "000000")], "size": 13.5},
        {"runs": [("|εX| + |εM| > 1", True, DARKOR)], "size": 22},
        {"runs": "εX: seberapa besar volume ekspor naik bila harganya bagi pembeli asing turun 1%. "
                 "εM: seberapa besar volume impor turun bila harganya dalam rupiah naik 1%.", "size": 11.5},
    ], fill=CREAM, inset=10, space=3)
    tbox(s, 44, 220, 430, 230, [
        [("Depresiasi memicu dua efek yang berlawanan.", True, None)],
        [("Efek harga (langsung, memperburuk): ", True, None),
         ("impor dengan volume yang sama kini lebih mahal dalam rupiah.", False, None)],
        [("Efek volume (bertahap, memperbaiki): ", True, None),
         ("ekspor lebih murah di mata pembeli asing sehingga lebih laku; impor lebih mahal sehingga dikurangi.", False, None)],
        [("Neraca membaik hanya jika efek volume mengalahkan efek harga. ", True, None),
         ("Syaratnya: jumlah kedua elastisitas lebih dari 1.", False, None)],
    ], size=12.5, bullets=True)
    plabel(s, X2, 90, W2, "Contoh angka: depresiasi 10%, ekspor = impor = Rp100 di awal",
           [("(nilai dalam rupiah)", False, None)])
    table(s, X2, 132, W2, [
        ["", "Kasus A: responsif", "Kasus B: tidak responsif"],
        ["Elastisitas εX ; εM", "0,8 ; 0,5", "0,2 ; 0,3"],
        ["Jumlah |εX| + |εM|", ("1,3 (> 1)", DARKOR), "0,5 (< 1)"],
        ["Ekspor: 100 × (1 + 0,1 × εX)", "108,0", "102,0"],
        ["Impor: 100 × 1,1 × (1 − 0,1 × εM)", "104,5", "106,7"],
        ["Neraca (ekspor − impor)", ("+3,5 membaik", DARKOR), "−4,7 memburuk"],
    ], [1.9, 1.1, 1.2], align=[L, R, R], size=11, row_h=27)
    pointers(s, [
        [("Cara membaca contoh: ", True, None),
         ("ekspor dalam rupiah naik hanya karena volumenya bertambah (εX × 10%). Impor dalam rupiah naik 10% karena harganya, "
          "lalu sedikit turun karena volumenya berkurang (εM × 10%). Neraca membaik bila kenaikan ekspor lebih besar daripada "
          "kenaikan tagihan impor.", False, None)],
        [("Relevansi untuk Indonesia: ", True, None),
         ("Indonesia cenderung mirip Kasus B. Ekspor batu bara, CPO, dan nikel dihargai dalam USD, sehingga rupiah yang murah "
          "tidak membuatnya lebih laku, sementara impor input sulit dikurangi (Tang 2002: elastisitas harga impor hanya −0,4).",
          False, None)],
    ], x=X2, y=304, w=W2, head="", size=11)
    source(s, "Marshall (1923), Lerner (1944), Tang (2002); contoh angka ilustratif")

    s = content(prs, "J-curve: neraca turun dulu karena harga bergerak lebih cepat daripada volume",
                notes="J-curve adalah versi dinamis Marshall-Lerner. Begitu rupiah melemah, harga impor dalam rupiah langsung "
                      "naik, tetapi volume perdagangan masih terkunci kontrak yang sudah disepakati. Akibatnya neraca turun "
                      "dulu. Beberapa bulan kemudian pembeli dan penjual menyesuaikan volume, dan bila Marshall-Lerner "
                      "terpenuhi, neraca naik melewati posisi awal. Bentuk grafiknya menyerupai huruf J.")
    plabel(s, X1, 90, W1, "Pola J-curve (ilustrasi)", [("(neraca perdagangan setelah depresiasi)", False, None)])
    pic(s, fig_jcurve_theory(), X1, 130, W1, 270)
    numbered(s, [
        ("Fase 1 · harga bergerak, volume belum",
         "Kontrak ekspor-impor sudah disepakati; impor yang sama kini lebih mahal dalam rupiah. Neraca memburuk."),
        ("Fase 2 · volume menyesuaikan",
         "Setelah kontrak lama habis, pembeli asing menambah pembelian dan importir mengurangi impor. Neraca membaik."),
        ("Syarat akhirnya tetap Marshall-Lerner",
         "Jika elastisitas terlalu kecil, fase 2 tidak cukup kuat dan neraca tidak pernah kembali ke atas posisi awal."),
    ], x=X2, w=W2, y0=94, step=96, desc=11.5, head=13)
    pointers(s, [
        [("Definisi empiris: ", True, None), ("efek ~short-run~ negatif yang diikuti efek ~long-run~ positif dan "
                                              "signifikan (Rose & Yellen 1989). Di riset ini diuji lewat ~dynamic multiplier~ "
                                              "ARDL dan ~impulse response~ local projections, bulan 0–24.", False, None)],
    ], y=410, h=58, head="Cara menguji", size=11.5)
    source(s, "Magee (1973), Rose & Yellen (1989), Bahmani-Oskooee & Ratha (2004)")

    s = content(prs, "Literatur global: bukti Marshall-Lerner dan J-curve bervariasi antar negara dan metode",
                notes="Literatur internasional tidak memberi jawaban tunggal. Studi awal di negara maju justru tidak "
                      "menemukan efek kurs yang kuat, sementara studi yang memakai data lebih rinci dan metode nonlinear "
                      "lebih sering menemukan J-curve. Pelajaran untuk kita: hasil sangat bergantung pada tingkat agregasi, "
                      "karena itu riset ini memecah analisis per mitra dan per kelompok barang.")
    table(s, 44, 94, 872, [
        ["Studi", "Topik", "Data dan metode", "Temuan"],
        ["Marshall (1923); Lerner (1944)", "Marshall-Lerner", "Teori", "Merumuskan syarat elastisitas |εX| + |εM| > 1"],
        ["Magee (1973), Brookings Papers", "J-curve", "Teori dan kasus AS", "Menamai J-curve: kontrak dan ~pass-through~ membuat neraca turun dulu"],
        ["Rose & Yellen (1989), J. Monetary Econ.", "J-curve", "AS bilateral, ~cointegration~", "Tidak menemukan J-curve yang andal"],
        ["Rose (1991), J. International Econ.", "Marshall-Lerner", "5 negara OECD", "Kurs riil tidak berpengaruh signifikan terhadap neraca"],
        ["Backus, Kehoe & Kydland (1994), AER", "J-curve", "Model dan data OECD", "Korelasi neraca–~terms of trade~ membentuk 'S-curve'"],
        ["Bahmani-Oskooee & Niroomand (1998), Econ. Letters", "Marshall-Lerner", "30 negara, ~cointegration~", "Terpenuhi di sebagian besar negara"],
        ["Bahmani-Oskooee & Ratha (2004), Applied Econ.", "Keduanya", "Survei literatur", "Hasil bergantung negara, periode, dan agregasi"],
        ["Bahmani-Oskooee & Fariditavana (2016), Open Econ. Rev.", "J-curve", "NARDL, banyak negara", "Nonlinear lebih sering menemukan J-curve"],
    ], [2.4, 1.1, 1.6, 3.0], align=[L, L, L, L], size=11, row_h=31)
    pointers(s, ["Studi agregat cenderung menemukan efek lemah; studi bilateral, per industri, dan nonlinear lebih sering "
                 "menemukan efek. Ini alasan riset ini tidak berhenti di level agregat."], y=380, h=56, head="Benang merah",
             size=12)
    source(s, "Lihat notes/4_litrev_metode.md untuk daftar pustaka lengkap")

    s = content(prs, "Studi Indonesia: efek kurs hanya muncul di sebagian mitra dan industri; di level agregat umumnya tidak "
                     "signifikan",
                notes="Sekarang khusus Indonesia. Gambarannya tidak seragam, dan justru di situ letak pentingnya. Di level "
                      "agregat, studi-studi awal umumnya tidak menemukan hubungan yang signifikan antara kurs rupiah dan neraca. "
                      "Bahmani-Oskooee dan Harvey (2015) merangkumnya secara eksplisit: studi yang memakai perdagangan "
                      "Indonesia dengan dunia maupun dengan AS tidak menemukan efek yang signifikan, dan efek baru terlihat "
                      "ketika data dipecah per industri, itu pun hanya di sembilan dari 23 industri. Tang (2002) menunjukkan "
                      "impor Indonesia tidak elastis terhadap harga, dan Wijaya (2020) tidak menemukan J-curve maupun "
                      "Marshall-Lerner untuk China dan Jepang, dua mitra terbesar. Studi yang menemukan efek hampir semuanya "
                      "bilateral, per industri, atau nonlinear. Dari sini research gap kami muncul: belum ada studi yang "
                      "menggabungkan level dunia, mitra, dan kelompok barang HS-6 dalam satu kerangka, dengan kontrol harga "
                      "komoditas dan local projections sebagai cek ~endogeneity~.")
    table(s, 44, 92, 872, [
        ["Studi", "Data dan metode", "Temuan", "Efek kurs?"],
        ["Tang (2002), IIUM J. Econ. & Mgmt.", "Impor agregat; ARDL bounds test", "Elastisitas harga impor hanya −0,4",
         ("Lemah", BROWN)],
        ["Bahmani-Oskooee & Harvey (2015), Int. Trade Journal", "AS–Indonesia, 23 industri; ARDL",
         "Studi agregat dan bilateral AS sebelumnya tidak menemukan efek signifikan; per industri hanya 9 dari 23 membaik",
         ("Tidak (agregat); sebagian (industri)", BROWN)],
        ["Wijaya (2020), J. Dinamika Ekonomi Pembangunan", "China, Jepang, Singapura; 2010–2017; ECM",
         "Tidak ada J-curve dan Marshall-Lerner untuk China dan Jepang; ada untuk Singapura", ("Tidak (China, Jepang)", BROWN)],
        ["Widarjono (2005), J. Indonesian Econ. & Business", "AS, Jepang, Singapura; 1988–2003; Johansen, VECM",
         "Marshall-Lerner dan J-curve hanya untuk Jepang", "Sebagian"],
        ["Bahmani-Oskooee & Harvey (2009), J. Econ. Integration", "13 mitra; ARDL", "J-curve pada 5 dari 13 mitra", "Sebagian"],
        ["Bahmani-Oskooee & Harvey (2019), New Zealand Econ. Papers", "Mitra utama; NARDL",
         "~Asymmetry~ ~long-run~ hanya di 5 model", "Sebagian"],
        ["Rifami & Heriqbaldi (2023), Iranian Econ. Review", "50 industri, Indonesia–China; ARDL, NARDL",
         "J-curve di 2 industri (ARDL), 9 industri (NARDL)", "Sebagian"],
        ["Salim dkk. (2023), J. Business & Information Systems", "Indonesia–China 2002–2017; ARDL, NARDL",
         "J-curve hanya muncul dengan pendekatan nonlinear", "Sebagian"],
    ], [2.3, 2.0, 2.7, 1.3], align=[L, L, L, L], size=10, row_h=31)
    pointers(s, [
        [("Studi yang tidak menemukan efek: ", True, None),
         ("Tang (2002), Wijaya (2020), dan studi agregat yang dirangkum Bahmani-Oskooee & Harvey (2015). Efek kurs baru "
          "muncul ketika data dipecah per mitra, per industri, atau dengan model nonlinear.", False, None)],
        [("Research gap: ", True, None),
         ("belum ada studi Indonesia yang menggabungkan level dunia, 10 mitra, dan 7 kelompok barang HS-6 dalam satu "
          "kerangka, dengan kontrol harga komoditas spesifik (BCOM, batu bara, CPO) dan local projections sebagai cek "
          "~endogeneity~.", False, None)],
    ], y=382, head="Posisi riset ini", size=11)
    source(s, "Studi yang dikutip di tabel; daftar pustaka di notes/4_litrev_metode.md")

    s = content(prs, "Tiga pertanyaan penelitian dan hipotesisnya",
                notes="Dari teori dan literatur tadi, kami turunkan tiga pertanyaan yang makin rinci. Pertama, di level paling "
                      "besar: apakah neraca Indonesia secara keseluruhan membaik ketika rupiah melemah? Dugaan kami tidak, "
                      "karena ekspor kita didominasi komoditas yang harganya ditentukan dalam USD, sehingga rupiah yang lebih "
                      "murah tidak membuat batu bara atau CPO lebih laku. Kedua, apakah jawabannya berbeda per mitra? Dugaan "
                      "kami neraca dengan pemasok mesin dan bahan baku seperti China dan Jepang memburuk, sedangkan dengan AS "
                      "sebagai pasar manufaktur bisa membaik. Ketiga, apakah berbeda per jenis barang? Dugaan kami hanya barang "
                      "yang sensitif harga, seperti barang konsumsi, yang bereaksi sesuai teori. Ketiga pertanyaan diukur dengan "
                      "satu ukuran yang sama supaya hasilnya bisa dibandingkan langsung.")
    numbered(s, [
        ("RQ1 · Apakah depresiasi rupiah memperbaiki neraca perdagangan Indonesia?",
         "Hipotesis: efek ~long-run~ kecil karena ekspor didominasi komoditas berharga USD (~dominant currency~, "
         "Gopinath dkk. 2020); dalam ~short-run~ neraca memburuk karena impor input langsung lebih mahal."),
        ("RQ2 · Apakah efeknya berbeda per negara mitra?",
         "Hipotesis: memburuk untuk mitra pemasok barang modal dan bahan baku (China, Jepang); membaik untuk tujuan ekspor "
         "manufaktur padat karya yang sensitif harga (AS)."),
        ("RQ3 · Apakah efeknya berbeda per kelompok barang?",
         "Hipotesis: barang yang sensitif harga (barang konsumsi, pangan olahan) membaik; komoditas berharga USD dan input "
         "impor tidak."),
    ], step=92)
    pointers(s, [
        [("Ukuran neraca: ", True, None),
         ("ln(ekspor/impor), standar literatur J-curve. Rasio dipakai, bukan selisih, karena tetap bisa dihitung saat neraca "
          "defisit dan tidak terpengaruh skala. Hasil dibaca sebagai % perubahan rasio ekspor/impor akibat depresiasi riil "
          "10%; positif berarti membaik.", False, None)]], y=376, h=76, head="Satu ukuran untuk semua pertanyaan")


    # =========================================================================
    section(prs, "02", "Data",
            "Apa yang diukur: mitra dagang, kelompok barang dari 6.883 kode HS-6, serta harga dan volume")

    fp, psh, tx, tm, tt = fig_partners()
    s = content(prs, f"Sepuluh mitra yang dianalisis mencakup {idn(tt, 0)}% perdagangan Indonesia selama 2006–2026",
                notes="Setelah variabel, pertanyaan berikutnya adalah dengan negara mana saja. Kami memilih sepuluh mitra dagang terbesar berdasarkan total nilai ekspor plus impor. Bersama-sama mereka "
                      "mewakili sekitar tujuh puluh persen perdagangan Indonesia, dan mencakup tiga tipe mitra yang berbeda: "
                      "pemasok input (China, Jepang, Korea), tujuan ekspor manufaktur (AS), dan mitra regional ASEAN. Syarat lainnya "
                      "praktis: kurs, inflasi, dan produksi industri bulanan harus tersedia untuk seluruh periode, supaya kurs "
                      "riil bilateral bisa dihitung. Sisa perdagangan tidak dibuang, karena tetap masuk di analisis level dunia.")
    plabel(s, X1, 90, W1, "Pangsa tiap mitra dalam perdagangan Indonesia", [("(% kumulatif Jan 2006–Agu 2026)", False, None)])
    pic(s, fp, X1, 128, W1, 372)
    table(s, X2, 96, W2, [
        ["Kriteria pemilihan", "Keterangan"],
        ["Ukuran", f"Mitra terbesar menurut nilai ekspor + impor; bersama {idn(tx, 0)}% ekspor dan {idn(tm, 0)}% impor"],
        ["Keragaman peran", "Pemasok input (China, Jepang, Korea), pasar ekspor manufaktur (AS, India), mitra ASEAN"],
        ["Ketersediaan data", "Kurs, CPI, dan IPI bulanan tersedia 2006–2026 untuk semua mitra"],
        ["Konsistensi", "Mitra yang sama dipakai di ARDL, panel PMG/MG, dan local projections"],
    ], [1.1, 2.9], align=[L, L], size=11, row_h=40)
    pointers(s, [
        f"China sendiri menyumbang {idn(psh.loc['CHN', 't'], 0)}% perdagangan; Jepang {idn(psh.loc['JPN', 't'], 0)}% dan "
        f"Singapura {idn(psh.loc['SGP', 't'], 0)}%.",
        "Peran tiap mitra berbeda: Indonesia defisit dengan China, Singapura, Thailand, dan Australia, tetapi surplus dengan "
        "AS, India, dan Jepang. Karena itu efek depresiasi bisa berlawanan arah antar mitra.",
        "Neraca dengan dunia (agregat) tetap dipakai untuk RQ1, sehingga sisa 29% perdagangan tidak hilang dari analisis.",
    ], x=X2, y=310, w=W2, size=11.5)
    source(s, "ITC Trade Map; olahan penulis")

    cw = cov[cov.ISO3 == "WLD"].set_index(["Flow", "Classification", "Class"]).Value_Share_pct
    mix_x = cw.loc[("Exports_USDk", "Commodity_Class", "mixed")] + cw.loc[("Exports_USDk", "Commodity_Class", "unclassified")]
    mix_m = cw.loc[("Imports_USDk", "BEC5_EndUse", "mixed")] + cw.loc[("Imports_USDk", "BEC5_EndUse", "unclassified")]
    s = content(prs, "Klasifikasi HS-6: 6.883 kode barang dipetakan ke 7 kelompok lewat tabel korespondensi resmi UNSD",
                notes="Untuk menjawab RQ3, barang perlu dikelompokkan. Data perdagangan tersedia per kode HS 6 digit, sekitar 6.900 jenis barang. Agar bisa dianalisis per "
                      "kelompok, setiap kode dipetakan dengan dua sumbu. Sumbu pertama, sifat barang: kode HS dipetakan ke "
                      "SITC Revisi 3, lalu ke definisi komoditas UNCTAD. Sumbu kedua, penggunaan: kode HS dipetakan ke BEC "
                      "Revisi 5, lalu ke kategori konsumsi, bahan baku, atau barang modal. Kode yang klasifikasinya berbeda "
                      "antar revisi HS tidak dipaksa masuk satu kelompok.")
    steps = [("1", "Kode HS-6", "Data ekspor-impor per kode 6 digit (sekitar 6.900 kode), Jan 2006–Agu 2026."),
             ("2", "Korespondensi UNSD", "Tabel resmi UNSD memetakan setiap HS-6 ke SITC Rev.3 dan BEC Rev.5, lintas revisi HS 1992–2022."),
             ("3", "Sumbu sifat barang", "SITC → definisi komoditas UNCTAD: SITC 0–4, 68, 667, 971 = komoditas; sisanya manufaktur."),
             ("4", "Sumbu penggunaan", "BEC5 → kategori SNA: konsumsi akhir, konsumsi antara (bahan baku), atau modal tetap."),
             ("5", "Konsensus antar revisi", "Kode dengan hasil berbeda antar revisi HS ditandai ~mixed~ dan dikeluarkan.")]
    for i, (n, hd, ds) in enumerate(steps):
        box(s, 44 + i * 176, 94, 168, 138, hd, ds, n)
    table(s, 44, 246, 520, [
        ["Contoh kode HS-6", "Sifat barang", "Penggunaan"],
        ["270112 Batu bara bituminus", "Komoditas energi & tambang", "Bahan baku"],
        ["260400 Bijih nikel", "Komoditas energi & tambang", "Bahan baku"],
        ["151110 CPO (minyak sawit mentah)", "Komoditas pertanian & pangan", "Bahan baku"],
        ["720260 Feronikel", "Manufaktur", "Bahan baku"],
        ["610910 Kaos katun", "Manufaktur", "Konsumsi"],
        ["847130 Laptop", "Manufaktur", "Barang modal"],
    ], [2.2, 2.0, 1.0], align=[L, L, L], size=11, row_h=30)
    pointers(s, [
        [("Cakupan tinggi: ", True, None), (f"kode ~mixed~ atau tidak terklasifikasi hanya {idn(mix_x, 1)}% nilai ekspor "
                                            f"(sumbu sifat barang) dan {idn(mix_m, 1)}% nilai impor (sumbu penggunaan).", False, None)],
        [("Catatan hilirisasi: ", True, None), ("feronikel (hasil olahan nikel) masuk manufaktur, bukan komoditas, mengikuti "
                                                "definisi UNCTAD.", False, None)],
        [("Dua sumbu tumpang tindih: ", True, None), ("batu bara adalah komoditas sekaligus bahan baku, sehingga pangsa antar "
                                                      "sumbu tidak dijumlahkan.", False, None)],
        [("Mengapa korespondensi resmi: ", True, None), ("memakai tabel UNSD membuat klasifikasi bisa direplikasi dan sebanding "
                                                         "dengan statistik internasional, bukan pilihan subjektif per kode.", False, None)],
    ], x=578, y=246, w=338, size=11)
    source(s, "UNSD (korespondensi HS–SITC3–BEC5), UNCTAD, ITC Trade Map; klasifikasi dikerjakan tim")

    s = content(prs, f"Tujuh kelompok barang: komoditas {idn(sh.loc['comm', 'share_x'], 0)}% ekspor; barang modal "
                     f"{idn(sh.loc['eu3', 'share_m'], 0)}% impor tetapi hanya {idn(sh.loc['eu3', 'share_x'], 0)}% ekspor",
                notes="Hasil pengelompokan: ekspor Indonesia didominasi komoditas, sedangkan impor didominasi manufaktur dan "
                      "bahan baku. Ketimpangan barang modal sangat mencolok: 13 persen dari impor tetapi hanya 2 persen dari "
                      "ekspor. Ini salah satu alasan depresiasi langsung memperburuk neraca: impor mesin tidak bisa "
                      "ditunda begitu saja.")
    table(s, 44, 96, 430, [
        ["Kelompok", "Aturan klasifikasi"],
        ["Komoditas (total)", "UNCTAD: SITC 0–4, 68, 667, 971"],
        ["  Energi & tambang", "Bahan bakar, bijih, logam nonferrous"],
        ["  Pertanian & pangan", "Pangan, minyak nabati, bahan mentah"],
        ["Manufaktur", "Nonkomoditas, SITC 5–8"],
        ["Barang konsumsi", "BEC5: konsumsi akhir"],
        ["Bahan baku/penolong", "BEC5: konsumsi antara"],
        ["Barang modal", "BEC5: pembentukan modal tetap"],
    ], [1.4, 2.0], align=[L, L], size=11.5, row_h=27)
    plabel(s, X2, 88, W2, "Pangsa tiap kelompok", [("(% total ekspor/impor ke dunia, 2006–2026)", False, None)])
    pic(s, fig_shares(), X2, 126, W2, 300)
    pointers(s, [
        "Ekspor didominasi komoditas; impor didominasi manufaktur dan bahan baku.",
        f"Barang modal {idn(sh.loc['eu3', 'share_m'], 0)}% impor tetapi {idn(sh.loc['eu3', 'share_x'], 0)}% ekspor: "
        "ketika rupiah melemah, tagihan impor mesin langsung naik tanpa penyeimbang dari sisi ekspor.",
        f"Secara kumulatif 2006–2026, komoditas mencatat surplus USD {idn(sh.loc['comm', 'tb_usdbn'], 0)} miliar, sedangkan "
        f"manufaktur defisit USD {idn(-sh.loc['noncomm', 'tb_usdbn'], 0)} miliar dan barang modal defisit USD "
        f"{idn(-sh.loc['eu3', 'tb_usdbn'], 0)} miliar.",
    ], y=322, w=430, size=11.5)
    pointers(s, [
        "Batang oranye = pangsa dalam ekspor, cokelat = pangsa dalam impor.",
        "Kelompok dengan batang oranye lebih panjang (komoditas, pertanian, konsumsi) adalah sumber surplus; sebaliknya "
        "manufaktur dan barang modal.",
    ], x=X2, y=352, w=W2, head="Cara membaca", size=11)
    source(s, "UNSD, ITC Trade Map; olahan penulis")

    cx_ = pvcov[pvcov.scope == "AGG10"].set_index("flow")["mean"]
    s = content(prs, "Dari nilai ke harga × volume: indeks unit value dari 6,7 juta observasi kuantitas HS-6",
                notes="Data nilai saja tidak bisa menjawab apakah neraca berubah karena harga atau karena jumlah barang. Karena itu "
                      "kami memakai data kuantitas HS-6 dari Trade Map. Untuk setiap barang dan mitra, nilai dibagi kuantitas "
                      "menghasilkan harga per kilogram. Harga ini dirangkum menjadi indeks Fisher yang diperbarui setiap tahun, "
                      "sama seperti indeks unit value BPS. Volume dihitung sebagai nilai dibagi harga. Hasilnya, rasio "
                      "ekspor/impor bisa dipecah persis menjadi terms of trade dan rasio volume.")
    numbered(s, [
        ("Unit value per barang",
         "Untuk tiap kode HS-6 dan mitra: nilai USD dibagi kuantitas (kg), yaitu harga rata-rata per kg barang itu di bulan itu."),
        ("Indeks harga Fisher berantai tahunan",
         "Harga tiap barang dibandingkan dengan rata-rata tahun sebelumnya, lalu dirata-rata dengan bobot nilai (Fisher = "
         "rata-rata Laspeyres dan Paasche), seperti indeks unit value BPS. ~Outlier~ (rasio harga di luar 1/4–4) dibuang."),
        ("Volume = nilai ÷ harga",
         "Hasilnya identitas: ln(X/M) = ln(Px/Pm) + ln(Qx/Qm). Perubahan neraca = perubahan ~terms of trade~ (harga) + "
         "perubahan rasio volume."),
    ], x=44, w=430, y0=92, step=104, desc=11.5, head=13)
    plabel(s, X2, 88, W2, "Indeks harga dan volume, Indonesia–10 mitra", [("(2006 = 100)", False, None)])
    pic(s, fig_pv_series(), X2, 126, W2, 282)
    pointers(s, [
        f"Cakupan: {idn(cx_['Export'], 0)}% nilai ekspor dan {idn(cx_['Import'], 0)}% nilai impor punya unit value valid; "
        "harga ekspor bergerak bersama BCOM (korelasi perubahan 12 bulan 0,86).",
        "Kuantitas hanya tersedia untuk 10 mitra (71% perdagangan), sehingga dekomposisi agregat memakai jumlah 10 mitra.",
        "Unit value per kg manufaktur ikut mencerminkan komposisi dan kualitas dalam ~long-run~; estimasi memakai perubahan "
        "sampai 24 bulan.",
    ], y=412, size=10.5, head="Catatan data")
    source(s, "ITC Trade Map (nilai dan kuantitas HS-6); IMF ~Export and Import Price Index Manual~ (2009); olahan penulis")

    s = content(prs, "Statistik deskriptif: variasi harga komoditas jauh lebih besar daripada variasi kurs riil",
                notes="Sebelum melihat episode depresiasi, ada satu fakta penting dari statistik deskriptif: ~standard deviation~ REER hanya sekitar 5 poin, "
                      "sedangkan BCOM 34 poin. Dengan kata lain, ~shock~ harga komoditas jauh lebih besar daripada "
                      "~shock~ kurs riil, sehingga wajar bila neraca lebih banyak digerakkan komoditas.")
    rows = [["Variabel", "N", "Rata-rata", "Std. dev.", "Min", "Maks", "Periode"]]
    fmtd = lambda v, d: idn(v, d) if abs(v) < 1000 else f"{v:,.0f}".replace(",", ".")
    for nm, r in sst.iterrows():
        d = 2 if r["mean"] < 10 else 1
        rows.append([nm, f"{int(r['count'])}", fmtd(r["mean"], d), fmtd(r["std"], d), fmtd(r["min"], d),
                     fmtd(r["max"], d), bln(r["periode"])])
    table(s, 44, 94, 590, rows, [2.4, 0.5, 0.9, 0.9, 0.8, 0.8, 1.7], size=10.5, row_h=23)
    plabel(s, 34, 292, 892, "Perkembangan variabel utama 2006–2026", [("(bulanan)", False, None)])
    pic(s, fig_stats_ts(), 34, 330, 892, 172)
    tbox(s, 648, 94, 270, 190, [
        [("Rasio X/M rata-rata 1,14 ", True, None), ("(surplus), dengan rentang lebar 0,85–1,93.", False, None)],
        [("REER relatif stabil: ", True, None), ("~standard deviation~ 5 poin, dibanding BCOM 34 poin.", False, None)],
        [("Rupiah melemah nominal dari Rp8.533 ke Rp18.011 per USD, ", True, None),
         ("tetapi REER hanya turun dari 113 ke 88 karena inflasi Indonesia lebih tinggi dari mitra.", False, None)],
    ], size=11.5, bullets=True, space=4)
    source(s, "ITC Trade Map, BIS, Bloomberg, CEIC; olahan penulis")


    # =========================================================================
    section(prs, "03", "Fakta awal",
            "Apa kata data sebelum model: delapan episode depresiasi rupiah 2007–2026")

    # neraca (USD miliar/bulan, rata-rata 3 bulan) di awal episode dan 12 bulan kemudian
    tbm = ((agg.exports_usdk - agg.imports_usdk) / 1e6).set_axis(agg.mdate)
    tb0, tb12 = [], []
    for r in E.itertuples():
        i = tbm.index.get_indexer([pd.to_datetime(r.mulai, format="%b %Y")], method="nearest")[0]
        tb0.append(tbm.iloc[i:i + 3].mean()); tb12.append(tbm.iloc[i + 12:i + 15].mean())
    E["tb0"], E["tb12"] = tb0, tb12
    n_up = int((E.tb12 > E.tb0).sum())
    big2 = E.nlargest(2, "dep_idr_usd")
    s = content(prs, f"Delapan episode depresiasi 2007–2026: rupiah melemah {idn(E.dep_idr_usd.min(), 0)}–"
                     f"{idn(E.dep_idr_usd.max(), 0)}%, tetapi neraca hanya membaik di {n_up} dari 8 episode",
                notes="Slide ini menempatkan tiga seri dalam satu sumbu waktu. Panel A adalah kurs rupiah per USD dengan delapan "
                      "episode depresiasi yang diarsir. Panel B adalah neraca perdagangan, yaitu ekspor dikurangi impor, dalam "
                      "USD miliar per bulan. Panel C adalah harga komoditas dunia. Kalau depresiasi memperbaiki neraca, panel B "
                      "seharusnya naik setiap kali area arsir muncul. Kenyataannya tidak begitu. Dua depresiasi terbesar, 2008 "
                      "dan 2013, justru diikuti surplus yang menyusut tajam, sedangkan surplus terbesar pada 2021–2022 muncul "
                      "ketika harga komoditas melonjak. Tabel di kanan merangkum hal yang sama dalam angka: neraca di awal "
                      "episode dibandingkan dengan neraca setahun kemudian. Dari sini muncul dugaan awal bahwa neraca lebih "
                      "mengikuti harga komoditas daripada kurs, dan dugaan inilah yang diuji di bagian berikutnya.")
    plabel(s, X1, 88, 566, "Kurs rupiah, neraca perdagangan, dan harga komoditas (BCOM)",
           [("(arsir oranye = episode depresiasi; neraca = ekspor − impor, rata-rata 12 bulan)", False, None)])
    pic(s, fig_timeline(), X1, 126, 566, 384)
    rows = [["Episode", "Depr.", "Neraca awal → +12 bln"]]
    for r in E.itertuples():
        up = r.tb12 > r.tb0
        rows.append([r.episode.replace("Komoditas jatuh", "Komod. jatuh").replace("Normalisasi", "Normal.")
                      .replace("Pengetatan", "Pengetat."),
                     f"+{idn(r.dep_idr_usd, 0)}%",
                     (f"{idn(r.tb0)} → {idn(r.tb12)}", DARKOR if up else BROWN)])
    table(s, 610, 94, 308, rows, [1.55, 0.6, 1.3], size=10, row_h=21)
    note(s, "Neraca = ekspor − impor, USD miliar/bulan, rata-rata 3 bulan. Episode: mulai di titik terendah Rp/USD sebelum "
            "rupiah melemah ≥10%; selesai di puncak sebelum menguat kembali ≥5%.", y=286, h=44, x=610, w=308)
    pointers(s, [
        [("Neraca membaik hanya di " + f"{n_up} dari 8 episode ", True, None),
         ("(angka oranye). Dua depresiasi terbesar, " + " dan ".join(big2.episode) + ", justru diikuti surplus yang menyusut "
          f"tajam ({idn(big2.tb0.iloc[0])} → {idn(big2.tb12.iloc[0])} dan {idn(big2.tb0.iloc[1])} → {idn(big2.tb12.iloc[1])}).",
          False, None)],
        [("Panel B mengikuti panel C, bukan panel A: ", True, None),
         ("surplus terbesar (2021–22) muncul saat harga komoditas melonjak; defisit 2012–14 dan 2018–19 muncul di tengah "
          "atau sesudah depresiasi.", False, None)],
    ], x=610, y=334, w=308, size=10.5)
    source(s, "BIS (kurs); ITC Trade Map (neraca); Bloomberg (BCOM); identifikasi episode oleh penulis")

    # ---- episode vs permintaan mitra dan PDB Indonesia
    am_ = agg.set_index("mdate")
    gdp_g, ipi_ = am_.lngdp_idn.diff(12) * 100, am_.yf_avg
    d_ipi, d_gdp = [], []
    for r in E.itertuples():
        i = am_.index.get_indexer([pd.to_datetime(r.mulai, format="%b %Y")], method="nearest")[0]
        d_ipi.append(ipi_.iloc[i + 12:i + 15].mean() - ipi_.iloc[i:i + 3].mean())
        d_gdp.append(gdp_g.iloc[i + 12:i + 15].mean() - gdp_g.iloc[i:i + 3].mean())
    E["dipi"], E["dgdp"] = d_ipi, d_gdp
    n_slow = int((E.dipi < 0).sum())
    best, worst_ = E.loc[E.d_xm_12m.idxmax()], E.loc[E.d_xm_12m.idxmin()]
    s = content(prs, f"Episode yang sama dari sisi permintaan: IPI mitra melambat di {n_slow} dari 8 episode, dan neraca "
                     "lebih mengikuti PDB Indonesia daripada kurs",
                notes="Slide sebelumnya membandingkan kurs dengan neraca dan harga komoditas. Slide ini memakai episode yang sama, "
                      "tetapi melihat sisi permintaan: ekspor dan impor secara terpisah, produksi industri di sepuluh negara mitra, "
                      "dan pertumbuhan ekonomi Indonesia. Ada dua pola. Pertama, depresiasi rupiah sering datang bersamaan dengan "
                      "perlambatan ekonomi mitra, seperti pada 2008, 2013, 2015, dan 2022. Pada saat seperti itu permintaan atas "
                      "ekspor kita memang sedang turun, sehingga kurs yang melemah tidak banyak membantu. Kedua, perubahan neraca "
                      "terbesar justru mengikuti ekonomi domestik. Pada 2020 rasio ekspor/impor naik tajam karena impor anjlok "
                      "ketika PDB Indonesia terkontraksi, bukan karena ekspor naik. Sebaliknya pada 2008 impor melonjak karena "
                      "ekonomi domestik tumbuh tinggi. Artinya, untuk mengukur efek kurs, permintaan mitra dan PDB domestik harus "
                      "dikontrol di model.")
    plabel(s, X1, 88, 566, "Episode depresiasi vs ekspor-impor, permintaan mitra, PDB, dan kurs riil",
           [("(arsir oranye = episode depresiasi)", False, None)])
    pic(s, fig_timeline_macro(), X1, 126, 566, 384)
    rows = [["Episode", "Δ X/M", "Δ IPI mitra", "Δ PDB"]]
    for r in E.itertuples():
        rows.append([r.episode.replace("Komoditas jatuh", "Komod. jatuh").replace("Normalisasi", "Normal.")
                      .replace("Pengetatan", "Pengetat."),
                     (idn(r.d_xm_12m, 0), DARKOR if r.d_xm_12m > 0 else BROWN),
                     (idn(r.dipi, sign=True), BROWN if r.dipi < 0 else "000000"),
                     (idn(r.dgdp, sign=True), BROWN if r.dgdp < 0 else "000000")])
    table(s, 610, 94, 308, rows, [1.55, 0.6, 0.85, 0.7], size=10, row_h=21)
    note(s, "12 bulan setelah awal episode. Δ X/M = % rasio ekspor/impor; Δ IPI mitra dan Δ PDB = perubahan pertumbuhan yoy "
            "(poin persen); cokelat = turun.", y=286, h=44, x=610, w=308)
    pointers(s, [
        [(f"Depresiasi datang bersama perlambatan global: ", True, None),
         (f"pertumbuhan IPI mitra turun di {n_slow} dari 8 episode, sehingga permintaan ekspor sedang lemah saat rupiah "
          "melemah.", False, None)],
        [("Neraca mengikuti ekonomi domestik: ", True, None),
         (f"perbaikan terbesar ({best.episode}, {idn(best.d_xm_12m, 0, sign=True)}%) datang dari impor yang anjlok saat PDB "
          f"turun {idn(abs(best.dgdp))} poin; kemerosotan terbesar ({worst_.episode}, {idn(worst_.d_xm_12m, 0)}%) saat impor "
          f"melonjak {idn(worst_.d_m_12m, 0)}%.", False, None)],
    ], x=610, y=334, w=308, size=10.5)
    source(s, "ITC Trade Map (ekspor-impor); CEIC (IPI mitra); BPS (PDB); BIS (REER); identifikasi episode oleh penulis")

    s = content(prs, f"Setelah depresiasi, rasio ekspor/impor rata-rata {idn(ep_mean)}% dalam 12 bulan, tidak lebih baik "
                     f"daripada bulan biasa ({idn(bench)}%)",
                notes="Slide sebelumnya memperlihatkan polanya secara visual; slide ini mengujinya dengan cara paling sederhana, tanpa "
                      "model. Kami mengindeks rasio ekspor/impor ke 100 di awal "
                      "setiap episode, lalu melihat pergerakannya. Garis cokelat adalah rata-rata delapan episode; area abu-abu "
                      "adalah ~interquartile range~, yaitu rentang tempat separuh episode berada. Bila teori benar, garis seharusnya naik ke zona "
                      "oranye setelah beberapa bulan. Kenyataannya garis turun dan di bulan ke-12 berada di bawah titik "
                      "pembanding bulan biasa. Tabel di kanan memperlihatkan bahwa arah perubahan neraca lebih mirip arah "
                      "harga komoditas daripada besarnya depresiasi.")
    plabel(s, X1, 88, W1, "Rasio ekspor/impor di sekitar episode depresiasi", [("(indeks, awal episode = 100)", False, None)])
    pic(s, fig_event(bench), X1, 126, W1, 290)
    rows = [["Episode", "Δ ekspor", "Δ impor", "Δ rasio X/M", "Δ BCOM"]]
    for r in E.itertuples():
        rows.append([r.episode, idn(r.d_x_12m), idn(r.d_m_12m),
                     (idn(r.d_xm_12m), DARKOR if r.d_xm_12m > 0 else BROWN), idn(r.d_bcom_12m)])
    rows.append(["Rata-rata 8 episode", idn(E.d_x_12m.mean()), idn(E.d_m_12m.mean()), idn(ep_mean), idn(E.d_bcom_12m.mean())])
    table(s, X2, 94, W2, rows, [2.1, 0.9, 0.9, 1.1, 0.9], size=10.5, row_h=21, hl_rows=(len(rows) - 1,))
    pointers(s, [
        [("Tabel: ", True, None), ("perubahan 12 bulan setelah awal episode (%). Rasio X/M naik di episode 2020 dan "
                                   "2024–26, turun di 2008 dan 2013, meskipun depresiasinya sama-sama besar.", False, None)],
        [("Uji Marshall-Lerner deskriptif: ", True, None),
         ("garis rata-rata tidak pernah naik ke zona membaik dan tidak membentuk huruf J; konsisten dengan "
          "|εX| + |εM| < 1.", False, None)],
    ], x=X2, y=312, w=W2, size=11.5)
    note(s, "Δ = perubahan log ×100 antara rata-rata 3 bulan di awal episode dan rata-rata 3 bulan 12 bulan kemudian, "
            "sehingga ~seasonality~ saling meniadakan.", y=468, h=30, w=430)
    source(s, "ITC Trade Map (HS-6), BIS, Bloomberg; olahan penulis")

    s = content(prs, f"Harga komoditas menjelaskan {idn(dr[('Ekspor', 'Harga komoditas (BCOM)')], 0)}% variasi ekspor, "
                     f"sedangkan depresiasi hanya {idn(dr[('Ekspor', 'Depresiasi riil (REER)')], 0)}%",
                notes="Kalau bukan kurs, lalu apa yang menggerakkan neraca? Grafik kiri mengukur seberapa besar setiap faktor menjelaskan naik-turunnya ekspor, impor, dan rasio "
                      "ekspor/impor dalam 12 bulan. R-squared 70 persen artinya 70 persen naik-turunnya ekspor sejalan dengan "
                      "naik-turunnya harga komoditas. Depresiasi hampir tidak menjelaskan apa pun. Namun karena harga komoditas "
                      "menaikkan ekspor dan impor sekaligus, efeknya ke rasio saling meniadakan. Untuk rasio, faktor terkuat "
                      "justru pertumbuhan ekonomi domestik: saat ekonomi tumbuh, impor ikut naik.")
    plabel(s, X1, 88, W1, "Keeratan tiap faktor dengan ekspor, impor, rasio X/M",
           [("(R², perubahan 12 bulan, 2007–2026; oranye = depresiasi)", False, None)])
    pic(s, fig_drivers(), X1, 130, W1, 258)
    plabel(s, X2, 88, W2, "Dua hubungan kunci dalam satu gambar", [("(tiap titik = satu bulan; perubahan 12 bulan, persen)", False, None)])
    pic(s, fig_scatter(), X2, 130, W2, 258)
    pointers(s, [
        [("Cara membaca R²: ", True, None), ("70% berarti naik-turunnya ekspor hampir selalu sejalan dengan faktor itu; di "
                                             "bawah 5% berarti hampir tidak ada hubungan. Titik di kanan: makin rapat ke garis, "
                                             "makin erat hubungannya.", False, None)],
        [("Harga komoditas menggerakkan ekspor dan impor sekaligus ", True, None),
         (f"(R² {idn(dr[('Ekspor', 'Harga komoditas (BCOM)')], 0)}% dan {idn(dr[('Impor', 'Harga komoditas (BCOM)')], 0)}%), "
          "sehingga efeknya ke rasio X/M saling meniadakan. Karena itu harga komoditas wajib dikontrol di semua model.", False, None)],
        [("Untuk rasio X/M, PDB domestik paling berpengaruh ", True, None),
         (f"(R² {idn(dr[('Rasio X/M', 'PDB riil Indonesia')], 0)}%): ekonomi tumbuh, impor naik. Depresiasi hanya "
          f"{idn(dr[('Rasio X/M', 'Depresiasi riil (REER)')], 0)}%, dengan tanda negatif.", False, None)],
    ], y=394, size=11)
    source(s, "ITC Trade Map, BIS, Bloomberg, CEIC, BPS; olahan penulis")

    hm, piv_m = fig_heat(ep_m, ["CHN", "JPN", "THA", "MYS", "SGP", "KOR", "AUS", "IND", "VNM", "USA"], CTRY,
                         "heat_mitra", (5.6, 3.75))
    worst = piv_m["Rata-rata"].sort_values()
    s = content(prs, f"Per mitra: setelah depresiasi, neraca dengan {CTRY[worst.index[0]]} dan {CTRY[worst.index[1]]} "
                     "rata-rata paling memburuk",
                notes="Rata-rata agregat bisa menyembunyikan perbedaan antar mitra, jadi polanya kami pecah. Setiap sel menunjukkan "
                      "perubahan rasio ekspor/impor dengan satu mitra, 12 bulan setelah awal satu "
                      "episode depresiasi. Warna cokelat berarti memburuk, oranye berarti membaik. Kolom terakhir adalah "
                      "rata-rata. Polanya tidak seragam: mitra yang sama bisa membaik di satu episode dan memburuk di "
                      "episode lain, karena ikut terbawa siklus komoditas dan permintaan mitra. Itulah mengapa kita butuh "
                      "model yang bisa memisahkan efek kurs dari ~common shock~.")
    plabel(s, 34, 88, 570, "Perubahan rasio X/M bilateral 12 bulan setelah awal episode",
           [("(persen; baris diurutkan dari rata-rata paling memburuk)", False, None)])
    pic(s, hm, 34, 126, 570, 380)
    pb = pointers(s, [
        "Satu sel = perubahan rasio ekspor/impor dengan satu mitra, 12 bulan setelah satu episode dimulai.",
        "Cokelat = memburuk, oranye = membaik; makin pekat makin besar. Kolom terakhir (tebal) = rata-rata 8 episode.",
    ], x=616, y=94, w=300, head="Cara membaca", size=11)
    pointers(s, [
        f"{CTRY[worst.index[0]]} dan {CTRY[worst.index[1]]} rata-rata paling memburuk "
        f"({idn(worst.iloc[0], 0)}% dan {idn(worst.iloc[1], 0)}%).",
        "Mitra yang sama bisa membaik di satu episode dan memburuk di episode lain, mengikuti siklus komoditas dan "
        "permintaan mitra.",
        "Karena itu efek bilateral perlu dipisahkan dari ~common shock~ lewat local projections dengan ~fixed effects~ "
        "bulan (bagian 05).",
    ], x=616, y=pb.top / 12700 + pb.height / 12700 + 8, w=300, size=11)
    source(s, "ITC Trade Map; olahan penulis")

    hg, piv_g = fig_heat(ep_g, ["sec2", "comm", "eu3", "eu2", "eu1", "noncomm", "sec1"], GRP, "heat_kelompok", (5.6, 3.5))
    gw = piv_g["Rata-rata"].sort_values()
    s = content(prs, f"Per kelompok: {GRP[gw.index[0]].lower()} paling memburuk setelah depresiasi; "
                     f"{GRP[gw.index[-1]].lower()} rata-rata paling membaik",
                notes="Pecahan yang sama, kali ini per kelompok barang untuk perdagangan Indonesia dengan "
                      "dunia. Barang modal hampir selalu memburuk: Indonesia tetap mengimpor mesin walaupun rupiah melemah. "
                      "Komoditas bergerak mengikuti harga dunia, bukan kurs. Pertanian dan pangan rata-rata paling membaik.")
    plabel(s, 34, 88, 570, "Perubahan rasio X/M per kelompok 12 bulan setelah awal episode",
           [("(persen, Indonesia–dunia; baris diurutkan dari rata-rata paling memburuk)", False, None)])
    pic(s, hg, 34, 126, 570, 360)
    pb = pointers(s, [
        [("Barang modal: ", True, None), ("hampir selalu memburuk; impor mesin tidak berkurang saat rupiah melemah.", False, None)],
        [("Komoditas: ", True, None), ("arah mengikuti harga dunia (lihat Δ BCOM per episode di slide sebelumnya), bukan "
                                       "kurs.", False, None)],
        [("Pertanian & pangan: ", True, None), ("satu-satunya kelompok yang rata-rata membaik cukup jelas.", False, None)],
    ], x=616, y=94, w=300, size=11)
    pointers(s, [
        [("Yang belum terjawab: ", True, None),
         ("pola ini masih bercampur dengan harga komoditas dan permintaan dunia. Bagian 04 menjelaskan cara memisahkan "
          "efek kurs dari faktor-faktor itu.", False, None)],
    ], x=616, y=pb.top / 12700 + pb.height / 12700 + 8, w=300, head="Jembatan ke metode", size=11)
    note(s, "Kelompok saling tumpang tindih (sifat barang vs penggunaan); lihat slide klasifikasi HS-6.", y=492, h=20, w=570)
    source(s, "ITC Trade Map (HS-6), UNSD; olahan penulis")


    # =========================================================================
    section(prs, "04", "Metodologi",
            "Bagaimana memisahkan efek kurs dari harga komoditas dan ~global shock~?")

    s = content(prs, "Tahapan analisis: delapan langkah dari data mentah sampai ~robustness check~",
                notes="Sebelum masuk ke rumus, slide ini memperlihatkan seluruh tahapan riset dari awal sampai akhir, supaya "
                      "tidak ada langkah yang terasa melompat. Baris atas adalah persiapan. Kami mengumpulkan data, "
                      "mengelompokkan ribuan kode barang, membangun indeks harga dan volume, lalu melihat pola di data mentah "
                      "tanpa model. Baris bawah adalah estimasi. Kami mulai dari ~unit root test~ untuk memastikan ARDL boleh "
                      "dipakai, lalu mengestimasi ARDL sebagai model utama dan local projections sebagai pembanding. Setelah "
                      "itu respons neraca dipecah menjadi harga dan volume, dan seluruh hasil diuji ulang dengan berbagai "
                      "asumsi. Setiap tahap memakai hasil tahap sebelumnya.")
    wf = [("1", "Kumpulkan data", "Nilai dan kuantitas HS-6 (ITC Trade Map), kurs dan CPI (BIS), komoditas (Bloomberg), "
                                  "IPI mitra (CEIC), PDB (BPS). Bagian 02."),
          ("2", "Kelompokkan barang", "6.883 kode HS-6 dipetakan ke 7 kelompok lewat korespondensi resmi UNSD: sifat barang "
                                      "dan penggunaan."),
          ("3", "Bangun indeks harga & volume", "~Unit value~ per HS-6 dan mitra, dirangkum menjadi indeks Fisher; "
                                                "volume = nilai ÷ harga."),
          ("4", "Lihat data tanpa model", "8 episode depresiasi, neraca sebelum-sesudah, dan faktor penggerak ekspor-impor. "
                                          "Bagian 03."),
          ("5", "~Unit root test~", "ADF dan PP memastikan tidak ada variabel I(2), syarat ARDL ~bounds test~. "
                                    "Hasil di bagian 06."),
          ("6", "Estimasi ARDL", "~Bounds test~, koefisien ~long-run~, dan ~dynamic multiplier~ bulan 0–24 untuk dunia, "
                                 "mitra, dan kelompok."),
          ("7", "Local projections", "Satu regresi per bulan; versi panel memakai ~fixed effects~ bulan untuk menyerap "
                                     "~common shock~."),
          ("8", "Dekomposisi & ~robustness~", "Respons dipecah menjadi harga vs volume; 11 spesifikasi alternatif, NARDL, "
                                              "PMG/MG, LP-IV.")]
    for i, (n, hd, ds) in enumerate(wf):
        box(s, 44 + (i % 4) * 220, 92 + (i // 4) * 140, 212, 132, hd, ds, n, dy=56, dsize=11,
            accent=BROWN if i < 4 else DARKOR)
    tbox(s, 44, 368, 400, 18, [[("Persiapan (1–4)", True, BROWN), ("   ·   ", False, GREY),
                                ("Estimasi dan pengujian (5–8)", True, DARKOR)]], size=11)
    pointers(s, [
        [("Satu satuan untuk semua hasil: ", True, None),
         ("koefisien dari langkah 6–8 diubah menjadi % perubahan rasio ekspor/impor bila rupiah melemah riil 10% (lihat slide "
          "\"Dari koefisien ke angka\"), sehingga ARDL, LP, dan dekomposisi bisa dibandingkan langsung.", False, None)],
        [("Mengapa dua metode estimasi: ", True, None),
         ("ARDL membuat hasil sebanding dengan studi Indonesia sebelumnya; local projections memeriksa apakah kesimpulannya "
          "bertahan tanpa asumsi hubungan ~long-run~ yang tetap.", False, None)],
    ], y=392, head="", size=11)
    source(s, "Olahan penulis")

    s = content(prs, "Mengapa dua model: ARDL dan local projections menjawab pertanyaan yang berbeda",
                notes="Fakta awal tadi masih bercampur dengan harga komoditas dan permintaan dunia, sehingga kita butuh model "
                      "untuk memisahkan efek kurs. Kami memakai dua model karena masing-masing menjawab pertanyaan yang berbeda. "
                      "ARDL menjawab apakah ada hubungan long-run antara kurs dan neraca, berapa besarnya, dan seberapa cepat "
                      "neraca kembali ke keseimbangan. Inilah ukuran Marshall-Lerner, dan ARDL adalah standar di literatur "
                      "J-curve, termasuk studi Indonesia, sehingga hasil kami bisa dibandingkan. Kelemahannya, seluruh jalur "
                      "respons diturunkan dari satu persamaan; bila persamaan itu keliru, seluruh jalurnya ikut keliru. Local "
                      "projections menjawab pertanyaan yang lebih langsung: setelah rupiah melemah, berapa perubahan neraca satu "
                      "bulan kemudian, enam bulan kemudian, setahun kemudian, dan seterusnya. Setiap bulan diestimasi terpisah, "
                      "sehingga bentuk J tidak dipaksakan maupun dihalangi. Versi panelnya membandingkan sepuluh mitra pada bulan "
                      "yang sama, sehingga global shock seperti harga komoditas terserap. Kesimpulan kami hanya dianggap kuat "
                      "bila muncul di kedua model.")
    table(s, 44, 92, 872, [
        ["", "ARDL (model utama)", "Local projections (pembanding)"],
        ["Pertanyaan yang dijawab", "Adakah hubungan ~long-run~ antara kurs riil dan neraca, berapa besarnya, dan seberapa cepat "
                                    "neraca kembali ke ~equilibrium~?",
         "Bagaimana neraca bergerak bulan demi bulan (0–24) setelah rupiah melemah, tanpa memaksakan bentuk hubungan?"],
        ["Cara kerja", "Satu persamaan: neraca dijelaskan nilai masa lalunya, kurs, dan kontrol; jalur 24 bulan diturunkan dari "
                       "koefisien (~dynamic multiplier~)",
         "25 regresi terpisah, satu untuk tiap bulan h; koefisien tiap regresi langsung menjadi satu titik di grafik"],
        ["Dipakai untuk", "Uji Marshall-Lerner (efek ~long-run~), elastisitas volume ekspor-impor, RQ3 per kelompok",
         "Uji J-curve (jalur bulanan), RQ2 per mitra dengan kurs bilateral, dekomposisi harga vs volume"],
        ["Kelebihan", "Standar literatur J-curve sehingga sebanding dengan studi Indonesia; sah untuk campuran I(0)/I(1)",
         "Tetap valid bila model kurang tepat; ~confidence interval~ per bulan; panel dengan ~fixed effects~ bulan menyerap "
         "~global shock~"],
        ["Keterbatasan", "~Single equation~ rawan ~endogeneity~; bila hubungan ~long-run~ keliru, seluruh jalur ikut keliru",
         "Lebih ~noisy~ di horizon jauh; tidak memberi satu angka ~long-run~"],
        ["Rujukan", "Pesaran, Shin & Smith (2001); Bahmani-Oskooee & Brooks (1999); Kripfganz & Schneider (2020)",
         "Jordà (2005); Plagborg-Møller & Wolf (2021); Montiel Olea & Plagborg-Møller (2021)"],
    ], [1.3, 3.0, 3.0], align=[L, L, L], size=10.5, row_h=44)
    pointers(s, [
        [("Aturan membaca hasil: ", True, None),
         ("kesimpulan dianggap kuat hanya bila muncul di kedua model; hasil yang hanya muncul di satu model ditandai belum "
          "robust.", False, None)],
        [("Metode pendukung: ", True, None),
         ("NARDL untuk ~asymmetry~ depresiasi vs apresiasi (Shin dkk. 2014), panel PMG/MG untuk efek ~long-run~ lintas mitra "
          "(Pesaran dkk. 1999), LP-IV dengan indeks dolar AS (dicoba, ~weak instrument~). VECM Johansen tidak dipakai karena "
          "ln(X/M) ~stationary~.", False, None)],
    ], y=410, head="", size=10.5)
    source(s, "Lihat notes/4_litrev_metode.md untuk daftar pustaka lengkap")

    s = content(prs, "Local projections secara intuitif: satu regresi untuk setiap bulan setelah rupiah melemah",
                notes="Local projections mungkin terdengar teknis, tetapi idenya sederhana. Kita ingin tahu: kalau rupiah melemah "
                      "bulan ini, apa yang terjadi pada neraca bulan ini, enam bulan lagi, setahun lagi, sampai dua tahun lagi. "
                      "Untuk menjawabnya, kami menjalankan satu regresi untuk setiap jarak waktu. Regresi pertama melihat "
                      "perubahan neraca di bulan yang sama, regresi berikutnya satu bulan kemudian, dan seterusnya sampai 24 "
                      "bulan. Setiap regresi membandingkan bulan-bulan ketika rupiah melemah dengan bulan-bulan lain yang "
                      "kondisinya serupa: harga komoditas, permintaan mitra, dan musimnya sama. Koefisien dari tiap regresi "
                      "adalah satu titik di grafik bawah. Kalau titik-titik itu dirangkai, kita mendapat jalur respons neraca. "
                      "Karena tiap bulan diestimasi sendiri, bentuk J tidak dipaksakan: kalau J-curve memang ada, ia akan "
                      "terlihat dengan sendirinya. Area arsir menunjukkan ketidakpastian; kalau seluruh arsir di bawah nol, "
                      "penurunan itu signifikan.")
    pic(s, fig_lp_intuition(), X1, 88, W1, 420)
    numbered(s, [
        ("Pertanyaannya",
         "Bila rupiah melemah riil 10% di bulan t, berapa beda rasio X/M h bulan kemudian, dibanding bulan lain dengan harga "
         "komoditas, permintaan mitra, dan musim yang sama?"),
        ("Satu regresi per bulan",
         "Untuk h = 0, 1, …, 24: perubahan rasio X/M dari t−1 ke t+h diregresikan pada depresiasi di t plus kontrol. "
         "Koefisiennya, bh, adalah efek di bulan ke-h."),
        ("Rangkai menjadi grafik",
         "25 koefisien diplot berurutan menjadi ~impulse response~. Arsir = 90% ~confidence interval~: bila seluruhnya di "
         "bawah nol, penurunan signifikan."),
    ], x=X2, w=W2, y0=92, step=96, desc=11.5, head=13)
    pointers(s, [
        [("Mengapa perlu, padahal sudah ada ARDL: ", True, None),
         ("ARDL menurunkan jalur dari satu persamaan; LP mengukur tiap bulan langsung, sehingga J-curve tidak dipaksakan "
          "maupun dihalangi. Versi panel membandingkan 10 mitra di bulan yang sama, sehingga ~global shock~ terserap.",
          False, None)],
    ], x=X2, y=384, w=W2, head="", size=11)
    source(s, "Jordà (2005); estimasi penulis")

    s = content(prs, "Daftar variabel: 14 seri bulanan Jan 2006–Jun 2026 dari 8 sumber resmi",
                notes="Tabel ini adalah peta bahan baku riset. Semua seri bulanan, dari 2006 sampai pertengahan 2026. Cara "
                      "membacanya dari atas ke bawah. Empat baris pertama adalah yang ingin kita jelaskan: neraca dengan dunia, "
                      "dengan tiap mitra, per kelompok barang, serta harga dan volumenya. Dua baris berikutnya adalah variabel "
                      "utama, yaitu kurs riil: REER untuk level agregat dan kurs riil bilateral untuk tiap mitra. Kurs riil "
                      "dipakai, bukan kurs nominal, karena yang menentukan daya saing adalah harga relatif setelah inflasi. "
                      "Sisanya adalah kontrol: harga komoditas, permintaan mitra, dan PDB Indonesia, karena ketiganya ikut "
                      "menggerakkan ekspor dan impor. Kalau tidak dikontrol, efeknya bisa keliru terbaca sebagai efek kurs. "
                      "Batu bara dan CPO dipakai khusus untuk kelompok energi dan pertanian. JISDOR, indeks IMF, dan indeks "
                      "dolar AS hanya dipakai untuk ~robustness check~ dan sebagai ~instrument~.")
    table(s, 44, 92, 872, [
        ["Variabel", "Notasi", "Definisi dan transformasi", "Sumber", "Periode", "Dipakai di"],
        ["Neraca Indonesia–dunia", "ln(X/M)", "ln ekspor/impor (USD ribu), baris TOTAL HS-6", "ITC Trade Map", "Jan 06–Agu 26", "RQ1"],
        ["Neraca bilateral", "ln(Xi/Mi)", "Idem, 10 mitra", "ITC Trade Map", "Jan 06–Agu 26", "RQ2"],
        ["Neraca per kelompok", "ln(Xg/Mg)", "Idem, 7 kelompok HS-6 (UNSD HS–SITC3–BEC5)", "ITC Trade Map; UNSD", "Jan 06–Agu 26", "RQ3"],
        ["Harga & volume", "Px, Pm, Qx, Qm", "Unit value Fisher (USD/kg per HS-6); volume = nilai ÷ harga",
         "ITC Trade Map (kuantitas)", "Jan 06–Agu 26", "Dekomposisi"],
        ["Kurs riil efektif", "ln q", "REER broad, 2020=100, naik = apresiasi", "BIS", "Jan 06–Sep 26", "ARDL, LP agregat"],
        ["Kurs riil bilateral", "reri", "ln(Rp/mata uang i) + ln CPIi − ln CPIIDN", "BIS (kurs, CPI)", "Jan 06–Okt 26", "LP panel"],
        ["Kurs nominal", "ln JISDOR", "Rp/USD, rata-rata hari kerja", "Bank Indonesia", "Jun 13–Okt 26", "~Robustness~"],
        ["Harga komoditas", "ln P", "Bloomberg Commodity Index (BCOM), rata-rata bulanan", "Bloomberg", "Jan 06–Jun 26", "Semua model"],
        ["Harga batu bara", "ln Pcoal", "Newcastle, rata-rata bulanan", "Bloomberg", "Jan 09–Jun 26", "RQ3 energi"],
        ["Harga CPO", "ln Pcpo", "Kontrak terdekat, rata-rata bulanan", "Bloomberg", "Jan 06–Jun 26", "RQ3 pertanian"],
        ["Permintaan mitra", "Y*", "IPI yoy, tertimbang pangsa ekspor 10 mitra", "CEIC", "Jan 06–Agu 26", "Semua model"],
        ["PDB riil Indonesia", "ln Y", "Indeks 2015=100, interpolasi bulanan", "BPS", "Mar 06–Jun 26", "~Robustness~"],
        ["Indeks dolar AS", "ln USD", "~Broad dollar index~, rata-rata bulanan", "Federal Reserve", "Jan 06–Okt 26", "Instrumen LP-IV"],
        ["Indeks komoditas IMF", "ln PIMF", "~All commodities~, 2016=100", "IMF", "Jan 06–Sep 26", "~Robustness~"],
    ], [1.6, 0.85, 2.7, 1.35, 1.05, 1.15], align=[L, L, L, L, L, L], size=10, row_h=21.5)
    pointers(s, [
        [("Peran tiap variabel: ", True, None),
         ("rasio ekspor/impor adalah ~dependent variable~; kurs riil adalah variabel utama (REER untuk agregat, kurs riil "
          "bilateral untuk mitra). Harga komoditas, permintaan mitra, dan PDB dikontrol karena ikut menggerakkan ekspor-impor; "
          "tanpa kontrol, efeknya keliru terbaca sebagai efek kurs. JISDOR, indeks IMF, dan dolar AS hanya untuk ~robustness "
          "check~ dan ~instrument~.", False, None)],
        [("Sampel: ", True, None),
         ("estimasi efektif Jan 2007–Jun 2026 (12 bulan pertama terpakai untuk lag; akhir sampel dibatasi data BCOM). "
          "~Dummy~: ~seasonal~ (11 bulan), krisis global Okt 2008–Jun 2009, COVID Mar–Agu 2020.", False, None)],
    ], y=422, head="", size=10.5)
    source(s, "ITC Trade Map, BIS, Bank Indonesia, Bloomberg, CEIC, BPS, Federal Reserve, IMF")

    s = content(prs, "~Model specification~: ARDL bentuk ~error correction~ dan local projections per horizon",
                notes="Model pertama, ARDL, menjelaskan perubahan neraca bulan ini dengan dua bagian: seberapa jauh neraca "
                      "menyimpang dari ~long-run equilibrium~nya bulan lalu, dan perubahan kurs serta kontrol di bulan-"
                      "bulan terakhir. Model kedua, local projections, menjalankan satu regresi untuk setiap horizon 0 sampai "
                      "24 bulan, sehingga setiap titik di grafik respons adalah satu regresi tersendiri.")
    tbox(s, 44, 94, 430, 120, [
        {"runs": [("Model 1 · ARDL (bentuk ~error correction~)", True, "000000")], "size": 13.5},
        {"runs": "Δln(X/M)t = α + φ[ln(X/M)t−1 − θ1 ln qt−1 − θ2 ln Pt−1 − θ3 Y*t−1] + Σ βj Δln qt−j + Σ γj ΔZt−j "
                 "+ ~seasonal~ + ~dummy~ krisis + εt", "size": 12},
        {"runs": [("q", True, None), (" = REER (naik = apresiasi)   ", False, None), ("P", True, None),
                  (" = harga komoditas   ", False, None), ("Y*", True, None), (" = IPI mitra", False, None)], "size": 11.5},
        {"runs": [("Marshall-Lerner: ", True, None), ("θ1 < 0 dan signifikan.   ", False, None),
                  ("J-curve: ", True, None), ("respons awal negatif lalu positif.", False, None)], "size": 11.5},
    ], fill=CREAM, inset=10, space=5)
    tbox(s, 492, 94, 428, 120, [
        {"runs": [("Model 2 · Local projections", True, "000000")], "size": 13.5},
        {"runs": "Agregat: ln(X/M)t+h − ln(X/M)t−1 = αh + bh Δdept + Σ lag + kontrol + εt+h", "size": 12},
        {"runs": "Panel: ln(X/M)i,t+h − ln(X/M)i,t−1 = αi,h + δt,h + bh Δreri,t + Σ lag + εi,t+h", "size": 12},
        {"runs": [("h = 0–24 bulan;  ", False, None), ("δt", True, None), (" = ~fixed effects~ bulan;  ", False, None),
                  ("rer", True, None), (" = kurs riil bilateral", False, None)], "size": 11.5},
    ], fill=CREAM, inset=10, space=5)
    numbered(s, [
        ("~Lag selection~", "ARDL: hingga 12 bulan, dipilih otomatis dengan AIC (paket Stata ~ardl~). LP: 12 lag variabel "
                          "dependen dan kurs (~lag augmentation~)."),
        ("~Inference~", "~Bounds test~ dengan nilai kritis Kripfganz-Schneider; ~standard error~ Newey-West (agregat) dan "
                      "Driscoll-Kraay (panel)."),
        ("Kontrol", "Harga komoditas (BCOM; batu bara untuk energi, CPO untuk pertanian), IPI mitra, ~seasonal dummy~ dan krisis."),
    ], y0=228, step=66, desc=12, head=13.5)
    pointers(s, [[("Mengapa bentuk ~error correction~: ", True, None),
                  ("koefisien φ (ADJ) langsung menunjukkan berapa persen penyimpangan dari ~long-run equilibrium~ yang "
                   "terkoreksi setiap bulan, sehingga dinamika ~short-run~ dan ~long-run~ terbaca dari satu persamaan.", False, None)]],
             y=432, head="", size=11.5)
    source(s, "Pesaran dkk. (2001); Jordà (2005); Kripfganz & Schneider (2023)")

    s = content(prs, "Interpretasi koefisien: efek depresiasi riil 10% adalah simulasi dari koefisien yang diestimasi",
                notes="Model menghasilkan koefisien dalam bentuk elastisitas, yang sulit dibaca langsung. Karena itu setiap koefisien "
                      "kami terjemahkan menjadi satu skenario yang sama: seandainya rupiah melemah riil 10 persen, berapa persen "
                      "rasio ekspor/impor berubah. Angka 10 persen ini bukan peristiwa nyata, melainkan simulasi dari koefisien. "
                      "Karena modelnya dalam logaritma, efeknya proporsional: depresiasi 5 persen memberi separuh efek, dan 20 "
                      "persen dua kalinya. Dengan satu skenario untuk semua model, hasil ARDL, local projections, per mitra, dan "
                      "per kelompok bisa dibandingkan langsung. Positif berarti neraca membaik.")
    numbered(s, [
        ("Langkah 1 · estimasi",
         "ARDL menghasilkan koefisien ~long-run~ θ1 untuk ln REER. Contoh model utama: θ1 = "
         f"{idn(A1.lr, 2)}. LP menghasilkan bh untuk setiap bulan h."),
        ("Langkah 2 · samakan arah",
         "REER naik berarti rupiah ~menguat~. Depresiasi riil 10% berarti ln REER turun 0,10, sehingga efeknya = −0,10 × θ1."),
        ("Langkah 3 · simulasikan depresiasi 10%",
         f"Efek = −0,10 × θ1 × 100 = −10 × θ1. Contoh: −10 × {idn(A1.lr, 2)} = {idn(A1.eff10_lr)}% perubahan rasio ekspor/impor."),
        ("Langkah 4 · baca jalurnya",
         "~Dynamic multiplier~ (ARDL) dan ~impulse response~ (LP) diubah dengan cara yang sama untuk bulan 0–24, lalu "
         "diplot. Bintang (*) = signifikan pada 10%; warna menunjukkan arah: cokelat = memburuk, oranye = membaik."),
    ], step=76, desc=12, head=13.5)
    pointers(s, [[("Simulasi, bukan peristiwa: ", True, None),
                  ("10% dipilih sebagai skenario yang mudah dibaca. Karena model dalam logaritma, efek depresiasi 5% = separuhnya "
                   "dan 20% = dua kalinya.", False, None)],
                 [("Contoh membaca: ", True, None),
                  ("angka −10 di bulan ke-12 berarti rasio ekspor/impor 1,10 menjadi 0,99 setahun setelah rupiah melemah riil "
                   "10%: surplus kecil berubah menjadi defisit kecil.", False, None)]], y=404, head="", size=11.5)
    source(s, "Olahan penulis")


    # =========================================================================
    section(prs, "05", "Hasil",
            "Apa jawaban ketiga pertanyaan penelitian?")

    s = content(prs, f"RQ1 · Depresiasi riil 10% menurunkan rasio ekspor/impor sekitar {idn(abs(lp12), 0)}% dalam 6–12 bulan "
                     "dan tidak pulih",
                notes="Kita mulai dari pertanyaan paling besar, RQ1. Kedua metode memberi gambaran sama: setelah rupiah melemah, rasio ekspor/impor turun "
                      "sekitar sepuluh persen dalam enam sampai dua belas bulan dan tidak kembali ke atas nol. Tidak ada "
                      "bentuk J, dan efek ~long-run~nya tidak signifikan, sehingga kondisi Marshall-Lerner tidak "
                      "terpenuhi untuk Indonesia.")
    plabel(s, X1, 88, W1, "ARDL: jalur yang diturunkan dari satu persamaan", [("(% rasio X/M; ~dynamic multiplier~)", False, None)])
    pic(s, fig_ardl_jcurve(), X1, 126, W1, 236)
    plabel(s, X2, 88, W2, "Local projections: diestimasi langsung per bulan",
           [("(% rasio X/M; tiap titik = satu regresi; arsir = 90% CI)", False, None)])
    pic(s, fig_lp_line(), X2, 126, W2, 236)
    rows = [["", "Bulan 0", "Bulan 6", "Bulan 12", "Bulan 24", "~Long-run~"],
            ["ARDL", idn(A1.eff10_sr0), idn(A1.eff10_m6), idn(A1.eff10_m12), idn(A1.eff10_m24),
             f"{idn(A1.eff10_lr)} (p = {idn(A1.lr_p, 2)})"],
            ["Local projections"] + [sig(lpv("A1_ols", "AGG", h), lpv("A1_ols", "AGG", h, "p")) for h in (0, 6, 12, 24)] + ["–"]]
    table(s, 44, 368, 872, rows, [1.6, 1, 1, 1, 1, 1.6], size=11, row_h=19)
    pointers(s, [
        [("Cara membaca: ", True, None),
         ("garis = % perubahan rasio X/M h bulan setelah rupiah melemah riil 10%. Kedua model sepakat: rasio turun sekitar 10% "
          "di bulan 6–12. Di grafik kanan, arsir seluruhnya di bawah nol pada bulan 6–12, artinya penurunan itu signifikan.",
          False, None)],
        [("Jawaban RQ1: ", True, None),
         ("tidak ada J-curve, karena garis tidak pernah masuk zona oranye dalam 24 bulan. Marshall-Lerner tidak terpenuhi, "
          "karena efek ~long-run~ ARDL tidak signifikan. Spesifikasi lain (garis abu-abu) memberi arah yang sama.", False, None)],
    ], y=430, head="", size=10.5)
    source(s, "Estimasi penulis")

    P = lambda v, h: pvv("P_agg", "AGG10", v, h)
    Pp = lambda v, h: pvv("P_agg", "AGG10", v, h, "p")
    st = lambda v, h: star(Pp(v, h))
    s = content(prs, "RQ1 dibedah: tahun pertama rasio turun karena volume ekspor, tahun kedua karena harga",
                notes="Slide ini menjawab pertanyaan lanjutan dari RQ1: neraca memburuk karena apa? Nilai ekspor dan impor selalu "
                      "sama dengan harga dikali jumlah barang. Karena itu rasio ekspor/impor bisa dipecah persis menjadi dua "
                      "bagian. Bagian pertama adalah terms of trade, yaitu harga ekspor dibagi harga impor. Kalau terms of "
                      "trade turun, barang yang kita jual makin murah dibanding barang yang kita beli. Bagian kedua adalah rasio "
                      "volume, yaitu jumlah barang yang diekspor dibanding yang diimpor. Di grafik kiri, garis cokelat tebal "
                      "adalah rasio X/M, dan nilainya selalu sama dengan jumlah garis oranye putus-putus (harga) dan garis abu-abu "
                      "titik-titik (volume). Di tahun pertama, penurunan terutama datang dari volume ekspor yang turun, padahal "
                      "teori memprediksi naik. Di tahun kedua polanya berbalik: volume naik ke atas nol, artinya membaik, tetapi "
                      "harga terus turun. Perbaikan volume itu dimakan penurunan harga, sehingga rasio X/M tetap di bawah nol. "
                      "Perbaikan volume ini juga belum signifikan, jadi jejak J-curve-nya terlalu lemah untuk disimpulkan.")
    plabel(s, X1, 88, W1, "Rasio X/M = harga (ToT) + volume", [("(LP, Indonesia–10 mitra; arsir = 90% CI rasio X/M)", False, None)])
    pic(s, fig_decomp_lines(), X1, 126, W1, 246)
    plabel(s, X2, 88, W2, "Asal penurunan di bulan ke-12", [("(kontribusi tiap komponen ke rasio X/M, %)", False, None)])
    pic(s, fig_waterfall(12), X2, 126, W2, 246)
    pointers(s, [
        [("Definisi: ", True, None),
         ("~terms of trade~ (ToT) = harga ekspor ÷ harga impor; turun berarti barang yang kita jual makin murah dibanding barang "
          "yang kita beli. Rasio volume = jumlah barang diekspor ÷ diimpor. Garis cokelat = garis oranye + garis abu-abu.",
          False, None)],
        [("Tahun pertama (bulan 0–12), volume: ", True, None),
         (f"rasio X/M {idn(P('lnxm', 12))}%{st('lnxm', 12)} = ToT {idn(P('lntot', 12))}% + volume {idn(P('lnqxm', 12))}%"
          f"{st('lnqxm', 12)}. Penyebabnya volume ekspor yang turun ({idn(P('lnqx', 12))}%{st('lnqx', 12)}), bukan impor yang "
          f"naik ({idn(P('lnqm', 12))}%, tidak signifikan).", False, None)],
        [("Tahun kedua (bulan 18–24), harga: ", True, None),
         (f"volume berbalik ke atas nol, artinya membaik ({idn(P('lnqxm', 24), sign=True)}%, belum signifikan), tetapi ToT makin "
          f"turun ({idn(P('lntot', 24))}%{st('lntot', 24)}). Perbaikan volume dimakan penurunan harga, sehingga rasio tetap di "
          "bawah nol.", False, None)],
    ], y=380, size=10.5, head="")
    source(s, "Estimasi penulis; ITC Trade Map (kuantitas HS-6)")

    vx, vm = avol.loc["V1_qx"], avol.loc["V2_qm"]
    epsx, epsm = vx.eff10_lr / 10, -vm.eff10_lr / 10
    s = content(prs, "Uji Marshall-Lerner dengan volume: elastisitas tidak signifikan dan jumlahnya jauh di bawah 1",
                notes="Uji Marshall-Lerner yang sebenarnya memakai elastisitas volume, bukan nilai. Kami mengestimasi volume ekspor "
                      "dan volume impor terhadap kurs riil dengan ARDL. Teori memprediksi volume ekspor naik dan volume impor "
                      "turun saat rupiah melemah, dan jumlah kedua elastisitas harus lebih dari satu. Hasilnya volume ekspor "
                      "justru turun, volume impor hampir tidak berubah, dan tidak ada yang signifikan. Jumlah elastisitasnya "
                      "negatif, jauh dari syarat lebih dari satu.")
    tbox(s, 44, 94, 300, 110, [
        {"runs": [("Syarat Marshall-Lerner", True, "000000")], "size": 13},
        {"runs": [("εX + εM > 1", True, DARKOR)], "size": 22},
        {"runs": "εX = % kenaikan volume ekspor, εM = % penurunan volume impor, per 1% depresiasi riil. Teori: keduanya "
                 "positif.", "size": 11},
    ], fill=CREAM, inset=10, space=3)
    cf = lambda r: "ya" if r.coint10 == 1 else "tidak"
    rows = [["Persamaan (ARDL, Indonesia–10 mitra)", "Efek LR (%)", "p", "~Coint.~", "Elastisitas", "LP bln 12", "LP bln 24"],
            ["Volume ekspor Qx", idn(vx.eff10_lr), idn(vx.lr_p, 2), cf(vx), (f"εX = {idn(epsx, 2)}", BROWN),
             pvs("P_agg", "AGG10", "lnqx", 12), pvs("P_agg", "AGG10", "lnqx", 24)],
            ["Volume impor Qm", idn(vm.eff10_lr), idn(vm.lr_p, 2), cf(vm), f"εM = {idn(epsm, 2)}",
             pvs("P_agg", "AGG10", "lnqm", 12), pvs("P_agg", "AGG10", "lnqm", 24)],
            ["Jumlah εX + εM", "", "", "", (idn(epsx + epsm, 2), BROWN), "", ""],
            ["Rasio volume Qx/Qm", idn(avol.loc['V3_qxm', 'eff10_lr']), idn(avol.loc['V3_qxm', 'lr_p'], 2),
             cf(avol.loc['V3_qxm']), "", pvs("P_agg", "AGG10", "lnqxm", 12), pvs("P_agg", "AGG10", "lnqxm", 24)],
            ["~Terms of trade~ Px/Pm", idn(avol.loc['V4_tot', 'eff10_lr']), idn(avol.loc['V4_tot', 'lr_p'], 2),
             cf(avol.loc['V4_tot']), "", pvs("P_agg", "AGG10", "lntot", 12), pvs("P_agg", "AGG10", "lntot", 24)]]
    table(s, 360, 94, 556, rows, [2.3, 0.9, 0.55, 0.65, 1.0, 0.85, 0.85], size=10.5, row_h=24, hl_rows=(3,))
    note(s, "Efek LR dan LP = % perubahan per depresiasi riil 10%. Kontrol: IPI mitra (ekspor), PDB riil Indonesia (impor), BCOM, "
            "~seasonal dummy~, krisis; lag maksimum 6.", y=244, h=34, x=X2, w=W2)
    plabel(s, X1, 214, W1, "Jalur volume setelah depresiasi riil 10%", [("(LP, Indonesia–10 mitra; arsir = 90% CI)", False, None)])
    pic(s, fig_vol_lines(), X1, 252, W1, 250)
    pointers(s, [
        [("Volume ekspor justru turun ", True, None),
         (f"(εX = {idn(epsx, 2)}), padahal teori memprediksi naik karena ekspor lebih murah bagi pembeli asing. Jalur LP "
          f"memberi arah sama: {idn(pvv('P_agg', 'AGG10', 'lnqx', 12))}%{star(pvv('P_agg', 'AGG10', 'lnqx', 12, 'p'))} di "
          "bulan ke-12.", False, None)],
        [("Volume impor hampir tidak bereaksi ", True, None),
         (f"(εM = {idn(epsm, 2)}, tidak signifikan), sejalan dengan Tang (2002): impor Indonesia didominasi input yang sulit "
          "diganti.", False, None)],
        [("Jumlahnya ", True, None),
         (f"{idn(epsx + epsm, 2)}, jauh di bawah 1: Marshall-Lerner tidak terpenuhi, juga bila diukur dengan volume. Tidak ada "
          "~cointegration~ di keempat persamaan, sehingga angka ~long-run~ dibaca sebagai arah, bukan besaran.", False, None)],
    ], x=X2, y=284, w=W2, size=11)
    source(s, "Estimasi penulis; ITC Trade Map (kuantitas HS-6)")

    s = content(prs, "RQ2 · Neraca dengan China dan Jepang memburuk paling dalam; tidak ada mitra yang membaik signifikan",
                notes="Setelah level agregat, kita pecah per mitra untuk menjawab RQ2. Grafik menunjukkan efek depresiasi rupiah terhadap mata uang setiap mitra, 12 bulan "
                      "kemudian, setelah semua ~global shock~ dikendalikan. China dan Jepang memburuk secara signifikan; "
                      "dugaan channel-nya adalah impor barang modal dan bahan baku yang sulit diganti. Tidak ada mitra yang "
                      "membaik secara signifikan, termasuk AS.")
    plabel(s, X1, 88, W1, "Rasio X/M per mitra, 12 bulan setelah depresiasi riil 10%",
           [("(LP panel; garis tipis = 90% ~confidence interval~)", False, None)])
    pic(s, fig_bar_partner(), X1, 128, W1, 340)
    rows = [["Mitra", "LP bln 0", "LP bln 12", "ARDL bln 0", "ARDL LR (p)"]]
    for c in ["CHN", "JPN", "THA", "USA", "SGP", "MYS"]:
        rows.append([CTRY[c], sig(lpv("B2_partner", c, 0), lpv("B2_partner", c, 0, "p")),
                     sig(lpv("B2_partner", c, 12), lpv("B2_partner", c, 12, "p")),
                     sig(am.loc[c, "eff10_sr0"], am.loc[c, "sr0_p"]),
                     f"{idn(am.loc[c, 'eff10_lr'])} ({idn(am.loc[c, 'lr_p'], 2)})"])
    table(s, X2, 94, W2, rows, [1.7, 1, 1, 1, 1.2], size=11, row_h=21)
    pb = pointers(s, [
        [("China dan Jepang: ", True, None), ("memburuk di bulan 0 dan 12 (LP); Jepang juga signifikan di ARDL. Dugaan "
                                              "~channel~: impor barang modal dan bahan baku yang sulit diganti.", False, None)],
        [("AS: ", True, None), (f"ARDL ~long-run~ {idn(am.loc['USA', 'eff10_lr'], sign=True)}% tetapi tidak signifikan; "
                                "di LP ≈ 0 setelah ~common shock~ dikendalikan.", False, None)],
        [("Rata-rata 10 mitra ≈ 0: ", True, None),
         (f"LP bulan 12 {idn(lpv('B1_panel', 'PANEL', 12))}% (p = {idn(lpv('B1_panel', 'PANEL', 12, 'p'), 2)}); "
          f"panel MG {idn(pmg.loc['MG', 'eff10_lr'])}% (p = {idn(pmg.loc['MG', 'lr_reer_p'], 2)}).", False, None)],
    ], x=X2, y=252, w=W2, size=11.5)
    pointers(s, [
        "Batang pekat = signifikan 10%; batang pucat = tidak signifikan (garis tipis memotong nol).",
        f"Thailand memburuk signifikan di LP ({idn(lpv('B2_partner', 'THA', 12))}%) tetapi tidak di ARDL, sehingga belum "
        "dianggap robust.",
    ], x=X2, y=pb.top / 12700 + pb.height / 12700 + 8, w=W2, head="Cara membaca dan catatan", size=11)
    source(s, "Estimasi penulis; kurs dan CPI BIS")

    Q = lambda c, v, h=12: pvv("Q_partner", c, v, h)
    s = content(prs, "RQ2 dibedah: China memburuk lewat harga, Thailand lewat volume, Jepang lewat keduanya",
                notes="Respons rasio ekspor/impor per mitra dipecah menjadi channel harga (terms of trade bilateral) dan channel "
                      "volume. Neraca dengan China memburuk karena harga: ekspor ke China didominasi batu bara dan produk nikel "
                      "yang harganya turun, sementara impor dari China berupa barang manufaktur yang harganya stabil. Thailand "
                      "memburuk karena volume. Jepang memburuk lewat keduanya.")
    plabel(s, X1, 88, W1, "Dua channel per mitra, bulan ke-12", [("(LP panel, kurs riil bilateral; urut dari rasio X/M paling buruk)",
                                                                   False, None)])
    pic(s, fig_two_channel("Q_partner", list(CTRY), CTRY, 12, "pv_mitra12"), X1, 128, W1, 330)
    rows = [["Mitra", "Rasio X/M", "Harga (ToT)", "Volume"]]
    for c in ["CHN", "JPN", "THA", "USA", "IND", "AUS"]:
        rows.append([CTRY[c], pvs("Q_partner", c, "lnxm", 12), pvs("Q_partner", c, "lntot", 12), pvs("Q_partner", c, "lnqxm", 12)])
    rows.append(["Rata-rata 10 mitra", pvs("Q_panel", "PANEL", "lnxm", 12), pvs("Q_panel", "PANEL", "lntot", 12),
                 pvs("Q_panel", "PANEL", "lnqxm", 12)])
    table(s, X2, 94, W2, rows, [1.6, 1, 1, 1], size=11, row_h=21, hl_rows=(7,))
    pointers(s, [
        [("China (harga): ", True, None),
         (f"~terms of trade~ {idn(Q('CHN', 'lntot'))}%*. Ekspor ke China didominasi batu bara dan produk nikel yang harganya "
          "turun; impor dari China berupa manufaktur yang harganya relatif stabil.", False, None)],
        [("Jepang (keduanya) dan Thailand (volume): ", True, None),
         (f"volume Thailand {idn(Q('THA', 'lnqxm'))}%*, Jepang {idn(Q('JPN', 'lnqxm'))}%* dan harga {idn(Q('JPN', 'lntot'))}%*.",
          False, None)],
        [("Australia: ", True, None),
         (f"satu-satunya mitra yang volumenya membaik ({idn(Q('AUS', 'lnqxm', 24), sign=True)}% di bulan ke-24, p = "
          f"{idn(pvv('Q_partner', 'AUS', 'lnqxm', 24, 'p'), 2)}), tetapi harganya memburuk.", False, None)],
    ], x=X2, y=272, w=W2, size=11)
    source(s, "Estimasi penulis; ITC Trade Map (kuantitas HS-6), BIS")

    s = content(prs, "RQ3 · Energi & tambang dan barang modal memburuk; pertanian dan konsumsi baru membaik setelah 2 tahun",
                notes="Terakhir, RQ3: apakah jenis barang menentukan? Kelompok dengan efek negatif yang paling kuat adalah energi dan tambang, karena harga batu "
                      "bara dan nikel ditentukan di pasar dunia dalam USD, dan barang modal, karena impor mesin tidak bisa "
                      "ditunda. Kelompok yang membaik, yaitu pertanian dan pangan serta barang konsumsi, baru terlihat "
                      "setelah sekitar dua tahun. Manufaktur secara keseluruhan tidak menunjukkan efek.")
    plabel(s, X1, 88, W1, "Perubahan rasio X/M per kelompok setelah rupiah melemah riil 10%",
           [("(LP panel; angka = %, * = signifikan 10%)", False, None)])
    pic(s, fig_group_two(), X1, 128, W1, 340)
    rows = [["Kelompok", "ARDL bln 0", "ARDL LR (p)", "LP bln 12", "LP bln 24"]]
    for g in ["sec2", "eu3", "eu2", "comm", "noncomm", "eu1", "sec1"]:
        lr_ok = ak.loc[g, "lr_p"] < .1 and ak.loc[g, "coint10"] == 1
        rows.append([GRP_S[g], sig(ak.loc[g, "eff10_sr0"], ak.loc[g, "sr0_p"]),
                     (f"{idn(ak.loc[g, 'eff10_lr'])} ({idn(ak.loc[g, 'lr_p'], 2)})",
                      (BROWN if ak.loc[g, "eff10_lr"] < 0 else DARKOR) if lr_ok else "000000"),
                     sig(lpv("C_group", g, 12), lpv("C_group", g, 12, "p")),
                     sig(lpv("C_group", g, 24), lpv("C_group", g, 24, "p"))])
    table(s, X2, 94, W2, rows, [1.5, 1, 1.25, 0.95, 0.95], size=11, row_h=21)
    pb = pointers(s, [
        [("Energi & tambang: ", True, None), (f"ARDL ~long-run~ {idn(ak.loc['sec2', 'eff10_lr'])}% (~cointegrated~), LP "
                                              f"{idn(lpv('C_group', 'sec2', 12))}% di bulan 12; harga batu bara dan nikel dalam USD.",
                                              False, None)],
        [("Barang modal: ", True, None), (f"ARDL {idn(ak.loc['eu3', 'eff10_sr0'])}% seketika; LP {idn(lpv('C_group', 'eu3', 12))}% "
                                          "di bulan 12.", False, None)],
        [("Pertanian & konsumsi: ", True, None), (f"membaik {idn(lpv('C_group', 'sec1', 24), sign=True)}% dan "
                                                  f"{idn(lpv('C_group', 'eu1', 24), sign=True)}% setelah 24 bulan (LP).", False, None)],
        [("Manufaktur: ", True, None), ("tidak ada efek; tidak ada J-curve.", False, None)],
    ], x=X2, y=272, w=W2, size=11)
    pointers(s, [
        "Panel kiri = bulan ke-12, kanan = bulan ke-24. Cokelat = memburuk, oranye = membaik; pucat = tidak signifikan.",
        "ARDL ~long-run~ barang konsumsi (+86%, p = 0,09) tidak ~cointegrated~ dan penyesuaiannya sangat lambat "
        "(ADJ −0,05), sehingga dibaca sebagai arah, bukan besaran.",
    ], x=X2, y=pb.top / 12700 + pb.height / 12700 + 8, w=W2, head="Cara membaca dan catatan", size=11)
    source(s, "Estimasi penulis; klasifikasi HS-6 UNSD")

    G = lambda g, v, h: pvv("R_group", g, v, h)
    s = content(prs, "RQ3 dibedah: komoditas memburuk lewat harga; barang konsumsi membaik lewat volume",
                notes="Dekomposisi per kelompok barang untuk jumlah 10 mitra. Channel harga memburukkan kelompok komoditas: "
                      "harga ekspor komoditas turun relatif terhadap harga impornya. Channel volume justru memperbaiki barang "
                      "konsumsi, satu-satunya kelompok yang bereaksi sesuai Marshall-Lerner: ekspor barang konsumsi naik "
                      "atau impornya turun setelah rupiah melemah. Pertanian dan pangan mendapat dua efek berlawanan.")
    plabel(s, X1, 88, W1, "Dua channel per kelompok, bulan ke-24", [("(LP, Indonesia–10 mitra, REER; urut dari rasio X/M paling buruk)",
                                                                    False, None)])
    pic(s, fig_two_channel("R_group", ["comm", "sec2", "sec1", "noncomm", "eu1", "eu2", "eu3"], GRP_S, 24, "pv_kelompok24"), X1, 128, W1, 330)
    rows = [["Kelompok", "Harga bln 12", "Volume bln 12", "Harga bln 24", "Volume bln 24"]]
    for g in ["comm", "sec2", "sec1", "eu2", "eu3", "noncomm", "eu1"]:
        rows.append([GRP_S[g], pvs("R_group", g, "lntot", 12), pvs("R_group", g, "lnqxm", 12),
                     pvs("R_group", g, "lntot", 24), pvs("R_group", g, "lnqxm", 24)])
    table(s, X2, 94, W2, rows, [1.5, 1, 1.05, 1, 1.05], size=10.5, row_h=21)
    pointers(s, [
        [("Komoditas (harga): ", True, None),
         (f"~terms of trade~ {idn(G('comm', 'lntot', 12))}%* di bulan 12 dan {idn(G('comm', 'lntot', 24))}%* di bulan 24; "
          "volumenya tidak bereaksi.", False, None)],
        [("Barang konsumsi (volume): ", True, None),
         (f"rasio volume {idn(G('eu1', 'lnqxm', 12), sign=True)}%* di bulan 12 dan {idn(G('eu1', 'lnqxm', 24), sign=True)}%* di "
          "bulan 24: satu-satunya channel Marshall-Lerner yang bekerja.", False, None)],
        [("Pertanian dan manufaktur: ", True, None),
         (f"volume membaik di bulan 24 (pertanian {idn(G('sec1', 'lnqxm', 24), sign=True)}%*, manufaktur "
          f"{idn(G('noncomm', 'lnqxm', 24), sign=True)}%*), tetapi pertanian kehilangan lewat harga.", False, None)],
    ], x=X2, y=272, w=W2, size=11)
    note(s, "Berbeda dari slide RQ3 (panel bilateral), dekomposisi ini memakai jumlah 10 mitra per kelompok dengan ~shock~ REER.",
         y=486, h=20, w=430)
    source(s, "Estimasi penulis; ITC Trade Map (kuantitas HS-6)")

    s = content(prs, "Ringkasan: hasil yang bertahan di kedua metode",
                notes="Tabel ringkasan ini menempatkan ARDL dan local projections berdampingan. Hasil yang kita yakini adalah "
                      "yang muncul di kedua metode: neraca agregat memburuk, terutama dengan China dan Jepang, serta pada "
                      "energi dan tambang dan barang modal. Hasil yang hanya muncul di satu metode, seperti AS, kami anggap "
                      "tidak robust.")
    fm = lambda e, p=None: sig(e, p)
    KS = {"-": ("▼ Memburuk", BROWN), "-r": ("▼ Memburuk, tidak pulih", BROWN), "-s": ("▼ Memburuk ringan", BROWN),
          "+": ("▲ Membaik setelah 2 tahun", DARKOR), "0": ("● Tidak ada efek", GREY)}
    rows = [["Cakupan", "ARDL bln 0", "ARDL bln 12", "LP bln 12", "LP bln 24", "Kesimpulan", "Channel utama"]]
    rows.append(["Indonesia–dunia", fm(A1.eff10_sr0, A1.sr0_p), fm(A1.eff10_m12), fm(lp12, lpv("A1_ols", "AGG", 12, "p")),
                 fm(lpv("A1_ols", "AGG", 24), lpv("A1_ols", "AGG", 24, "p")), KS["-r"], "volume ekspor turun"])
    for c, k, ch in [("CHN", "-", "harga (ToT)"), ("JPN", "-", "harga dan volume"), ("USA", "0", "–")]:
        rows.append([CTRY[c], fm(am.loc[c, "eff10_sr0"], am.loc[c, "sr0_p"]), fm(am.loc[c, "eff10_m12"]),
                     fm(lpv("B2_partner", c, 12), lpv("B2_partner", c, 12, "p")),
                     fm(lpv("B2_partner", c, 24), lpv("B2_partner", c, 24, "p")), KS[k], ch])
    for g, k, ch in [("sec2", "-", "tidak tegas"), ("eu3", "-", "tidak tegas"), ("eu2", "-s", "harga dan volume"),
                     ("sec1", "+", "volume (+), harga (−)"), ("eu1", "+", "volume"), ("noncomm", "0", "volume (+) bln 24")]:
        rows.append([GRP[g], fm(ak.loc[g, "eff10_sr0"], ak.loc[g, "sr0_p"]), fm(ak.loc[g, "eff10_m12"]),
                     fm(lpv("C_group", g, 12), lpv("C_group", g, 12, "p")),
                     fm(lpv("C_group", g, 24), lpv("C_group", g, 24, "p")), KS[k], ch])
    table(s, 44, 94, 872, rows, [2.4, 0.85, 0.9, 0.85, 0.85, 1.9, 1.45], size=11, row_h=26, align=[L, R, R, R, R, L, L])
    note(s, "Angka = % perubahan rasio X/M per depresiasi riil 10%; * signifikan 10% (cokelat = memburuk, oranye = membaik). "
            "ARDL bulan 0 = koefisien ~short-run~; ARDL bulan 12 = ~dynamic multiplier~ (tanpa ~confidence interval~). LP mitra "
            "dan kelompok = panel 10 mitra dengan ~fixed effects~ bulan.", y=386, h=30)
    pointers(s, [
        [("Inti temuan: ", True, None),
         ("depresiasi tidak memperbaiki neraca. ~Channel~ yang memburuk (energi, barang modal, mitra China dan Jepang) "
          "lebih besar dan lebih cepat daripada ~channel~ yang membaik (pertanian, konsumsi).", False, None)],
        [("Belum robust: ", True, None), ("AS dan Thailand hanya muncul di satu metode; perbaikan manufaktur (pola J-curve "
                                          "di versi awal) tidak bertahan.", False, None)],
        [("Implikasi: ", True, None), ("efek depresiasi ditentukan struktur barang. Selama ekspor bertumpu pada komoditas "
                                       "berharga USD dan impor pada input yang sulit diganti, rupiah yang lebih lemah tidak "
                                       "memperbaiki neraca.", False, None)],
    ], y=422, size=11, head="")
    source(s, "Estimasi penulis")


    pre = ev[ev.k.isin([-6, 0])].groupby("k").xm_idx.mean()
    pre_drop = (pre.loc[0] / pre.loc[-6] - 1) * 100
    fcorr, cv = fig_corr_dep()
    s = content(prs, "Mengapa depresiasi tidak memperbaiki neraca? Tiga penjelasan dan buktinya",
                notes="Hasil kami berlawanan dengan teori, jadi wajar bertanya mengapa. Kami menguji tiga penjelasan. Pertama, "
                      "volume tidak bereaksi seperti yang diharapkan. Teori mengatakan rupiah yang murah membuat ekspor lebih "
                      "laku dan impor berkurang. Kenyataannya, ekspor kita didominasi batu bara, CPO, dan nikel yang harganya "
                      "ditetapkan dalam dolar dan jumlahnya dibatasi kapasitas produksi, sementara impor kita sebagian besar "
                      "bahan baku dan mesin yang sulit diganti. Kedua, harga ekspor ikut turun. Depresiasi sering terjadi "
                      "bersamaan dengan jatuhnya harga komoditas, sehingga nilai ekspor tergerus dari sisi harga. Dua penjelasan "
                      "ini didukung langsung oleh dekomposisi harga dan volume. Ketiga, bisa jadi arah sebab-akibatnya terbalik: "
                      "rupiah melemah karena neraca sedang memburuk, atau karena ekonomi dunia melambat. Kalau begitu, kurs "
                      "bukan penyebab, melainkan gejala. Penjelasan ketiga ini belum bisa kami singkirkan, dan buktinya kami "
                      "tunjukkan di slide berikutnya.")
    table(s, 44, 92, 872, [
        ["Penjelasan", "Apa yang terjadi", "Bukti dari riset ini", "Status"],
        ["1 · Volume tidak bereaksi",
         "Rupiah murah seharusnya membuat ekspor lebih laku dan impor berkurang. Tetapi ekspor komoditas dihargai dalam USD "
         "(~dominant currency~) dan dibatasi kapasitas; impor didominasi input yang sulit diganti.",
         f"Volume ekspor {idn(pvv('P_agg', 'AGG10', 'lnqx', 12))}%* di bulan 12; volume impor "
         f"{idn(pvv('P_agg', 'AGG10', 'lnqm', 12))}% (tidak signifikan); εX + εM = {idn(epsx + epsm, 2)}, jauh di bawah 1.",
         ("Didukung", BROWN)],
        ["2 · Harga ekspor ikut turun",
         "Depresiasi sering datang bersamaan dengan jatuhnya harga batu bara dan nikel, sehingga nilai ekspor tergerus dari "
         "sisi harga.",
         f"ToT komoditas {idn(pvv('R_group', 'comm', 'lntot', 12))}%*; ToT bilateral China "
         f"{idn(pvv('Q_partner', 'CHN', 'lntot', 12))}%*; harga ekspor {idn(pvv('P_agg', 'AGG10', 'lnpx', 24))}%* di bulan 24.",
         ("Didukung", BROWN)],
        ["3 · ~Reverse causality~ atau ~common shock~",
         "Rupiah melemah karena neraca sedang memburuk atau karena ekonomi dunia melambat. Kurs menjadi gejala, bukan penyebab.",
         f"Rasio X/M sudah turun {idn(abs(pre_drop))}% dalam 6 bulan sebelum episode; depresiasi berkorelasi "
         f"{idn(cv['IPI mitra'], 2)} dengan IPI mitra; instrumen USD lemah (F = {idn(LPIV_F, 2)}).",
         ("Belum bisa disingkirkan", DARKOR)],
    ], [1.45, 2.9, 2.75, 0.95], align=[L, L, L, L], size=10.5, row_h=62)
    pointers(s, [
        [("Artinya: ", True, None),
         ("penjelasan 1 dan 2 berarti efek kurs memang lemah karena struktur ekspor-impor Indonesia. Penjelasan 3 berarti angka "
          "negatif bisa melebih-lebihkan efek buruk depresiasi. Dalam kedua kasus, rupiah yang lebih lemah tidak memperbaiki "
          "neraca.", False, None)],
        [("Lanjutan: ", True, None),
         ("slide berikutnya menunjukkan bukti untuk penjelasan 3.", False, None)],
    ], y=362, head="", size=11)
    source(s, "Estimasi penulis; Gopinath dkk. (2020) untuk ~dominant currency~")

    s = content(prs, "Lanjutan: neraca sudah melemah sebelum rupiah turun, dan depresiasi datang bersama perlambatan global",
                notes="Ini bukti untuk penjelasan ketiga. Grafik kiri memakai delapan episode depresiasi yang sama seperti di "
                      "bagian fakta awal, tetapi kini kita melihat enam bulan sebelum rupiah mulai melemah. Rasio ekspor/impor "
                      "ternyata sudah turun sebelum episode dimulai. Artinya, neraca yang memburuk bisa jadi justru ikut "
                      "mendorong rupiah melemah, bukan sebaliknya. Grafik kanan menunjukkan dengan apa depresiasi biasanya "
                      "terjadi bersamaan. Saat rupiah melemah, produksi industri negara mitra dan ekspor kita cenderung ikut "
                      "turun. Jadi depresiasi sering menjadi bagian dari perlambatan global yang juga menekan ekspor. Dalam "
                      "situasi seperti itu, regresi akan melihat rupiah melemah bersamaan dengan neraca memburuk, walaupun "
                      "kurs bukan penyebabnya. Untuk memisahkannya, kita perlu shock kurs yang benar-benar dari luar, misalnya "
                      "perubahan kebijakan moneter Amerika Serikat. Itulah langkah lanjutan riset ini.")
    plabel(s, X1, 88, W1, "Rasio ekspor/impor sebelum dan sesudah awal episode",
           [("(rata-rata 8 episode; area abu-abu = ~interquartile range~)", False, None)])
    pic(s, fig_pretrend(), X1, 126, W1, 262)
    plabel(s, X2, 88, W2, "Korelasi depresiasi riil dengan variabel lain",
           [("(perubahan 12 bulan, 2007–2026; cokelat = korelasi lebih kuat)", False, None)])
    pic(s, fcorr, X2, 126, W2, 262)
    pointers(s, [
        [("Neraca memburuk lebih dulu: ", True, None),
         (f"rasio X/M rata-rata turun {idn(abs(pre_drop))}% dalam 6 bulan sebelum rupiah mulai melemah. Sebagian penurunan "
          "neraca setelah depresiasi bisa jadi kelanjutan tren itu, bukan akibat kurs.", False, None)],
        [("Depresiasi datang bersama perlambatan global: ", True, None),
         (f"saat rupiah melemah, IPI mitra ({idn(cv['IPI mitra'], 2)}) dan ekspor ({idn(cv['Ekspor'], 2)}) cenderung ikut "
          "turun. Efek kurs bercampur dengan ~common shock~ yang juga menekan ekspor.", False, None)],
        [("Langkah lanjutan: ", True, None),
         ("identifikasi ~shock~ kurs yang benar-benar eksogen (SVAR ~sign restrictions~ atau ~US monetary policy shock~) "
          "untuk memisahkan efek kurs dari ~reverse causality~.", False, None)],
    ], y=394, size=10.5, head="")
    source(s, "ITC Trade Map, BIS, CEIC, Bloomberg, BPS; olahan penulis")


    # =========================================================================
    section(prs, "06", "Diagnostik dan robustness",
            "Seberapa yakin kita: apakah hasil bertahan bila asumsi diubah?")

    s = content(prs, "~Unit root test~: tidak ada variabel I(2), sehingga ARDL ~bounds test~ sah dipakai",
                notes="Bagian ini menjawab seberapa yakin kita pada hasil tadi. Pemeriksaan pertama sebenarnya dilakukan sebelum "
                      "estimasi: setiap variabel diuji apakah ~stationary~. ARDL hanya sah bila tidak ada variabel yang "
                      "I(2). Hasilnya: rasio ekspor/impor dan IPI mitra ~stationary~, sedangkan kurs dan harga komoditas ~stationary~ "
                      "setelah ~first difference~. Kombinasi campuran ini justru alasan ARDL dipilih dibanding Johansen.")
    VN = {"lntb": "ln(X/M) dunia", "lntb10": "ln(X/M) 10 mitra", "lnreer": "ln REER", "lnjis": "ln JISDOR",
          "lncom": "ln BCOM", "lncom_nrg": "ln batu bara", "lncom_fd": "ln CPO", "lncom_imf": "ln indeks IMF",
          "lngdp_idn": "ln PDB riil", "yf_avg": "IPI mitra"}
    u = unitroot.pivot(index="var", columns="form", values=["adf_p", "pp_p"])
    rows = [["Variabel", "ADF level (p)", "PP level (p)", "ADF diff (p)", "PP diff (p)", "Kesimpulan"]]
    for v, nm in VN.items():
        if v not in u.index:
            continue
        al, pl, ad, pd_ = u.loc[v, ("adf_p", "level")], u.loc[v, ("pp_p", "level")], u.loc[v, ("adf_p", "diff")], u.loc[v, ("pp_p", "diff")]
        k = "I(0)" if (al < .05 or pl < .05) else ("I(1)" if (ad < .05 or pd_ < .05) else "?")
        rows.append([nm, idn(al, 3), idn(pl, 3), idn(ad, 3), idn(pd_, 3), (k, DARKOR if k == "I(0)" else "000000")])
    table(s, 44, 94, 872, rows, [2, 1.2, 1.2, 1.2, 1.2, 1.1], size=11.5, row_h=24)
    pointers(s, [
        [("Cara membaca: ", True, None), ("p < 0,05 berarti ~null hypothesis~ 'ada ~unit root~' ditolak, artinya variabel ~stationary~. "
                                          "I(0) = ~stationary~ di level; I(1) = ~stationary~ setelah ~first difference~.", False, None)],
        [("Konsekuensi: ", True, None), ("ln(X/M) ~stationary~, sementara kurs I(1). Efek permanen kurs terhadap rasio karena itu "
                                         "secara struktural kecil, sehingga hasil dibaca dari jalur respons, bukan hanya dari uji "
                                         "~cointegration~.", False, None)],
    ], y=372, h=98, size=11.5)
    note(s, "ADF dengan 4 lag dan konstanta; PP dengan lag Newey-West.", y=478, h=18)
    source(s, "Estimasi penulis")

    s = content(prs, "~Cointegration~ dan ~residual~: model utama lolos ~autocorrelation test~, ~heteroskedasticity test~, dan ~stability test~",
                notes="Tiga pemeriksaan untuk memastikan model layak. Bounds test menguji apakah ada hubungan ~long-run~. "
                      "Uji LM dan ARCH memeriksa apakah ~residual~ masih berpola; p di atas 0,05 berarti tidak ada masalah. "
                      "Grafik CUSUM di kanan memeriksa apakah koefisien stabil sepanjang waktu; garis yang tetap di dalam "
                      "~confidence band~ abu-abu berarti stabil.")
    rows = [["Model", "p F", "p t", "~Coint.~", "LM(12) p", "ARCH p"]]
    for i, nm in [("A1_main", "Agregat utama")] + [(g, GRP_S[g]) for g in ["comm", "sec2", "sec1", "noncomm", "eu1", "eu2", "eu3"]]:
        r = A.loc[i] if i in A.index else ak.loc[i]
        rows.append([nm, idn(r.pF, 3), idn(r.pt, 3), "ya" if r.coint10 == 1 else "tidak",
                     (idn(r.p_lm12, 2), DARKOR if r.p_lm12 < .05 else "000000"),
                     (idn(r.p_arch12, 2), DARKOR if r.p_arch12 < .05 else "000000")])
    table(s, 44, 94, 440, rows, [1.7, 0.7, 0.7, 0.8, 0.8, 0.8], size=11.5, row_h=27)
    plabel(s, X2, 88, W2, "~Stability test~ CUSUM, model agregat utama", [("(garis di dalam ~confidence band~ 95% = koefisien stabil)", False, None)])
    pic(s, f"{D1}/cusum_agregat.png", X2, 128, W2, 290)
    pointers(s, [
        [("~Bounds test~: ", True, None), ("p F dan p t untuk batas I(1); hubungan ~long-run~ (~cointegration~) ada bila "
                                           "keduanya < 0,10.", False, None)],
        [("Residual: ", True, None), ("LM(12) dan ARCH(12) p > 0,05 berarti tidak ada ~autocorrelation~ atau ~heteroskedasticity~. "
                                      "Semua model kelompok lolos.", False, None)],
    ], y=346, w=440, h=120, size=11)
    note(s, "Diagnostik per mitra di Lampiran C.", y=486, h=18, w=440)
    source(s, "Estimasi penulis")

    lab = {"A1_main": "Utama (Indonesia–dunia, AIC)", "A2_bic": "Lag dipilih BIC", "A3_trend": "Dengan ~linear trend~",
           "A4_lag6": "~Maximum lag~ 6", "A5_nocom": "Tanpa harga komoditas", "A6_pre2020": "Sampel 2006–2019",
           "A7_jisdor": "Kurs nominal JISDOR (2013+)", "A7b_reer2013": "REER, sampel 2013+",
           "A10_10mitra": "Jumlah 10 mitra (bukan dunia)", "A11_imf": "Indeks komoditas IMF (bukan BCOM)",
           "A12_gdp": "Dengan PDB riil Indonesia"}
    s = content(prs, "~Robustness~ ARDL: tidak satu pun dari 11 spesifikasi menunjukkan perbaikan neraca yang signifikan",
                notes="Model utama kami ubah dengan sebelas cara: memilih lag dengan kriteria lain, menambah tren, memotong "
                      "sampel, memakai kurs nominal, mengganti indeks komoditas, dan menambah PDB domestik. Tidak ada satu "
                      "pun yang menunjukkan perbaikan neraca yang signifikan. Satu-satunya efek ~long-run~ yang signifikan "
                      "justru negatif.")
    rows = [["Spesifikasi", "Bulan 6", "Bulan 12", "~Long-run~", "p", "~Cointegration~", "LM p"]]
    for i, nm in lab.items():
        r = A.loc[i]
        rows.append([nm, idn(r.eff10_m6), idn(r.eff10_m12), idn(r.eff10_lr), idn(r.lr_p, 2),
                     "ya" if r.coint10 == 1 else "tidak", idn(r.p_lm12, 2)])
    table(s, 44, 94, 872, rows, [3, 1, 1, 1.3, 0.8, 1.1, 0.8], size=11.5, row_h=24)
    pointers(s, [
        "Semua 11 spesifikasi memberi efek negatif di bulan 6 dan 12: arah hasil tidak bergantung pada pilihan model.",
        f"Satu-satunya efek ~long-run~ yang signifikan (REER sampel 2013+, {idn(A.loc['A7b_reer2013', 'eff10_lr'])}%, p = "
        f"{idn(A.loc['A7b_reer2013', 'lr_p'], 2)}) justru negatif: neraca memburuk.",
    ], y=392, h=78, size=11.5)
    source(s, "Estimasi penulis")

    s = content(prs, "~Robustness~ lain: tidak ada ~asymmetry~, efek antar mitra heterogen, dan instrumen USD lemah",
                notes="Pemeriksaan tambahan. NARDL menguji apakah depresiasi dan apresiasi berpengaruh berbeda; hasilnya tidak. "
                      "Panel PMG dan MG menguji apakah efek sama untuk semua mitra; ~Hausman test~ menolak itu, jadi efek memang "
                      "berbeda per mitra. Kami juga mencoba instrumen indeks dolar AS, tetapi instrumen itu terlalu lemah "
                      "sehingga tidak dipakai.")
    na = lambda t, c: nardl.loc[t, c]
    rows = [["Uji", "Hasil", "Kesimpulan"],
            ["NARDL: apresiasi vs depresiasi", f"LR apresiasi {idn(na('LR:reer_app', 'b'), 2)} (p = {idn(na('LR:reer_app', 'p'), 2)}); "
             f"depresiasi {idn(na('LR:reer_dep', 'b'), 2)} (p = {idn(na('LR:reer_dep', 'p'), 2)}); ~symmetry test~ p = "
             f"{idn(na('Wald LR simetri (F)', 'p'), 2)}", "~Symmetric~"],
            ["Panel PMG (efek sama antar mitra)", f"~Long-run~ {idn(pmg.loc['PMG', 'eff10_lr'])}% (p = {idn(pmg.loc['PMG', 'lr_reer_p'], 2)})",
             "Tidak signifikan"],
            ["Panel MG (efek berbeda per mitra)", f"~Long-run~ {idn(pmg.loc['MG', 'eff10_lr'])}% (p = {idn(pmg.loc['MG', 'lr_reer_p'], 2)}); "
             f"Hausman p = {idn(pmg.loc['MG', 'hausman_p'], 3)}", "MG dipilih; tidak signifikan"],
            ["LP panel tanpa Vietnam (CPI pendekatan)", f"Bulan 12: {idn(lpv('B3_novnm', 'PANEL', 12))}% vs {idn(lpv('B1_panel', 'PANEL', 12))}% "
             "dengan Vietnam", "Tidak berubah"],
            ["LP-IV, instrumen indeks dolar AS", f"F ~first stage~ = {idn(LPIV_F, 2)} (batas aman ≥ 10)", "~Weak instrument~, tidak dipakai"],
            ["Persamaan ekspor dan impor terpisah", f"Ekspor LR {idn(A.loc['A8_exports', 'eff10_lr'])}% (p = {idn(A.loc['A8_exports', 'lr_p'], 2)}); "
             f"impor LR {idn(A.loc['A9_imports', 'eff10_lr'])}% (p = {idn(A.loc['A9_imports', 'lr_p'], 2)})", "Tidak ~cointegrated~"]]
    table(s, 44, 94, 872, rows, [2.2, 3.5, 1.7], align=[L, L, L], size=11.5, row_h=36)
    pointers(s, [
        [("~Asymmetry~: ", True, None), ("depresiasi tidak lebih berpengaruh daripada apresiasi, berbeda dari temuan NARDL "
                                      "bilateral Bahmani-Oskooee & Harvey (2019).", False, None)],
        [("~Heterogeneity~: ", True, None), ("Hausman menolak PMG; rata-rata panel ≈ 0 menyembunyikan China dan Jepang yang "
                                           "memburuk.", False, None)],
        [("~Endogeneity~ agregat: ", True, None), ("belum tertangani penuh; kandidat ~instrument~ berikutnya adalah ~US "
                                                 "monetary policy shock~ (~high-frequency~).", False, None)],
    ], y=362, h=104, size=11.5)
    source(s, "Estimasi penulis")


    # =========================================================================
    s = content(prs, "Kesimpulan dan implikasi",
                notes="Empat pesan utama. Pertama, depresiasi tidak memperbaiki neraca perdagangan Indonesia, dan syarat "
                      "Marshall-Lerner tidak terpenuhi bahkan bila diukur dengan volume. Kedua, harga komoditas dan permintaan "
                      "domestik jauh lebih menentukan daripada kurs. Ketiga, neraca memburuk lewat volume ekspor yang turun dan "
                      "harga komoditas yang ikut jatuh. Keempat, channel volume hanya bekerja untuk barang konsumsi, dan lambat, "
                      "sehingga pelemahan rupiah bukan alat yang efektif untuk memperbaiki neraca.")
    numbered(s, [
        ("Depresiasi tidak memperbaiki neraca perdagangan Indonesia",
         "Rasio ekspor/impor turun sekitar 9–10% dalam 6–12 bulan setelah depresiasi riil 10% (ARDL dan LP) dan tidak pulih. Tidak "
         "ada J-curve; Marshall-Lerner tidak terpenuhi, juga bila diukur dengan elastisitas volume (εX + εM < 0)."),
        ("Harga komoditas dan permintaan domestik lebih menentukan daripada kurs",
         "BCOM menjelaskan sekitar 70% variasi ekspor; PDB domestik paling berkaitan dengan rasio X/M; depresiasi < 6%."),
        ("Neraca memburuk lewat volume ekspor dan harga komoditas",
         "Volume ekspor turun alih-alih naik; ~terms of trade~ komoditas dan mitra China memburuk. Energi & tambang, barang "
         "modal, China, dan Jepang paling terdampak."),
        ("Channel volume hanya bekerja untuk barang konsumsi, dan lambat",
         "Barang konsumsi (serta pertanian dan manufaktur di bulan 24) membaik lewat volume. Kebijakan lebih efektif bila "
         "menyasar substitusi impor input dan diversifikasi ekspor ke barang yang sensitif harga."),
    ], step=84)
    pointers(s, [
        [("Keterbatasan: ", True, None), ("~endogeneity~ agregat belum tertangani penuh; unit value per kg untuk barang "
                                          "manufaktur ikut mencerminkan komposisi; data kuantitas hanya 10 mitra (71%); CPI "
                                          "Vietnam dan PDB bulanan masih pendekatan.", False, None)],
        [("Langkah lanjutan: ", True, None), ("identifikasi ~shock~ kurs (SVAR ~sign restrictions~ atau ~US monetary policy "
                                              "shock~) untuk memisahkan efek kurs dari ~reverse causality~.",
                                              False, None)],
    ], y=436, head="", size=11)

    prs.slides.add_slide(layout(prs, "Closing_DEN_bhs"))

    # =========================================================================
    section(prs, "", "Lampiran")

    s = content(prs, "Lampiran A1 · Glosarium istilah umum",
                notes="Glosarium ini untuk pembaca yang tidak berlatar ekonomi. Lampiran A1 berisi istilah perdagangan dan kurs; "
                      "A2 dan A3 berisi istilah ekonometrika; A4 berisi istilah teori, harga-volume, dan cara membaca hasil. "
                      "Setiap istilah dijelaskan dengan bahasa sehari-hari, tanpa rumus.")
    table(s, 44, 92, 872, [
        ["Istilah", "Arti sederhana"],
        ["Neraca perdagangan", "Ekspor dikurangi impor. Positif = surplus, negatif = defisit."],
        ["Rasio ekspor/impor (X/M)", "Ekspor dibagi impor. Di atas 1 = surplus. Dipakai dalam bentuk logaritma: ln(X/M)."],
        ["Depresiasi nominal", "Rupiah melemah terhadap mata uang lain, misalnya dari Rp15.000 ke Rp16.500 per USD (10%)."],
        ["Depresiasi riil", "Depresiasi nominal setelah memperhitungkan perbedaan inflasi; mengukur perubahan daya saing harga."],
        ["REER", "~Real effective exchange rate~: kurs riil rupiah terhadap rata-rata tertimbang mitra dagang. Naik = rupiah menguat."],
        ["Kurs riil bilateral", "Kurs riil rupiah terhadap satu mitra tertentu, misalnya terhadap yuan."],
        ["BCOM", "Bloomberg Commodity Index: indeks harga komoditas dunia (energi, logam, pertanian)."],
        ["HS-6", "~Harmonized System~ 6 digit: kode internasional untuk sekitar 6.900 jenis barang yang diperdagangkan."],
        ["SITC, BEC, UNCTAD", "Klasifikasi PBB: SITC untuk sifat barang, BEC untuk penggunaan (konsumsi, bahan baku, modal)."],
        ["Episode depresiasi", "Periode rupiah melemah ≥10% dari titik terendah sampai puncaknya (definisi riset ini)."],
        ["~Dominant currency~", "Perdagangan dunia sebagian besar dihargai dalam USD, sehingga kurs rupiah tidak mengubah harga ekspor."],
        ["~Pass-through~", "Seberapa besar perubahan kurs diteruskan ke harga barang ekspor atau impor."],
        ["~Channel~", "Jalur atau mekanisme yang membuat depresiasi memengaruhi neraca, misalnya lewat impor mesin."],
    ], [1.6, 5.4], align=[L, L], size=10.5, row_h=29)
    source(s, "Disusun penulis")

    s = content(prs, "Lampiran A2 · Glosarium ekonometrika (1/2)",
                notes="Istilah ekonometrika bagian pertama: ukuran kekuatan hubungan (elastisitas, R², p-value, confidence "
                      "interval), sifat data (stationary, unit root, cointegration), dan istilah dalam model ARDL.")
    table(s, 44, 92, 872, [
        ["Istilah", "Arti sederhana"],
        ["Elastisitas", "Persentase perubahan suatu variabel bila variabel lain berubah 1%."],
        ["R²", "Persentase naik-turunnya satu variabel yang sejalan dengan variabel lain (0–100%)."],
        ["p-value", "Peluang hasil sebesar itu muncul kebetulan bila sebenarnya tidak ada efek. p < 0,10 dianggap signifikan."],
        ["~Confidence interval~ (CI)", "Rentang nilai yang kemungkinan besar memuat efek sebenarnya; 90% CI dipakai di grafik LP."],
        ["~Stationary~, I(0), I(1)", "~Stationary~ = rata-rata dan variasinya stabil. I(0) ~stationary~ di level; I(1) ~stationary~ setelah ~first difference~."],
        ["~Unit root test~ (ADF, PP)", "Uji untuk menentukan apakah variabel ~stationary~."],
        ["~Cointegration~", "Dua variabel ~non-stationary~ yang bergerak bersama dalam ~long-run~."],
        ["ARDL", "~Autoregressive distributed lag~: regresi yang memakai nilai masa lalu ~dependent variable~ dan penjelas."],
        ["~Bounds test~", "Uji ada-tidaknya hubungan ~long-run~ dalam ARDL (Pesaran dkk. 2001)."],
        ["~Error correction~ (ADJ)", "Kecepatan neraca kembali ke ~equilibrium~ ~long-run~ setiap bulan."],
        ["~Dynamic multiplier~", "Jalur efek kumulatif depresiasi dari bulan ke bulan, dihitung dari koefisien ARDL."],
        ["NARDL", "ARDL nonlinear: memisahkan efek depresiasi dan apresiasi."],
        ["AIC / BIC", "Kriteria otomatis untuk memilih panjang lag; BIC cenderung memilih model lebih sederhana."],
    ], [1.6, 5.4], align=[L, L], size=10.5, row_h=29)
    source(s, "Disusun penulis")

    s = content(prs, "Lampiran A3 · Glosarium ekonometrika (2/2)",
                notes="Istilah ekonometrika bagian kedua: local projections dan data panel, masalah endogeneity dan cara "
                      "mengatasinya dengan instrument, serta uji-uji diagnostik untuk memeriksa apakah model layak.")
    table(s, 44, 92, 872, [
        ["Istilah", "Arti sederhana"],
        ["Local projections (LP)", "Satu regresi untuk tiap horizon (bulan 0, 1, …, 24) untuk melihat respons dari waktu ke waktu."],
        ["~Impulse response~", "Respons suatu variabel dari waktu ke waktu setelah satu ~shock~, misalnya depresiasi."],
        ["~Fixed effects~", "~Dummy variable~ yang menyerap faktor yang sama untuk semua mitra di bulan yang sama (~common shock~, misalnya harga komoditas)."],
        ["Panel", "Data yang menggabungkan banyak unit (10 mitra) dan banyak periode (bulan)."],
        ["PMG / MG", "Estimator panel: PMG mengasumsikan efek ~long-run~ sama untuk semua mitra, MG membiarkannya berbeda."],
        ["~Hausman test~", "Uji untuk memilih antara PMG dan MG."],
        ["~Endogeneity~", "Masalah ketika variabel penjelas ikut dipengaruhi ~dependent variable~ atau faktor lain yang sama."],
        ["~Instrument~ / LP-IV", "Variabel luar yang memengaruhi kurs tetapi tidak langsung memengaruhi neraca, untuk mengatasi ~endogeneity~."],
        ["F ~first stage~", "Ukuran kekuatan ~instrument~; di bawah 10 dianggap ~weak instrument~."],
        ["Newey-West, Driscoll-Kraay", "Cara menghitung ~standard error~ yang tahan terhadap korelasi antar waktu (dan antar mitra)."],
        ["~LM test~, ~ARCH test~", "Uji apakah ~residual~ masih berpola (~autocorrelation~) atau variansnya berubah-ubah (~heteroskedasticity~)."],
        ["CUSUM", "~Stability test~ koefisien sepanjang waktu."],
        ["~Robustness check~", "Mengulang estimasi dengan asumsi berbeda untuk memastikan hasil tidak bergantung pada satu pilihan."],
    ], [1.6, 5.4], align=[L, L], size=10.5, row_h=29)
    source(s, "Disusun penulis")

    s = content(prs, "Lampiran A4 · Glosarium teori, harga-volume, dan cara membaca hasil",
                notes="Glosarium terakhir berisi istilah teori dan istilah yang muncul di bagian harga dan volume, ditambah "
                      "istilah untuk membaca tabel dan grafik hasil.")
    table(s, 44, 92, 872, [
        ["Istilah", "Arti sederhana"],
        ["Marshall-Lerner", "Syarat agar depresiasi memperbaiki neraca: jumlah elastisitas volume ekspor dan impor lebih dari 1."],
        ["J-curve", "Pola neraca yang turun dulu setelah depresiasi (harga bergerak lebih cepat) lalu naik melewati posisi awal."],
        ["~Terms of trade~ (ToT)", "Harga ekspor dibagi harga impor (Px/Pm). Turun = setiap unit ekspor membeli lebih sedikit impor."],
        ["~Unit value~", "Nilai dibagi kuantitas, misalnya USD per kg. Dipakai sebagai ukuran harga per kode HS-6."],
        ["Indeks Fisher", "Rata-rata indeks Laspeyres (bobot tahun basis) dan Paasche (bobot bulan berjalan); dipakai BPS dan IMF."],
        ["Volume implisit", "Indeks nilai dibagi indeks harga: ukuran jumlah barang yang diperdagangkan."],
        ["Dekomposisi", "Memecah perubahan rasio X/M menjadi ~terms of trade~ (harga) dan rasio volume; keduanya dijumlah persis."],
        ["~Shock~ / ~common shock~", "Kejadian mendadak, misalnya rupiah melemah; ~common shock~ = yang menimpa semua mitra sekaligus."],
        ["~Reverse causality~", "Arah sebab-akibat terbalik: neraca yang memburuk membuat rupiah melemah, bukan sebaliknya."],
        ["~Research gap~", "Pertanyaan yang belum dijawab studi sebelumnya dan menjadi kontribusi riset ini."],
        ["Horizon (bulan ke-h)", "Jarak waktu sejak rupiah melemah; bulan 0 = bulan yang sama, bulan 12 = setahun kemudian."],
        ["Signifikan 10% (*)", "p-value < 0,10: efeknya cukup kecil kemungkinannya muncul kebetulan. Angka tanpa * dibaca hati-hati."],
        ["~Interquartile range~", "Rentang tempat separuh observasi di tengah berada (antara kuartil 25% dan 75%)."],
        ["~Outlier~", "Observasi ekstrem yang dibuang agar tidak mendistorsi indeks, misalnya harga naik lebih dari 4 kali."],
    ], [1.6, 5.4], align=[L, L], size=10.5, row_h=27.5)
    source(s, "Disusun penulis")

    def ardl_rows(df, ids, labels):
        rows = [["Model", "Lag", "N", "p bounds (F/t)", "ADJ", "Bulan 0", "Bulan 12", "~Long-run~ (p)", "LM p", "ARCH p"]]
        df = df.set_index("id")
        for i, lb in zip(ids, labels):
            r = df.loc[i]
            if r.lags == "gagal":
                rows.append([lb, "gagal"] + [""] * 8); continue
            rows.append([lb, r.lags, f"{int(r.N)}", f"{idn(r.pF, 2)} / {idn(r.pt, 2)}", idn(r.adj, 2), idn(r.eff10_sr0),
                         idn(r.eff10_m12), f"{idn(r.eff10_lr)} ({idn(r.lr_p, 2)})", idn(r.p_lm12, 2), idn(r.p_arch12, 2)])
        return rows

    colw = [2.6, 1.3, 0.55, 1.3, 0.75, 0.8, 0.85, 1.5, 0.65, 0.7]
    s = content(prs, "Lampiran B · ARDL agregat: semua spesifikasi",
                notes="Jumlah observasi berbeda antar model karena tiga hal: panjang ~maximum lag~, pemotongan sampel, dan "
                      "ketersediaan data variabel kontrol.")
    ids = list(ardl_ag.id)
    labs = [lab.get(i, {"A8_exports": "ln ekspor (bukan rasio)", "A9_imports": "ln impor (bukan rasio)"}.get(i, i)) for i in ids]
    table(s, 44, 92, 872, ardl_rows(ardl_ag, ids, labs), colw, size=10, row_h=22)
    pointers(s, [
        [("~Maximum lag~: ", True, None), ("12 bulan pertama terpakai untuk lag, sehingga sampel 2006m1–2026m6 menjadi 234 bulan. "
                                          "Dengan ~maximum lag~ 6, hanya 6 bulan terpakai (240).", False, None)],
        [("Pemotongan sampel: ", True, None), ("sampel 2006–2019 (156); JISDOR baru tersedia Jun 2013 (145 dan 157).", False, None)],
        [("Data kontrol: ", True, None), ("tanpa BCOM, sampel bisa sampai Agu 2026 (236); indeks IMF tersedia s.d. Sep 2026 (236); "
                                          "PDB mulai Mar 2006 (238).", False, None)],
    ], y=404, h=96, head="Mengapa jumlah observasi (N) berbeda", size=10.5)
    source(s, "Estimasi penulis")

    s = content(prs, "Lampiran C · ARDL per mitra dagang dan per kelompok barang",
                notes="Tabel lengkap ARDL untuk tiap mitra dan tiap kelompok barang. Kolom Lag menunjukkan panjang lag yang "
                      "dipilih AIC untuk tiap variabel; p bounds menunjukkan ada tidaknya hubungan long-run; ADJ adalah kecepatan "
                      "koreksi per bulan. N energi lebih kecil karena harga batu bara baru tersedia sejak 2009.")
    ids = list(ardl_mi.id)
    gids = ["comm", "sec2", "sec1", "noncomm", "eu1", "eu2", "eu3"]
    rows = ardl_rows(ardl_mi, ids, [CTRY[i] for i in ids]) + ardl_rows(ardl_kg, gids, [GRP[g] for g in gids])[1:]
    table(s, 44, 92, 872, rows, colw, size=10, row_h=22)
    note(s, "Mitra: REER multilateral (BIS) yang sama untuk semua mitra. Kelompok: Indonesia–dunia; energi memakai harga batu bara "
            "(tersedia sejak 2009, sehingga N = 198), pertanian memakai CPO.", y=492, h=22, w=560)
    source(s, "Estimasi penulis")

    s = content(prs, "Lampiran D · Local projections: efek per horizon",
                notes="Angka lengkap local projections untuk setiap horizon. Satu baris adalah satu model; satu kolom adalah "
                      "jarak waktu sejak rupiah melemah. Jumlah observasi makin kecil di horizon yang lebih jauh, karena "
                      "respons bulan ke-24 membutuhkan data 24 bulan setelah setiap titik awal.")
    rows = [["Model", "Bulan 0", "Bulan 3", "Bulan 6", "Bulan 12", "Bulan 18", "Bulan 24"]]
    spec = [("A1_ols", "AGG", "Agregat Indonesia–dunia"), ("B1_panel", "PANEL", "Panel 10 mitra (rata-rata)"),
            ("B3_novnm", "PANEL", "Panel tanpa Vietnam")] + [("B2_partner", c, CTRY[c]) for c in CTRY] + \
           [("C_group", g, GRP[g]) for g in gids]
    for m, i, lb in spec:
        rows.append([lb] + [sig(lpv(m, i, h), lpv(m, i, h, "p")) for h in (0, 3, 6, 12, 18, 24)])
    table(s, 44, 90, 872, rows, [3, 1, 1, 1, 1, 1, 1], size=9.5, row_h=19)
    note(s, "* signifikan 10%. Efek dalam % rasio X/M per depresiasi riil 10%. N berkurang di horizon yang lebih jauh: respons "
            "bulan ke-h membutuhkan data h bulan setelah titik awal (agregat: N = 233 di bulan 0, 211 di bulan 24).", y=497, h=18, w=740)
    source(s, "Estimasi penulis")

    s = content(prs, "Lampiran E · Dekomposisi harga vs volume: efek per horizon",
                notes="Angka lengkap dekomposisi harga dan volume. Untuk setiap model, baris rasio X/M sama dengan jumlah "
                      "terms of trade dan rasio volume, karena semua persamaan memakai kontrol yang sama.")
    rows = [["Model", "Variabel", "Bulan 0", "Bulan 6", "Bulan 12", "Bulan 18", "Bulan 24"]]
    VL = {"lnxm": "Rasio X/M", "lntot": "~Terms of trade~ Px/Pm", "lnqxm": "Rasio volume Qx/Qm", "lnpx": "Harga ekspor Px",
          "lnqx": "Volume ekspor Qx", "lnpm": "Harga impor Pm", "lnqm": "Volume impor Qm"}
    for v in VL:
        rows.append(["Agregat 10 mitra" if v == "lnxm" else "", VL[v]] + [pvs("P_agg", "AGG10", v, h) for h in (0, 6, 12, 18, 24)])
    for v in ["lnxm", "lntot", "lnqxm"]:
        rows.append(["Panel 10 mitra" if v == "lnxm" else "", VL[v]] + [pvs("Q_panel", "PANEL", v, h) for h in (0, 6, 12, 18, 24)])
    for c in ["CHN", "JPN", "THA"]:
        for v in ["lntot", "lnqxm"]:
            rows.append([CTRY[c] if v == "lntot" else "", VL[v]] + [pvs("Q_partner", c, v, h) for h in (0, 6, 12, 18, 24)])
    table(s, 44, 88, 872, rows, [1.6, 2, 1, 1, 1, 1, 1], align=[L, L, R, R, R, R, R], size=9, row_h=19)
    note(s, "* signifikan 10%. % per depresiasi riil 10%; harga impor dan volume impor positif = naik (memperburuk neraca). "
            "Kontrol: lag 1–6 keempat komponen, kurs, BCOM, IPI mitra, ~seasonal dummy~, krisis.", y=498, h=18, w=740)
    source(s, "Estimasi penulis")

    out = f"{OUT}/Depresiasi_Rupiah_Trade_Balance.pptx"
    try:
        prs.save(out)
    except PermissionError:
        out = out.replace(".pptx", "_baru.pptx")
        prs.save(out)
        print("PERHATIAN: file lama sedang terbuka, disimpan sebagai", out)
    print("tersimpan:", out, "| slide:", len(prs.slides))


if __name__ == "__main__":
    build()
