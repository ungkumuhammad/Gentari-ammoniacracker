"""Calc_Sensitivity -- CAPEX and ISBL plot-footprint sensitivity for KBR and
Duiker, at the required capacity and across a capacity grid.

Two sensitivities, reported separately and then stacked:

1. Scaling exponent, n +/- SensExponentDelta. The curve pivots on the
   nearest licensor-quoted capacity (nearest in log terms), so
   V(n +/- d) = V_base * (C / C_anchor)^(+/- d). At a quoted capacity the
   swing is zero; it grows the further C is from quoted data.
2. Accuracy class, V * (1 +/- accuracy). CAPEX only: KBR Class V +/-50%
   (§4.1), Duiker +/-40% (§4.1 Table 8). Neither licensor states an
   accuracy class for footprint, so none is applied.

Stacked envelope = exponent low x (1 - accuracy) ... exponent high x
(1 + accuracy): a worst-case stack, not a statistical range.

Base curves: KBR uses the same piecewise log-log interpolation as
Calc_CapacitySizing inside 12-80 ktpa and the global log-log fit outside
it. Duiker CAPEX is the single quoted point (EUR47M @ 12 ktpa) scaled with
the assumed exponent on Inputs (six-tenths rule) -- this is a sensitivity
view only and does not feed the headline CAPEX_Total_Own. Duiker footprint
uses the two-point power law through 12 ktpa / 900 m2 and the 276 tpd /
3,660 m2 standard train.
"""
from openpyxl.worksheet.worksheet import Worksheet

from tools.cracker_model import data
from tools.cracker_model import named_ranges as nr
from tools.cracker_model import styles as st

CAP = nr.REQUIRED_H2_CAPACITY_KTPA
LIC = nr.LICENSOR_SELECTED
MODE = nr.COMMERCIAL_MODE
D = nr.SENS_EXPONENT_DELTA
KBR_CAPS = [nr.KBR_CAP1, nr.KBR_CAP2, nr.KBR_CAP3, nr.KBR_CAP4]
KBR_CAPEX = [nr.KBR_CAPEX1, nr.KBR_CAPEX2, nr.KBR_CAPEX3, nr.KBR_CAPEX4]
KBR_FP = [nr.KBR_FP1, nr.KBR_FP2, nr.KBR_FP3, nr.KBR_FP4]
MAX_CF_YEARS = 30  # matches Calc_CashFlow_IRR.MAX_YEARS


# --- formula-expression generators (c = capacity cell ref or name) ---

def kbr_curve(c: str, vals: list, a: str, b: str) -> str:
    """Piecewise log-log through KBR's 4 points inside 12-80 ktpa, global fit outside."""
    def seg(i):
        return (f"{vals[i]}*({c}/{KBR_CAPS[i]})^"
                f"(LN({vals[i + 1]}/{vals[i]})/LN({KBR_CAPS[i + 1]}/{KBR_CAPS[i]}))")
    piece = f"IF({c}<={KBR_CAPS[1]},{seg(0)},IF({c}<={KBR_CAPS[2]},{seg(1)},{seg(2)}))"
    return f"IF(AND({c}>={KBR_CAPS[0]},{c}<={KBR_CAPS[3]}),{piece},{a}*{c}^{b})"


def kbr_anchor(c: str) -> str:
    """Nearest KBR-quoted capacity in log terms (switch at the geometric mean)."""
    k = KBR_CAPS
    return (f"IF({c}<SQRT({k[0]}*{k[1]}),{k[0]},IF({c}<SQRT({k[1]}*{k[2]}),{k[1]},"
            f"IF({c}<SQRT({k[2]}*{k[3]}),{k[2]},{k[3]})))")


def duiker_capex(c: str) -> str:
    return f"{nr.DUIKER_CAPEX_TOTAL_EUR_M}*({c}/{nr.DUIKER_BASE_CAP_KTPA})^{nr.DUIKER_CAPEX_EXPONENT}"


def duiker_fp(c: str) -> str:
    return f"{nr.DUIKER_FP_BASE_M2}*({c}/{nr.DUIKER_BASE_CAP_KTPA})^{nr.DUIKER_FP_EXPONENT}"


