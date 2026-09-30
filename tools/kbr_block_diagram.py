"""KBR H2ACT simplified block flow diagram -- deck PNG (1920x1080).

Built from KBR's ISBL Process Description (Licensor/kbr/
I.D_GENTARIProcess_Description_GENERAL_Rev0.md, Gentari-PR-GEN-PSD-001, Rev 0,
22 Dec 2025) §1-6, with stream values from the Feed & Product Summary
(I.E_GENTARIFeed__Product_ALL_Rev0.md, Gentari-PR-GEN-F&F-001) for 12 ktpa,
100% cracked-gas (clean) fuel mode -- the case comparable with the Duiker
NH3-fired diagram. Start-up system (N2 circulator, electric heater) omitted.

Output: tcoedatabase/figures/kbr_h2act_block_diagram.png
Run:    python tools/kbr_block_diagram.py
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

OUT = Path(__file__).resolve().parents[1] / "tcoedatabase" / "figures" / "kbr_h2act_block_diagram.png"

INK, INK_2, MUTED = "#0b0b0b", "#52514e", "#8a8984"
MAIN = "#7030A0"       # main process units + fuel streams
SECONDARY = "#0070C0"  # auxiliary units + heating side (air / flue gas) + heat recovery
MAIN_LIGHT = "#8f5bb8"
SURFACE = "#ffffff"

plt.rcParams.update({"font.family": "DejaVu Sans"})
fig = plt.figure(figsize=(12.8, 7.2), dpi=150, facecolor=SURFACE)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 160)
ax.set_ylim(0, 90)
ax.axis("off")


def box(x0, y0, w, h, title, sub="", core=False, fill=None, osbl=False, tsize=None, ssize=7.9):
    if osbl:
        fc, ec, tc, ls = "#f4f3ef", MUTED, INK_2, (0, (3, 2))
    elif core:
        fc, ec, tc, ls = fill or MAIN, MAIN, SURFACE, "-"
    else:
        fc, ec, tc, ls = SURFACE, SECONDARY, INK, "-"
    ax.add_patch(FancyBboxPatch((x0, y0), w, h, boxstyle="round,pad=0,rounding_size=1.2",
                                fc=fc, ec=ec, lw=1.8, ls=ls, zorder=3))
    tsize = tsize or (9.4 if osbl else 10)
    cx, cy = x0 + w / 2, y0 + h / 2
    if not sub:
        ax.text(cx, cy, title, ha="center", va="center", fontsize=tsize, fontweight="bold",
                color=tc, zorder=4, linespacing=1.1)
        return
    ax.text(cx, y0 + h - 1.3, title, ha="center", va="top", fontsize=tsize, fontweight="bold",
            color=tc, zorder=4, linespacing=1.1)
    ax.text(cx, y0 + 1.2, sub, ha="center", va="bottom", fontsize=ssize,
            color=tc if core else INK_2, zorder=4, linespacing=1.15)


def path(points, color, ls="-", lw=2.0):
    xs, ys = zip(*points)
    ax.plot(xs, ys, color=color, lw=lw, ls=ls, zorder=2, solid_capstyle="butt")
    ax.add_patch(FancyArrowPatch(points[-2], points[-1], arrowstyle="-|>", mutation_scale=13,
                                 color=color, lw=0, zorder=2, shrinkA=0, shrinkB=0))


def note(x, y, text, ha="center", va="center", color=INK_2, size=7.8, weight="normal"):
    ax.text(x, y, text, ha=ha, va=va, fontsize=size, color=color, fontweight=weight,
            zorder=5, linespacing=1.2)


# ISBL boundary
ax.add_patch(FancyBboxPatch((16.5, 11.5), 125, 62.5, boxstyle="round,pad=0,rounding_size=2",
                            fc="none", ec=MUTED, lw=1.2, ls=(0, (5, 3)), zorder=1))
note(18.5, 72.3, "ISBL (KBR scope)", ha="left", color=MUTED, size=8.5)

# --- feed & cracking (top row) ---------------------------------------------------
box(0.8, 57, 14, 12, "NH₃ storage", "OSBL\nliquid, −33 °C", osbl=True)
box(20, 57, 14, 12, "Feed drum\n& pump", "300-D · 301-J\n→ ~44 bar(g)")
box(39, 42, 21, 27, "Preheat train",
    "301-C liquid preheater\n302-C vaporizer\n303-C start-up vaporizer\n(LP steam)\n300-L oil filter\n"
    "304-C feed/effluent\nexchanger\n\nheated by cracker\neffluent", ssize=7.6)
box(69, 57, 17, 12, "Adiabatic\npre-cracker", "301-D · Ni catalyst", core=True)
box(96, 55, 29, 14, "Fired cracker 301-B",
    "radiant box · down-fired burners\nNi catalyst tubes · 2NH₃ → N₂ + 3H₂", core=True)
box(96, 38, 29, 14, "Convection section",
    "heat recovered to:\nNH₃ superheat & reheat · MP steam\nBFW · combustion air · tail-gas fuel",
    core=True, fill=MAIN_LIGHT, ssize=7.6)

# --- heating side (right column) -----------------------------------------------------
box(145, 57, 14.2, 12, "Air", "ambient", osbl=True)
box(128.5, 57, 11.5, 12, "FD fan", "301-BJ1")
box(128.5, 40, 11.5, 11, "SCR", "301-BSCR\nNOx < 10 ppmv")
box(128.5, 26.5, 11.5, 10, "ID fan\n& stack", "301-BJ")
box(145, 26.5, 14.2, 10, "Flue gas", "no CO₂ (clean\nfuel mode)", osbl=True)

# --- recovery, purification, fuel, steam (bottom row) ------------------------------
box(20, 17, 14, 13, "NH₃\ndistillation", "325-D + reboiler\n360-C (MP steam)", core=True, ssize=7.4)
box(39, 17, 15, 13, "HP NH₃\nscrubber", "324-D\nwater wash", core=True)
box(59.5, 17, 13, 13, "PSA", "301-L\nremoves N₂", core=True)
box(75.5, 16.5, 21, 13.5, "Steam system", "MP steam raised in convection\ndeaerator 301-U · BFW pump\n"
    "drum 341-D, 23.5 bar(g)", ssize=7.2)
box(99.5, 16.5, 19, 13.5, "Fuel system", "tail-gas compressor 311-J\nseparate fuel headers", ssize=7.2)
box(145, 9.5, 14.2, 11, "H₂ product", "99.97 mol%", osbl=True)

# --- process streams (ink) -------------------------------------------------------------
path([(14.8, 63), (20, 63)], INK)
path([(34, 63), (39, 63)], INK)
path([(60, 63), (69, 63)], INK)
note(64.5, 65.6, "superheat in\nconvection", size=7.2, va="bottom")
path([(86, 63), (96, 63)], INK)
note(91, 65.6, "reheat in\nconvection", size=7.2, va="bottom")
path([(96, 58.5), (90.5, 58.5), (90.5, 47), (60, 47)], INK)                  # effluent back to preheat
note(75, 49.3, "cracker effluent: H₂/N₂ + few % NH₃\n→ cools against incoming feed", size=7.4)
path([(49.5, 42), (49.5, 30)], INK)                                          # cooled effluent to scrubber
note(50.5, 36, "cooled\neffluent", ha="left", size=7.2)
path([(39, 23.5), (34, 23.5)], INK)                                          # scrubber bottoms
note(36.5, 25.6, "aq. NH₃", size=7, va="bottom")
path([(27, 30), (27, 57)], INK)                                              # recovered NH3 recycle
note(28.2, 36, "recovered NH₃\nrecycled to feed", ha="left", size=7.2)
path([(54, 23.5), (59.5, 23.5)], INK)                                        # scrubbed gas to PSA
path([(66, 17), (66, 14.5), (145, 14.5)], INK)                               # H2 product
note(120, 12.6, "1,426 kg/h (34.2 MTPD) · 27–28 bar(g)*, 30 °C", size=7.6)

# --- heating side (secondary) ----------------------------------------------------------
path([(145, 63), (140, 63)], SECONDARY)
path([(128.5, 63), (125, 63)], SECONDARY)
path([(110.5, 55), (110.5, 52)], SECONDARY)
note(111.5, 53.5, "flue gas", ha="left", size=6.8, color=SECONDARY)
path([(125, 45.5), (128.5, 45.5)], SECONDARY)
path([(134.25, 40), (134.25, 36.5)], SECONDARY)
path([(140, 31.5), (145, 31.5)], SECONDARY)

# --- fuel streams (main, dashed) ------------------------------------------------------
path([(69, 30), (69, 32), (103, 32), (103, 30)], MAIN, ls=(0, (4, 2)))       # PSA tail gas
note(71, 33.4, "PSA tail gas (main fuel)", ha="left", va="bottom", size=7.4, color=MAIN, weight="bold")
path([(56.8, 23.5), (56.8, 35.5), (108, 35.5), (108, 30)], MAIN, ls=(0, (4, 2)))  # cracked-gas split
note(59, 36.2, "cracked-gas split (clean-fuel top-up)", ha="left", va="bottom", size=7.4, color=MAIN,
     weight="bold")
path([(113.5, 30), (113.5, 38)], MAIN, ls=(0, (4, 2)))                       # to furnace
note(114.5, 34, "preheated →\nburners", ha="left", size=7.2, color=MAIN)
path([(124, 23), (118.5, 23)], MUTED, ls=(0, (2, 2)))                          # optional NG
note(124.5, 23, "Natural gas\n(NG modes only)", ha="left", size=7.2, color=MUTED)

# --- stream data (I.E, 12 ktpa, 100% cracked-gas fuel) ----------------------------------
note(7.8, 55.5, "10,290 kg/h\n(247 MTPD)\n2 bar(g)", va="top", size=7.6)

# --- legend, titles, utilities, footnote ----------------------------------------------------
handles = [
    Line2D([], [], color=INK, lw=2, label="Process stream (NH₃ → H₂)"),
    Line2D([], [], color=SECONDARY, lw=2, label="Heating side (air → flue gas)"),
    Line2D([], [], color=MAIN, lw=2, ls=(0, (4, 2)), label="Fuel to burners"),
    Line2D([], [], marker="s", ls="none", ms=11, color=MAIN, label="Main process unit"),
]
ax.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.012, 0.875), ncol=5, frameon=False,
          fontsize=8.6, labelcolor=INK_2, handlelength=2.4, columnspacing=1.6)
fig.text(0.02, 0.945, "KBR H₂ACT® — how the ammonia cracker works", fontsize=19, fontweight="bold",
         color=INK)
fig.text(0.02, 0.9, "Adiabatic pre-cracker + down-fired cracking furnace, water-wash NH₃ recovery, PSA · "
         "stream values for 12 ktpa, 100% cracked-gas (clean) fuel mode", fontsize=11.5, color=INK_2)
note(80, 7.2, "Utilities: electricity 342 kWh/t H₂ (all motor drives) · cooling water 30 → 40 °C · "
     "demin water make-up to deaerator · no steam import", color=INK, size=8.8)
fig.text(0.02, 0.012,
         "Source: KBR Process Description Gentari-PR-GEN-PSD-001 (I.D), Rev 0, 22 Dec 2025, §1–6; stream values "
         "from Feed & Product Summary Gentari-PR-GEN-F&F-001 (I.E). Simplified; start-up system not shown.\n"
         "* H₂ battery-limit pressure differs across KBR documents: 28 bar(g) (I.D), 27 bar(g) (I.E), "
         "20 bar(g) minimum (main package §3.1). Off-gas from NH₃ distillation goes via LP scrubber 323-D to fuel.",
         fontsize=7.8, color=MUTED, va="bottom")

fig.savefig(OUT, facecolor=SURFACE)
print(OUT)
