# memory.md — Gentari Ammonia Cracker Workstream

Persistent memory for this repo. Read at the start of any task; update
whenever a decision, assumption, sourced data point, or open question
changes. See `CLAUDE.md` for the protocol this file follows.

---

## Decisions

- **2026-07-08** — Repo scope confirmed as the **global** ammonia cracker
  technology workstream (licensor selection, tolling benchmarking, RFNBO/CI
  compliance), spanning all of Gentari's cracker projects (Johor, Antwerp,
  Rotterdam, and future sites) — not limited to the Malaysia→Singapore
  corridor covered by `MYSGH2project`. Decided by repo owner.
- **2026-07-08** — This repo inherits `MYSGH2project`'s memory.md protocol and
  No-Fabrication Rule verbatim (same discipline, separate file/state).
- **2026-07-08** — RFNBO/clean-molecule regulatory scope for the AI agent
  persona is **EU RFNBO (RED II/III)** and **Korea KEEI Clean Hydrogen
  Certification**. Other frameworks (Japan, Singapore, UK LCHS) are out of
  scope until explicitly requested.
- **2026-07-08** — Agent's primary day-to-day output is integrated across all
  three lenses: licensor technical screening, RFNBO/CI compliance reasoning,
  and tolling commercial benchmarking — not siloed.

## Data Provenance

- **2026-07-08** — `Licensor/`, `tcoedatabase/`, `tolling/` replicated
  verbatim (byte-identical, verified via `git` tree SHA match and SHA-256
  checksum) from `ungkumuhammad/MYSGH2project` at commit
  `8bb37a8c1a699a9f078cb272baf61027c6a7dfd5` (branch `main`). Source tree
  SHAs: `Licensor` = `6615c5b9b7de8020926326ed015621296faa8855`,
  `tcoedatabase` = `2db8e3679f4c6d8c28c2c763e0a36a6a7c07c8de`,
  `tolling` = `51c661f546248e23034767dceb8228aecf876d67`. If these folders are
  later edited independently in either repo, they will diverge from this
  baseline — that's expected once each repo starts doing its own analysis;
  just don't assume they're still in sync without checking.
- The TCOE database (`tcoedatabase/WIP_Ammonia_Cracker_Database.md`) itself
  states its licensor data was "refreshed from December 2025 technical
  packages" as of its Rev entry dated 30 June 2026 (i.e. the source document's
  own internal revision history — not a claim being made by this repo).

## Baseline Licensor Comparison (from tcoedatabase, clean-fuel mode unless noted)

| Licensor | H₂ capacity used | NH₃:H₂ (t/t) | H₂ purity | Energy eff. | Direct CI (kgCO₂/kgH₂) | ISBL CAPEX (Class V) |
|---|---|---|---|---|---|---|
| Haldor Topsoe | 50 ktpa | 7.20 | 99.9% | 96%* | 0.136 | $100M |
| Technip Energies | 50 ktpa | 7.09 | 99.95% | 88% | 0.136 | not available |
| KBR (H2ACT®) | 68 ktpa, 100% NG mode | 6.35 | 99.97% | 89.8% | 0.80 | $191M |
| Casale (MACH²™) | self-sustaining scheme | 7.20 | 99.999% | 89% | **0** (self-sustaining); up to 0.3 low-carbon; >1.2 max-fuel | not available (technical-only proposal) |
| Duiker (AHC) | 12 ktpa, NH₃-fired | 7.03 | 99.97% | 90.9% | 0 (NH₃-fired); 0.21 (NG-fired) | €47M lump-sum (±40%) |

\* Topsoe's 96% figure is flagged in the source as not necessarily
methodologically comparable to other licensors' efficiency definitions —
carry that caveat forward whenever quoting it.

