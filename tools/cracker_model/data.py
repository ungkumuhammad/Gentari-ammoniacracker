"""Single source-of-truth for every quantitative figure in the workbook.

Per CLAUDE.md §5 (No-Fabrication Rule): every numeric value defined here
must carry either a `Citation` (source document + section + revision date)
or be explicitly marked `is_assumption=True` with an `Assumption` note that
also appears in memory.md. `validate_data.py` enforces this mechanically.

Sheet-builder modules under tools/cracker_model/sheets/ import from this
module and must not hardcode any sourced number themselves.
"""
from dataclasses import dataclass, field
from typing import Optional


# ---------------------------------------------------------------------------
# Provenance primitives
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Citation:
    doc: str            # repo-relative path
    section: str         # section/table reference within the doc
    revision_date: str   # as stated in the source document
    note: str = ""


@dataclass(frozen=True)
class Assumption:
    note: str
    memory_md_ref: str  # short pointer to the memory.md entry


@dataclass(frozen=True)
class Fact:
    """A single sourced-or-assumed numeric value, or an explicit N/A."""
    value: Optional[float]
    unit: str
    citation: Optional[Citation] = None
    assumption: Optional[Assumption] = None
    na_reason: Optional[str] = None

    def __post_init__(self):
        if self.value is not None and self.citation is None and self.assumption is None:
            raise ValueError(f"Fact({self.value} {self.unit}) has no citation or assumption")
        if self.value is None and self.na_reason is None:
            raise ValueError("Fact with value=None must carry na_reason")
        if self.citation is not None and self.assumption is not None:
            raise ValueError("Fact cannot carry both a citation and an assumption label")


def NA(unit: str, reason: str) -> Fact:
    return Fact(value=None, unit=unit, na_reason=reason)


# ---------------------------------------------------------------------------
# Shared citations
# ---------------------------------------------------------------------------

KBR_DOC = "Licensor/kbr/kbr-johor-hub.md"
KBR_REV = "Rev 0, 23 Dec 2025"
CASALE_PROPOSAL_DOC = "Licensor/Casale/Casale_Ammonia_Cracker__JohorHub.md"
CASALE_DESIGN_BASIS_DOC = "Licensor/Casale/Casale_Cracker_Design_Basis__JohorHub.md"
CASALE_REV = "Rev.00, 05 Dec 2025"
DUIKER_DOC = "Licensor/duiker/duiker-johor-hub.md"
DUIKER_REV = "05 Dec 2025 (Budgetary Proposal 122380)"
TCOE_DOC = "tcoedatabase/WIP_Ammonia_Cracker_Database.md"
TCOE_REV = "Rev 30-Jun-2026"
VOPAK_DOC = "tolling/vopak/Vopak_Cracker_Tolling_Fee.md"
VOPAK_REV = "LoI effective 20 Aug 2025"
VTTI_DOC = "tolling/vtti/VTTI_Cracker_Tolling_Fee.md"
VTTI_REV = "Commercial Info Package, Process Letter 2, 25 Apr 2025"

FX_SOURCE_NOTE = (
    "ECB euro foreign exchange reference rate, 1 EUR = 1.1448 USD, "
    "as of 3 July 2026. A snapshot published rate, not a repo source "
    "document -- still ASSUMPTION-labeled because applying one day's "
    "rate across a multi-year project cash flow is itself a modeling "
    "choice. Admin-editable in Constants."
)

# ---------------------------------------------------------------------------
# KBR (H2ACT) -- the only licensor with a multi-point capacity dataset
# ---------------------------------------------------------------------------

KBR_CAPACITIES_KTPA = [12, 24, 68, 80]

