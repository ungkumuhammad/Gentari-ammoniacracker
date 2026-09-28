# CAPEX Reference — Ammonia Cracker Licensors

> Single reference table for every CAPEX figure held in this repo's database
> (`tcoedatabase/` + the licensor packages under `Licensor/`). Compiled
> 2026-09-28. Every number is either quoted from the cited source, or marked
> **[DERIVED]** with its calculation shown. Nothing here is a firm price — all
> figures are indicative, non-binding licensor estimates; always carry the
> accuracy class forward when quoting.

---

## 1. Quoted CAPEX — as stated in source documents

| # | Licensor / technology | H₂ capacity | Fuel-mode basis | CAPEX (as quoted) | Cost scope | Accuracy class | Cost basis / date | Source |
|---|---|---|---|---|---|---|---|---|
| 1 | KBR H₂ACT® | 12 ktpa | CAPEX fuel-mode-invariant¹ | **US$ 78M** | ISBL TIC | Class V, ±50% | Q3 2025, no forward escalation; factored from a KBR Class IV TIC for a similar plant in East Asia | `Licensor/kbr/kbr-johor-hub.md` §4.1 & §3.3 KPI table (Rev 0, 23 Dec 2025) |
| 2 | KBR H₂ACT® | 12 ktpa | Same across 100% NG / 50% NG / 100% clean fuel | **US$ 120.9M** | ISBL + OSBL (OSBL ≈ 55% of ISBL) | Class V, ±50% | as #1 | `kbr-johor-hub.md` §4.2 (OPEX table) |
| 3 | KBR H₂ACT® | 24 ktpa | CAPEX fuel-mode-invariant¹ | **US$ 110M** | ISBL TIC | Class V, ±50% | as #1 | `kbr-johor-hub.md` §4.1 |
| 4 | KBR H₂ACT® | 68 ktpa | CAPEX fuel-mode-invariant¹ | **US$ 191M** | ISBL TIC | Class V, ±50% | as #1 | `kbr-johor-hub.md` §4.1; also TCOE database §6.1 (KBR column) |
| 5 | KBR H₂ACT® | 80 ktpa | CAPEX fuel-mode-invariant¹ | **US$ 209M** | ISBL TIC | Class V, ±50% | as #1 | `kbr-johor-hub.md` §4.1 |
| 6 | Duiker AHC | 12 ktpa (36 tpd), single customised train | NH₃-fired (clean fuel) | **€ 47M** = € 20M equipment + € 27M engineering, installation & EPC | ISBL, lump-sum turnkey (LSTK) | ±40% | Dec 2025 | `Licensor/duiker/duiker-johor-hub.md` §4.1 Table 8 (Budgetary Proposal 122380, 05 Dec 2025) |
| 7 | Duiker AHC (TCOE restatement) | 12 ktpa | NH₃-fired | **US$ 51M (lumpsum)** | as #6 | "Class V" | Unstated EUR→USD conversion² | `tcoedatabase/WIP_Ammonia_Cracker_Database.md` §6.1 |
| 8 | Haldor Topsoe H2Retake™ | 50 ktpa | Not separable³ | **US$ 100M** | ISBL | Class V (± band not stated) | Not stated | TCOE database §6.1 only — **no Topsoe package in repo** |
| 9 | Technip Energies Hynext by T.EN™ | 50 ktpa | — | **Not available** | — | — | — | TCOE database §6.1: "Not available at current maturity" |
| 10 | Casale MACH²™ | 12/24/68/80 ktpa (process cases only) | — | **Not available** | — | — | — | TCOE database §6.1; Casale Dec-2025 package is technical-only (no cost data) |

¹ KBR's Total CAPEX (ISBL+OSBL) is identical (US$ 120.9M) across all three
fuel modes at 12 ktpa (`kbr-johor-hub.md` §4.2), so the ISBL figures are
treated as fuel-mode-invariant. The TCOE database labels the 68 ktpa KBR
column "100% NG fuel mode" for its KPIs, not because the CAPEX differs.

² The source figure is € 47M. TCOE's US$ 51M implies ≈1.085 USD/EUR
(51 ÷ 47), but the rate and date are not documented. At the ECB reference
rate already logged in `memory.md` (1.1448 USD/EUR, 3 Jul 2026) the same
€ 47M is ≈ US$ 53.8M **[DERIVED]**. Quote the EUR figure where possible.

