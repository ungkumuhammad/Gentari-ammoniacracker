"""KBR H2ACT 12 kTPA H2 -- preliminary OSBL equipment sizing (Units 101-114).

Sizes the items on KBR's OSBL equipment list (I.H, Gentari-PR-GEN-LST-0002)
from KBR's own utility, feed/product and HMB figures. Every KBR input below
carries its source; every non-KBR input is tagged ASSUMPTION (A-number, as
listed in tcoedatabase/KBR_OSBL_Sizing_12ktpa.md) or cites a public source.

KBR sources (Licensor/kbr/, all Rev 0, Dec 2025):
  I.A  Process Design Basis          Gentari-PR-GEN-PDB-001
  I.C  Heat & Material Balance       Gentari-PR-GEN-HMB-001 (12 kTPA, NG mode)
  I.E  Feed & Product Summary        Gentari-PR-GEN-F&F-001
  I.F  Utility Summary (ISBL)        Gentari-PR-GEN-BLS-001 (12 kTPA)
  hub  Technical Information Package kbr-johor-hub.md

Run: python tools/kbr_osbl_sizing_12ktpa.py
"""
import math

# ---- KBR inputs -------------------------------------------------------------
P_MAX_KW = 540            # I.F Electrical Power, maximum (Notes 7, 9)
P_EMERG_KBR_KW = 300      # I.F Note 9, KBR's own emergency backup estimate
DEMIN_NOR, DEMIN_MAX = 245, 270      # kg/h, I.F
CW_NOR, CW_MAX = 30.1, 40.0          # t/h, I.F (max incl. start-up coolers)
CW_DT = 40 - 30                      # degC, I.A s.6 / I.D s.6 (30 -> 40 degC)
PA_NOR, PA_MAX = 150, 250            # Nm3/h plant air, I.F
IA_NOR, IA_MAX = 300, 350            # Nm3/h instrument air, I.F
AIR_P_BARG = 7.5                     # I.F
N2_NOR, N2_MAX = 150, 500            # Nm3/h, I.F (max intermittent, start-up)
NG_MAX = 450                         # kg/h, I.F (covers start-up, Note 10)
NG_MW, NG_LHV = 16.95, 49.560        # I.C stream 13 / I.E
NH3_FEED = 9104                      # kg/h total incl. water, I.C stream 1
NH3_KMOL = 531.9                     # kmol/h dry NH3, I.C stream 1
H2_KG, H2_NM3, H2_AM3 = 1435, 15890, 648   # I.C stream 8 (27 barg, 30 degC)
H2_IE = 1426                         # kg/h, I.E (12 kTPA, 100% NG)
TURNDOWN = 0.40                      # I.A s.9
BD_T_PER_T_H2 = 0.06                 # hub s.3.5 steam blowdown (< 0.06 t/t H2)
DNW_T_PER_T_H2 = 0.1                 # hub s.3.3 DNW consumption
CW_T_PER_T_H2 = 25                   # hub s.3.3 CW consumption
T_AMB, RH = 28.0, 80.0               # I.A s.4

# ---- User-specified inputs (Emergency power method) ------------------------
P_FACTOR = 2.0            # x2 on I.F max: Note 7 excludes OSBL/intermittent users
BACKUP_H = 24             # h of backup autonomy
GEN_EFF = 0.50            # engine/genset efficiency

# ---- Public-source constants -----------------------------------------------
DIESEL_LHV = 43.0         # MJ/kg, IPCC 2006 GL Vol.2 Ch.1 Table 1.2 (gas/diesel oil NCV 43.0 TJ/Gg)
DIESEL_RHO = 820          # kg/m3, EN 590 density range 820-845 @15 degC (low end -> larger volume)
CP_W = 4.186              # kJ/kg.K water
HFG_30C = 2430            # kJ/kg latent heat of water @30 degC (steam tables)
LN2_RHO, N2_GAS_RHO = 806.6, 1.2506  # kg/m3 liquid N2 @ NBP; N2 gas @0 degC, 1 atm
NM3_PER_KMOL = 22.414
SHOWER_LPM, SHOWER_MIN = 75.7, 15    # ANSI/ISEA Z358.1: 20 gpm for 15 min
POTABLE_LPPD = 100        # L/person/day, WHO/UN 50-100 L/p/d (upper end)