# ISBL CAPEX is fuel-mode-invariant (confirmed: "Total CAPEX (ISBL+OSBL)"
# is identical 120.9 MM$ across all 3 fuel modes at 12 ktpa, KBR doc Table
# in §4.2). Class V +/-50%, Q3 2025 USD, "similar technology plant in East
# Asia" (KBR doc §4.1) -- NOT "Europe"; flagged in Guide/RegionalFactor.
KBR_ISBL_CAPEX_MUSD = {
    12: Fact(78, "MM USD", Citation(KBR_DOC, "§4.1 / §3.3 KPI table", KBR_REV,
             "ISBL only, Class V +/-50%, Q3 2025, no forward escalation")),
    24: Fact(110, "MM USD", Citation(KBR_DOC, "§4.1 / §3.3 KPI table", KBR_REV)),
    68: Fact(191, "MM USD", Citation(KBR_DOC, "§4.1 / §3.3 KPI table", KBR_REV)),
    80: Fact(209, "MM USD", Citation(KBR_DOC, "§4.1 / §3.3 KPI table", KBR_REV)),
}

KBR_OSBL_PCT_OF_ISBL = Fact(
    0.55, "fraction of ISBL",
    assumption=Assumption(
        "KBR states OSBL ~=55% of ISBL only at the 12 ktpa base case "
        "(Total CAPEX 120.9MM - ISBL 78MM = 42.9MM OSBL = 55.0%); KBR's "
        "own note says this % 'reduced for larger capacity' but gives no "
        "second data point. Applied flat to 24/68/80 ktpa as the only "
        "way to produce a usable Own & Operate total CAPEX at those "
        "capacities.",
        "memory.md: KBR OSBL 55% assumption, dated entry",
    ),
)

KBR_PROJECT_LIFE_YR = Fact(25, "years", Citation(KBR_DOC, "§3.3 KPI table footnote 5", KBR_REV))
KBR_LCOH_DISCOUNT_RATE_PCT = Fact(
    8, "%", Citation(KBR_DOC, "§4.2 Cost input assumptions table", KBR_REV,
    "KBR's own assumption for its LCOH calc -- NOT Gentari's hurdle rate; "
    "kept as a separate named range from DiscountRate_pct."))
KBR_ONSTREAM_DAYS_YR = Fact(350, "days/yr", Citation(KBR_DOC, "§3.3 KPI table footnote 5", KBR_REV))
KBR_TURNDOWN_PCT = Fact(40, "%", Citation(KBR_DOC, "§3.7", KBR_REV))

KBR_H2_DELIVERY_PRESSURE_CONFLICT = (
    "KBR document states two different H2 delivery pressures: 28 barg "
    "(§3.3 KPI table / p.1 summary) vs. 20 barg minimum (§3.1 Design "
    "Basis, §3.8). Unresolved in the source itself -- shown on Guide, "
    "not silently picked."
)

FUEL_MODES = ["NG100", "NG50", "CF100"]  # 100% Nat Gas / 50-50 / 100% Clean Fuel (NH3)
FUEL_MODE_LABELS = {
    "NG100": "100% Natural Gas",
    "NG50": "50% Natural Gas / 50% Ammonia (cracked gas)",
    "CF100": "100% Clean Fuel (Ammonia / cracked gas)",
}

# KBR fuel-mode coverage: 12 & 80 ktpa have all 3 modes; 24 & 68 ktpa
# have 100% NG only (KBR doc §3.2).
KBR_FUEL_MODES_AVAILABLE = {12: FUEL_MODES, 24: ["NG100"], 68: ["NG100"], 80: FUEL_MODES}


@dataclass(frozen=True)
class KBRCaseRow:
    """One (capacity, fuel_mode) row from KBR's §3.3 KPI table -- values
    quoted verbatim in 8-column order: 12[NG100,NG50,CF100] / 24[NG100] /
    68[NG100] / 80[NG100,NG50,CF100]."""
    capacity_ktpa: int
    fuel_mode: str
    h2_production_tpd: float
    nh3_ratio_t_per_t: float          # ton NH3 / ton H2
    energy_efficiency_pct: float
    h2_yield_pct: float               # mass basis
    ci_kgco2_per_kgh2: float
    electricity_kwh_per_tH2: float
    # OPEX (MM USD/yr) and LCOH ($/kg H2) at 3 ammonia price points
    opex_500: float
    opex_950: float
    opex_1100: float
    lcoh_500: float
    lcoh_950: float
    lcoh_1100: float