³ The TCOE §6.1 table title says "Clean Fuel Mode" but footnote ¹ says
"natural gas fuel mode" — the table's own review remarks flag this as
unreconciled, so Topsoe's fuel-mode basis cannot be pinned down.

---

## 2. Specific CAPEX (per tonne-per-year of H₂ capacity) — [DERIVED]

Calculation: quoted CAPEX ÷ (capacity in t/yr). Same accuracy class as the
input figure; the scopes are **not** like-for-like (see §3).

| Licensor | Capacity | Quoted CAPEX | **Specific CAPEX** | Scope |
|---|---|---|---|---|
| KBR | 12 ktpa | US$ 78M | **US$ 6,500 / (t/yr)** | ISBL |
| KBR | 12 ktpa | US$ 120.9M | **US$ 10,075 / (t/yr)** | ISBL + OSBL |
| KBR | 24 ktpa | US$ 110M | **US$ 4,583 / (t/yr)** | ISBL |
| KBR | 68 ktpa | US$ 191M | **US$ 2,809 / (t/yr)** | ISBL |
| KBR | 80 ktpa | US$ 209M | **US$ 2,613 / (t/yr)** | ISBL |
| Duiker | 12 ktpa | € 47M | **€ 3,917 / (t/yr)** | ISBL, LSTK (incl. commissioning & licence fee) |
| Topsoe | 50 ktpa | US$ 100M | **US$ 2,000 / (t/yr)** | ISBL (TCOE table only) |

KBR's four points show the expected economy of scale: specific ISBL CAPEX
falls ≈60% from 12 → 80 ktpa.

---

## 3. What each CAPEX figure includes / excludes

The KBR and Duiker figures are both labelled "ISBL" but have **different
scopes** — Duiker's lump-sum includes several items KBR explicitly excludes.
Do not rank them on headline value without adjusting for this.

| Cost item | KBR H₂ACT® (ISBL TIC) | Duiker AHC (LSTK) | Topsoe (TCOE) |
|---|---|---|---|
| Equipment inside battery limit | ✅ Included | ✅ Included (€ 20M) | Not stated |
| Engineering, installation, piping, instrumentation, electrical | ✅ Included (TIC) | ✅ Included (in € 27M) | Not stated |
| Buildings & civil, foundations | Buildings = OSBL (excluded) | ✅ Included (in € 27M) | Not stated |
| Commissioning & start-up | ❌ Excluded | ✅ Included | Not stated |
| Plant construction licence fee | ❌ Excluded ("license fees or any royalties") | ✅ Included — capacity-adjusted from € 2.7M/train (§4.2)⁴ | Not stated |
| Contingency | ❌ Excluded | Not stated | Not stated |
| Spares (capital, commissioning, O&M) | ❌ Excluded | Not stated | Not stated |
| Owner's cost, permitting, sales tax, import duties, currency risk | ❌ Excluded | Not stated (taxes/duties excluded from licence fees) | Not stated |
| OSBL (NH₃ storage, flare, utilities, water/waste treatment, buildings, labs) | ❌ Excluded from ISBL; ≈55% of ISBL at 12 ktpa (US$ 42.9M), % "reduced for larger capacity" | ❌ Excluded (flare, NH₃ storage, loading/unloading, control room) | Not stated |

⁴ **Discrepancy flagged (not corrected here):** Duiker §4.2 states the
adjusted Plant Construction License Fee "is added in the CAPEX estimations
in Table 8", i.e. it is **inside** the € 47M. `tools/cracker_model/data.py`
(`DUIKER_LICENSE_FEE_CONSTRUCTION_EUR`) annotates it as "additive to CAPEX,
not folded into the EUR47M total", which contradicts both the source and the
same file's own `DUIKER_CAPEX_TOTAL_EUR_M` note. If the workbook adds the
€ 2.7M on top of € 47M, Duiker CAPEX is double-counted. Logged in `memory.md`.

---

## 4. Related capital-type charges (not in the CAPEX figures above unless noted)

| Licensor | Charge | Amount | Treatment | Source |
|---|---|---|---|---|
| Duiker | Plant Construction License Fee (one-time) | € 2.7M per train, for trains up to 276 tpd H₂ @ 99.97 mol% | Capacity-adjusted amount **included** in € 47M (row 6) | `duiker-johor-hub.md` §4.2 |
| Duiker | Plant Operation License Fee (annual) | € 8.50 / t H₂ exported | OPEX, not CAPEX | `duiker-johor-hub.md` §4.2 |
| KBR | Licence fee / royalties | Not quoted | Explicitly excluded from ISBL TIC | `kbr-johor-hub.md` §4.1 |