**Open correction already applied in source**: Casale's CI was previously
mis-copied as 0.136 (Topsoe/Technip's value) in an earlier table revision;
the TCOE database's Dec-2025 refresh corrected it to 0 for the self-sustaining
scheme, per Casale Technical Proposal A23070S Table 1. Casale's "Specific
Energy Consumption," "Electrical power consumption," and "Footprint" figures
in the same table are flagged **unverified** — not stated in the Dec-2025
Casale package. Do not treat those three cells as sourced until confirmed.

## Baseline Tolling Comparison (from tcoedatabase + tolling/ source docs)

| Party | Site | H₂ capacity | Tariff (indicative) | Term | Basis |
|---|---|---|---|---|---|
| Vopak (storage) + Linde (cracker) | Antwerp | up to 120 ktpa (min 35 ktpa/100 tpd booked) | €0.50–1.00/kg H₂ cracking; €30–60/t NH₃ terminalling | 15–20 yr, ToP | LoI, 20 Aug 2025 |
| VTTI | Rotterdam/Antwerp (Amplifhy) | 140 ktpa (also considering 70 ktpa) | ~€1.15–1.67/kg H₂ (take-or-pay only); ~€1.58–2.21/kg H₂ (incl. variable pass-through) | — | Commercial Info Package, Process Letter 2 |
| Hoegh EVI (floating) | — | 110 mtpd (≈40 ktpa) | $1.50/kg H₂ (Class IV, ex-passthrough) | — | tcoedatabase §6.2 |

VTTI indicative direct CI: **7.7 gCO₂e/MJ** (924 gCO₂/kgH₂) NG-maximised vs.
**1.13 gCO₂e/MJ** (135.6 gCO₂/kgH₂) green-ammonia-maximised — both from
CertifHy/Hinicio modelling per VTTI's package. Useful reference pair for
RFNBO CI-ceiling comparisons (28.2 gCO₂e/MJ) — the green-ammonia-maximised
case would clear it; the NG-maximised case would not, on this figure alone
(subject to full additionality/correlation verification, per CLAUDE.md §4.3).

## Open Questions

- **RESOLVED 2026-07-08** — ~~`Licensor/technip-offer-lbc-tolling.md` is
  mislabeled~~. Repo owner clarified: the underlying cracker technology in
  that document **is** Technip Energies (Hynext by T.EN™) — the document is
  filed under Nippon Sanso / LBC Tank Terminals because **Nippon Sanso is the
  operator/tolling counterparty for that Netherlands site, not the
  technology licensor**. This is a recurring pattern in this market: KBR's
  technology is also operated by Nippon Sanso as tolling party in some other
  regions; which licensor Nippon Sanso pairs with is region-specific, and for
  the Netherlands it is confirmed to be Technip. File moved to
  `Licensor/technip/technip-nippon-sanso-lbc-tolling.md` for structural
  consistency with the Casale/duiker/kbr subfolder pattern. See `CLAUDE.md`
  §2.1 (Licensor ≠ Operator) for the general pattern this establishes —
  apply the same "check the underlying licensor, don't assume the operator
  named on a tolling doc is the technology provider" logic to any new
  tolling document added to this repo (Vopak/Linde, VTTI, Hoegh EVI, etc.).
- **No standalone Topsoe (H2Retake™) technical package exists in this repo
  yet**, even though it appears in the TCOE database's licensor comparison
  table and reference-project lists. If/when obtained, add under
  `Licensor/topsoe/`.
- CI figures across sources use inconsistent bases (kgCO₂/kgH₂,
  kgCO₂e/kgH₂, gCO₂e/MJ) and inconsistent fuel-mode assumptions — no
  unified conversion table exists yet in this repo. Consider building one
  before doing cross-licensor RFNBO/KEEI screening at scale.
- **OPEN 2026-07-09** — `mdlguideline.md` (Engineering Excel Development
  Specification) calls for a companion `copilot.md` / AI-development
  guideline that tells an AI assistant exactly how to generate each
  worksheet against the spec (naming, formatting, formula-writing
  practices). Not yet created — needed before the first Excel workbook
  (ammonia cracker sizing/CI screening tool) is built.

## Assumptions & Data Gaps — Ammonia Cracker Sizing/Economics Workbook v1

Logged 2026-07-09, per `tools/cracker_model/data.py` and the approved plan
at `/root/.claude/plans/i-want-to-start-mutable-dongarra.md`. Each is
admin-editable on the workbook's `Constants` sheet.

- **EUR/USD FX rate**: no EUR→USD rate exists in any source document in
  this repo. Defaulted to the **ECB euro foreign exchange reference rate,
  1 EUR = 1.1448 USD, as of 3 July 2026**
  ([ECB reference rates](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html)).
  A real, dated, citable snapshot rate — still ASSUMPTION-labeled because
  applying one day's rate across a multi-year project cash flow is itself
  a modeling choice, not because the rate itself is unsourced.
- **KBR OSBL % beyond 12 ktpa**: KBR's package quantifies OSBL only at 12
  ktpa (≈55% of ISBL: $120.9M total − $78M ISBL = $42.9M ≈ 55.0%); KBR's
  own note says this ratio declines at larger scale but gives no second
  data point. Applied flat (55%) to 24/68/80 ktpa as the only way to
  produce a usable Own & Operate CAPEX total at those capacities — decided
  by repo owner via `AskUserQuestion` during planning.
- **Regional CAPEX factors**: no freely citable regional location-factor
  table exists (Compass International / Intratec Plant Location Factor /
  Aspen Richardson all publish real ones but are paywalled — confirmed via
  web search). All regions (Malaysia, Netherlands, Belgium, Other) default
  to factor = 1.00, explicitly flagged "pending licensed source; admin to
  update" on the `Constants` sheet. Do not treat 1.00 as a researched
  finding that these regions have equivalent costs.
- **Casale fuel-scheme → shared fuel-mode mapping**: Casale's package
  gives only a generic 3-scheme table (Self-sustaining / Low-carbon /
  Max-fuel), never mapped to the NG100/50-50/Clean-Fuel dropdown shared
  with KBR/Duiker. Mapped (decided by repo owner): Self-sustaining → 100%
  Clean Fuel/Ammonia (CI=0, ammonia-only-fired); Low-carbon → 50% NG/50%
  Ammonia ("admits...limited external fuel source" per Casale's own
  text); Maximum Fuel Source → 100% Natural Gas (heaviest external-fuel
  use, highest CI, consistent with footnote 5's "100% CH4 assumed as
  external fuel source"). This correspondence is Gentari's interpretation
  for comparability, not something Casale's package itself states —
  printed next to the mapped values on `Calc_CarbonIntensity`/`Constants`.
- **KBR H2 delivery pressure conflict, unresolved**: KBR's own package
  states two different figures — 28 barg (§3.3 KPI table) vs. 20 barg
  minimum (§3.1 Design Basis, §3.8). Shown on the workbook's `Guide` sheet
  as an open conflict, not silently picked either way.
- **Nippon Sanso/LBC (Technip-licensed) tolling excluded from v1**: has a
  fixed Monthly Cracking Service Fee structure (€4,167,000/month for 100
  ktpa reservation) plus separate €40/t NH₃ terminalling — structurally
  different from the shared $/kg-H₂ tariff model used by Vopak & Linde /
  VTTI / Hoegh EVI. Excluded from the `TollingParty` dropdown; logged here
  as a v2 candidate, not silently dropped.
- **Duiker NH₃:H₂ ratio discrepancy**: this file's existing "Baseline
  Licensor Comparison" table (above) carries Duiker NH₃:H₂ = 7.03 t/t
  (sourced via `tcoedatabase`). Duiker's own primary package
  (`Licensor/duiker/duiker-johor-hub.md`) states **7.05 t/t for the
  NH₃-fired case (@ 90.9% enthalpy efficiency) and 6.83 t/t for the
  NG-fired case (@ 90.6% enthalpy efficiency)** — two discrete figures,
  not one blended value. The workbook uses the primary-source 7.05/6.83
  figures; this 7.03-vs-7.05/6.83 discrepancy is flagged here per
  `CLAUDE.md` §6, not silently reconciled.
- **v1 scope limitation — OPEX/CI are not regression-extrapolated**:
  unlike CAPEX (which uses a global log-log regression outside KBR's
  12–80 ktpa range, per repo owner's explicit request), OPEX and CI stay
  N/A outside that range in v1, because both depend on capacity, fuel
  mode, and (for OPEX) ammonia price simultaneously — a robust
  multi-dimensional regression was judged disproportionate for v1. Noted
  as a v2 candidate.
- **Casale project life (20 yr) vs. KBR (25 yr)**: `ProjectLife_yr`
  defaults per-licensor (KBR 25 yr per its own §3.3 footnote 5; Casale 20
  yr per its Technical Proposal §6.1) rather than a single hardcoded
  value; the workbook flags a mismatch if the user overrides
  `ProjectLife_yr` away from the selected licensor's own stated basis.
- **`mdlguideline.md` §7 deviation**: the openpyxl-based build pipeline
  uses classic `INDEX`/`MATCH`/`IFERROR`/named-range formulas instead of
  the guideline's preferred `LET()`/`LAMBDA()`, because openpyxl cannot
  verify dynamic-array formulas render correctly against this
  environment's only recalculation engine (headless LibreOffice). See
  `mdlguideline.md` §7 for the scoped caveat added alongside this entry.
- **Environment limitation — no live Excel/LibreOffice recalculation
  available**: headless LibreOffice (`soffice --headless --convert-to
  ...`) fails to load even a trivial file in this build environment
  (confirmed by direct testing, not specific to this workbook) — this is
  a sandbox/environment constraint, not a defect in the generated file.
  `tools/cracker_model/qa_recalc.py` therefore validates formula *logic*
  via an independent pure-Python re-implementation of the KBR piecewise
  interpolation and global regression (cross-checked against all 4
  sourced data points, matching exactly) and a static named-range
  reference check, rather than live golden-value assertions. Opening the
  workbook in a real Excel or working LibreOffice install (which
  recalculates on open, per `fullCalcOnLoad=True` set in `build.py`) is
  the outstanding verification step before treating any cell value as
  confirmed correct.

## Changelog

- **2026-07-08** — Repo initialized: replicated `Licensor/`, `tcoedatabase/`,
  `tolling/` from MYSGH2project; added `CLAUDE.md` (agent persona + regulatory
  scope) and this `memory.md` (seed baseline + open questions).
- **2026-07-08** — Corrected the Technip/Nippon Sanso open question: moved
  `Licensor/technip-offer-lbc-tolling.md` → `Licensor/technip/technip-nippon-sanso-lbc-tolling.md`;
  documented the licensor-vs-operator pattern (Technip licenses, Nippon Sanso
  operates, in the Netherlands; KBR uses the same Nippon Sanso operator model
  in other regions) in `CLAUDE.md` §2.1. Merged branch
  `claude/ammonia-cracker-ai-agent-9n7xfx` to `main`.
- **2026-07-09** — Added `mdlguideline.md`: Engineering Excel Development
  Specification governing every future engineering calculation workbook
  built for the ammonia cracker modeling database (cover/guide/inputs/
  calc/dashboard/report structure, color coding, formula standards, naming
  conventions, RFNBO/KEEI wording rule tying back to `CLAUDE.md` §4.3, and
  a No-Fabrication-Rule equivalent for hardcoded vs. formula-derived
  values). Logged as prerequisite groundwork before any `.xlsx` tool is
  built in this repo. Open follow-up: companion `copilot.md` (see Open
  Questions).
- **2026-07-09** — Built v1 of the Ammonia Cracker Capacity Sizing &
  Project Economics workbook (`tools/cracker_model/`, generates
  `output/Ammonia_Cracker_Sizing_Economics_v1.xlsx`, git-ignored —
  regenerate via `python -m tools.cracker_model.build`). All 5 licensors
  (Topsoe, Technip, KBR, Casale, Duiker) selectable with explicit N/A
  flagging where source data is missing; Own & Operate and Tolling
  (Vopak & Linde / VTTI / Hoegh EVI) commercial modes; NG100/50-50/
  Clean-Fuel fuel-mode toggle; regional CAPEX factor mechanism; unlevered
  merchant-sale IRR; qualitative-only equipment lists; password-protected
  `Constants`/`Settings` sheets (documented deterrent per `mdlguideline.md`
  §12); a `Comparison` sheet independently re-deriving all 8 licensor x
  mode permutations. Every sourced/assumed figure traces through
  `tools/cracker_model/data.py`, mechanically checked by
  `validate_data.py` (62 figures, all cited or ASSUMPTION-labeled). See
  "Assumptions & Data Gaps" above for every labeled assumption this build
  required, and `mdlguideline.md` §7 for the logged LET/LAMBDA deviation.