_KBR_CITATION = Citation(KBR_DOC, "§3.3 KPI table / §4.2 OPEX table", KBR_REV)

KBR_CASES = [
    KBRCaseRow(12, "NG100", 34.3, 6.40, 89.5, 88.6, 0.81, 324, 47.5, 81.8, 93.2, 4.90, 7.76, 8.71),
    KBRCaseRow(12, "NG50", 34.4, 6.74, 89.0, 83.6, 0.45, 335, 49.2, 85.6, 97.8, 5.04, 8.08, 9.09),
    KBRCaseRow(12, "CF100", 34.3, 7.22, 88.4, 78.0, 0.00, 342, 51.3, 90.3, 103.3, 5.22, 8.47, 9.55),
    KBRCaseRow(24, "NG100", 68.6, 6.35, 89.6, 88.7, 0.80, 305, 89.3, 157.9, 180.8, 4.36, 7.22, 8.17),
    KBRCaseRow(68, "NG100", 194.3, 6.35, 89.8, 88.8, 0.80, 290, 237.7, 432.1, 496.8, 3.85, 6.71, 7.66),
    KBRCaseRow(80, "NG100", 228.6, 6.35, 89.8, 88.8, 0.80, 280, 278.4, 507.1, 583.3, 3.81, 6.67, 7.62),
    KBRCaseRow(80, "NG50", 228.6, 6.72, 89.3, 83.8, 0.45, 284, 274.1, 502.7, 578.9, 3.76, 6.61, 7.57),
    KBRCaseRow(80, "CF100", 228.6, 7.20, 88.7, 78.2, 0.00, 290, 302.8, 562.0, 648.4, 4.11, 7.35, 8.43),
]
KBR_CASES_CITATION = _KBR_CITATION

KBR_AMMONIA_PRICE_POINTS_USD_PER_T = [500, 950, 1100]
KBR_COST_ASSUMPTIONS_OWN_DOC = {
    "ammonia_usd_per_t": Fact(500, "USD/t NH3", Citation(KBR_DOC, "§4.2 footnote 1", KBR_REV,
                               "KBR's own LCOH-calc base case, distinct from Gentari's AmmoniaPrice_USDpert input")),
    "electricity_usd_per_mwh": Fact(140, "USD/MWh", Citation(KBR_DOC, "§4.2 footnote 2", KBR_REV)),
    "ng_usd_per_mwh": Fact(30, "USD/MWh", Citation(KBR_DOC, "§4.2 footnote 2", KBR_REV)),
}

KBR_FOOTPRINT_M = {
    12: Fact("70 x 50", "m x m", Citation(KBR_DOC, "§3.6", KBR_REV)),
    24: Fact("80 x 55", "m x m", Citation(KBR_DOC, "§3.6", KBR_REV)),
    68: Fact("95 x 75", "m x m", Citation(KBR_DOC, "§3.6", KBR_REV)),
    80: Fact("100 x 75", "m x m", Citation(KBR_DOC, "§3.6", KBR_REV)),
}
KBR_H2_PURITY_PCT = Fact(99.97, "mol%", Citation(KBR_DOC, "§3.1", KBR_REV, "99.5 wt%"))
KBR_CATALYST_LIFE_YR = Fact(4, "years (expected; guaranteed 2 yr)", Citation(KBR_DOC, "§3.4", KBR_REV))

KBR_EQUIPMENT_QUALITATIVE = [
    "Adiabatic (pre-cracker) reactor, Ni-based catalyst",
    "Ammonia Cracking Furnace (down-fired primary-reformer design), proprietary, KBR-supplied",
    "Feed/Effluent Exchanger, proprietary, KBR-supplied",
    "Ammonia Recovery Unit (H2O/NH3 absorption-distillation)",
    "Hydrogen PSA unit (vendor package)",
    "Selective Catalytic Reduction (SCR) system, standard (optional 2-in-series)",
]
KBR_EQUIPMENT_CITATION = Citation(KBR_DOC, "§3.2, §3.9", KBR_REV,
    "Qualitative only -- no itemized sizes/counts/costs in source package (Annexure I referenced but not delivered)")


