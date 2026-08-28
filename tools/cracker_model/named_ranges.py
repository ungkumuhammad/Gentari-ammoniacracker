"""Central registry of workbook named ranges.

Every named range used anywhere in the workbook is declared here as a
constant string, so sheet modules never hand-type a name (avoids typos
causing #NAME? errors) and `test_named_ranges.py` can check for
duplicates/orphans. Extends mdlguideline.md §15.
"""

# --- Inputs (Inputs sheet, user-editable) ---
LICENSOR_SELECTED = "LicensorSelected"
COMMERCIAL_MODE = "CommercialMode"
TOLLING_PARTY = "TollingParty"
CRACKER_FUEL_MODE = "CrackerFuelMode"
PROJECT_REGION = "ProjectRegion"
REQUIRED_H2_CAPACITY_KTPA = "RequiredH2Capacity_ktpa"
CERTIFICATION_FRAMEWORK = "CertificationFramework"

# --- Inputs (Inputs sheet, ASSUMPTION, yellow-filled, user-editable) ---
OFFTAKE_H2_PRICE_USD_PER_KG = "OfftakeH2Price_USDperkg"
PROJECT_LIFE_YR = "ProjectLife_yr"
DISCOUNT_RATE_PCT = "DiscountRate_pct"
AMMONIA_PRICE_USD_PER_T = "AmmoniaPrice_USDpert"
ELECTRICITY_PRICE_USD_PER_MWH = "ElectricityPrice_USDperMWh"
NG_PRICE_USD_PER_MWH = "NGPrice_USDperMWh"
EURUSD_FX_RATE = "EURUSD_FXRate"

# --- Constants: KBR capacity/CAPEX interpolation ---
KBR_CAP1, KBR_CAP2, KBR_CAP3, KBR_CAP4 = "KBR_Cap1", "KBR_Cap2", "KBR_Cap3", "KBR_Cap4"
KBR_CAPEX1, KBR_CAPEX2, KBR_CAPEX3, KBR_CAPEX4 = "KBR_Capex1", "KBR_Capex2", "KBR_Capex3", "KBR_Capex4"
KBR_OSBL_PCT_ASSUMPTION = "KBR_OSBLPct_ASSUMPTION"
KBR_LCOH_DISCOUNT_RATE = "KBR_LCOH_DiscountRate"
KBR_PROJECT_LIFE_YR = "KBR_ProjectLife_yr"
CASALE_PROJECT_LIFE_YR = "Casale_ProjectLife_yr"
CAPACITY_REGRESSION_SLOPE_B = "CapacityRegressionSlope_b"
CAPACITY_REGRESSION_INTERCEPT_A = "CapacityRegressionIntercept_a"
CAPACITY_REGRESSION_RSQUARED = "CapacityRegressionRSquared"

# --- Constants: regional / currency ---
REGIONAL_FACTOR_SELECTED = "RegionalFactorSelected"
LHV_H2_MJ_PER_KG = "LHV_H2_MJperkg"
RFNBO_CEILING_GCO2E_PER_MJ = "RFNBOCeiling_gCO2eperMJ"
KEEI_THRESHOLD_KGCO2_PER_KGH2 = "KEEIThreshold_kgCO2perkgH2"

# --- Constants: tolling ---
TOLLING_TARIFF_LOW = "TollingTariffLow_{party}"
TOLLING_TARIFF_HIGH = "TollingTariffHigh_{party}"
TOLLING_CAPACITY_MIN = "TollingCapacityMin_{party}"