# ---- Assumptions (see A-list in the markdown) -------------------------------
MARGIN = 1.10             # A1 design margin on KBR maximum flows
HOLD_H = 24               # A2 storage autonomy, h (mirrors user's 24 h diesel basis)
FILL = 0.90               # A2 net/nominal tank volume
COC = 5                   # A6 cooling tower cycles of concentration
DEMIN_RECOVERY = 0.80     # A7 demin plant product/feed
HEADCOUNT = 30            # A8 persons on site (owner to confirm)
SHOWERS = 2               # A8 simultaneous safety showers
DRYER_PURGE = 0.15        # A9 heatless IA dryer purge fraction
IA_HOLD_MIN, IA_P_MIN_BARG = 15, 4.0   # A10 IA receiver hold-up
WET_HOLD_MIN = 2          # A10 wet air receiver, min of compressor output
COMP_DISCH_BARG = 8.5     # A9 compressor discharge (1 bar over 7.5 barg header)
ISOTHERMAL_EFF = 0.65     # A9 for power cross-check only
N2_STARTUP_H = 24         # A11 duration of start-up N2 peak
PIPE_V_MAX = 20           # A12 m/s max gas velocity for H2 export line
CW_PUMP_DP_BAR, PUMP_EFF = 5.5, 0.70   # cross-check only


def tank(flow_per_h, hours=HOLD_H):
    net = flow_per_h * hours
    return net, net / FILL


def stull_wet_bulb(t, rh):
    """Stull (2011) J. Appl. Meteor. Climatol. 50, 2267 -- valid 5-99 %RH, -20..50 degC."""
    return (t * math.atan(0.151977 * (rh + 8.313659) ** 0.5) + math.atan(t + rh)
            - math.atan(rh - 1.676331) + 0.00391838 * rh ** 1.5 * math.atan(0.023101 * rh)
            - 4.686035)


