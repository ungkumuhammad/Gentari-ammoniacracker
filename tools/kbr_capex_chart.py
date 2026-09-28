"""KBR H2ACT ISBL CAPEX vs H2 capacity, with linear trendline -- deck PNG.

Data: Licensor/kbr/kbr-johor-hub.md §4.1 (ISBL TIC, Class V ±50%, Q3 2025,
no forward escalation). Output: tcoedatabase/figures/kbr_capex_linear.png
Run: python tools/kbr_capex_chart.py
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

CAP_KTPA = np.array([12, 24, 68, 80], dtype=float)
CAPEX_MUSD = np.array([78, 110, 191, 209], dtype=float)
ACCURACY = 0.50  # Class V ±50% (kbr-johor-hub.md §4.1)
EXTRAP_KTPA = 100

INK, INK_2, MUTED, GRID = "#0b0b0b", "#52514e", "#8a8984", "#e6e5e0"
SERIES = "#2a78d6"
SURFACE = "#ffffff"

m, c = np.polyfit(CAP_KTPA, CAPEX_MUSD, 1)
fit = m * CAP_KTPA + c
r2 = 1 - ((CAPEX_MUSD - fit) ** 2).sum() / ((CAPEX_MUSD - CAPEX_MUSD.mean()) ** 2).sum()
extrap = m * EXTRAP_KTPA + c

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})
fig, ax = plt.subplots(figsize=(12.8, 7.2), dpi=150, facecolor=SURFACE)
ax.set_facecolor(SURFACE)
fig.subplots_adjust(left=0.08, right=0.97, top=0.83, bottom=0.17)

# Class V ±50% accuracy band per quoted point
ax.errorbar(CAP_KTPA, CAPEX_MUSD, yerr=CAPEX_MUSD * ACCURACY, fmt="none",
            ecolor=SERIES, alpha=0.35, elinewidth=2, capsize=6, capthick=2, zorder=2)

# Linear trendline across quoted range, dashed extrapolation beyond it
xs = np.linspace(CAP_KTPA.min(), CAP_KTPA.max(), 50)
ax.plot(xs, m * xs + c, color=SERIES, lw=2, zorder=3)
xe = np.linspace(CAP_KTPA.max(), EXTRAP_KTPA, 20)
ax.plot(xe, m * xe + c, color=SERIES, lw=2, ls=(0, (4, 3)), zorder=3)

# Quoted points (surface ring) + extrapolated point (hollow)
ax.scatter(CAP_KTPA, CAPEX_MUSD, s=110, color=SERIES, edgecolor=SURFACE,
           linewidth=2, zorder=4)
ax.scatter([EXTRAP_KTPA], [extrap], s=110, facecolor=SURFACE, edgecolor=SERIES,
           linewidth=2, zorder=4)

for x, y in zip(CAP_KTPA, CAPEX_MUSD):
    ax.annotate(f"US${y:.0f}M", (x, y), xytext=(-12, 12), textcoords="offset points",
                ha="right", fontsize=12, fontweight="bold", color=INK)
ax.annotate(f"≈US${extrap:.0f}M\n(extrapolated)", (EXTRAP_KTPA, extrap),
            xytext=(-12, 12), textcoords="offset points", ha="right",
            fontsize=11, color=INK_2)

# Formula box
ax.text(0.03, 0.95,
        f"Linear fit:  CAPEX (US$M) = {m:.3f} × Capacity (ktpa) + {c:.2f}\n"
        f"R² = {r2:.4f}   ·   ≈ US${m:.1f}M per additional ktpa H₂",
        transform=ax.transAxes, va="top", ha="left", fontsize=12, color=INK,
        bbox=dict(boxstyle="round,pad=0.6", fc="#f4f3ef", ec=GRID))

ax.set_xlim(0, 105)
ax.set_ylim(0, 340)
ax.set_xticks([0, 12, 24, 40, 68, 80, 100])
ax.set_xlabel("H₂ capacity (ktpa)", color=INK_2, fontsize=12)
ax.set_ylabel("ISBL CAPEX (US$ million)", color=INK_2, fontsize=12)
ax.grid(axis="y", color=GRID, lw=1)
ax.set_axisbelow(True)
for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(MUTED)
ax.tick_params(colors=INK_2, length=0)

# Legend
from matplotlib.lines import Line2D
handles = [
    Line2D([], [], marker="o", ls="none", ms=10, color=SERIES, label="KBR quoted ISBL CAPEX"),
    Line2D([], [], color=SERIES, lw=2, label="Linear fit (12–80 ktpa)"),
    Line2D([], [], color=SERIES, lw=2, ls=(0, (4, 3)), marker="o", mfc=SURFACE, ms=9,
           label="Extrapolation to 100 ktpa (not KBR-quoted)"),
    Line2D([], [], color=SERIES, alpha=0.35, lw=2, marker="_", ms=12, label="Class V accuracy ±50%"),
]
ax.legend(handles=handles, loc="lower right", frameon=False, fontsize=10.5, labelcolor=INK_2)

fig.text(0.08, 0.93, "KBR H₂ACT® — ISBL CAPEX vs hydrogen capacity",
         fontsize=19, fontweight="bold", color=INK)
fig.text(0.08, 0.875, "Indicative ISBL TIC, Class V ±50%, Q3 2025 USD, no forward escalation · "
         "CAPEX identical across NG / 50-50 / clean-fuel modes",
         fontsize=12, color=INK_2)
fig.text(0.08, 0.045,
         "Source: KBR H₂ACT® Technical Information Package for Gentari, Rev 0, 23 Dec 2025, §4.1 "
         "(factored from a KBR Class IV TIC for a similar plant in East Asia).\n"
         "ISBL only — excludes OSBL (≈55% of ISBL at 12 ktpa), contingency, spares, commissioning, "
         "owner's cost, licence fees, taxes/duties. Trendline and 100 ktpa value are Gentari-derived.",
         fontsize=9, color=MUTED, va="bottom")

out = Path(__file__).resolve().parents[1] / "tcoedatabase" / "figures" / "kbr_capex_linear.png"
fig.savefig(out, facecolor=SURFACE)
print(out, f"m={m:.4f} c={c:.4f} r2={r2:.4f} extrap100={extrap:.1f}")