---

## 5. Normalised to 100 ktpa H₂ — [DERIVED] estimates

No licensor quotes CAPEX at 100 ktpa. These are the scaled estimates
already recorded in `memory.md` ("Derived Assessment — Licensor CAPEX
Normalized to 100 ktpa H₂", 2026-07-08), re-computed here as a check.

| Licensor | Anchor data | Method | **Est. 100 ktpa ISBL CAPEX** | Confidence |
|---|---|---|---|---|
| KBR | 4 points (12/24/68/80 ktpa) | Log-log regression on all 4 points: CAPEX ≈ 21.25 × (ktpa)^0.521, R² = 0.9997 (same method as the workbook's `Calc_CapacitySizing`) | **≈ US$ 234M** (Class V ±50%, wider for extrapolation) | Medium — 25% beyond KBR's largest quoted case, within KBR's 1,200 MTPD single-train limit |
| KBR (alt.) | 68 & 80 ktpa only | Two-point power law, exponent 0.554 | ≈ US$ 237M | Medium — as above; used in the 2026-07-08 `kbr_100ktpa_sizing.pdf` |
| Duiker | 1 point (12 ktpa, € 47M) | Generic six-tenths rule: 47 × (100/12)^0.6 | **≈ € 168M**⁵ | Low — single anchor, generic exponent; 100 ktpa ≈ Duiker's standard 276 tpd 4-reactor train, which likely prices differently from scaling the customised 12 ktpa train |
| Topsoe | 1 point (50 ktpa, US$ 100M) | Six-tenths rule: 100 × (100/50)^0.6 | **≈ US$ 152M** | Low — single anchor, and the anchor is from the TCOE summary table, not a Topsoe package |
| Technip | None | — | **N/A** | Only 100 ktpa figure is a tolling fee (see §6), not CAPEX |
| Casale | None | — | **N/A** | No cost data at any capacity |

⁵ **Discrepancy flagged:** `memory.md` records ≈ € 166M for this estimate;
re-computing 47 × (100/12)^0.6 gives € 167.7M. The difference is within
rounding of a ±40%-class number but the two should match — logged in
`memory.md`.

---

## 6. Not CAPEX — tolling fees that embed capital recovery (for context only)

Tolling offers bundle the operator's capital, O&M and margin into a
service fee. They **cannot** be converted to a CAPEX without an undisclosed
discount rate and OPEX split, so they are listed only to show where the
capital cost sits in those structures.

| Operator (underlying licensor) | Capacity | Fee | Source |
|---|---|---|---|
| Nippon Sanso / LBC Tank Terminals (Technip Energies) | 100 ktpa full capacity reservation | € 50M/yr Monthly Cracking Service Fee (€ 4.167M/month) + € 40/t NH₃ (±40%) terminalling | `Licensor/technip/technip-nippon-sanso-lbc-tolling.md` |
| Vopak (storage) + Linde (cracker) | Up to 120 ktpa | € 0.50–1.00/kg H₂ cracking; € 30–60/t NH₃ terminalling | `tolling/vopak/Vopak_Cracker_Tolling_Fee.md` (LoI, 20 Aug 2025) |
| VTTI | 140 ktpa | ≈ € 1.15–1.67/kg H₂ (take-or-pay only) | `tolling/vtti/VTTI_Cracker_Tolling_Fee.md` |
| Hoegh EVI (floating) | 110 mtpd | US$ 1.50/kg H₂ (Class IV, ex-pass-through) | TCOE database §6.2 |

---

## 7. Caveats to carry with any figure from this table

- **Currencies are not harmonised** (KBR/Topsoe in USD, Duiker in EUR).
  Convert only with a dated, cited FX rate.
- **Accuracy classes differ**: KBR Class V ±50%; Duiker ±40%; Topsoe Class V
  with no stated band.
- **Location basis differs**: KBR's estimate is referenced to a plant in East
  Asia; Duiker's and Topsoe's locations are not stated. The workbook's
  regional factors are all 1.00 placeholders (see `memory.md`).
- **None of these are total installed project cost.** Add OSBL, contingency,
  owner's cost, spares and (for KBR) licence fees and commissioning before
  using any figure in an investment case.