# ---------------------------------------------------------------------------
# Casale (MACH2) -- technical-only, capacity-invariant, no CAPEX/OPEX
# ---------------------------------------------------------------------------

CASALE_SCHEMES = ["SELF_SUSTAINING", "LOW_CARBON", "MAX_FUEL"]
CASALE_SCHEME_LABELS = {
    "SELF_SUSTAINING": "Self-sustaining (CO2-free)",
    "LOW_CARBON": "Low-carbon (limited external fuel)",
    "MAX_FUEL": "Maximum fuel source",
}

# ASSUMPTION mapping onto the shared NG100/NG50/CF100 dropdown -- Casale's
# own package never states this correspondence. Locked via user sign-off;
# see memory.md and plan §2.6.
CASALE_SCHEME_TO_FUEL_MODE = {
    "SELF_SUSTAINING": "CF100",
    "LOW_CARBON": "NG50",
    "MAX_FUEL": "NG100",
}
CASALE_MAPPING_ASSUMPTION = Assumption(
    "Self-sustaining (CI=0) mapped to 100% Clean Fuel/Ammonia; Low-carbon "
    "(CI<=0.3, 'admits...limited external fuel source' per Casale's own "
    "text) mapped to 50% NG/50% Ammonia; Maximum Fuel Source (CI>1.2, "
    "footnote 5 '100% CH4 assumed as external fuel source') mapped to "
    "100% Natural Gas. This 3-way correspondence is Gentari's "
    "interpretation for comparability with KBR/Duiker's dropdown, not a "
    "mapping Casale's package itself states.",
    "memory.md: Casale fuel-scheme mapping assumption, dated entry",
)

_CASALE_KPI_CITATION = Citation(CASALE_PROPOSAL_DOC, "§3 Table 1 (MACH2 KPI)", CASALE_REV)


@dataclass(frozen=True)
class CasaleSchemeRow:
    scheme: str
    nh3_ratio_t_per_t_upto: float
    h2_molar_efficiency_pct_upto: float
    energy_efficiency_pct_upto: float
    ci_kgco2_per_kgh2: str   # kept as string: "0", "up to 0.3", "> 1.2"


CASALE_ROWS = [
    CasaleSchemeRow("SELF_SUSTAINING", 7.2, 78, 89, "0"),
    CasaleSchemeRow("LOW_CARBON", 6.4, 87, 90, "up to 0.3"),
    CasaleSchemeRow("MAX_FUEL", 6.4, 96, 90, "> 1.2"),  # "< 6.4" per source, shown as upper bound
]
CASALE_ROWS_CITATION = _CASALE_KPI_CITATION

CASALE_H2_PURITY_PCT = Fact(99.999, "mol%", Citation(CASALE_PROPOSAL_DOC, "§3 Table 1", CASALE_REV, "grade 5"))
CASALE_TURNDOWN_PCT = Fact(40, "%", Citation(CASALE_PROPOSAL_DOC, "§3 Table 1", CASALE_REV))
CASALE_PROJECT_LIFE_YR = Fact(20, "years", Citation(CASALE_DESIGN_BASIS_DOC, "§6.1 item 1 (catalytic tube design life reference)", CASALE_REV,
    "Casale Technical Proposal design basis; distinct from KBR's 25-yr life -- default per-licensor, not hardcoded"))

CASALE_CAPEX = NA("MM USD", "Casale package is technical-only (Rev 05-Dec-2025) -- no CAPEX/OPEX data at any capacity")
CASALE_OPEX = NA("MM USD/yr", "Casale package is technical-only -- no OPEX data at any capacity")
CASALE_FOOTPRINT = NA("m x m", "Not stated in Casale's Dec-2025 package ('Licensor will define the required plot area'); "
                                "TCOE database carries an unverified placeholder '80x80' -- not used here")
