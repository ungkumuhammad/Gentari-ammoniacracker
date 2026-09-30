"""Licensor scaling charts (deck PNGs, 1920x1080) -- CAPEX and ISBL footprint vs H2 capacity.

Each chart plots the licensor's quoted points and a power-law curve
y = a * capacity^n, either fitted (log-log least squares, >= 2 points) or
anchored on a single point with an assumed exponent (flagged as such).

Sources:
  KBR    -- Licensor/kbr/kbr-johor-hub.md §4.1 (CAPEX), §3.6 (plot footprint)
            (H2ACT Technical Information Package, Rev 0, 23 Dec 2025)
  Duiker -- Licensor/duiker/duiker-johor-hub.md §4.1 Table 8 (CAPEX),
            §3.10 (plot space) (Budgetary Proposal 122380, 05 Dec 2025)

Output: tcoedatabase/figures/*.png
Run:    python tools/licensor_charts.py
"""
from dataclasses import dataclass, field
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

OUT_DIR = Path(__file__).resolve().parents[1] / "tcoedatabase" / "figures"
EXTRAP_KTPA = 100

INK, INK_2, MUTED, GRID = "#0b0b0b", "#52514e", "#8a8984", "#e6e5e0"
MAIN = "#7030A0"       # quoted points + fitted curve
SECONDARY = "#0070C0"  # derived / extrapolated values + accuracy band
SURFACE = "#ffffff"

# Duiker states 12 ktpa = 36 tpd, i.e. an implied 333.3 onstream days/yr.
# Its standard 276 tpd train converts to ktpa on that same implied basis.
DUIKER_DAYS = 12_000 / 36
SQFT_PER_M2 = 1 / 0.3048 ** 2  # 10.7639 (international foot, exact definition)
DUIKER_STD_TRAIN_KTPA = 276 * DUIKER_DAYS / 1000  # ~92.0 ktpa [DERIVED]


@dataclass
class Chart:
    filename: str
    title: str
    subtitle: str
    ylabel: str
    footnote: str
    cap: list                  # capacity, ktpa
    val: list                  # quoted value (y)
    point_labels: list
    value_fmt: str             # e.g. "US${:.0f}M" -- used for extrapolated label
    unit: str                  # y unit in formula text, e.g. "US$M"
    ylim: float
    accuracy: float = None     # ± fraction for error bars (None = not stated)
    accuracy_label: str = ""
    assumed_n: float = None    # set -> anchor on single point with this exponent
    fit_label: str = "Power-law fit"
    vline: tuple = None        # (x, label) reference marker
    xticks: list = field(default_factory=lambda: [0, 12, 24, 40, 68, 80, 100])
    labels_below: bool = False  # put point labels below-right of the marker
    label_pos: list = None      # per-point override: "ul" above-left, "br" below-right, "ac"/"ah" above-centre (near/high)
    sqft: bool = False          # footprint charts: also show ft² (labels, formula, right axis)
    legend_anchor: tuple = (1.0, 0.0)


