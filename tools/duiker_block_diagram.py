"""Duiker AHC simplified block flow diagram -- deck PNG (1920x1080).

Reconstructed from Duiker's process description, because the source Figure 3
(BFD) is an image that did not survive the PDF->Markdown conversion:
  Licensor/duiker/duiker-johor-hub.md -- §2 (technology benefits, Table 2
  reactor comparison), §3.2 (process description), §3.4 (H2 spec), §3.6
  (battery limits), §3.7 Table 5 (material balance, NH3-fired, 12 ktpa),
  §3.9 (utilities), §3.9.1 Table 7 (fuel options).
Stream values are Table 5 (NH3-fired, 12 ktpa / 36 tpd). The heat-exchanger
arrangement is indicative only -- Duiker's text states gas-gas heat recovery
to the NH3 inlet (Table 2) but not the exact exchanger network.

Output: tcoedatabase/figures/duiker_ahc_block_diagram.png
Run:    python tools/duiker_block_diagram.py
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

OUT = Path(__file__).resolve().parents[1] / "tcoedatabase" / "figures" / "duiker_ahc_block_diagram.png"

INK, INK_2, MUTED, GRID = "#0b0b0b", "#52514e", "#8a8984", "#e6e5e0"
MAIN = "#7030A0"       # core Duiker units + fuel streams
SECONDARY = "#0070C0"  # auxiliary units + heating-side (air / hot gas / flue gas)
MAIN_LIGHT = "#8f5bb8"
SURFACE = "#ffffff"

plt.rcParams.update({"font.family": "DejaVu Sans"})
fig = plt.figure(figsize=(12.8, 7.2), dpi=150, facecolor=SURFACE)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 160)
ax.set_ylim(0, 90)
ax.axis("off")


def box(x0, y0, w, h, title, sub="", core=False, fill=None, osbl=False):
    if osbl:
        fc, ec, tc, ls = "#f4f3ef", MUTED, INK_2, (0, (3, 2))
    elif core:
        fc, ec, tc, ls = fill or MAIN, fill or MAIN, SURFACE, "-"
    else:
        fc, ec, tc, ls = SURFACE, SECONDARY, INK, "-"
    ax.add_patch(FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0,rounding_size=1.2",
                                fc=fc, ec=ec, lw=1.8, ls=ls, zorder=3))
    cy = y0 + h / 2
    tsize = 9.6 if osbl else 10.5
    if sub:
        ax.text(x0 + w / 2, cy + (2.6 if "\n" in title else 1.6), title, ha="center", va="center", fontsize=tsize,
                fontweight="bold", color=tc, zorder=4)
        ax.text(x0 + w / 2, cy - (3.0 if "\n" in title else 2.2), sub, ha="center", va="center", fontsize=8.3,
                color=tc if core else INK_2, zorder=4, linespacing=1.15)
    else:
        ax.text(x0 + w / 2, cy, title, ha="center", va="center", fontsize=10.5,
                fontweight="bold", color=tc, zorder=4)


def path(points, color, ls="-", lw=2.0, arrow=True):
    xs, ys = zip(*points)
    ax.plot(xs[:-1] + (xs[-1],), ys[:-1] + (ys[-1],), color=color, lw=lw, ls=ls,
            zorder=2, solid_capstyle="butt")
    if arrow:
        ax.add_patch(FancyArrowPatch(points[-2], points[-1], arrowstyle="-|>", mutation_scale=14,
                                     color=color, lw=0, zorder=2, shrinkA=0, shrinkB=0))


def note(x, y, text, ha="center", va="center", color=INK_2, size=8.3, weight="normal"):
    ax.text(x, y, text, ha=ha, va=va, fontsize=size, color=color, fontweight=weight,
            zorder=5, linespacing=1.2)


# --- rows ---------------------------------------------------------------
TOP_Y, TOP_H = 52, 12      # process side (NH3 -> H2), flows left to right
BOT_Y, BOT_H = 28, 12      # heating side (air -> hot gas -> flue gas), flows right to left
top_c, bot_c = TOP_Y + TOP_H / 2, BOT_Y + BOT_H / 2

# ISBL boundary
ax.add_patch(FancyBboxPatch((16, 19), 125, 55, boxstyle="round,pad=0,rounding_size=2",
                            fc="none", ec=MUTED, lw=1.2, ls=(0, (5, 3)), zorder=1))
note(18, 72.3, "ISBL (Duiker scope)", ha="left", color=MUTED, size=8.5)

# Process side
box(0.8, TOP_Y, 14, TOP_H, "NH₃ storage", "OSBL\nliquid, −33 °C", osbl=True)
box(20, TOP_Y, 17, TOP_H, "NH₃ pump &\nvaporizer")
box(44, TOP_Y, 16, TOP_H, "NH₃ preheat", "gas–gas exchanger")
box(67, BOT_Y, 26, (TOP_Y + TOP_H) - BOT_Y, "", core=True)             # reactor outline
ax.add_patch(FancyBboxPatch((67, BOT_Y), 26, 18, boxstyle="round,pad=0,rounding_size=1.2",
                            fc=MAIN_LIGHT, ec=MAIN, lw=1.8, zorder=3))  # shell side (lower)
note(80, 59.5, "Ammonia cracking\nreactor", color=SURFACE, size=10.5, weight="bold")
note(80, 51.5, "Tube side: 2NH₃ → N₂ + 3H₂\nover catalyst", color=SURFACE, size=8.6)
note(80, 38.5, "Shell side: hot gas heats\ntubes by convection only —\nno flame, no radiant box", color=SURFACE, size=8.3)
note(80, 31.5, "counter-current\n1,000 → 600 °C", color=SURFACE, size=8.3, weight="bold")
box(100, TOP_Y, 17, TOP_H, "Cracked-gas\ncooling", "H₂ + N₂ + trace NH₃\nheat integrated")
box(122, TOP_Y, 14, TOP_H, "PSA", "removes N₂ + NH₃\nin one step", core=True)
box(145, TOP_Y, 14.2, TOP_H, "H₂ product", "99.97 mol%", osbl=True)

# Heating side
box(99, BOT_Y, 20, BOT_H, "SCO combustor", "Stoichiometry-Controlled\nOxidation · one burner", core=True)
box(124, BOT_Y, 13, BOT_H, "Air blower")
box(145, BOT_Y, 14.2, BOT_H, "Air", "12.5 °C", osbl=True)
box(44, BOT_Y, 16, BOT_H, "Flue-gas\nheat recovery", "heats NH₃ feed")
box(29.5, BOT_Y, 11, BOT_H, "SCR", "small unit\nNOx → 5 ppm")
box(19, BOT_Y, 8.5, BOT_H, "Stack", "+ CEMS")
box(0.8, BOT_Y, 14, BOT_H, "Flue gas", "to atmosphere", osbl=True)

# --- process streams (ink) ------------------------------------------------
path([(14.8, top_c), (20, top_c)], INK)
path([(37, top_c), (44, top_c)], INK)
path([(60, top_c), (67, top_c)], INK)
path([(93, top_c), (100, top_c)], INK)
path([(117, top_c), (122, top_c)], INK)
path([(136, top_c), (145, top_c)], INK)
note(40.5, top_c - 2.6, "NH₃ gas", size=7.8)

# --- heating-side streams (secondary) --------------------------------------
path([(145, bot_c), (137, bot_c)], SECONDARY)
path([(124, bot_c), (119, bot_c)], SECONDARY)
path([(99, bot_c), (93, bot_c)], SECONDARY)
note(96, bot_c + 2.6, "1,000 °C", color=SECONDARY, size=7.4)
path([(67, bot_c), (60, bot_c)], SECONDARY)
note(63.5, bot_c + 2.6, "~600 °C", color=SECONDARY, size=7.8)
path([(44, bot_c), (40.5, bot_c)], SECONDARY)
path([(29.5, bot_c), (27.5, bot_c)], SECONDARY)
path([(19, bot_c), (14.8, bot_c)], SECONDARY)
# heat recovered from flue gas to NH3 feed
path([(52, BOT_Y + BOT_H), (52, TOP_Y)], SECONDARY, ls=(0, (2, 2)))
note(53.2, 46, "heat", ha="left", color=SECONDARY, size=8, weight="bold")

# --- fuel streams to SCO (main, dashed) ------------------------------------
path([(40.5, top_c), (40.5, 69), (96.5, 69), (96.5, 44), (103, 44), (103, BOT_Y + BOT_H)], MAIN,
     ls=(0, (4, 2)))
note(68.5, 70.6, "small share of NH₃ feed burned as fuel", color=MAIN, size=8.3, weight="bold")
path([(129, TOP_Y), (129, 46), (114, 46), (114, BOT_Y + BOT_H)], MAIN, ls=(0, (4, 2)))
note(127.8, 46.8, "PSA tail gas (N₂, H₂, some NH₃)\nrecycled as fuel", ha="right", va="bottom",
     color=MAIN, size=8.1, weight="bold")
path([(109, 21), (109, BOT_Y)], MUTED, ls=(0, (2, 2)))
note(107.5, 21.5, "Alternative fuel: natural gas (adds 0.21 kgCO₂/kgH₂)", ha="right", color=MUTED, size=7.8)

# --- stream data (Table 5, NH3-fired, 12 ktpa) ------------------------------
note(7.8, TOP_Y - 1.5, "10,448 kg/h\n0.04 bar(g)", va="top", size=7.8)
note(159.2, TOP_Y - 1.5, "1,487 kg/h (36 tpd)\n50 bar(g), 30 °C\nlet down to 20 bar(g)", ha="right", va="top", size=7.8)
note(152, BOT_Y - 1.5, "50,000 kg/h", va="top", size=7.8)
note(0.8, BOT_Y - 1.5, "58,961 kg/h, 45 °C\nno CO₂, NOx < 5 ppm", ha="left", va="top", size=7.8)

# --- legend -----------------------------------------------------------------
handles = [
    Line2D([], [], color=INK, lw=2, label="Process stream (NH₃ → H₂)"),
    Line2D([], [], color=SECONDARY, lw=2, label="Heating side (air → hot gas → flue gas)"),
    Line2D([], [], color=MAIN, lw=2, ls=(0, (4, 2)), label="Fuel to SCO"),
    Line2D([], [], color=SECONDARY, lw=2, ls=(0, (2, 2)), label="Heat recovery"),
    Line2D([], [], marker="s", ls="none", ms=11, color=MAIN, label="Duiker core unit (3)"),
]
ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.012, 0.875), ncol=5, frameon=False,
          fontsize=8.6, labelcolor=INK_2, handlelength=2.4, columnspacing=1.6)

# --- titles, utilities, footnote -------------------------------------------
fig.text(0.02, 0.945, "Duiker AHC — how the ammonia cracker works", fontsize=19, fontweight="bold",
         color=INK)
fig.text(0.02, 0.9, "Three core units: SCO combustor, convective cracking reactor, PSA · "
         "process at 50 bar(g) · stream values for 12 ktpa (36 tpd), NH₃-fired case",
         fontsize=11.5, color=INK_2)
note(80, 12, "Utilities: electricity 0.25 kWh/kg H₂ (blowers, pumps, instruments) · purge N₂ · "
     "closed-loop glycol · no steam system, no cooling water", color=INK, size=9)
fig.text(0.02, 0.018,
         "Source: Duiker AHC Concept Study / Budgetary Proposal 122380, 05 Dec 2025 — §2 & Table 2, "
         "§3.2, §3.4, §3.6, §3.9, Table 5 (material balance), Table 7. Simplified diagram reconstructed "
         "by Gentari from Duiker's text;\nDuiker's Figure 3 BFD is not reproduced and the "
         "heat-exchanger arrangement shown is indicative. OSBL (grey, dashed): NH₃ storage, "
         "loading/unloading, flare, control room.",
         fontsize=8, color=MUTED, va="bottom")

fig.savefig(OUT, facecolor=SURFACE)
print(OUT)
