"""
09_build_ppt.py : deck hasil riset (template DEN, mengikuti deck Banking Stress Test)

Urutan: alur penelitian -> 01 teori & literatur -> 02 pertanyaan & fakta -> 03 metodologi & data
        -> 04 hasil ekonometrika -> 05 diagnostik & robustness -> kesimpulan -> lampiran (glosarium, tabel)

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


def sig(e, p):
    if e is None or (isinstance(e, float) and np.isnan(e)):
        return "–"
    return (idn(e) + star(p), DARKOR if (p is not None and not np.isnan(p) and p < 0.10) else "000000")


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
    fig, (ax, bx, cx) = plt.subplots(3, 1, figsize=(6.4, 5.2), sharex=True, gridspec_kw={"height_ratios": [1, 1, 1]})
    for r in eps.itertuples():
        st, en = pd.to_datetime(r.mulai, format="%b %Y"), pd.to_datetime(r.puncak, format="%b %Y")
        st = max(st, s.index[0])
        for x in (ax, bx, cx):
            x.axvspan(st, en, color=C(ORANGE), alpha=0.18, lw=0)
        ax.text(st + (en - st) / 2, s.max() * 1.01, EP_SHORT[r.episode], ha="center", va="bottom", fontsize=8,
                color="#404040")
    ax.plot(s.index, s.values, color=C(BROWN), lw=1.8)
    ax.set_ylim(s.min() * 0.95, s.max() * 1.10)
    ax.set_ylabel("Rp per USD", fontsize=10)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:,.0f}".replace(",", ".")))
    bx.axhline(0, color="#404040", lw=0.9)
    bx.fill_between(tb.index, tb.values, 0, where=tb.values >= 0, color=C(ORANGE), alpha=0.55, lw=0)
    bx.fill_between(tb.index, tb.values, 0, where=tb.values < 0, color=C(BROWN), alpha=0.7, lw=0)
    bx.plot(tb.index, tb.values, color="#404040", lw=0.8)
    bx.set_ylabel("Neraca, USD miliar/bln", fontsize=10)
    cx.plot(bcom.index, bcom.values, color=C(BROWN), lw=1.8)
    cx.set_ylabel("BCOM (indeks)", fontsize=10)
    fig.tight_layout(h_pad=0.6)
    return save(fig, "episode_timeline")


def fig_event():
    fig, ax = plt.subplots(figsize=(4.3, 3.0))
    for e, g in ev.groupby("episode"):
        ax.plot(g.k, g.xm_idx, color=C(MUTED), lw=0.9, alpha=0.8)
    m = ev.groupby("k").xm_idx.mean()
    ax.plot(m.index, m.values, color=C(ORANGE), lw=3, label="Rata-rata 8 episode")
    ax.axhline(100, color="#404040", lw=0.9)
    ax.axvline(0, color="#7F7F7F", lw=0.9, ls="--")
    ax.set_xticks(range(-6, 25, 6))
    ax.set_xlabel("Bulan sejak awal episode depresiasi")
    ax.plot([], [], color=C(MUTED), lw=0.9, label="Tiap episode")
    ax.legend(frameon=False, fontsize=9, loc="lower left")
    return save(fig, "episode_event")


def fig_drivers():
    order = ["Depresiasi riil (REER)", "Harga komoditas (BCOM)", "Permintaan mitra (IPI)", "PDB riil Indonesia"]
    lab = ["Depresiasi\nriil", "Harga\nkomoditas", "Permintaan\nmitra", "PDB riil\nIndonesia"]
    fig, ax = plt.subplots(figsize=(4.4, 3.0))
    x = np.arange(4)
    for k, (y, c) in enumerate([("Ekspor", BROWN), ("Impor", MUTED), ("Rasio X/M", ORANGE)]):
        v = drv[drv.y == y].set_index("driver").loc[order].r2 * 100
        ax.bar(x + (k - 1) * 0.27, v, width=0.26, color=C(c), label=y)
        for xi, vi in zip(x + (k - 1) * 0.27, v):
            ax.text(xi, vi + 1, f"{vi:.0f}", ha="center", fontsize=8.5, color="#404040")
    ax.set_xticks(x); ax.set_xticklabels(lab)
    ax.set_ylabel("R² (%)")
    ax.grid(axis="x", visible=False)
    ax.legend(frameon=False, fontsize=9, loc="upper right")
    return save(fig, "driver_r2")


def fig_scatter():
    fig, axs = plt.subplots(1, 2, figsize=(4.4, 3.0))
    for ax, (xv, yv, xl, yl, c) in zip(axs, [("d_bcom", "d_x", "Δ BCOM (%)", "Δ ekspor (%)", ORANGE),
                                             ("d_dep", "d_xm", "Δ depresiasi riil (%)", "Δ rasio X/M (%)", BROWN)]):
        ax.scatter(sct[xv], sct[yv], s=9, color=C(c), alpha=0.7, lw=0)
        b = np.polyfit(sct[xv], sct[yv], 1)
        xx = np.linspace(sct[xv].min(), sct[xv].max(), 10)
        ax.plot(xx, np.polyval(b, xx), color="#404040", lw=1.2)
        ax.set_title(f"r = {sct[xv].corr(sct[yv]):.2f}".replace(".", ","), fontsize=10, color="#404040")
        ax.set_xlabel(xl, fontsize=9.5); ax.set_ylabel(yl, fontsize=9.5)
    fig.tight_layout(w_pad=1.2)
    return save(fig, "driver_scatter")


def fig_heat(df, rows, rowlab, name, figsize):
    piv = df.pivot(index=df.columns[0], columns="episode", values="d_xm_12m").loc[rows, list(eps.episode)]
    piv.columns = [EP_SHORT[c] for c in piv.columns]
    piv["Rata-rata"] = piv.mean(axis=1)
    fig, ax = plt.subplots(figsize=figsize)
    v = piv.values.astype(float)
    ax.imshow(np.clip(v, -50, 50), cmap=CMAP, vmin=-50, vmax=50, aspect="auto")
    for i in range(v.shape[0]):
        for j in range(v.shape[1]):
            if not np.isnan(v[i, j]):
                ax.text(j, i, f"{v[i, j]:.0f}".replace("-", "−"), ha="center", va="center", fontsize=8.5,
                        fontweight="bold" if j == v.shape[1] - 1 else "normal", color="#262626")
    ax.set_xticks(range(v.shape[1])); ax.set_xticklabels(piv.columns, fontsize=8.5)
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


def fig_ardl_jcurve():
    fig, ax = plt.subplots(figsize=(4.3, 2.9))
    d = dm_ag[dm_ag.h <= 24]
    for id_, c, ls, lab in [("A2_bic", BROWN, "--", "Lag BIC"), ("A10_10mitra", MUTED, ":", "10 mitra"),
                            ("A1_main", ORANGE, "-", "Utama (dunia)")]:
        s = d[d.id == id_]
        ax.plot(s.h, s.eff10, color=C(c), ls=ls, lw=2.6 if id_ == "A1_main" else 1.5, label=lab)
    ax.axhline(0, color="#7F7F7F", lw=0.9)
    ax.set_xticks(range(0, 25, 6)); ax.set_xlabel("Bulan setelah depresiasi")
    ax.legend(frameon=False, fontsize=9, loc="lower left")
    return save(fig, "ardl_jcurve")


def fig_lp_line():
    s = lp[(lp.model == "A1_ols") & (lp.id == "AGG")].sort_values("h")
    fig, ax = plt.subplots(figsize=(4.3, 2.9))
    ax.fill_between(s.h, s.lo90, s.hi90, color=C(ORANGE), alpha=0.22, lw=0, label="90% confidence interval")
    ax.plot(s.h, s.eff, color=C(ORANGE), lw=2.6, label="Estimasi")
    ax.axhline(0, color="#7F7F7F", lw=0.9)
    ax.set_xticks(range(0, 25, 6)); ax.set_xlabel("Bulan setelah depresiasi")
    ax.legend(frameon=False, fontsize=9, loc="lower left")
    return save(fig, "lp_agregat")


def fig_bar_partner():
    d = lp[(lp.model == "B2_partner") & (lp.h == 12)].copy()
    d["lab"] = d.id.map(CTRY)
    d = d.sort_values("eff")
    fig, ax = plt.subplots(figsize=(4.3, 3.1))
    ax.barh(d.lab, d.eff, color=[C(ORANGE) if p < .1 else C(MUTED) for p in d.p], height=0.62)
    ax.errorbar(d.eff, d.lab, xerr=[d.eff - d.lo90, d.hi90 - d.eff], fmt="none", ecolor="#595959",
                elinewidth=0.9, capsize=2)
    ax.axvline(0, color="#404040", lw=0.9); ax.grid(axis="y", visible=False)
    ax.set_xlabel("Perubahan rasio X/M (%), bulan ke-12")
    return save(fig, "lp_mitra12")


def fig_group_two():
    d = lp[(lp.model == "C_group") & (lp.h.isin([12, 24]))].copy()
    d["lab"] = d.id.map(GRP_S)
    order = d[d.h == 24].sort_values("eff").lab.tolist()
    fig, ax = plt.subplots(figsize=(4.3, 3.1))
    y = np.arange(len(order))
    for h, off, base, light in [(12, 0.19, BROWN, "D9C3BA"), (24, -0.19, ORANGE, "F7D9A8")]:
        s = d[d.h == h].set_index("lab").loc[order]
        ax.barh(y + off, s.eff, height=0.36, color=[C(base) if p < .1 else C(light) for p in s.p])
    ax.set_yticks(y); ax.set_yticklabels(order)
    ax.axvline(0, color="#404040", lw=0.9); ax.grid(axis="y", visible=False)
    ax.set_xlabel("Perubahan rasio X/M (%)")
    ax.legend(handles=[Patch(color=C(BROWN), label="bulan ke-12"), Patch(color=C(ORANGE), label="bulan ke-24")],
              frameon=False, fontsize=9, loc="lower right")
    return save(fig, "lp_kelompok")


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


def box(slide, x, y, w, h, head, desc, num, fill=CREAM, accent=BROWN):
    """kartu tahap: nomor, judul tebal, deskripsi"""
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Pt(x), Pt(y), Pt(w), Pt(h))
    sh.fill.solid(); sh.fill.fore_color.rgb = rgb(fill)
    sh.line.fill.background()
    sh.shadow.inherit = False
    tbox(slide, x + 6, y + 4, w - 12, 30, num, size=20, color=accent, bold=True)
    tbox(slide, x + 6, y + 34, w - 12, 40, [{"runs": [(head, True, "000000")]}], size=12.5)
    tbox(slide, x + 6, y + 76, w - 12, h - 80, desc, size=11, color=TXT)


def section(prs, num, text):
    s = prs.slides.add_slide(layout(prs, "SubTitle_DEN_bhs"))
    ph = s.placeholders[1]
    ph.text_frame.text = text
    for r in ph.text_frame.paragraphs[0].runs:
        r.font.size = Pt(26); r.font.bold = True
    if num:
        tbox(s, 45, 180, 200, 76, num, size=60, color=SECNUM, bold=True)


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

    # ---- outline
    s = content(prs, "Outline")
    cols = [("01", "Teori dan literatur", "Marshall-Lerner, J-curve, dan bukti untuk Indonesia"),
            ("02", "Pertanyaan dan fakta", "Pertanyaan penelitian, pemilihan mitra, dan 8 episode depresiasi rupiah"),
            ("03", "Metodologi dan data", "Literatur metode, klasifikasi HS-6, daftar variabel, dan spesifikasi model"),
            ("04", "Hasil ekonometrika", "Jawaban tiap pertanyaan: agregat, per mitra, per kelompok barang"),
            ("05", "Diagnostik dan robustness", "~Unit root test~, ~cointegration~, residual, dan ~alternative specification~")]
    for i, (n, h, d) in enumerate(cols):
        x = 44 + i * 176
        hline(s, x, 160, 160, color=BROWN, weight=2.5)
        tbox(s, x, 172, 160, 60, n, size=36, bold=True, color="000000")
        tbox(s, x, 240, 160, 56, h, size=16, bold=True, color="000000")
        tbox(s, x, 300, 160, 110, d, size=13, color=TXT)
    tbox(s, 44, 440, 872, 30, [[("Lampiran: ", True, None), ("glosarium istilah umum dan istilah ekonometrika, serta tabel "
                                                             "estimasi lengkap.", False, None)]], size=12.5, color=GREY)

    # ---- alur penelitian
    s = content(prs, "Alur penelitian: tujuh tahap dari data mentah sampai kesimpulan",
                notes="Slide ini adalah peta seluruh presentasi. Setiap tahap menjawab satu kebutuhan: data dan klasifikasi "
                      "menyiapkan bahan, statistik deskriptif memberi gambaran awal tanpa model, ~unit root test~ menentukan "
                      "metode yang sah, lalu dua metode estimasi saling mengecek, dan diagnostik memastikan hasilnya tidak "
                      "bergantung pada satu spesifikasi.")
    steps = [("1", "Data", "Ekspor-impor HS-6 bulanan 2006–2026 (ITC Trade Map); kurs, CPI (BIS); harga komoditas "
                           "(Bloomberg); IPI mitra (CEIC)."),
             ("2", "Klasifikasi", "6.883 kode HS-6 dipetakan ke 7 kelompok barang lewat tabel korespondensi resmi UNSD."),
             ("3", "Deskriptif", "8 episode depresiasi; perilaku neraca sebelum dan sesudahnya; faktor yang paling "
                                 "menggerakkan neraca."),
             ("4", "~Pre-estimation test~", "~Unit root test~ (ADF, PP) untuk memastikan ARDL sah dipakai."),
             ("5", "Estimasi ARDL", "Efek ~short-run~ dan panjang; uji J-curve dan Marshall-Lerner."),
             ("6", "Local projections", "Cek ulang dengan kurs riil bilateral dan ~fixed effects~ bulan."),
             ("7", "Diagnostik & robustness", "~Residual test~, stabilitas, dan 11 ~alternative specification~.")]
    bw = 118
    for i, (n, hd, ds) in enumerate(steps):
        x = 44 + i * (bw + 7.7)
        box(s, x, 96, bw, 190, hd, ds, n, accent=(DARKOR if i in (4, 5) else BROWN))
    sec = ["Bagian 02–03", "Bagian 03", "Bagian 02", "Bagian 05", "Bagian 04", "Bagian 04", "Bagian 05"]
    for i, t in enumerate(sec):
        tbox(s, 44 + i * (bw + 7.7), 290, bw, 18, t, size=10.5, color=GREY, align=PP_ALIGN.CENTER)
    pointers(s, [
        [("Dua metode, satu pertanyaan: ", True, None),
         ("ARDL adalah standar literatur J-curve, sehingga hasil kita bisa dibandingkan dengan studi Indonesia "
          "sebelumnya. Local projections dipakai sebagai pemeriksa independen karena tidak memaksa satu hubungan "
          "~long-run~ dan bisa menyerap guncangan global lewat ~fixed effects~.", False, None)],
        [("Statistik deskriptif datang sebelum model: ", True, None),
         ("kalau pola di data mentah dan hasil model sejalan, kesimpulannya lebih meyakinkan.", False, None)],
    ], y=320)

    # =========================================================================
    section(prs, "01", "Teori dan literatur")

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
        "Indonesia cenderung mirip Kasus B: ekspor batu bara, CPO, dan nikel dihargai dalam USD, sehingga rupiah yang murah "
        "tidak membuat ekspor lebih laku, sementara impor input sulit dikurangi (Tang 2002: elastisitas harga impor hanya −0,4).",
    ], x=X2, y=304, w=W2, h=100, head="Relevansi untuk Indonesia", size=11.5)
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

    s = content(prs, "Untuk Indonesia, bukti terbelah: sebagian studi menemukan efek, sebagian tidak",
                notes="Studi Indonesia memberi gambaran campuran. Beberapa menemukan J-curve atau Marshall-Lerner untuk mitra "
                      "tertentu, tetapi Wijaya (2020) secara tegas tidak menemukan keduanya untuk China dan Jepang, dua mitra "
                      "terbesar. Tang (2002) menunjukkan impor Indonesia tidak elastis terhadap harga. Research gap yang kami isi: "
                      "belum ada studi yang menggabungkan level dunia, mitra, dan kelompok barang HS-6 dalam satu kerangka, "
                      "dengan kontrol harga komoditas yang spesifik dan local projections sebagai cek ~endogeneity~.")
    table(s, 44, 94, 872, [
        ["Studi", "Data dan metode", "Temuan", "Efek kurs?"],
        ["Tang (2002), IIUM J. Econ. & Mgmt.", "Impor agregat; ARDL bounds test", "Elastisitas harga impor hanya −0,4",
         ("Lemah", BROWN)],
        ["Widarjono (2005), J. Indonesian Econ. & Business", "AS, Jepang, Singapura; 1988–2003; Johansen, VECM",
         "Marshall-Lerner dan J-curve hanya untuk Jepang", "Sebagian"],
        ["Bahmani-Oskooee & Harvey (2009), J. Econ. Integration", "13 mitra; ARDL", "J-curve pada 5 dari 13 mitra", "Sebagian"],
        ["Bahmani-Oskooee & Harvey (2019), New Zealand Econ. Papers", "Mitra utama; NARDL",
         "~Asymmetry~ ~long-run~ hanya di 5 model", "Sebagian"],
        ["Wijaya (2020), J. Dinamika Ekonomi Pembangunan", "China, Jepang, Singapura; 2010–2017; ECM",
         "Tidak ada J-curve dan Marshall-Lerner untuk China dan Jepang; ada untuk Singapura", ("Tidak (China, Jepang)", BROWN)],
        ["Rifami & Heriqbaldi (2023), Iranian Econ. Review", "50 industri, Indonesia–China; ARDL, NARDL",
         "J-curve di 2 industri (ARDL), 9 industri (NARDL)", "Sebagian"],
        ["Salim dkk. (2023), J. Business & Information Systems", "Indonesia–China 2002–2017; ARDL, NARDL",
         "J-curve hanya muncul dengan pendekatan nonlinear", "Sebagian"],
    ], [2.3, 2.2, 2.6, 1.1], align=[L, L, L, L], size=10.5, row_h=34)
    pointers(s, [
        [("Research gap: ", True, None),
         ("belum ada studi Indonesia yang menggabungkan level dunia, 10 mitra, dan 7 kelompok barang HS-6 dalam satu "
          "kerangka, dengan kontrol harga komoditas spesifik (BCOM, batu bara, CPO) dan local projections sebagai cek "
          "~endogeneity~.", False, None)],
    ], y=376, h=70, head="Posisi riset ini", size=12)
    source(s, "Studi yang dikutip di tabel; daftar pustaka di notes/4_litrev_metode.md")

    # =========================================================================
    section(prs, "02", "Pertanyaan penelitian dan fakta")

    s = content(prs, "Tiga pertanyaan penelitian dan hipotesisnya")
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

    fp, psh, tx, tm, tt = fig_partners()
    s = content(prs, f"Sepuluh mitra yang dianalisis mencakup {idn(tt, 0)}% perdagangan Indonesia selama 2006–2026",
                notes="Kami memilih sepuluh mitra dagang terbesar berdasarkan total nilai ekspor plus impor. Bersama-sama mereka "
                      "mewakili sekitar tujuh puluh persen perdagangan Indonesia, dan mencakup tiga tipe mitra yang berbeda: "
                      "pemasok input (China, Jepang, Korea), tujuan ekspor manufaktur (AS), dan mitra regional ASEAN.")
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

    s = content(prs, f"Delapan episode depresiasi 2007–2026: rupiah melemah {idn(E.dep_idr_usd.min(), 0)}–"
                     f"{idn(E.dep_idr_usd.max(), 0)}%, tetapi neraca tidak bergerak searah",
                notes="Panel atas menunjukkan kurs rupiah dengan delapan episode depresiasi yang diarsir. Panel bawah menunjukkan "
                      "neraca perdagangan bulanan dalam USD. Perhatikan bahwa neraca tidak selalu membaik setelah rupiah melemah: "
                      "di episode 2008 dan 2013 neraca justru jatuh ke defisit, sedangkan surplus besar 2021–2022 terjadi saat "
                      "harga komoditas melonjak. Ini petunjuk awal bahwa harga komoditas lebih menentukan daripada kurs.")
    plabel(s, X1, 88, 600, "Kurs rupiah, neraca perdagangan, dan harga komoditas (BCOM)",
           [("(Rp/USD; neraca = ekspor − impor, USD miliar/bulan, rata-rata 12 bulan; arsir = episode depresiasi)", False, None)])
    pic(s, fig_timeline(), X1, 126, 600, 384)
    rows = [["Episode", "Periode", "Depr."]]
    for r in E.itertuples():
        rows.append([r.episode.replace("Komoditas jatuh", "Komod. jatuh").replace("Normalisasi", "Normal."),
                     f"{bln(r.mulai)[:3]} {r.mulai[-2:]}–{bln(r.puncak)[:3]} {r.puncak[-2:]}", f"+{idn(r.dep_idr_usd, 0)}%"])
    table(s, 648, 96, 270, rows, [1.6, 1.25, 0.6], size=10, row_h=21)
    note(s, "Episode: mulai di titik terendah Rp/USD sebelum rupiah melemah ≥10%; selesai di puncak sebelum menguat kembali ≥5%.",
         y=290, h=40, x=648, w=270)
    pointers(s, [
        "Surplus terbesar (2006–08, 2021–22) terjadi saat harga komoditas tinggi, bukan saat rupiah melemah.",
        "Defisit 2012–14 dan 2018–19 justru muncul di tengah atau sesudah episode depresiasi.",
        "Panel bawah: neraca bergerak searah dengan BCOM (naik 2007–08 dan 2021–22, jatuh 2015–16), bukan dengan kurs.",
    ], x=648, y=336, w=270, h=128, size=11)
    source(s, "BIS (kurs); ITC Trade Map (neraca); Bloomberg (BCOM); identifikasi episode oleh penulis")

    s = content(prs, f"Setelah depresiasi, rasio ekspor/impor rata-rata {idn(ep_mean)}% dalam 12 bulan, tidak lebih baik "
                     f"daripada bulan biasa ({idn(bench)}%)",
                notes="Ini uji Marshall-Lerner versi sederhana tanpa model. Kami mengindeks rasio ekspor/impor ke 100 di awal "
                      "setiap episode, lalu melihat pergerakannya. Rata-rata delapan episode (garis oranye) turun, bukan naik, "
                      "dan tidak menunjukkan bentuk J. Tabel di kanan memperlihatkan bahwa arah perubahan neraca lebih mirip "
                      "arah harga komoditas daripada besarnya depresiasi.")
    plabel(s, X1, 88, W1, "Rasio ekspor/impor di sekitar episode depresiasi", [("(indeks, awal episode = 100)", False, None)])
    pic(s, fig_event(), X1, 126, W1, 290)
    rows = [["Episode", "Δ ekspor", "Δ impor", "Δ rasio X/M", "Δ BCOM"]]
    for r in E.itertuples():
        rows.append([r.episode, idn(r.d_x_12m), idn(r.d_m_12m),
                     (idn(r.d_xm_12m), DARKOR if r.d_xm_12m > 0 else "000000"), idn(r.d_bcom_12m)])
    rows.append(["Rata-rata 8 episode", idn(E.d_x_12m.mean()), idn(E.d_m_12m.mean()), idn(ep_mean), idn(E.d_bcom_12m.mean())])
    table(s, X2, 94, W2, rows, [2.1, 0.9, 0.9, 1.1, 0.9], size=10.5, row_h=21, hl_rows=(len(rows) - 1,))
    pointers(s, [
        [("Cara membaca: ", True, None), ("angka adalah perubahan 12 bulan setelah awal episode (%). Rasio X/M naik di "
                                          "episode 2020 dan 2024–26, turun di 2008 dan 2013, meskipun depresiasinya sama-"
                                          "sama besar.", False, None)],
        [("Uji Marshall-Lerner deskriptif: ", True, None),
         ("rasio tidak membaik setelah depresiasi dan tidak ada pola J; konsisten dengan |εX| + |εM| < 1.", False, None)],
    ], x=X2, y=312, w=W2, h=150, size=11.5)
    note(s, "Δ = perubahan log ×100 antara rata-rata 3 bulan di awal episode dan rata-rata 3 bulan 12 bulan kemudian, "
            "sehingga ~seasonality~ saling meniadakan.", y=468, h=30, w=430)
    source(s, "ITC Trade Map (HS-6), BIS, Bloomberg; olahan penulis")

    s = content(prs, f"Harga komoditas menjelaskan {idn(dr[('Ekspor', 'Harga komoditas (BCOM)')], 0)}% variasi ekspor, "
                     f"sedangkan depresiasi hanya {idn(dr[('Ekspor', 'Depresiasi riil (REER)')], 0)}%",
                notes="Grafik kiri mengukur seberapa besar setiap faktor menjelaskan naik-turunnya ekspor, impor, dan rasio "
                      "ekspor/impor dalam 12 bulan. R-squared 70 persen artinya 70 persen naik-turunnya ekspor sejalan dengan "
                      "naik-turunnya harga komoditas. Depresiasi hampir tidak menjelaskan apa pun. Namun karena harga komoditas "
                      "menaikkan ekspor dan impor sekaligus, efeknya ke rasio saling meniadakan. Untuk rasio, faktor terkuat "
                      "justru pertumbuhan ekonomi domestik: saat ekonomi tumbuh, impor ikut naik.")
    plabel(s, X1, 88, W1, "Seberapa besar tiap faktor menjelaskan perubahan 12 bulan",
           [("(R² bivariat, persen; Jan 2007–Jun 2026)", False, None)])
    pic(s, fig_drivers(), X1, 126, W1, 262)
    plabel(s, X2, 88, W2, "Ekspor vs BCOM dan rasio X/M vs depresiasi", [("(perubahan 12 bulan, persen)", False, None)])
    pic(s, fig_scatter(), X2, 126, W2, 262)
    pointers(s, [
        [("Cara membaca R²: ", True, None), ("persentase naik-turunnya variabel yang sejalan dengan faktor tersebut. 70% "
                                             "berarti hubungan sangat erat; di bawah 5% berarti hampir tidak ada hubungan.", False, None)],
        [("Harga komoditas menggerakkan ekspor dan impor sekaligus ", True, None),
         (f"(R² {idn(dr[('Ekspor', 'Harga komoditas (BCOM)')], 0)}% dan {idn(dr[('Impor', 'Harga komoditas (BCOM)')], 0)}%), "
          "sehingga efeknya ke rasio X/M saling meniadakan. Karena itu harga komoditas wajib dikontrol di semua model.", False, None)],
        [("Untuk rasio X/M, PDB domestik paling berpengaruh ", True, None),
         (f"(R² {idn(dr[('Rasio X/M', 'PDB riil Indonesia')], 0)}%): ekonomi tumbuh, impor naik. Depresiasi hanya "
          f"{idn(dr[('Rasio X/M', 'Depresiasi riil (REER)')], 0)}%, dengan tanda negatif.", False, None)],
    ], y=394, h=106, size=11)
    source(s, "ITC Trade Map, BIS, Bloomberg, CEIC, BPS; olahan penulis")

    hm, piv_m = fig_heat(ep_m, ["CHN", "JPN", "THA", "MYS", "SGP", "KOR", "AUS", "IND", "VNM", "USA"], CTRY,
                         "heat_mitra", (5.6, 3.75))
    worst = piv_m["Rata-rata"].sort_values()
    s = content(prs, f"Per mitra: setelah depresiasi, neraca dengan {CTRY[worst.index[0]]} dan {CTRY[worst.index[1]]} "
                     "rata-rata paling memburuk",
                notes="Setiap sel menunjukkan perubahan rasio ekspor/impor dengan satu mitra, 12 bulan setelah awal satu "
                      "episode depresiasi. Warna cokelat berarti memburuk, oranye berarti membaik. Kolom terakhir adalah "
                      "rata-rata. Polanya tidak seragam: mitra yang sama bisa membaik di satu episode dan memburuk di "
                      "episode lain, karena ikut terbawa siklus komoditas dan permintaan mitra. Itulah mengapa kita butuh "
                      "model yang bisa memisahkan efek kurs dari guncangan bersama.")
    plabel(s, 34, 88, 570, "Perubahan rasio X/M bilateral 12 bulan setelah awal episode",
           [("(persen; cokelat = memburuk, oranye = membaik)", False, None)])
    pic(s, hm, 34, 126, 570, 370)
    pic(s, fig_avg_bar(worst, CTRY, "avg_mitra"), 616, 92, 300, 214)
    pointers(s, [
        "Mitra yang sama bisa membaik di satu episode dan memburuk di episode lain, mengikuti siklus komoditas dan "
        "permintaan mitra.",
        "Karena itu efek bilateral dipisahkan dari guncangan bersama lewat local projections dengan ~fixed effects~ "
        "bulan (bagian 04).",
    ], x=616, y=314, w=300, h=150, size=11)
    source(s, "ITC Trade Map; olahan penulis")

    hg, piv_g = fig_heat(ep_g, ["sec2", "comm", "eu3", "eu2", "eu1", "noncomm", "sec1"], GRP, "heat_kelompok", (5.6, 3.5))
    gw = piv_g["Rata-rata"].sort_values()
    s = content(prs, f"Per kelompok: {GRP[gw.index[0]].lower()} paling memburuk setelah depresiasi; "
                     f"{GRP[gw.index[-1]].lower()} rata-rata paling membaik",
                notes="Sama seperti slide sebelumnya, tetapi dipecah per kelompok barang untuk perdagangan Indonesia dengan "
                      "dunia. Barang modal hampir selalu memburuk: Indonesia tetap mengimpor mesin walaupun rupiah melemah. "
                      "Komoditas bergerak mengikuti harga dunia, bukan kurs. Pertanian dan pangan rata-rata paling membaik.")
    plabel(s, 34, 88, 570, "Perubahan rasio X/M per kelompok 12 bulan setelah awal episode",
           [("(persen, Indonesia–dunia; cokelat = memburuk, oranye = membaik)", False, None)])
    pic(s, hg, 34, 126, 570, 350)
    pic(s, fig_avg_bar(gw, GRP_S, "avg_kelompok"), 616, 92, 300, 214)
    pointers(s, [
        [("Barang modal: ", True, None), ("hampir selalu memburuk; impor mesin tidak berkurang saat rupiah melemah.", False, None)],
        [("Komoditas: ", True, None), ("arah mengikuti harga dunia (lihat Δ BCOM per episode), bukan kurs.", False, None)],
    ], x=616, y=314, w=300, h=120, size=11)
    note(s, "Kelompok saling tumpang tindih (sifat barang vs penggunaan); lihat slide klasifikasi HS-6.", y=486, h=20, w=570)
    source(s, "ITC Trade Map (HS-6), UNSD; olahan penulis")

    s = content(prs, "Statistik deskriptif: variasi harga komoditas jauh lebih besar daripada variasi kurs riil",
                notes="Tabel ini merangkum data yang dipakai. Hal terpenting: ~standard deviation~ REER hanya sekitar 5 poin, "
                      "sedangkan BCOM 34 poin. Dengan kata lain, guncangan harga komoditas jauh lebih besar daripada "
                      "guncangan kurs riil, sehingga wajar bila neraca lebih banyak digerakkan komoditas.")
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
    section(prs, "03", "Metodologi dan data")

    s = content(prs, "Literatur metodologi: ARDL sebagai standar J-curve, local projections sebagai cek ~endogeneity~",
                notes="Tabel ini menjelaskan setiap metode yang dipakai, kegunaannya, dan rujukannya. ARDL dipilih sebagai "
                      "model utama karena menjadi standar studi J-curve, termasuk di Indonesia. Kelemahannya adalah persamaan "
                      "tunggal yang rawan ~endogeneity~, sehingga kami menambahkan local projections dengan kurs bilateral dan "
                      "fixed effects bulan. VECM Johansen tidak dipakai karena rasio ekspor/impor ternyata ~stationary~.")
    table(s, 44, 94, 872, [
        ["Metode", "Kegunaan", "Literatur", "Di riset ini"],
        ["ARDL ~bounds test~", "Efek ~short-run~ dan panjang; variabel I(0)/I(1) campuran; sampel kecil",
         "Pesaran, Shin & Smith (2001); Bahmani-Oskooee & Brooks (1999); Kripfganz & Schneider (2020)", "Model utama RQ1–RQ3"],
        ["NARDL", "~Asymmetry~ depresiasi vs apresiasi", "Shin, Yu & Greenwood-Nimmo (2014); Bahmani-Oskooee & Fariditavana (2016)",
         "~Robustness~ RQ1"],
        ["Panel PMG / MG", "Efek ~long-run~ lintas mitra, homogen vs heterogen", "Pesaran, Shin & Smith (1999)", "~Robustness~ RQ2"],
        ["Local projections", "~Impulse response~ per horizon dengan ~confidence interval~; panel dengan ~fixed effects~",
         "Jordà (2005); Plagborg-Møller & Wolf (2021); Montiel Olea & Plagborg-Møller (2021)", "Konfirmasi RQ1–RQ3"],
        ["LP-IV", "Efek kausal dengan instrumen eksternal", "Stock & Watson (2018)", "Dicoba; ~weak instrument~"],
        ["VAR / VECM Johansen", "Sistem endogen, banyak vektor ~cointegration~", "Johansen (1991); Widarjono (2005)",
         "Tidak dipakai: ln(X/M) ~stationary~"],
    ], [1.3, 2.4, 2.9, 1.4], align=[L, L, L, L], size=11, row_h=40)
    pointers(s, [[("Mengapa dua metode: ", True, None),
                  ("ARDL membuat hasil sebanding dengan literatur Indonesia, tetapi ~single equation~ rawan ~endogeneity~: rupiah "
                   "dan neraca sama-sama digerakkan siklus komoditas. Local projections dengan kurs bilateral dan ~fixed "
                   "effects~ bulan menyerap guncangan bersama itu.", False, None)]], y=392, h=70, head="Strategi identifikasi")
    source(s, "Lihat notes/4_litrev_metode.md untuk daftar pustaka lengkap")

    cw = cov[cov.ISO3 == "WLD"].set_index(["Flow", "Classification", "Class"]).Value_Share_pct
    mix_x = cw.loc[("Exports_USDk", "Commodity_Class", "mixed")] + cw.loc[("Exports_USDk", "Commodity_Class", "unclassified")]
    mix_m = cw.loc[("Imports_USDk", "BEC5_EndUse", "mixed")] + cw.loc[("Imports_USDk", "BEC5_EndUse", "unclassified")]
    s = content(prs, "Klasifikasi HS-6: 6.883 kode barang dipetakan ke 7 kelompok lewat tabel korespondensi resmi UNSD",
                notes="Data perdagangan tersedia per kode HS 6 digit, sekitar 6.900 jenis barang. Agar bisa dianalisis per "
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

    s = content(prs, "Daftar variabel: 13 seri bulanan Jan 2006–Jun 2026 dari 8 sumber resmi",
                notes="Semua variabel berfrekuensi bulanan. Neraca perdagangan berasal dari ITC Trade Map, kurs dan CPI dari BIS, "
                      "harga komoditas dari Bloomberg, permintaan mitra dari CEIC, dan PDB dari BPS. Kolom terakhir "
                      "menunjukkan di model mana setiap variabel dipakai.")
    table(s, 44, 92, 872, [
        ["Variabel", "Notasi", "Definisi dan transformasi", "Sumber", "Periode", "Dipakai di"],
        ["Neraca Indonesia–dunia", "ln(X/M)", "ln ekspor/impor (USD ribu), baris TOTAL HS-6", "ITC Trade Map", "Jan 06–Agu 26", "RQ1"],
        ["Neraca bilateral", "ln(Xi/Mi)", "Idem, 10 mitra", "ITC Trade Map", "Jan 06–Agu 26", "RQ2"],
        ["Neraca per kelompok", "ln(Xg/Mg)", "Idem, 7 kelompok HS-6 (UNSD HS–SITC3–BEC5)", "ITC Trade Map; UNSD", "Jan 06–Agu 26", "RQ3"],
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
    ], [1.6, 0.85, 2.7, 1.35, 1.05, 1.15], align=[L, L, L, L, L, L], size=10, row_h=26)
    note(s, "Sampel estimasi efektif Jan 2007–Jun 2026 (12 bulan pertama terpakai untuk lag; akhir sampel dibatasi data BCOM). "
            "~Dummy~: ~seasonal~ (11 bulan), krisis global Okt 2008–Jun 2009, COVID Mar–Agu 2020.", y=462, h=30)
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
                   "terkoreksi setiap bulan, sehingga dinamika ~short-run~ dan panjang terbaca dari satu persamaan.", False, None)]],
             y=432, head="", size=11.5)
    source(s, "Pesaran dkk. (2001); Jordà (2005); Kripfganz & Schneider (2023)")

    s = content(prs, "Dari koefisien ke angka di slide: semua hasil diubah ke efek depresiasi riil 10%",
                notes="Slide ini menjelaskan langkah yang biasanya terlewat: bagaimana angka di tabel hasil diperoleh dari output "
                      "regresi. Koefisien kurs dikalikan 10 dan tandanya disesuaikan, sehingga semua angka bisa dibaca "
                      "seragam: persen perubahan rasio ekspor/impor bila rupiah melemah riil 10 persen. Positif berarti "
                      "membaik.")
    numbered(s, [
        ("Langkah 1 · estimasi",
         "ARDL menghasilkan koefisien ~long-run~ θ1 untuk ln REER. Contoh model utama: θ1 = "
         f"{idn(A1.lr, 2)}. LP menghasilkan bh untuk setiap bulan h."),
        ("Langkah 2 · samakan arah",
         "REER naik berarti rupiah ~menguat~. Depresiasi riil 10% berarti ln REER turun 0,10, sehingga efeknya = −0,10 × θ1."),
        ("Langkah 3 · ubah ke persen",
         f"Efek = −0,10 × θ1 × 100 = −10 × θ1. Contoh: −10 × {idn(A1.lr, 2)} = {idn(A1.eff10_lr)}% perubahan rasio ekspor/impor."),
        ("Langkah 4 · baca jalurnya",
         "~Dynamic multiplier~ (ARDL) dan ~impulse response~ (LP) diubah dengan cara yang sama untuk bulan 0–24, lalu "
         "diplot. Bintang (*) atau warna oranye = signifikan pada 10%."),
    ], step=78, desc=12, head=13.5)
    pointers(s, [[("Contoh membaca: ", True, None),
                  ("angka −10 di bulan ke-12 berarti rasio ekspor/impor 1,10 menjadi 0,99 setahun setelah rupiah melemah riil "
                   "10%: surplus kecil berubah menjadi defisit kecil.", False, None)]], y=418, h=50, head="")
    source(s, "Olahan penulis")

    # =========================================================================
    section(prs, "04", "Hasil ekonometrika")

    s = content(prs, f"RQ1 · Depresiasi riil 10% menurunkan rasio ekspor/impor sekitar {idn(abs(lp12), 0)}% dalam 6–12 bulan "
                     "dan tidak pulih",
                notes="Jawaban RQ1. Kedua metode memberi gambaran sama: setelah rupiah melemah, rasio ekspor/impor turun "
                      "sekitar sepuluh persen dalam enam sampai dua belas bulan dan tidak kembali ke atas nol. Tidak ada "
                      "bentuk J, dan efek ~long-run~nya tidak signifikan, sehingga kondisi Marshall-Lerner tidak "
                      "terpenuhi untuk Indonesia.")
    plabel(s, X1, 88, W1, "ARDL: respons kumulatif rasio X/M", [("(persen; ~dynamic multiplier~)", False, None)])
    pic(s, fig_ardl_jcurve(), X1, 126, W1, 250)
    plabel(s, X2, 88, W2, "Local projections: respons rasio X/M", [("(persen; arsir = 90% ~confidence interval~)", False, None)])
    pic(s, fig_lp_line(), X2, 126, W2, 250)
    rows = [["", "Bulan 0", "Bulan 6", "Bulan 12", "Bulan 24", "~Long-run~"],
            ["ARDL", idn(A1.eff10_sr0), idn(A1.eff10_m6), idn(A1.eff10_m12), idn(A1.eff10_m24),
             f"{idn(A1.eff10_lr)} (p = {idn(A1.lr_p, 2)})"],
            ["Local projections"] + [sig(lpv("A1_ols", "AGG", h), lpv("A1_ols", "AGG", h, "p")) for h in (0, 6, 12, 24)] + ["–"]]
    table(s, 44, 384, 872, rows, [1.6, 1, 1, 1, 1, 1.6], size=11, row_h=20)
    pointers(s, [
        "Tidak ada J-curve: respons tidak pernah naik di atas nol dalam 24 bulan, di kedua metode.",
        "Marshall-Lerner tidak terpenuhi: efek ~long-run~ ARDL tidak signifikan. Garis putus-putus (lag BIC, 10 mitra) "
        "memberi arah yang sama.",
    ], y=448, h=58, head="", size=11)
    source(s, "Estimasi penulis")

    s = content(prs, "RQ2 · Neraca dengan China dan Jepang memburuk paling dalam; tidak ada mitra yang membaik signifikan",
                notes="Jawaban RQ2. Grafik menunjukkan efek depresiasi rupiah terhadap mata uang setiap mitra, 12 bulan "
                      "kemudian, setelah semua guncangan global dikendalikan. China dan Jepang memburuk secara signifikan; "
                      "dugaan channel-nya adalah impor barang modal dan bahan baku yang sulit diganti. Tidak ada mitra yang "
                      "membaik secara signifikan, termasuk AS.")
    plabel(s, X1, 88, W1, "Efek depresiasi riil bilateral 10%, bulan ke-12",
           [("(persen; LP panel; oranye = signifikan 10%; garis = 90% CI)", False, None)])
    pic(s, fig_bar_partner(), X1, 126, W1, 330)
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
                                "di LP ≈ 0 setelah guncangan bersama dikendalikan.", False, None)],
        [("Rata-rata 10 mitra ≈ 0: ", True, None),
         (f"LP bulan 12 {idn(lpv('B1_panel', 'PANEL', 12))}% (p = {idn(lpv('B1_panel', 'PANEL', 12, 'p'), 2)}); "
          f"panel MG {idn(pmg.loc['MG', 'eff10_lr'])}% (p = {idn(pmg.loc['MG', 'lr_reer_p'], 2)}).", False, None)],
    ], x=X2, y=252, w=W2, size=11.5)
    pointers(s, [
        "Batang = efek 12 bulan setelah rupiah melemah riil 10% terhadap mata uang mitra; garis = 90% ~confidence interval~. "
        "Bila garis memotong nol, efeknya tidak signifikan.",
        "Thailand memburuk signifikan di LP (−15,2%) tetapi tidak di ARDL, sehingga belum dianggap robust.",
    ], x=X2, y=pb.top / 12700 + pb.height / 12700 + 8, w=W2, head="Cara membaca dan catatan", size=11)
    source(s, "Estimasi penulis; kurs dan CPI BIS")

    s = content(prs, "RQ3 · Energi & tambang dan barang modal memburuk; pertanian dan konsumsi baru membaik setelah 2 tahun",
                notes="Jawaban RQ3. Kelompok dengan efek negatif yang paling kuat adalah energi dan tambang, karena harga batu "
                      "bara dan nikel ditentukan di pasar dunia dalam USD, dan barang modal, karena impor mesin tidak bisa "
                      "ditunda. Kelompok yang membaik, yaitu pertanian dan pangan serta barang konsumsi, baru terlihat "
                      "setelah sekitar dua tahun. Manufaktur secara keseluruhan tidak menunjukkan efek.")
    plabel(s, X1, 88, W1, "Efek depresiasi riil bilateral 10% per kelompok",
           [("(persen; LP panel; warna pekat = signifikan 10%)", False, None)])
    pic(s, fig_group_two(), X1, 126, W1, 330)
    rows = [["Kelompok", "ARDL bln 0", "ARDL LR (p)", "LP bln 12", "LP bln 24"]]
    for g in ["sec2", "eu3", "eu2", "comm", "noncomm", "eu1", "sec1"]:
        rows.append([GRP_S[g], sig(ak.loc[g, "eff10_sr0"], ak.loc[g, "sr0_p"]),
                     (f"{idn(ak.loc[g, 'eff10_lr'])} ({idn(ak.loc[g, 'lr_p'], 2)})",
                      DARKOR if ak.loc[g, "lr_p"] < .1 and ak.loc[g, "coint10"] == 1 else "000000"),
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
        "Batang cokelat = bulan ke-12, oranye = bulan ke-24; warna pekat = signifikan 10%.",
        "ARDL ~long-run~ barang konsumsi (+86%, p = 0,09) tidak ~cointegrated~ dan penyesuaiannya sangat lambat "
        "(ADJ −0,05), sehingga dibaca sebagai arah, bukan besaran.",
    ], x=X2, y=pb.top / 12700 + pb.height / 12700 + 8, w=W2, head="Cara membaca dan catatan", size=11)
    source(s, "Estimasi penulis; klasifikasi HS-6 UNSD")

    s = content(prs, "Ringkasan: hasil yang bertahan di kedua metode",
                notes="Tabel ringkasan ini menempatkan ARDL dan local projections berdampingan. Hasil yang kita yakini adalah "
                      "yang muncul di kedua metode: neraca agregat memburuk, terutama dengan China dan Jepang, serta pada "
                      "energi dan tambang dan barang modal. Hasil yang hanya muncul di satu metode, seperti AS, kami anggap "
                      "tidak robust.")
    fm = lambda e, p=None: sig(e, p)
    rows = [["Cakupan", "ARDL bulan 0", "ARDL bulan 12", "LP bulan 12", "LP bulan 24", "Kesimpulan"]]
    rows.append(["Indonesia–dunia", fm(A1.eff10_sr0, A1.sr0_p), fm(A1.eff10_m12), fm(lp12, lpv("A1_ols", "AGG", 12, "p")),
                 fm(lpv("A1_ols", "AGG", 24), lpv("A1_ols", "AGG", 24, "p")), "Memburuk, tidak pulih"])
    for c, k in [("CHN", "Memburuk"), ("JPN", "Memburuk"), ("USA", "Tidak ada efek")]:
        rows.append([CTRY[c], fm(am.loc[c, "eff10_sr0"], am.loc[c, "sr0_p"]), fm(am.loc[c, "eff10_m12"]),
                     fm(lpv("B2_partner", c, 12), lpv("B2_partner", c, 12, "p")),
                     fm(lpv("B2_partner", c, 24), lpv("B2_partner", c, 24, "p")), k])
    for g, k in [("sec2", "Memburuk"), ("eu3", "Memburuk"), ("eu2", "Memburuk ringan"), ("sec1", "Membaik setelah 2 tahun"),
                 ("eu1", "Membaik setelah 2 tahun"), ("noncomm", "Tidak ada efek")]:
        rows.append([GRP[g], fm(ak.loc[g, "eff10_sr0"], ak.loc[g, "sr0_p"]), fm(ak.loc[g, "eff10_m12"]),
                     fm(lpv("C_group", g, 12), lpv("C_group", g, 12, "p")),
                     fm(lpv("C_group", g, 24), lpv("C_group", g, 24, "p")), k])
    table(s, 44, 94, 872, rows, [2.5, 1.1, 1.15, 1.1, 1.1, 1.9], size=11.5, row_h=26, align=[L, R, R, R, R, L])
    note(s, "* signifikan 10%. ARDL bulan 0 = koefisien ~short-run~; ARDL bulan 12 = ~dynamic multiplier~ (tanpa ~confidence "
            "interval~). LP agregat = Indonesia–dunia; LP mitra dan kelompok = panel 10 mitra dengan ~fixed effects~ bulan.",
         y=386, h=30)
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

    # =========================================================================
    section(prs, "05", "Diagnostik dan robustness")

    s = content(prs, "~Unit root test~: tidak ada variabel I(2), sehingga ARDL ~bounds test~ sah dipakai",
                notes="Sebelum estimasi, setiap variabel diuji apakah ~stationary~. ARDL hanya sah bila tidak ada variabel yang "
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
                      "Grafik CUSUM di kanan memeriksa apakah koefisien stabil sepanjang waktu; garis yang tetap di dalam pita "
                      "abu-abu berarti stabil.")
    rows = [["Model", "p F", "p t", "~Coint.~", "LM(12) p", "ARCH p"]]
    for i, nm in [("A1_main", "Agregat utama")] + [(g, GRP_S[g]) for g in ["comm", "sec2", "sec1", "noncomm", "eu1", "eu2", "eu3"]]:
        r = A.loc[i] if i in A.index else ak.loc[i]
        rows.append([nm, idn(r.pF, 3), idn(r.pt, 3), "ya" if r.coint10 == 1 else "tidak",
                     (idn(r.p_lm12, 2), DARKOR if r.p_lm12 < .05 else "000000"),
                     (idn(r.p_arch12, 2), DARKOR if r.p_arch12 < .05 else "000000")])
    table(s, 44, 94, 440, rows, [1.7, 0.7, 0.7, 0.8, 0.8, 0.8], size=11.5, row_h=27)
    plabel(s, X2, 88, W2, "~Stability test~ CUSUM, model agregat utama", [("(garis di dalam pita 95% = koefisien stabil)", False, None)])
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
        [("~Endogeneity~ agregat: ", True, None), ("belum tertangani penuh; kandidat instrumen berikutnya adalah kejutan "
                                                 "kebijakan moneter AS (~high-frequency~).", False, None)],
    ], y=362, h=104, size=11.5)
    source(s, "Estimasi penulis")

    # =========================================================================
    s = content(prs, "Kesimpulan dan implikasi",
                notes="Empat pesan utama. Pertama, depresiasi tidak memperbaiki neraca perdagangan Indonesia. Kedua, harga "
                      "komoditas dan permintaan domestik jauh lebih menentukan daripada kurs. Ketiga, channel yang memburuk "
                      "adalah energi dan tambang, barang modal, dan perdagangan dengan China dan Jepang. Keempat, channel yang "
                      "membaik kecil dan lambat, sehingga pelemahan rupiah bukan alat yang efektif untuk memperbaiki neraca.")
    numbered(s, [
        ("Depresiasi tidak memperbaiki neraca perdagangan Indonesia",
         "Rasio ekspor/impor turun sekitar 9–10% dalam 6–12 bulan setelah depresiasi riil 10% (ARDL dan LP) dan tidak pulih. Tidak "
         "ada J-curve dan Marshall-Lerner tidak terpenuhi; 8 episode depresiasi memberi gambaran yang sama."),
        ("Harga komoditas dan permintaan domestik lebih menentukan daripada kurs",
         "BCOM menjelaskan sekitar 70% variasi ekspor; PDB domestik paling berkaitan dengan rasio X/M; depresiasi < 6%."),
        ("~Channel~ yang memburuk: energi & tambang, barang modal, mitra China dan Jepang",
         "Harga dunia dalam USD dan impor input yang sulit diganti; arahnya konsisten di ARDL dan LP."),
        ("~Channel~ yang membaik kecil dan lambat",
         "Pertanian & pangan serta barang konsumsi membaik setelah sekitar 2 tahun. Kebijakan lebih efektif bila menyasar "
         "substitusi impor input dan diversifikasi ekspor, bukan mengandalkan pelemahan rupiah."),
    ], step=84)
    note(s, "Keterbatasan: data nilai (bukan volume); ~endogeneity~ agregat belum tertangani penuh; CPI Vietnam dan PDB bulanan masih "
            "pendekatan; analisis bilateral hanya 10 mitra.", y=436, h=30)

    prs.slides.add_slide(layout(prs, "Closing_DEN_bhs"))

    # =========================================================================
    section(prs, "", "Lampiran")

    s = content(prs, "Lampiran A1 · Glosarium istilah umum")
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

    s = content(prs, "Lampiran A2 · Glosarium ekonometrika (1/2)")
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

    s = content(prs, "Lampiran A3 · Glosarium ekonometrika (2/2)")
    table(s, 44, 92, 872, [
        ["Istilah", "Arti sederhana"],
        ["Local projections (LP)", "Satu regresi untuk tiap horizon (bulan 0, 1, …, 24) untuk melihat respons dari waktu ke waktu."],
        ["~Impulse response~", "Respons suatu variabel dari waktu ke waktu setelah satu guncangan, misalnya depresiasi."],
        ["~Fixed effects~", "~Dummy variable~ yang menyerap faktor yang sama untuk semua mitra di bulan yang sama (misalnya harga komoditas)."],
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

    s = content(prs, "Lampiran C · ARDL per mitra dagang dan per kelompok barang")
    ids = list(ardl_mi.id)
    gids = ["comm", "sec2", "sec1", "noncomm", "eu1", "eu2", "eu3"]
    rows = ardl_rows(ardl_mi, ids, [CTRY[i] for i in ids]) + ardl_rows(ardl_kg, gids, [GRP[g] for g in gids])[1:]
    table(s, 44, 92, 872, rows, colw, size=10, row_h=22)
    note(s, "Mitra: REER multilateral (BIS) yang sama untuk semua mitra. Kelompok: Indonesia–dunia; energi memakai harga batu bara "
            "(tersedia sejak 2009, sehingga N = 198), pertanian memakai CPO.", y=492, h=22, w=560)
    source(s, "Estimasi penulis")

    s = content(prs, "Lampiran D · Local projections: efek per horizon")
    rows = [["Model", "Bulan 0", "Bulan 3", "Bulan 6", "Bulan 12", "Bulan 18", "Bulan 24"]]
    spec = [("A1_ols", "AGG", "Agregat Indonesia–dunia"), ("B1_panel", "PANEL", "Panel 10 mitra (rata-rata)"),
            ("B3_novnm", "PANEL", "Panel tanpa Vietnam")] + [("B2_partner", c, CTRY[c]) for c in CTRY] + \
           [("C_group", g, GRP[g]) for g in gids]
    for m, i, lb in spec:
        rows.append([lb] + [sig(lpv(m, i, h), lpv(m, i, h, "p")) for h in (0, 3, 6, 12, 18, 24)])
    table(s, 44, 90, 872, rows, [3, 1, 1, 1, 1, 1, 1], size=9.5, row_h=19)
    note(s, "* signifikan 10%. Efek dalam % rasio X/M per depresiasi riil 10%.", y=500, h=16, w=400)
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