def duiker_fp_anchor(c: str) -> str:
    return (f"IF({c}<SQRT({nr.DUIKER_BASE_CAP_KTPA}*{nr.DUIKER_STD_TRAIN_CAP_KTPA}),"
            f"{nr.DUIKER_BASE_CAP_KTPA},{nr.DUIKER_STD_TRAIN_CAP_KTPA})")


def swing(c: str, anchor: str) -> str:
    """(C / C_anchor)^delta -- multiply base by this for n + delta, divide for n - delta."""
    return f"({c}/({anchor}))^{D}"


def _grid_capacity_cell(ws, r, cap):
    """Grid row label: a live link for the required capacity, a fixed number otherwise."""
    if isinstance(cap, str):
        st.style_calculated(ws.cell(r, 2, f"={cap}"))
    else:
        st.style_label(ws.cell(r, 2, cap), bold=False)


def build(wb, cs_rows: dict, cashflow_rows: dict) -> Worksheet:
    ws = wb.create_sheet(nr.SHEET_CALC_SENSITIVITY)
    ws.sheet_view.showGridLines = False
    ws.column_dimensions["A"].width = 2
    ws.column_dimensions["B"].width = 44
    ws.column_dimensions["C"].width = 9
    for col in "DEFGHIJKLMNOP":
        ws.column_dimensions[col].width = 14
    ws.column_dimensions["L"].width = 58

    note_font = st.body_font(italic=True, color=st.COLOR_SECONDARY_STEEL_GRAY)

    r = 2
    ws.cell(r, 2, "Calc_Sensitivity -- CAPEX & Footprint")
    st.style_title(ws.cell(r, 2))
    r += 1
    for line in [
        "Scaling exponent: V(n +/- d) = V_base x (C / C_anchor)^(+/- d); C_anchor = nearest "
        "licensor-quoted capacity (log distance), so the swing is zero at a quoted point.",
        "Accuracy class (CAPEX only): V x (1 +/- acc). KBR Class V +/-50% (§4.1); Duiker +/-40% "
        "(§4.1 Table 8). No accuracy class is stated for footprint by either licensor.",
        "Stacked = exponent low x (1 - acc) to exponent high x (1 + acc) -- worst-case stack, "
        "not a statistical confidence interval.",
    ]:
        ws.cell(r, 2, line)
        ws.cell(r, 2).font = st.body_font(italic=True)
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=12)
        r += 1
    r += 1

    def header(title, end_col=12):
        nonlocal r
        ws.cell(r, 2, title)
        st.style_section_header(ws.cell(r, 2))
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=end_col)
        r += 1

    def label_row(labels, start_col=2):
        for j, h in enumerate(labels):
            c = ws.cell(r, start_col + j, h)
            st.style_label(c)
            c.alignment = st.Alignment(wrap_text=True, vertical="center")
        ws.row_dimensions[r].height = 30

    # --- Section A: drivers ---
    header("Sensitivity drivers (edit on Inputs / Constants)")
    for label, ref, note in [
        ("Required H2 capacity C (ktpa)", CAP, "Inputs"),
        ("Exponent swing d (+/- on n)", D, "Inputs -- ASSUMPTION, not sourced"),
        ("Duiker CAPEX exponent n", nr.DUIKER_CAPEX_EXPONENT,
         "Inputs -- ASSUMPTION (six-tenths rule), Duiker quotes one CAPEX point"),
        ("KBR CAPEX exponent n (global log-log fit)", nr.CAPACITY_REGRESSION_SLOPE_B,
         "Constants -- in-range base uses KBR's piecewise segments"),
        ("KBR footprint exponent n (global log-log fit)", nr.KBR_FP_REGRESSION_SLOPE_B,
         "Constants -- in-range base uses KBR's piecewise segments"),
        ("Duiker footprint exponent n (two-point fit)", nr.DUIKER_FP_EXPONENT, "Constants"),
        ("KBR CAPEX accuracy (+/- %)", nr.KBR_CAPEX_ACCURACY_PCT, "Constants -- KBR §4.1"),
        ("Duiker CAPEX accuracy (+/- %)", nr.DUIKER_CAPEX_ACCURACY_PCT, "Constants -- Duiker §4.1 Table 8"),
        ("sqft per m2", nr.SQFT_PER_M2, "Constants -- 1 ft = 0.3048 m exact"),
    ]:
        ws.cell(r, 2, label)
        st.style_label(ws.cell(r, 2), bold=False)
        st.style_calculated(ws.cell(r, 4, f"={ref}"))
        ws.cell(r, 5, note).font = note_font
        r += 1
    r += 1

    # --- Section B: point sensitivity at the required capacity ---
    header("Sensitivity at the required capacity")
    label_row(["Series", "Unit", "Base", "n - d", "n + d", "Accuracy low", "Accuracy high",
               "Stacked low", "Stacked high", "Anchor (ktpa)", "Basis / flag"])
    r += 1
    rows = {}

    kbr_in_range = f"AND({CAP}>={KBR_CAPS[0]},{CAP}<={KBR_CAPS[3]})"
    series = [
        # key, label, unit, base formula, anchor expr, accuracy name or None, flag formula
        ("kbr_capex", "KBR ISBL CAPEX", "MUSD",
         f"='{nr.SHEET_CALC_CAPACITY_SIZING}'!$D${cs_rows['kbr_capex_row']}",
         kbr_anchor(CAP), nr.KBR_CAPEX_ACCURACY_PCT,
         f'=IF({kbr_in_range},"Within KBR quoted 12-80 ktpa (piecewise)",'
         f'"EXTRAPOLATED -- global log-log fit, not KBR-quoted")'),
        ("duiker_capex", "Duiker CAPEX (no ISBL/OSBL split)", "MEUR",
         f"={duiker_capex(CAP)}", nr.DUIKER_BASE_CAP_KTPA, nr.DUIKER_CAPEX_ACCURACY_PCT,
         f'=IF({CAP}={nr.DUIKER_BASE_CAP_KTPA},"Duiker quoted point (12 ktpa)",'
         f'"SCALED -- n = "&TEXT({nr.DUIKER_CAPEX_EXPONENT},"0.00")&" ASSUMED; sensitivity only, '
         f'headline CAPEX stays N/A")'),
        ("kbr_fp", "KBR ISBL plot footprint", "m2",
         f"={kbr_curve(CAP, KBR_FP, nr.KBR_FP_REGRESSION_INTERCEPT_A, nr.KBR_FP_REGRESSION_SLOPE_B)}",
         kbr_anchor(CAP), None,
         f'=IF({kbr_in_range},"Within KBR quoted 12-80 ktpa (piecewise)",'
         f'"EXTRAPOLATED -- global log-log fit, not KBR-quoted")'),
        ("duiker_fp", "Duiker plot space (single train)", "m2",
         f"={duiker_fp(CAP)}", duiker_fp_anchor(CAP), None,
         f'=IF(AND({CAP}>={nr.DUIKER_BASE_CAP_KTPA},{CAP}<={nr.DUIKER_STD_TRAIN_CAP_KTPA}),'
         f'"Within Duiker 12-92 ktpa span (two-point fit)","EXTRAPOLATED beyond Duiker two-point fit")'),
    ]
    for key, label, unit, base_f, anchor_f, acc, flag_f in series:
        ws.cell(r, 2, label)
        st.style_label(ws.cell(r, 2), bold=False)
        ws.cell(r, 3, unit)
        st.style_calculated(ws.cell(r, 4, base_f))
        st.style_calculated(ws.cell(r, 11, f"={anchor_f}"))
        sw = swing(CAP, f"K{r}")
        st.style_calculated(ws.cell(r, 5, f"=D{r}/{sw}"))
        st.style_calculated(ws.cell(r, 6, f"=D{r}*{sw}"))
        if acc:
            st.style_calculated(ws.cell(r, 7, f"=D{r}*(1-{acc}/100)"))
            st.style_calculated(ws.cell(r, 8, f"=D{r}*(1+{acc}/100)"))
            st.style_calculated(ws.cell(r, 9, f"=MIN(E{r},F{r})*(1-{acc}/100)"))
            st.style_calculated(ws.cell(r, 10, f"=MAX(E{r},F{r})*(1+{acc}/100)"))
        else:
            for col in (7, 8):
                st.style_na_flag(ws.cell(r, col, "N/A -- none stated"))
            st.style_calculated(ws.cell(r, 9, f"=MIN(E{r},F{r})"))
            st.style_calculated(ws.cell(r, 10, f"=MAX(E{r},F{r})"))
        st.style_extrapolation_flag(ws.cell(r, 12, flag_f))
        rows[key] = r
        r += 1
        if unit == "m2":
            ws.cell(r, 2, f"{label} (sqft)")
            st.style_label(ws.cell(r, 2), bold=False)
            ws.cell(r, 3, "sqft")
            for col in (4, 5, 6, 9, 10):
                letter = "DEFGHIJ"[col - 4]
                st.style_calculated(ws.cell(r, col, f"={letter}{r - 1}*{nr.SQFT_PER_M2}"))
            for col in (7, 8):
                st.style_na_flag(ws.cell(r, col, "N/A -- none stated"))
            rows[f"{key}_sqft"] = r
            r += 1
        elif key == "duiker_capex":
            ws.cell(r, 2, f"{label} in USD")
            st.style_label(ws.cell(r, 2), bold=False)
            ws.cell(r, 3, "MUSD")
            for col in range(4, 11):
                letter = "DEFGHIJ"[col - 4]
                st.style_calculated(ws.cell(r, col, f"={letter}{r - 1}*{nr.EURUSD_FX_RATE}"))
            ws.cell(r, 12, "Converted at EURUSD_FXRate (Inputs)").font = note_font
            rows["duiker_capex_usd"] = r
            r += 1
    ws.cell(r, 2, "Footprint: KBR excludes offsites & utilities; Duiker excludes NH3 storage and H2 "
                  "compression beyond 50 barg -- scopes not verified as like-for-like.").font = note_font
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=12)
    r += 2

    # --- Section C: selected licensor -> total CAPEX, NPV, IRR ---
    header("Selected licensor -- CAPEX_Total_Own range and its effect on NPV / IRR (Own & Operate)")
    ws.cell(r, 2, "CAPEX_Total_Own base (MUSD, incl. OSBL where modelled, region-adjusted)")
    st.style_label(ws.cell(r, 2), bold=False)
    st.style_calculated(ws.cell(r, 4, f"={nr.CAPEX_TOTAL_OWN}"))
    base_total_row = r
    r += 1
    ws.cell(r, 2, "NPV / IRR at base CAPEX")
    st.style_label(ws.cell(r, 2), bold=False)
    st.style_calculated(ws.cell(r, 4, f"={nr.NPV_RESULT}"))
    st.style_calculated(ws.cell(r, 5, f"={nr.IRR_RESULT}"))
    ws.cell(r, 6, "NPV (MUSD) | IRR -- from Calc_CashFlow_IRR").font = note_font
    r += 2
    label_row(["Case", "", "CAPEX low (MUSD)", "CAPEX high (MUSD)", "NPV @ CAPEX low",
               "NPV @ CAPEX high", "IRR @ CAPEX low", "IRR @ CAPEX high"])
    r += 1

    kc, dc = rows["kbr_capex"], rows["duiker_capex"]
    capex_ok = (f"AND(ISNUMBER({nr.CAPEX_TOTAL_OWN}),OR({LIC}=\"KBR\",{LIC}=\"Duiker\"))")
    na_capex = ('"N/A -- no CAPEX range: licensor has no scalable CAPEX or accuracy class, '
                'or headline CAPEX is N/A at this capacity"')

    def ratio(col):
        return f'IF({LIC}="KBR",{col}{kc}/D{kc},{col}{dc}/D{dc})'

    ncf_ref = f"'{nr.SHEET_CALC_CASHFLOW_IRR}'!$D${cashflow_rows['annual_ncf_row']}"
    # ISNUMBER(ncf) guard: when OPEX is N/A the cash-flow rows are text, NPV() skips them and
    # NPV_Result collapses to -CAPEX -- not a result to carry into the sensitivity.

    def npv_ok(x):
        return f'AND(ISNUMBER({x}),{MODE}="Own & Operate",ISNUMBER({nr.NPV_RESULT}),ISNUMBER({ncf_ref}))'

    life = f"MIN({nr.PROJECT_LIFE_YR},{MAX_CF_YEARS})"
    case_rows = {}
    for key, label, lo_col, hi_col in [
        ("exponent", "Scaling exponent (n +/- d)", "E", "F"),
        ("accuracy", "Accuracy class (+/- %)", "G", "H"),
        ("stacked", "Stacked (exponent x accuracy)", "I", "J"),
    ]:
        ws.cell(r, 2, label)
        st.style_label(ws.cell(r, 2), bold=False)
        both = f"{nr.CAPEX_TOTAL_OWN}*{ratio(lo_col)},{nr.CAPEX_TOTAL_OWN}*{ratio(hi_col)}"
        st.style_calculated(ws.cell(r, 4, f"=IF({capex_ok},MIN({both}),{na_capex})"))
        st.style_calculated(ws.cell(r, 5, f"=IF({capex_ok},MAX({both}),{na_capex})"))
        for col, x in ((6, f"D{r}"), (7, f"E{r}")):
            cond = npv_ok(x)
            st.style_calculated(ws.cell(
                r, col, f'=IF({cond},{nr.NPV_RESULT}+{nr.CAPEX_TOTAL_OWN}-{x},"N/A")'))
        for col, x in ((8, f"D{r}"), (9, f"E{r}")):
            cond = npv_ok(x)
            c = ws.cell(r, col, f'=IFERROR(IF({cond},RATE({life},{ncf_ref},-{x}),"N/A"),"N/A")')
            st.style_calculated(c)
            c.number_format = "0.0%"
        case_rows[key] = r
        r += 1
    for rr in case_rows.values():
        for col in (4, 5, 6, 7):
            ws.cell(rr, col).number_format = "#,##0.0"
    ws.cell(r, 2, "Total CAPEX low/high = CAPEX_Total_Own x (licensor ISBL-basis low or high / base), so "
                  "OSBL % and regional factor scale with it. NPV shift = -(CAPEX change): CAPEX is the "
                  "undiscounted Year 0 outflow. IRR = RATE(life, annual net cash flow, -CAPEX): the "
                  "Year 1..N cash flow is level, so this equals the IRR() on Calc_CashFlow_IRR. "
                  "Tolling mode has no CAPEX, so NPV/IRR show N/A.").font = note_font
    ws.cell(r, 2).alignment = st.Alignment(wrap_text=True, vertical="top")
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=12)
    ws.row_dimensions[r].height = 45
    nr.register(wb, nr.CAPEX_SENS_LOW, f"'{nr.SHEET_CALC_SENSITIVITY}'!$D${case_rows['stacked']}")
    nr.register(wb, nr.CAPEX_SENS_HIGH, f"'{nr.SHEET_CALC_SENSITIVITY}'!$E${case_rows['stacked']}")
    r += 2

    ws.cell(r, 2, "Selected licensor ISBL plot footprint")
    st.style_label(ws.cell(r, 2))
    r += 1
    label_row(["", "Unit", "Base", "Low (n - d / n + d)", "High"])
    r += 1
    na_fp = ('"N/A -- no scalable footprint for this licensor (Topsoe/Technip: single TCOE '
             '80 x 80 m entry; Casale: not stated)"')
    kf, df = rows["kbr_fp"], rows["duiker_fp"]
    fp_rows = {}
    for unit, k_row, d_row in (("m2", kf, df), ("sqft", rows["kbr_fp_sqft"], rows["duiker_fp_sqft"])):
        ws.cell(r, 2, f"Footprint ({unit})")
        st.style_label(ws.cell(r, 2), bold=False)
        ws.cell(r, 3, unit)
        for col, src in ((4, "D"), (5, "I"), (6, "J")):
            c = ws.cell(r, col, f'=IF({LIC}="KBR",{src}{k_row},IF({LIC}="Duiker",{src}{d_row},{na_fp}))')
            st.style_calculated(c)
            c.number_format = "#,##0"
        fp_rows[unit] = r
        r += 1
    nr.register(wb, nr.FOOTPRINT_BASE_M2, f"'{nr.SHEET_CALC_SENSITIVITY}'!$D${fp_rows['m2']}")
    nr.register(wb, nr.FOOTPRINT_SENS_LOW_M2, f"'{nr.SHEET_CALC_SENSITIVITY}'!$E${fp_rows['m2']}")
    nr.register(wb, nr.FOOTPRINT_SENS_HIGH_M2, f"'{nr.SHEET_CALC_SENSITIVITY}'!$F${fp_rows['m2']}")
    r += 1

    # --- Section D: capacity grids ---
    grid_caps = [CAP] + data.SENSITIVITY_GRID_KTPA

    header("CAPEX across capacity -- stacked low / base / high (exponent x accuracy)")
    label_row(["Capacity (ktpa)", "", "KBR ISBL low (MUSD)", "KBR ISBL base", "KBR ISBL high",
               "Duiker low (MEUR)", "Duiker base", "Duiker high"])
    r += 1
    capex_grid_start = r
    for cap in grid_caps:
        _grid_capacity_cell(ws, r, cap)
        c = f"$B{r}"
        kb = kbr_curve(c, KBR_CAPEX, nr.CAPACITY_REGRESSION_INTERCEPT_A, nr.CAPACITY_REGRESSION_SLOPE_B)
        ks = swing(c, kbr_anchor(c))
        ds = swing(c, nr.DUIKER_BASE_CAP_KTPA)
        cells = {
            4: f"=E{r}*MIN({ks},1/{ks})*(1-{nr.KBR_CAPEX_ACCURACY_PCT}/100)",
            5: f"={kb}",
            6: f"=E{r}*MAX({ks},1/{ks})*(1+{nr.KBR_CAPEX_ACCURACY_PCT}/100)",
            7: f"=H{r}*MIN({ds},1/{ds})*(1-{nr.DUIKER_CAPEX_ACCURACY_PCT}/100)",
            8: f"={duiker_capex(c)}",
            9: f"=H{r}*MAX({ds},1/{ds})*(1+{nr.DUIKER_CAPEX_ACCURACY_PCT}/100)",
        }
        for col, f in cells.items():
            cell = ws.cell(r, col, f)
            st.style_calculated(cell)
            cell.number_format = "#,##0.0"
        r += 1
    ws.cell(r, 2, "First row = required capacity. KBR outside 12-80 ktpa and Duiker away from 12 ktpa "
                  "are extrapolated / scaled (see flags above), not licensor-quoted.").font = note_font
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=12)
    r += 2

    header("ISBL plot footprint across capacity -- low / base / high (exponent only)", end_col=15)
    label_row(["Capacity (ktpa)", "", "KBR low (m2)", "KBR base (m2)", "KBR high (m2)",
               "KBR base (sqft)", "Duiker low (m2)", "Duiker base (m2)", "Duiker high (m2)",
               "Duiker base (sqft)", "KBR range (sqft)", "Duiker range (sqft)"])
    r += 1
    fp_grid_start = r
    for cap in grid_caps:
        _grid_capacity_cell(ws, r, cap)
        c = f"$B{r}"
        kb = kbr_curve(c, KBR_FP, nr.KBR_FP_REGRESSION_INTERCEPT_A, nr.KBR_FP_REGRESSION_SLOPE_B)
        ks = swing(c, kbr_anchor(c))
        ds = swing(c, duiker_fp_anchor(c))
        cells = {
            4: f"=E{r}*MIN({ks},1/{ks})",
            5: f"={kb}",
            6: f"=E{r}*MAX({ks},1/{ks})",
            7: f"=E{r}*{nr.SQFT_PER_M2}",
            8: f"=I{r}*MIN({ds},1/{ds})",
            9: f"={duiker_fp(c)}",
            10: f"=I{r}*MAX({ds},1/{ds})",
            11: f"=I{r}*{nr.SQFT_PER_M2}",
            12: f'=TEXT(D{r}*{nr.SQFT_PER_M2},"#,##0")&" - "&TEXT(F{r}*{nr.SQFT_PER_M2},"#,##0")',
            13: f'=TEXT(H{r}*{nr.SQFT_PER_M2},"#,##0")&" - "&TEXT(J{r}*{nr.SQFT_PER_M2},"#,##0")',
        }
        for col, f in cells.items():
            cell = ws.cell(r, col, f)
            st.style_calculated(cell)
            cell.number_format = "#,##0"
        r += 1
    ws.column_dimensions["M"].width = 20
    ws.cell(r, 2, "Footprint low/high comes from the exponent swing only -- no accuracy class is stated "
                  "for footprint. KBR: piecewise inside 12-80 ktpa, global fit outside. Duiker: two-point "
                  "fit (12 ktpa / 900 m2 and ~92 ktpa / 3,660 m2).").font = note_font
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=13)

    rows.update({
        "base_total_row": base_total_row,
        "case_rows": case_rows,
        "fp_rows": fp_rows,
        "capex_grid_start": capex_grid_start,
        "fp_grid_start": fp_grid_start,
    })
    return ws, rows