CASALE_ELECTRICAL_CONSUMPTION = NA("kWh/kg H2", "Not stated in Casale's Dec-2025 package -- flagged unverified in memory.md")
CASALE_SPECIFIC_ENERGY_CONSUMPTION = NA("kWh/kg H2", "Not stated in Casale's Dec-2025 package -- flagged unverified in memory.md")

CASALE_EQUIPMENT_QUALITATIVE = [
    "MACH2 Adiabatic Ammonia Cracker (Axial-Radial design)",
    "MACH2 Ammonia Cracking Furnace (SMR/top-fired, multi-parallel catalyst tubes)",
    "Ammonia Recovery Unit (H2O/NH3 absorption & distillation)",
    "Hydrogen PSA unit",
    "H2 cooler (E-1006)",
]
CASALE_EQUIPMENT_CITATION = Citation(CASALE_PROPOSAL_DOC, "§2, §2.1", CASALE_REV,
    "Qualitative only -- single equipment tag (E-1006) is the only itemized reference in the package")


# ---------------------------------------------------------------------------
# Duiker (AHC) -- single capacity point (12 ktpa), NH3-fired base case
# ---------------------------------------------------------------------------

DUIKER_CAPACITY_KTPA = 12
DUIKER_CAPEX_TOTAL_EUR_M = Fact(47, "MM EUR", Citation(DUIKER_DOC, "§4.1 / Table 7-8", DUIKER_REV,
    "+/-40%. Equipment cost EUR20M + Buildings & Civil EUR27M = EUR47M lump-sum, "
    "inclusive of engineering/installation/EPC/construction license fee -- "
    "no separate ISBL/OSBL split exists for Duiker; shown as one Total "
    "Installed Cost line, not force-split. NOTE: TCOE database's '$51M' "
    "figure (Duiker row) is an unstated/undocumented EUR->USD conversion "
    "of this EUR47M -- not used here; convert via EURUSD_FXRate instead."))
DUIKER_OPEX_EUR_M_PER_YR = Fact(2.9, "MM EUR/yr", Citation(DUIKER_DOC, "§4.3 Table 9", DUIKER_REV,
    "+/-40%. Utility+catalyst+labor+maintenance. Cost basis: ammonia EUR600/t, electricity EUR100/MWh (§4.3)."))
DUIKER_LICENSE_FEE_CONSTRUCTION_EUR = Fact(2_700_000, "EUR lump sum", Citation(DUIKER_DOC, "§4.2", DUIKER_REV,
    "Plant Construction License Fee, for 12 ktpa base capacity; additive to CAPEX, not folded into the EUR47M total"))
DUIKER_LICENSE_FEE_OPERATION_EUR_PER_T_H2 = Fact(8.50, "EUR/t H2", Citation(DUIKER_DOC, "§4.2", DUIKER_REV,
    "Plant Operation License Fee per metric ton H2 exported; additive to OPEX"))

# Two firing cases -- Duiker's own package, not a KBR-style shared dropdown.
DUIKER_NH3_FIRED_RATIO = Fact(7.05, "t NH3/t H2", Citation(DUIKER_DOC, "§3.x (Table 4 area)", DUIKER_REV, "@ 90.9% enthalpy efficiency"))
DUIKER_NG_FIRED_RATIO = Fact(6.83, "t NH3/t H2", Citation(DUIKER_DOC, "§3.x (Table 4 area)", DUIKER_REV, "@ 90.6% enthalpy efficiency"))
DUIKER_MEMORY_MD_RATIO_DISCREPANCY = (
    "memory.md's baseline comparison table carries Duiker NH3:H2 = 7.03 "
    "t/t (sourced from tcoedatabase, NH3-fired). The primary Duiker "
    "package states 7.05 t/t (NH3-fired, 90.9% eff.) and 6.83 t/t "
    "(NG-fired, 90.6% eff.). This model uses the primary-source 7.05/6.83 "
    "figures and flags the discrepancy with the TCOE-table 7.03 rather "
    "than silently reconciling it, per CLAUDE.md §6."
)
DUIKER_CI_NH3_FIRED = Fact(0, "kgCO2/kgH2", Citation(DUIKER_DOC, "§3.11.2", DUIKER_REV,
    "Zero direct Scope-1 CO2; only NOx (<100 ppm) and negligible NH3 slip"))