# --- Constants: Duiker / Topsoe / Technip single-point figures ---
DUIKER_CAPEX_TOTAL_EUR_M = "Duiker_CAPEX_Total_EUR_M"
DUIKER_OPEX_EUR_M_PER_YR = "Duiker_OPEX_EUR_M_per_yr"
DUIKER_LICENSE_FEE_CONSTRUCTION_EUR = "Duiker_LicenseFee_Construction_EUR"
DUIKER_LICENSE_FEE_OPERATION_EUR_PER_T_H2 = "Duiker_LicenseFee_Operation_EURperTH2"
DUIKER_NH3_RATIO_NH3FIRED = "Duiker_NH3Ratio_NH3fired"
DUIKER_NH3_RATIO_NGFIRED = "Duiker_NH3Ratio_NGfired"
DUIKER_CI_NH3FIRED = "Duiker_CI_NH3fired"
DUIKER_CI_NGFIRED = "Duiker_CI_NGfired"
TOPSOE_ISBL_CAPEX_MUSD = "Topsoe_ISBL_CAPEX_MUSD"
TOPSOE_NH3_RATIO = "Topsoe_NH3_Ratio"
TOPSOE_CI = "Topsoe_CI_kgCO2ekgH2"
TECHNIP_NH3_RATIO = "Technip_NH3_Ratio"
TECHNIP_CI = "Technip_CI_kgCO2ekgH2"

# --- Cash flow / IRR results ---
CAPEX_TOTAL_OWN = "CAPEX_Total_Own"
ANNUAL_OPEX_OWN = "AnnualOPEX_Own"
ANNUAL_TOLLING_FEE = "AnnualTollingFee_Tolling"
IRR_RESULT = "IRR_Result"
NPV_RESULT = "NPV_Result"

# --- Tables ---
TBL_INPUTS = "tblInputs"
TBL_LICENSORS = "tblLicensors"
TBL_KBR_CAPEX_POINTS = "tblKBRCapexPoints"
TBL_TOLLING_PARTIES = "tblTollingParties"
TBL_REGIONAL_FACTORS = "tblRegionalFactors"
TBL_CASH_FLOW = "tblCashFlow"
TBL_COMPARISON = "tblComparison"
TBL_RESULTS = "tblResults"
TBL_CONSTANTS = "tblConstants"

# --- Sheet name constants (mdlguideline.md §15) ---
SHEET_COVER = "Cover"
SHEET_GUIDE = "Guide"
SHEET_INPUTS = "Inputs"
SHEET_CONSTANTS = "Constants"
SHEET_SETTINGS = "Settings"
SHEET_CALC_CAPACITY_SIZING = "Calc_CapacitySizing"
SHEET_CALC_CAPEX_ISBL_OSBL = "Calc_CAPEX_ISBL_OSBL"
SHEET_CALC_OPEX = "Calc_OPEX"
SHEET_CALC_TOLLING = "Calc_Tolling"
SHEET_CALC_REGIONAL_FACTOR = "Calc_RegionalFactor"
SHEET_CALC_CARBON_INTENSITY = "Calc_CarbonIntensity"
SHEET_CALC_CASHFLOW_IRR = "Calc_CashFlow_IRR"
SHEET_DASHBOARD = "Dashboard"
SHEET_COMPARISON = "Comparison"
SHEET_REPORT = "Report"

SHEET_ORDER = [
    SHEET_COVER, SHEET_GUIDE, SHEET_INPUTS,
    SHEET_CALC_CAPACITY_SIZING, SHEET_CALC_CAPEX_ISBL_OSBL, SHEET_CALC_OPEX,
    SHEET_CALC_TOLLING, SHEET_CALC_REGIONAL_FACTOR, SHEET_CALC_CARBON_INTENSITY,
    SHEET_CALC_CASHFLOW_IRR, SHEET_DASHBOARD, SHEET_COMPARISON, SHEET_REPORT,
    SHEET_CONSTANTS, SHEET_SETTINGS,
]

PROTECTED_SHEETS = {SHEET_CONSTANTS, SHEET_SETTINGS}


def register(workbook, name: str, ref: str) -> None:
    """Define a workbook-level named range, ref like "'Inputs'!$B$5"."""
    from openpyxl.workbook.defined_name import DefinedName
    workbook.defined_names[name] = DefinedName(name, attr_text=ref)