def draw(ch: Chart) -> dict:
    x = np.asarray(ch.cap, dtype=float)
    y = np.asarray(ch.val, dtype=float)

    if ch.assumed_n is None:
        n, ln_a = np.polyfit(np.log(x), np.log(y), 1)
        a = np.exp(ln_a)
        ly = np.log(y)
        r2 = 1 - ((ly - (n * np.log(x) + ln_a)) ** 2).sum() / ((ly - ly.mean()) ** 2).sum()
    else:
        n = ch.assumed_n
        a = y[0] / x[0] ** n
        r2 = None
    extrap = a * EXTRAP_KTPA ** n

    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
    fig, ax = plt.subplots(figsize=(12.8, 7.2), dpi=150, facecolor=SURFACE)
    ax.set_facecolor(SURFACE)
    fig.subplots_adjust(left=0.08, right=0.91 if ch.sqft else 0.97, top=0.83, bottom=0.20)

    if ch.accuracy:
        ax.errorbar(x, y, yerr=y * ch.accuracy, fmt="none", ecolor=SECONDARY, alpha=0.35,
                    elinewidth=2, capsize=6, capthick=2, zorder=2)

    if ch.vline:
        vx, vlabel = ch.vline
        ax.axvline(vx, color=MUTED, lw=1, ls=(0, (1, 3)), zorder=1)
        ax.text(vx - 0.8, ch.ylim * 0.04, vlabel, rotation=90, ha="right", va="bottom",
                fontsize=9.5, color=MUTED)

    if ch.assumed_n is None:
        xs = np.linspace(x.min(), x.max(), 100)
        ax.plot(xs, a * xs ** n, color=MAIN, lw=2, zorder=3)
        xe = np.linspace(x.max(), EXTRAP_KTPA, 30)
    else:
        xe = np.linspace(x.min(), EXTRAP_KTPA, 100)
    ax.plot(xe, a * xe ** n, color=SECONDARY, lw=2, ls=(0, (4, 3)), zorder=3)

    ax.scatter(x, y, s=110, color=MAIN, edgecolor=SURFACE, linewidth=2, zorder=4)
    ax.scatter([EXTRAP_KTPA], [extrap], s=110, facecolor=SURFACE, edgecolor=SECONDARY,
               linewidth=2, zorder=4)

    placements = {"ul": ((-12, 12), "right", "bottom"), "br": ((12, -12), "left", "top"),
                  "ac": ((0, 16), "center", "bottom"), "ah": ((0, 40), "center", "bottom")}
    for i, (xi, yi, lab) in enumerate(zip(x, y, ch.point_labels)):
        if ch.label_pos:
            off, ha, va = placements[ch.label_pos[i]]
            ax.annotate(lab, (xi, yi), xytext=off, textcoords="offset points",
                        ha=ha, va=va, fontsize=12, fontweight="bold", color=INK)
        elif ch.labels_below:
            ax.annotate(lab, (xi, yi), xytext=(12, -12), textcoords="offset points",
                        ha="left", va="top", fontsize=12, fontweight="bold", color=INK)
        else:
            ax.annotate(lab, (xi, yi), xytext=(-12, 12), textcoords="offset points",
                        ha="right", fontsize=12, fontweight="bold", color=INK)
    extrap_txt = f"{EXTRAP_KTPA} ktpa\n≈{ch.value_fmt.format(extrap)}"
    if ch.sqft:
        extrap_txt += f"\n≈{extrap * SQFT_PER_M2:,.0f} sqft"
    ax.annotate(f"{extrap_txt}\n(extrapolated)", (EXTRAP_KTPA, extrap),
                xytext=(0, 16), textcoords="offset points", ha="center", va="bottom",
                fontsize=11, color=INK_2)

    if ch.assumed_n is None:
        fit_note = f"(R² = {r2:.4f}, log-log)" if len(x) > 2 else "(two-point fit — exact through both points)"
        box = (f"Scaling factor  n ≈ {n:.2f}\n"
               f"{ch.unit} ≈ {a:,.2f} × Capacity (ktpa)^{n:.2f}   {fit_note}")
        if ch.sqft:
            box += f"\nArea (sqft) ≈ {a * SQFT_PER_M2:,.0f} × Capacity (ktpa)^{n:.2f}"
    else:
        box = (f"Scaling factor  n = {n:.1f}  (ASSUMED — six-tenths rule, not Duiker-specific)\n"
               f"{ch.unit} ≈ {a:.2f} × Capacity (ktpa)^{n:.1f}   (anchored on the single quoted point)")
    ax.text(0.03, 0.95, box, transform=ax.transAxes, va="top", ha="left", fontsize=13,
            color=INK, bbox=dict(boxstyle="round,pad=0.6", fc="#f4f3ef", ec=GRID))

    ax.set_xlim(0, 109 if ch.sqft else 105)
    ax.set_ylim(0, ch.ylim)
    ax.set_xticks(ch.xticks)
    ax.set_xlabel("H₂ capacity (ktpa)", color=INK_2, fontsize=12)
    ax.set_ylabel(ch.ylabel, color=INK_2, fontsize=12)
    ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:,.0f}"))
    if ch.sqft:
        sec = ax.secondary_yaxis("right", functions=(lambda v: v * SQFT_PER_M2,
                                                      lambda v: v / SQFT_PER_M2))
        sec.set_ylabel("ISBL plot area (sqft)", color=INK_2, fontsize=12)
        sec.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:,.0f}"))
        sec.tick_params(colors=INK_2, length=0)
        sec.spines["right"].set_visible(False)
    ax.grid(axis="y", color=GRID, lw=1)
    ax.set_axisbelow(True)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(MUTED)
    ax.tick_params(colors=INK_2, length=0)

    handles = [Line2D([], [], marker="o", ls="none", ms=10, color=MAIN, label=ch.point_labels_legend)]
    if ch.assumed_n is None:
        handles.append(Line2D([], [], color=MAIN, lw=2,
                              label=f"{ch.fit_label}, n ≈ {n:.2f} ({x.min():.0f}–{x.max():.0f} ktpa)"))
        handles.append(Line2D([], [], color=SECONDARY, lw=2, ls=(0, (4, 3)), marker="o", mfc=SURFACE,
                              ms=9, label="Extrapolation to 100 ktpa (not licensor-quoted)"))
    else:
        handles.append(Line2D([], [], color=SECONDARY, lw=2, ls=(0, (4, 3)), marker="o", mfc=SURFACE,
                              ms=9, label=f"Six-tenths scaling, n = {n:.1f} (assumed, not Duiker-quoted)"))
    if ch.accuracy:
        handles.append(Line2D([], [], color=SECONDARY, alpha=0.35, lw=2, marker="_", ms=12,
                              label=ch.accuracy_label))
    ax.legend(handles=handles, loc="lower right", bbox_to_anchor=ch.legend_anchor, frameon=False, fontsize=10.5, labelcolor=INK_2)

    fig.text(0.08, 0.93, ch.title, fontsize=19, fontweight="bold", color=INK)
    fig.text(0.08, 0.875, ch.subtitle, fontsize=12, color=INK_2)
    fig.text(0.08, 0.045, ch.footnote, fontsize=9, color=MUTED, va="bottom")

    out = OUT_DIR / ch.filename
    fig.savefig(out, facecolor=SURFACE)
    plt.close(fig)
    return {"file": out.name, "a": a, "n": n, "r2": r2, "at_100_ktpa": extrap}