DUIKER_CI_NG_FIRED = Fact(0.21, "kgCO2/kgH2", Citation(DUIKER_DOC, "§3.11.2", DUIKER_REV))
DUIKER_H2_PURITY_PCT = Fact(99.97, "mol%", Citation(DUIKER_DOC, "§3.x", DUIKER_REV, "99.5 wt%"))
DUIKER_ENERGY_EFFICIENCY_PCT = Fact(90, "% (LHV basis)", Citation(DUIKER_DOC, "§3.x / summary", DUIKER_REV, ">90%, end-of-run catalyst basis"))
DUIKER_FOOTPRINT_M2 = Fact(900, "m2 (approx. 30 x 30 m)", Citation(DUIKER_DOC, "§3.10", DUIKER_REV,
    "Scaled down from the full-scale 276 tpd / 3660 m2 reference train"))
DUIKER_OUTPUT_PRESSURE_BARG = Fact(20, "barg", Citation(DUIKER_DOC, "§3.x", DUIKER_REV,
    "Battery-limit spec; PSA delivers at 50 barg, let down to 20 barg per project requirement"))
DUIKER_PROJECT_LIFE_YR = NA("years", "Not stated in Duiker's Budgetary Proposal 122380 -- defaults to KBR's 25-yr basis "
                                       "only if the user does not override; flagged as unsourced-for-Duiker on Dashboard")

DUIKER_EQUIPMENT_QUALITATIVE = [
    "Stoichiometry Controlled Oxidation (SCO) combustor",
    "Ammonia cracking reactor (convective, non-radiant)",
    "Hydrogen PSA unit",
]
DUIKER_EQUIPMENT_CITATION = Citation(TCOE_DOC, "§4 licensor technology descriptions", TCOE_REV,
    "Qualitative only -- no itemized sizes/counts/costs in the Duiker package")


# ---------------------------------------------------------------------------
# Topsoe & Technip -- single TCOE-table data point each, no dedicated
# package in this repo (memory.md open question: no standalone Topsoe file)
# ---------------------------------------------------------------------------

_TCOE_TABLE_CITATION = Citation(TCOE_DOC, "§6.1 Table A (Licensors, Clean Fuel Mode)", TCOE_REV,
    "Synthesis table, not a standalone licensor package")

TOPSOE_CAPACITY_KTPA = 50
TOPSOE_ISBL_CAPEX_MUSD = Fact(100, "MM USD", _TCOE_TABLE_CITATION, )
TOPSOE_NH3_RATIO = Fact(7.20, "t/t", _TCOE_TABLE_CITATION)
TOPSOE_H2_PURITY_PCT = Fact(99.9, "%", _TCOE_TABLE_CITATION)
TOPSOE_ENERGY_EFFICIENCY_PCT = Fact(96, "%", Citation(
    TCOE_DOC, "§6.1 Table A footnote 2", TCOE_REV,
    "'may not align with those of other licensors; detailed assessment pending'"))
TOPSOE_FOOTPRINT = Fact("80 x 80", "m x m", _TCOE_TABLE_CITATION)
TOPSOE_CI = Fact(0.136, "kgCO2e/kgH2", _TCOE_TABLE_CITATION)
TOPSOE_OPEX = NA("MM USD/yr", "No OPEX figure exists in any source in this repo for Topsoe")
TOPSOE_NO_PACKAGE_NOTE = ("No standalone Topsoe (H2Retake) technical package exists in this repo "
                           "(memory.md open item) -- all Topsoe figures trace to the TCOE synthesis table only.")