def main():
    r = {}
    # Unit 101 emergency power
    p = P_MAX_KW * P_FACTOR
    e_el = p * BACKUP_H
    fuel_mj = e_el / GEN_EFF * 3.6
    fuel_kg = fuel_mj / DIESEL_LHV
    r["101 genset kWe"] = p
    r["101 genset kVA @0.8pf"] = p / 0.8
    r["101 diesel burn kg/h"] = fuel_kg / BACKUP_H
    r["101 diesel burn L/h"] = fuel_kg / BACKUP_H / DIESEL_RHO * 1000
    r["101 diesel kg / 24h"] = fuel_kg
    r["101 tank net m3"], r["101 tank nominal m3"] = fuel_kg / DIESEL_RHO, fuel_kg / DIESEL_RHO / FILL
    r["101 sens: 40% eff net m3"] = e_el / 0.40 * 3.6 / DIESEL_LHV / DIESEL_RHO
    r["101 sens: KBR 300 kW net m3"] = P_EMERG_KBR_KW * BACKUP_H / GEN_EFF * 3.6 / DIESEL_LHV / DIESEL_RHO

    # Unit 107 cooling water
    cw = CW_MAX * MARGIN
    duty_kw = cw * 1000 * CP_W * CW_DT / 3600
    evap = duty_kw * 3600 / HFG_30C
    bd = evap / (COC - 1)
    r["107 CW circ m3/h"] = cw
    r["107 CW duty kW"] = duty_kw
    r["107 evap kg/h"], r["107 blowdown kg/h"], r["107 makeup kg/h"] = evap, bd, evap + bd
    r["107 wet bulb degC"] = stull_wet_bulb(T_AMB, RH)
    r["107 pump hyd->shaft kW (total)"] = cw / 3600 * CW_PUMP_DP_BAR * 1e5 / PUMP_EFF / 1000
    r["107 hub-derived CW t/h"] = CW_T_PER_T_H2 * H2_IE / 1000

    # Units 103/104 demin + polishing
    demin = DEMIN_MAX * MARGIN
    r["103 demin design kg/h"] = demin
    r["103/104 tank net, nominal m3"] = tank(demin / 1000)
    r["103 demin feed kg/h"] = demin / DEMIN_RECOVERY
    r["103 demin waste kg/h"] = demin / DEMIN_RECOVERY - demin
    r["132-F neutralisation tank net, nominal m3"] = tank(r["103 demin waste kg/h"] / 1000)
    r["hub-derived DNW kg/h"] = DNW_T_PER_T_H2 * H2_IE

    # Unit 105 potable
    pot_d = HEADCOUNT * POTABLE_LPPD / 1000
    shower = SHOWERS * SHOWER_LPM * SHOWER_MIN / 1000
    r["105 potable m3/d"] = pot_d
    r["105 tank net, nominal m3"] = (pot_d + shower, (pot_d + shower) / FILL)
    r["105 pump m3/h"] = SHOWERS * SHOWER_LPM * 60 / 1000 + 3 * pot_d / 24

    # Unit 102 raw water (excl. fire water reserve)
    raw = r["107 makeup kg/h"] + r["103 demin feed kg/h"] + pot_d / 24 * 1000
    r["102 raw continuous kg/h"] = raw
    r["102 tank net, nominal m3 (excl fire)"] = tank(raw / 1000)

    # Unit 108 flare + fuel gas
    cracked_kmol = NH3_KMOL * 2  # 2 NH3 -> N2 + 3 H2 : 2 mol out per mol NH3
    r["108 flare kg/h"] = NH3_FEED * MARGIN
    r["108 flare Nm3/h"] = cracked_kmol * MARGIN * NM3_PER_KMOL
    r["108 cracked gas MW"] = (NH3_KMOL * 17.031) / cracked_kmol
    ng = NG_MAX * MARGIN
    r["182 NG kg/h"], r["182 NG Nm3/h"] = ng, ng / NG_MW * NM3_PER_KMOL
    r["182 NG LHV MW"] = ng * NG_LHV / 3600

    # Unit 109 air
    ia = IA_MAX * MARGIN
    dryer_in = ia / (1 - DRYER_PURGE)
    comp = PA_MAX * MARGIN + dryer_in
    r["191-L dryer product / inlet Nm3/h"] = (ia, dryer_in)
    r["191-J total / each of 2 duty Nm3/h"] = (comp, comp / 2)
    w_iso = 101325 * math.log((COMP_DISCH_BARG + 1.01325) / 1.01325) / 3.6e6  # kWh/Nm3
    r["191-J shaft kW est (total)"] = comp * w_iso / ISOTHERMAL_EFF
    r["192-D IA receiver m3"] = IA_MAX * IA_HOLD_MIN / 60 * 1.01325 / (AIR_P_BARG - IA_P_MIN_BARG)
    r["191-D wet receiver m3"] = comp * WET_HOLD_MIN / 60 * 1.01325 / (AIR_P_BARG - IA_P_MIN_BARG)

    # Unit 110 N2
    gen = N2_NOR * MARGIN
    deficit = N2_MAX - gen
    ln2 = deficit * N2_STARTUP_H / (LN2_RHO / N2_GAS_RHO)
    r["201-L gen Nm3/h"] = gen
    r["201-D LN2 net, nominal m3"] = (ln2, ln2 / FILL)
    r["201-C vaporiser each Nm3/h"] = N2_MAX * MARGIN

    # Unit 112 waste water
    bd_steam = BD_T_PER_T_H2 * H2_IE
    r["112 steam blowdown kg/h"] = bd_steam
    r["112 continuous effluent kg/h"] = bd_steam + bd + r["103 demin waste kg/h"]

    # Unit 113 H2 export
    r["232-L design kg/h / Nm3/h / Am3/h"] = (H2_KG * MARGIN, H2_NM3 * MARGIN, H2_AM3 * MARGIN)
    r["232-L min kg/h (40% turndown)"] = H2_KG * TURNDOWN
    q = H2_AM3 * MARGIN / 3600
    r["231-L min ID mm @20 m/s"] = math.sqrt(4 * q / math.pi / PIPE_V_MAX) * 1000
    r["231-L v in DN150 sch40 (154.1 mm) m/s"] = q / (math.pi / 4 * 0.1541 ** 2)

    for k, v in r.items():
        if isinstance(v, tuple):
            print(f"{k:45s} " + " / ".join(f"{x:,.2f}" for x in v))
        else:
            print(f"{k:45s} {v:,.2f}")


if __name__ == "__main__":
    main()