def m2(dims):
    return dims[0] * dims[1]


KBR_CAP = [12, 24, 68, 80]
KBR_FOOTPRINT_M = [(70, 50), (80, 55), (95, 75), (100, 75)]

CHARTS = [
    Chart(
        filename="kbr_capex_scaling.png",
        title="KBR H₂ACT® — ISBL CAPEX scaling with hydrogen capacity",
        subtitle="Indicative ISBL TIC, Class V ±50%, Q3 2025 USD, no forward escalation · "
                 "CAPEX identical across NG / 50-50 / clean-fuel modes",
        ylabel="ISBL CAPEX (US$ million)",
        footnote=("Source: KBR H₂ACT® Technical Information Package for Gentari, Rev 0, 23 Dec 2025, §4.1 "
                  "(factored from a KBR Class IV TIC for a similar plant in East Asia).\n"
                  "ISBL only — excludes OSBL (≈55% of ISBL at 12 ktpa), contingency, spares, commissioning, "
                  "owner's cost, licence fees, taxes/duties.\n"
                  "Fit, scaling factor and 100 ktpa value are Gentari calculations from KBR's Class V ±50% "
                  "ISBL estimates (Q3 2025) — the ±50% accuracy band still applies."),
        cap=KBR_CAP, val=[78, 110, 191, 209],
        point_labels=["US$78M", "US$110M", "US$191M", "US$209M"],
        value_fmt="US${:.0f}M", unit="CAPEX (US$M)", ylim=340,
        accuracy=0.50, accuracy_label="Class V accuracy ±50%",
    ),
    Chart(
        filename="duiker_capex_scaling.png",
        title="Duiker AHC — ISBL CAPEX scaling with hydrogen capacity",
        subtitle="Lump-sum turnkey ISBL, ±40%, EUR (Dec 2025) · single quoted point: "
                 "12 ktpa (36 tpd), one customised reactor, NH₃-fired",
        ylabel="ISBL CAPEX (€ million)",
        footnote=("Source: Duiker AHC Concept Study / Budgetary Proposal 122380, 05 Dec 2025, §4.1 Table 8 — "
                  "€20M equipment + €27M engineering, installation & EPC\n"
                  "(incl. commissioning, start-up, construction licence fee). Excludes OSBL (flare, NH₃ storage, "
                  "loading/unloading, control room).\n"
                  "Duiker quotes CAPEX at one capacity only, so no Duiker scaling factor can be fitted. "
                  "Curve and 100 ktpa value are Gentari\ncalculations using a generic n = 0.6 (ASSUMPTION); "
                  "Duiker's standard 4-reactor train may price differently. The ±40% band still applies."),
        cap=[12], val=[47], point_labels=["€47M"],
        value_fmt="€{:.0f}M", unit="CAPEX (€M)", ylim=260,
        accuracy=0.40, accuracy_label="Duiker accuracy ±40%",
        assumed_n=0.6,
        vline=(DUIKER_STD_TRAIN_KTPA, f"Standard train 276 tpd ≈ {DUIKER_STD_TRAIN_KTPA:.0f} ktpa"),
        legend_anchor=(0.80, 0.0),
    ),
    Chart(
        filename="kbr_footprint_scaling.png",
        title="KBR H₂ACT® — ISBL plot footprint scaling with hydrogen capacity",
        subtitle="Indicative ISBL plot footprint, single cracking unit · "
                 "offsites & utilities (outside licensor scope) not included",
        ylabel="ISBL plot area (m²)",
        footnote=("Source: KBR H₂ACT® Technical Information Package for Gentari, Rev 0, 23 Dec 2025, §3.6 "
                  "(12 ktpa: see also Preliminary Plot Plan, Annexure I.I).\n"
                  "KBR notes the footprint can be optimised further, especially on an existing industrial site, "
                  "and that modularisation is possible. No accuracy class is stated.\n"
                  "Areas (length × width), sqft conversion (1 m² = 10.764 sqft), fit, scaling factor and "
                  "100 ktpa value are Gentari calculations from KBR's quoted plot dimensions."),
        cap=KBR_CAP, val=[m2(d) for d in KBR_FOOTPRINT_M],
        point_labels=[f"{c} ktpa\n{l} × {w} m\n{l * w:,} m²\n({l * w * SQFT_PER_M2:,.0f} sqft)"
                      for c, (l, w) in zip(KBR_CAP, KBR_FOOTPRINT_M)],
        label_pos=["ah", "br", "br", "ac"],
        value_fmt="{:,.0f} m²", unit="Area (m²)", ylim=12000,
        fit_label="Power-law fit",
        labels_below=True, sqft=True,
    ),
    Chart(
        filename="duiker_footprint_scaling.png",
        title="Duiker AHC — ISBL plot footprint scaling with hydrogen capacity",
        subtitle="Plot space per single train · excludes liquid NH₃ storage and H₂ compression "
                 "beyond 50 bar(g)",
        ylabel="ISBL plot area (m²)",
        footnote=("Source: Duiker AHC Concept Study / Budgetary Proposal 122380, 05 Dec 2025, §3.10: "
                  "276 tpd standard train = 3,660 m² (122 × 30 m);\n"
                  "12 ktpa (36 tpd) customised train ≈ 900 m², itself estimated by Duiker by scaling down the "
                  "full-scale plant.\n276 tpd converted to "
                  f"≈{DUIKER_STD_TRAIN_KTPA:.0f} ktpa at Duiker's implied {DUIKER_DAYS:.1f} d/yr "
                  "(12 ktpa = 36 tpd). Conversion, two-point fit, scaling factor and 100 ktpa value are "
                  "Gentari calculations;\n"
                  "sqft conversion 1 m² = 10.764 sqft. No accuracy class is stated for footprint."),
        cap=[12, DUIKER_STD_TRAIN_KTPA], val=[900, 3660],
        point_labels=[f"12 ktpa (36 tpd)\n≈900 m²\n({900 * SQFT_PER_M2:,.0f} sqft)",
                      f"≈{DUIKER_STD_TRAIN_KTPA:.0f} ktpa (276 tpd): 122 × 30 m\n"
                      f"3,660 m² ({3660 * SQFT_PER_M2:,.0f} sqft)"],
        value_fmt="{:,.0f} m²", unit="Area (m²)", ylim=6000,
        fit_label="Two-point power-law fit", sqft=True,
        xticks=[0, 12, 24, 40, 68, 80, 92, 100],
    ),
]

# Legend label for the quoted-point marker, per chart
for _c, _lab in zip(CHARTS, ["KBR quoted ISBL CAPEX", "Duiker quoted CAPEX (single point)",
                             "KBR quoted ISBL footprint", "Duiker quoted plot space"]):
    _c.point_labels_legend = _lab


if __name__ == "__main__":
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for c in CHARTS:
        r = draw(c)
        r2 = "n/a" if r["r2"] is None else f"{r['r2']:.4f}"
        print(f"{r['file']:32s} a={r['a']:.4f} n={r['n']:.4f} R2={r2} @100ktpa={r['at_100_ktpa']:,.1f}")