TECHNIP_CAPACITY_KTPA = 50
TECHNIP_ISBL_CAPEX_MUSD = NA("MM USD", "TCOE table states 'Not available at current maturity' for Technip")
TECHNIP_NH3_RATIO = Fact(7.09, "t/t", _TCOE_TABLE_CITATION)
TECHNIP_H2_PURITY_PCT = Fact(99.95, "%", _TCOE_TABLE_CITATION)
TECHNIP_ENERGY_EFFICIENCY_PCT = Fact(88, "%", _TCOE_TABLE_CITATION)
TECHNIP_FOOTPRINT = Fact("80 x 80", "m x m", _TCOE_TABLE_CITATION)
TECHNIP_CI = Fact(0.136, "kgCO2e/kgH2", _TCOE_TABLE_CITATION)
TECHNIP_OPEX = NA("MM USD/yr", "No OPEX figure exists in any source in this repo for Technip")


# ---------------------------------------------------------------------------
# Tolling parties (Commercial Mode = Tolling)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class TollingPartyRecord:
    name: str
    tariff_low: float
    tariff_high: float
    currency: str
    capacity_min_ktpa: Optional[float]
    capacity_max_ktpa: Optional[float]
    accuracy_class: str
    citation: Citation


TOLLING_VOPAK_LINDE = TollingPartyRecord(
    name="Vopak & Linde (Antwerp)",
    tariff_low=0.50, tariff_high=1.00, currency="EUR",
    capacity_min_ktpa=35, capacity_max_ktpa=120,
    accuracy_class="AACE Class 5",
    citation=Citation(VOPAK_DOC, "Ammonia Cracker tariff", VOPAK_REV,
        "Cracker tariff only (excl. terminalling); min 35 ktpa or 100 tpd booked; 15-20 yr ToP contract term"),
)
TOLLING_VOPAK_PASSTHROUGH = {
    "ammonia_feed_t_per_t_h2": (6, 7),
    "ammonia_fuel_t_per_t_h2": (0.4, 0.6),
    "ng_fuel_mwh_per_t_h2": (2, 3),
    "power_mw": (0.5, 1),
}
TOLLING_VOPAK_TERMINAL_EUR_PER_T_NH3 = Fact("30-60", "EUR/t NH3", Citation(VOPAK_DOC, "Ammonia Terminal tariff", VOPAK_REV,
    "Class 3 estimate, min 250,000 tpa throughput, separate from the cracker tariff above"))

TOLLING_VTTI = TollingPartyRecord(
    name="VTTI (Rotterdam/Antwerp, Amplifhy)",
    tariff_low=1.15, tariff_high=1.67, currency="EUR",
    capacity_min_ktpa=70, capacity_max_ktpa=140,
    accuracy_class="Not stated in VTTI's own package (TCOE table labels it 'Class IV' vs its own footnote 'Class V' -- internally inconsistent, flagged not resolved)",
    citation=Citation(VTTI_DOC, "Take-or-pay tariff (excl. passthrough)", VTTI_REV,
        "ToP-only range EUR1.15-1.67/kg H2; incl. variable passthrough EUR1.58-2.21/kg H2; 140 ktpa base case, 70 ktpa alternative"),
)
TOLLING_VTTI_PASSTHROUGH_NOTE = (
    "6.3-6.5 t NH3/t H2 (NG-maximized) / 7.1-7.3 t NH3/t H2 (clean-maximized), "
    "per VTTI package -- direct CI 7.7 gCO2e/MJ (NG-max) vs 1.13 gCO2e/MJ (clean-max)."
)

TOLLING_HOEGH_EVI = TollingPartyRecord(
    name="Hoegh EVI (Floating Solution)",
    tariff_low=1.50, tariff_high=1.50, currency="USD",
    capacity_min_ktpa=None, capacity_max_ktpa=40,  # 110 mtpd ~= 40 ktpa
    accuracy_class="Class IV",
    citation=Citation(TCOE_DOC, "§6.2 Table B", TCOE_REV, "110 mtpd H2, tolling fee w/o cost pass-through, with storage"),
)

TOLLING_NIPPON_SANSO_EXCLUDED_NOTE = (
    "Nippon Sanso/LBC (Technip-licensed, Netherlands) has a fixed Monthly "
    "Cracking Service Fee structure (EUR4,167,000/month for 100 ktpa "
    "capacity reservation) plus separate EUR40/t NH3 (+/-40%) terminalling "
    "-- structurally different from the $/kg-H2 tariff model shared by "
    "Vopak/VTTI/Hoegh EVI. Excluded from the v1 TollingParty dropdown; "
    "logged as a v2 candidate in memory.md, not silently dropped."
)


# ---------------------------------------------------------------------------
# Regional CAPEX factor -- mechanism only, no fabricated numeric factors
# ---------------------------------------------------------------------------

REGIONAL_FACTOR_NO_SOURCE_NOTE = (
    "No freely citable regional CAPEX location-factor table exists "
    "(confirmed via web search -- Compass International / Intratec Plant "
    "Location Factor / Aspen Richardson publish real ones but they are "
    "paywalled). All regions default to 1.00 (no adjustment)."
)

REGIONAL_FACTORS = {
    "Malaysia (Johor)": Fact(1.00, "dimensionless",
        assumption=Assumption("No adjustment -- matches KBR's own stated cost basis region (East Asia)",
                               "memory.md: regional factor placeholders, dated entry")),
    "Netherlands": Fact(1.00, "dimensionless",
        assumption=Assumption("ASSUMPTION -- pending licensed source (e.g. Compass International / "
                               "Intratec Plant Location Factor); admin to update",
                               "memory.md: regional factor placeholders, dated entry")),
    "Belgium": Fact(1.00, "dimensionless",
        assumption=Assumption("ASSUMPTION -- pending licensed source; admin to update",
                               "memory.md: regional factor placeholders, dated entry")),
    "Other (specify)": Fact(1.00, "dimensionless",
        assumption=Assumption("ASSUMPTION -- pending licensed source; admin to update",
                               "memory.md: regional factor placeholders, dated entry")),
}
KBR_COST_BASIS_REGION_NOTE = (
    "KBR's ISBL CAPEX basis is stated in its own package (§4.1) as "
    "'reference from recent TIC Class IV estimate that KBR performed for "
    "similar technology plant in East Asia' -- not 'Europe'. Shown "
    "verbatim next to the regional-factor lookup so the region-vs-basis "
    "comparison is visible on-screen, not asserted either way."
)

# ---------------------------------------------------------------------------
# Currency
# ---------------------------------------------------------------------------

EURUSD_FX_RATE = Fact(
    1.1448, "USD per EUR",
    assumption=Assumption(FX_SOURCE_NOTE, "memory.md: EUR/USD FX assumption, dated entry"),
)

# ---------------------------------------------------------------------------
# Shared engineering constants
# ---------------------------------------------------------------------------

LHV_H2_MJ_PER_KG = Fact(120, "MJ/kg", assumption=Assumption(
    "Standard LHV of hydrogen, ~120 MJ/kg -- used for kgCO2/kgH2 <-> "
    "gCO2e/MJ conversion per CLAUDE.md §4.2 (1 kgCO2/kgH2 ~= 8.33 gCO2/MJ)",
    "Documented in mdlguideline.md §9, not a repo-specific figure"))

RFNBO_CI_CEILING_GCO2E_PER_MJ = Fact(28.2, "gCO2e/MJ", Citation(
    "CLAUDE.md", "§4.1", "n/a", "Derived figure carrying the TCOE database's own citation basis -- "
    "re-confirm before use in a new deliverable per CLAUDE.md §4.1"))
KEEI_CI_THRESHOLD_KGCO2_PER_KGH2 = Fact(4.0, "kgCO2/kgH2", Citation(
    "CLAUDE.md", "§4.2", "n/a", "Korea KEEI proposed threshold"))
