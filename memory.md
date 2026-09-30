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
- **2026-07-08** — Added five new KBR Gentari-specific proposal documents to
  `Licensor/kbr/`, converted PDF→Markdown via
  [microsoft/markitdown](https://github.com/microsoft/markitdown) at the
  user's request. All five are Rev 0, "Issued for Proposal," KBR Doc Nos.
  `Gentari-PR-GEN-*`, scoped to the Johor project's 12/24/68/80 kTPA H₂,
  99.97 mol% H₂ product case (three firing modes: 100% NG, 50% NG/50%
  cracked NH₃, 100% cracked NH₃):
  - `I.A_GENTARIProcess_Design_Basis_Rev0.md` — Process Design Basis
    (Gentari-PR-GEN-PDB-001, dated 22/Dec/25)
  - `I.B_GENTARIBFD_12kTPA_100NG_Rev0.md` — ISBL Block Flow Diagram, Scenario
    1 (12 kTPA H₂, 100% NG fuel) (Gentari-PR-GEN-BFD1A-001, dated 23-Dec-25)
  - `I.C_GENTARIHMB_12kTPA_100NG_Rev0.md` — Preliminary Heat & Material
    Balance (Gentari-PR-GEN-HMB-001, dated 23/Dec/25)
  - `I.D_GENTARIProcess_Description_GENERAL_Rev0.md` — Ammonia Cracking Unit
    Process Description, ISBL (Gentari-PR-GEN-PSD-001, dated 22/12/2025)
  - `I.E_GENTARIFeed__Product_ALL_Rev0.md` — Preliminary ISBL Feed & Product
    Summary, all four capacities (Gentari-PR-GEN-F&F-001, dated 22/Dec/25)

  These are more granular than the existing `kbr-johor-hub.md` (KBR's
  December 2025 general H2ACT® Technical Information Package) — they are the
  Gentari/Johor-specific proposal package underlying it. Markitdown's PDF
  conversion is text/table extraction only; it does not preserve diagram
  graphics (`I.B`, the BFD, converts to scattered stream labels/numbers with
  no visual flow — read alongside the source PDF for actual diagram
  topology). Tables in `I.C` (HMB) and `I.E` (Feed & Product) render with
  some column-alignment ambiguity from the source PDF's merged cells —
  cross-check figures against the original PDF before citing exact numbers
  in downstream analysis.
- **2026-07-08** — Added four more KBR Gentari proposal documents to
  `Licensor/kbr/`, same conversion method (markitdown) and same document
  series (Rev 0, Johor 12/24/68/80 kTPA H2 case):
  - `I.F_GENTARIUtilities_12KTPA_Rev0.md` — Preliminary Utility Summary,
    ISBL (Gentari-PR-GEN-BLS-001)
  - `I.G_GENTARICatalyst__Chemicals_12kTPA_Rev0.md` — Preliminary Catalyst &
    Chemicals Summary (Gentari-PR-GEN-C&C-001, dated 23/Dec/25)
  - `I.H_GENTARIEquipment_List_OSBL_Rev0.md` — Preliminary Equipment List,
    OSBL (Gentari-PR-GEN-LST-0002, dated 23/12/2025, "Issued for info" not
    "Issued for Proposal" like the others — note the different issue status)
  - `I.I_GENTARIPreliminary_PP_12kTPA_Rev0.md` — Preliminary Plot Plan
    (CAD/drawing-derived; markitdown extraction is fragmented drawing-note
    text with no preserved layout — not usable as prose, refer to source PDF
    for actual plot plan geometry)

  **Flagged, not corrected**: `I.G`'s document header (line 2 of the
  converted file) reads "Fluxys ammonia Cracking Proposal" instead of
  "Gentari" — appears to be a leftover from a KBR document template reused
  from an unrelated client engagement (Fluxys is a Belgian gas
  infrastructure company, unrelated to this project). Left as-is in the
  converted markdown per source fidelity; flagged here per CLAUDE.md §6
  discrepancy convention. Do not treat this document's content as
  compromised — only the header/title artifact is suspect — but verify
  against the source PDF or with KBR if this document is used in a formal
  deliverable.

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

## Equipment List & 100 ktpa H₂ Capacity Sizing (KBR-led, cross-licensor highlighted)

- **2026-07-08** — Initially verified (before the I.A–I.I annexures existed in this repo — see
  correction below): KBR's Technical Information Package (`Licensor/kbr/kbr-johor-hub.md`) Table
  of Contents references "Annexure I.(H) – Equipment List OSBL" (p.27) with no populated content
  in that single-file document. The de facto equipment list used for the first sizing pass was
  reconstructed from KBR's process narrative (§2.1, §3.2, §3.9) only.
- **2026-07-08 (correction, same day)** — A concurrent session added the full I.A–I.I annexure
  set to `Licensor/kbr/` (converted from the licensor's PDFs; see that session's own memory.md
  entries and commits `17c0dc4`/`a0766d6`). This **populates** `I.H_GENTARIEquipment_List_OSBL_Rev0.md`
  — but, as its title says, it is the **OSBL** equipment list only (Units 101–114: emergency
  power, raw/demin/potable/fire water, cooling towers, HP flare, plant/instrument air, N₂
  generation, waste water treatment, H₂ export metering) — correctly excluded from ISBL sizing,
  same conclusion as before. Real tagged **ISBL** equipment numbers do exist, scattered across
  two of the new annexures rather than in one consolidated ISBL list: `I.G` (Catalyst &amp;
  Chemicals Summary) tags 301-B (Fired Cracker, 4.70 m³ Ni catalyst, HyProGen 830, 4-yr life),
  301-D (Adiabatic Reactor, 4.50 m³ Ni catalyst, HyProGen 820/821, 4-yr life), 301-BSCR (SCR
  unit, 550±50 m³ WO₃/V₂O₅-on-TiO₂, 4-yr life) — all at 12 ktpa; `I.I` (Preliminary Plot Plan)
  additionally tags U-103/304-J (PSA), KRCSB-103 (H₂ compressor package), 305-C (combustion air
  preheater). `I.C` (HMB, 12 ktpa NG mode) cross-validates the main package's summary KPIs:
  ammonia feed 9,104 kg/h = 218.5 TPD vs. the summary table's 217.7 TPD; H₂ product 1,435 kg/h =
  34.4 TPD vs. 34.3 TPD — consistent to within rounding. `I.A` confirms KBR's onstream factor as
  8,400 h/yr (=350 d/yr), matching the figure already used from the main package's footnote 5.
  Deliverable `kbr_100ktpa_sizing.pdf` was corrected to reflect this before merging to main; a
  catalyst-volume-at-100-ktpa row (≈76.6 m³, linearly scaled from the single 12 ktpa data
  point — flagged, since only one data point exists to scale from) was added to the sizing table.
- **2026-07-08** — 100 ktpa H₂ capacity sizing developed against this equipment list. KBR's own
  package tabulates only 12/24/68/80 ktpa — 100 ktpa is **above KBR's highest published case**.
  Method: read across KBR's own flat ratios (H₂/NH₃ conversion 6.35 t/t, cooling water 25 t/t,
  demin water 0.1 t/t, all constant 24–80 ktpa) directly; **extrapolated** (flagged as assumption)
  electricity demand (linear fit on 68→80 ktpa trend → ≈263 kWh/t H₂) and ISBL CAPEX (power-law
  fit on KBR's own 68/80 ktpa points, exponent ≈0.555 → ≈US$237M, Class V ±50%, uncertainty
  widens further given the extrapolation). Reaction duty (≈50.3 MW, thermodynamic minimum only)
  calculated from H₂ production rate + ΔH=46 kJ/mol NH₃ (sourced, tcoedatabase Mass/Energy
  Balance section) — excludes preheat/sensible-heat/furnace losses, not a real fired-duty figure.
  Full working shown in `kbr_100ktpa_sizing.pdf` (delivered to repo owner 2026-07-08, not checked
  into the repo as it's a working deliverable, not a source document).
- **2026-07-08** — Cross-licensor highlight for the same 100 ktpa sizing exercise: Casale
  (self-sustaining/clean scheme, NH₃:H₂=7.20 t/t per tcoedatabase) uses its **own** stated
  onstream factor of 8,500 h/yr (354.2 d/yr) — this **differs from KBR's 350 d/yr** even though
  both packages were prepared for the same Johor Hub RFP and the same four nominal capacities
  (12/24/68/80 ktpa). Flagged as a discrepancy, not silently reconciled, per CLAUDE.md §6.
  Casale has no CAPEX or electricity-vs-scale trend published in its Dec-2025 package (technical
  proposal only) so those cells are N/A, not derived. Duiker's onstream days (333.3 d/yr) are
  **implied** (not stated) from its own two figures (12 ktpa = 36 tpd); Duiker's largest
  documented single train is 276 tpd (≈92 ktpa at that implied basis) — the closest
  equipment-level data point to 100 ktpa anywhere in the repo besides the item below. Duiker's
  CAPEX is a single data point (€47M @ 12 ktpa only) so no scaling curve can be fit without an
  unsourced assumption — not attempted.
- **2026-07-08** — The **only literal "100 ktpa" figure anywhere in this repo** is in
  `Licensor/technip/technip-nippon-sanso-lbc-tolling.md`: Nippon Sanso/LBC's "Full Capacity
  Reservation of 100 ktpa" under a proposed Ammonia Cracking Service Agreement (Monthly Cracking
  Service Fee €4,167,000 = 1/12 of €50,000,000). This is a **commercial/tolling capacity
  reservation**, not an equipment list or mass/energy balance — it has no published NH₃:H₂
  ratio or equipment breakdown in this repo and was not merged into the technical sizing table.
  Noted as market evidence that 100 ktpa is a realistic single-ACU scale being quoted in this
  market (Netherlands Hynetwork H₂-Backbone), underlying licensor = Technip Energies per
  CLAUDE.md §2.1.

## Derived Assessment — Licensor CAPEX Normalized to 100 ktpa H₂ (2026-07-08)

Requested by repo owner: compare licensor CAPEX at a common 100 ktpa H₂ capacity.
**No licensor package in this repo quotes CAPEX at exactly 100 ktpa** — each
licensor sized its indicative case differently (KBR gave 4 discrete cases;
Duiker, Topsoe gave 1 each; Casale and Technip gave none). Per CLAUDE.md §5,
figures below that are not directly quoted are explicitly labeled
**[DERIVED/ASSUMPTION]** with method shown; nothing was invented.

| Licensor | Quoted CAPEX (ISBL) data points, as sourced | Source doc | Scaling method to 100 ktpa | **Est. 100 ktpa ISBL CAPEX** | Confidence |
|---|---|---|---|---|---|
| **KBR (H₂ACT®)** | 12 ktpa=$78M; 24 ktpa=$110M; 68 ktpa=$191M; 80 ktpa=$209M (Class V ±50%, Q3 2025 factored, ISBL only) | `Licensor/kbr/kbr-johor-hub.md` §4.1 | Log-log (power-law) regression on KBR's own 4 quoted points: Cost ≈ 21.2 × (ktpa)^0.52 | **[DERIVED] ≈ $234M** | Medium — regression on 4 real KBR points, but 100 ktpa is an extrapolation ~25% beyond KBR's largest quoted case (80 ktpa); within KBR's stated single-train ceiling of 1,200 MTPD (~420 ktpa), so no train-count step-change expected |
| **Duiker (AHC)** | 12 ktpa=€47M lump-sum turnkey (±40%), single **customized** 1-reactor train | `Licensor/duiker/duiker-johor-hub.md` §4.1 | Generic six-tenths engineering scaling rule (Cost₂=Cost₁×(Cap₂/Cap₁)^0.6) — **not** Duiker-specific, since only 1 Duiker data point exists to anchor a regression | **[DERIVED, HIGH UNCERTAINTY] ≈ €166M** (not converted to USD — no verified FX rate sourced in-repo) | Low — single anchor point, generic exponent borrowed from general chem-eng heuristic, not Duiker's own cost curve |
| **Haldor Topsoe** | 50 ktpa=$100M (Class V) | `tcoedatabase/WIP_Ammonia_Cracker_Database.md` table only — **no standalone Topsoe technical package exists in this repo** (see Open Questions) | Generic six-tenths rule (same caveat as Duiker — single anchor point) | **[DERIVED, HIGH UNCERTAINTY] ≈ $152M** | Low — same single-point caveat, plus underlying source document itself is not in repo, only the TCOE summary table |
| **Technip Energies (Hynext by T.EN™)** | None. TCOE table: "Not available at current maturity." Only quantitative 100 ktpa figure available is a **tolling service fee**, not CAPEX: €50M/yr (€4.167M/mo) Monthly Cracking Service Fee for a "Full Capacity Reservation of 100 ktpa," Nippon Sanso/LBC Netherlands offer | `Licensor/technip/technip-nippon-sanso-lbc-tolling.md` | Not derivable — the €50M/yr figure is an annuity bundling initial investment + construction + O&M + margin over a ≥15-yr take-or-pay term; no disclosed discount rate/OPEX split to back out implied CAPEX | **N/A — cannot estimate without fabricating a discount-rate assumption** | — |
| **Casale (MACH²™)** | None at any capacity. TCOE table explicitly: "Not available at current maturity" (Dec-2025 package is technical-proposal-only; Casale's 12/24/68/80 ktpa cases in the Design Basis are process cases, not cost cases) | `Licensor/Casale/*.md`; `tcoedatabase/WIP_Ammonia_Cracker_Database.md` | Not derivable — zero cost anchor points | **N/A — no basis to estimate** | — |

**Method notes (carry forward when this table is reused):**
- All CAPEX figures above are **ISBL only** (KBR and Duiker packages both explicitly
  exclude OSBL, contingency, spares, commissioning/start-up cost, Owner's cost,
  license fees, duties, and currency risk — see kbr-johor-hub.md §4.1 basis notes
  and Duiker Table 8 notes). Total installed cost at 100 ktpa would be materially
  higher than any figure in this table.
- Accuracy classes differ and are not harmonized: KBR ±50% (Class V, Q3 2025,
  no forward escalation); Duiker ±40% (lump-sum); Topsoe's ± band not stated in
  the TCOE table.
- Currency basis differs (KBR/Topsoe in USD; Duiker in EUR) — not converted here
  to avoid introducing an unsourced FX-rate assumption; convert only with a
  verified rate at time of use.
- Fuel-mode basis differs and is **not** separable from these ISBL figures:
  KBR's quoted cases are 100% NG fuel mode; Duiker's is NH₃-fired (clean fuel).
  A furnace/combustor sized for NG firing vs. NH₃/cracked-gas firing is not
  necessarily cost-equivalent equipment, so this is a genuine technology
  difference embedded in the CAPEX, not just a scaling artifact.
- Single-train vs. multi-train topology at 100 ktpa differs by licensor: Duiker's
  own **undownscaled standard train is 276 tpd (≈97–101 ktpa/yr depending on
  330–365 onstream days)** — i.e. 100 ktpa sits almost exactly at Duiker's
  standard 4-reactor train nameplate, not a multiple of the customized
  12 ktpa/1-reactor case quoted. This means the six-tenths scale-up from the
  12 ktpa customized quote is likely a **poor proxy** for Duiker's actual
  100 ktpa economics (a standard 4-reactor train likely prices differently,
  probably more favorably per-unit, than continued scale-up of a bespoke
  single-reactor design) — but Duiker's source package gives no cost figure
  for the full-scale train, so this cannot be quantified from source; flagged
  as a qualitative caveat only. KBR's single-train ceiling (1,200 MTPD ≈
  420 ktpa) comfortably covers 100 ktpa in one train.
- Casale and Technip cannot be ranked on CAPEX at all with current repo data —
  any comparison matrix produced from this table should show them as
  "not available" rather than omit them silently, per CLAUDE.md's comparison-
  matrix convention.

## CAPEX Reference Table (2026-09-28)

- Consolidated every CAPEX figure in the repo into
  `tcoedatabase/CAPEX_Reference.md` (quoted figures, specific CAPEX per t/yr,
  scope inclusions/exclusions, licence fees, 100 ktpa derived estimates,
  tolling fees shown as context only). Two discrepancies surfaced while
  re-checking, **flagged, not corrected**:
  - **Duiker construction licence fee — in or out of €47M?** Duiker §4.2
    says the capacity-adjusted Plant Construction License Fee "is added in
    the CAPEX estimations in Table 8" (i.e. inside €47M, and Table 8 lists it
    under "Includes"). `tools/cracker_model/data.py`
    `DUIKER_LICENSE_FEE_CONSTRUCTION_EUR` says "additive to CAPEX, not folded
    into the EUR47M total" — contradicting the source and the same file's
    `DUIKER_CAPEX_TOTAL_EUR_M` note. Check whether the workbook adds €2.7M on
    top of €47M (double count) before relying on Duiker CAPEX from it.
  - **Duiker 100 ktpa six-tenths estimate**: the Derived Assessment section
    above records ≈€166M; recomputing 47 × (100/12)^0.6 gives €167.7M.
    Within rounding of a ±40% figure, but should be reconciled.
  - Also noted: two KBR 100 ktpa estimates coexist in this file — ≈$234M
    (all-4-point regression, exponent 0.521, R² 0.9997, used by the
    workbook) and ≈$237M (68/80 two-point fit, exponent 0.555, used in
    `kbr_100ktpa_sizing.pdf`). Both shown in the reference table with their
    method; not a data error, but pick one per deliverable and say which.

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
- **2026-07-08** — Converted 5 KBR Gentari proposal PDFs (Process Design
  Basis, BFD, HMB, Process Description, Feed & Product Summary — all Rev 0,
  Johor 12/24/68/80 kTPA H₂ case) to Markdown via markitdown and added to
  `Licensor/kbr/`. See Data Provenance for file list and conversion caveats.
- **2026-07-08** — Converted 4 more KBR Gentari proposal PDFs (Utilities,
  Catalyst & Chemicals, Equipment List OSBL, Preliminary Plot Plan) to
  Markdown via markitdown and added to `Licensor/kbr/`, completing documents
  I.A through I.I of the series. Flagged a "Fluxys" template-leftover
  anomaly in `I.G`'s header — see Data Provenance.
- **2026-07-08** — Merged branch `claude/markdown-licensor-kbr-ertd6w` to
  `main` (fast-forward, no conflicts): adds the 9 KBR Gentari proposal
  markdown conversions (I.A–I.I) under `Licensor/kbr/`. Note: GitHub's
  repo default branch is still `claude/ammonia-cracker-ai-agent-9n7xfx`,
  not `main`, though the two are content-identical up to this merge's base —
  changing the default is a GitHub repo setting, not something git merge
  affects.
- **2026-07-08** — Built KBR H2ACT® equipment list verification + 100 ktpa H₂ capacity sizing,
  cross-highlighted against Casale/Duiker/Technip-Nippon Sanso; delivered as
  `kbr_100ktpa_sizing.pdf`. First pass was built before the I.A–I.I annexures above existed on
  `main` (branched earlier the same day); corrected afterwards once merged in — see "Equipment
  List & 100 ktpa H₂ Capacity Sizing" section above for the full assumption log, including the
  correction and the real ISBL equipment tags (301-B, 301-D, 301-BSCR, U-103, KRCSB-103) found in
  `I.G`/`I.I`. Merged branch `claude/equipment-capacity-h2-sizing-qozx8g` to `main`.
- **2026-07-08** — Added "Derived Assessment — Licensor CAPEX Normalized to
  100 ktpa H₂" section: none of the 5 licensor packages quote CAPEX at exactly
  100 ktpa, so produced labeled [DERIVED] estimates via power-law regression
  (KBR, using KBR's own 4 quoted cost/capacity points) or generic six-tenths
  scaling (Duiker, Topsoe — single anchor point each, low confidence); Casale
  and Technip flagged N/A (zero cost anchors / tolling-fee-only, cannot
  estimate CAPEX without fabricating inputs). Full method notes and caveats
  recorded so the derivation is reproducible and re-auditable. Merged branch
  `claude/licensor-capex-h2-cracker-nc72ag` to `main`.
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
  Merged branch `claude/engineering-excel-guidelines-5begjx` to `main`.
- **2026-09-28** — Added `tcoedatabase/CAPEX_Reference.md`: consolidated
  CAPEX reference table across all licensors (KBR 4 capacity points + 12 ktpa
  ISBL+OSBL, Duiker, Topsoe, Technip/Casale N/A), with scope comparison and
  derived specific/100 ktpa figures. Flagged the Duiker licence-fee and
  €166M-vs-€168M discrepancies — see "CAPEX Reference Table" section.
- **2026-09-28** — Added deck chart `tcoedatabase/figures/kbr_capex_linear.png` (renamed `kbr_capex_scaling.png` same day, see below)
  (generated by `tools/kbr_capex_chart.py`): KBR's 4 quoted ISBL CAPEX points
  (12/24/68/80 ktpa → US$78/110/191/209M, `kbr-johor-hub.md` §4.1) with ±50%
  Class V bars and a **linear** least-squares trendline, requested by repo
  owner: CAPEX (US$M) = 1.901 × ktpa + 59.54, R² = 0.9955 [DERIVED]. Linear
  extrapolation to 100 ktpa gives ≈US$250M — note this is **higher** than
  the log-log estimate (≈US$234M) used in the workbook and the CAPEX
  reference table, because a straight line ignores economy of scale beyond
  80 ktpa. State which fit a deliverable uses; the two are not interchangeable.
- **2026-09-28** — **Decision (repo owner): the deck quotes KBR's CAPEX
  scaling factor as n ≈ 0.52**, with the power-law formula
  CAPEX (US$M) ≈ 21.25 × Capacity(ktpa)^0.52 (log-log fit on KBR's 4 quoted
  ISBL points, R² = 0.9997) as the primary fit, and the linear fit
  (1.901x + 59.54) shown alongside as reference only. Chart regenerated and
  renamed to `tcoedatabase/figures/kbr_capex_scaling.png`; 100 ktpa ≈ US$234M
  (power law) vs ≈ US$250M (linear), both [DERIVED]. Pairwise exponents
  between KBR points range 0.50 (12→24) to 0.55 (68→80) — slight flattening
  of scale economy at the top of the quoted range. All derived from KBR's
  Class V ±50% ISBL estimates (Q3 2025); the ±50% band still applies.
- **2026-09-28** — Repo owner: deck chart `kbr_capex_scaling.png` now shows
  the **power-law fit only** (linear fit removed from the chart; the linear
  formula stays recorded above for reference). Colours set by repo owner:
  #7030A0 main (quoted points + fitted curve), #0070C0 secondary (100 ktpa
  extrapolation + ±50% accuracy bars).
- **2026-09-28** — Merged `claude/capex-reference-table-pqneh6` to `main` via
  PR #2 (merge commit `aab9894`; shell git was blocked by a transient
  permission-check failure, so the merge was done on GitHub).
- **2026-09-30** — Added three deck charts alongside `kbr_capex_scaling.png`,
  all generated by `tools/licensor_charts.py` (replaces
  `tools/kbr_capex_chart.py`), same style and colours (#7030A0 main,
  #0070C0 secondary):
  - `duiker_capex_scaling.png` — Duiker quotes CAPEX at **one capacity only**
    (€47M @ 12 ktpa, ±40%, §4.1 Table 8), so **no Duiker scaling factor can
    be fitted**. Curve uses the generic six-tenths rule, **n = 0.6
    [ASSUMPTION]**, the same method as the 100 ktpa Derived Assessment above
    → ≈€168M @ 100 ktpa. The chart labels the curve as assumed. Applying KBR's
    fitted n ≈ 0.52 instead would give a lower figure; not used, to avoid
    carrying one licensor's cost curve over to another.
  - `kbr_footprint_scaling.png` — KBR §3.6 plot footprints 70×50 / 80×55 /
    95×75 / 100×75 m at 12/24/68/80 ktpa (3,500 / 4,400 / 7,125 / 7,500 m²).
    Power-law fit **n ≈ 0.41**, Area ≈ 1,225.8 × ktpa^0.41, R² = 0.9952
    [DERIVED] → ≈8,231 m² @ 100 ktpa. No accuracy class is stated for the footprints.
  - `duiker_footprint_scaling.png` — Duiker §3.10: 276 tpd standard train =
    3,660 m² (122×30 m); 12 ktpa (36 tpd) ≈ 900 m². 276 tpd converted to
    ≈92 ktpa at Duiker's implied 333.3 d/yr [DERIVED]. Two-point fit
    **n ≈ 0.69** → ≈3,876 m² @ 100 ktpa. Caveat: Duiker's 900 m² is itself
    Duiker's scaled-down estimate from the full-scale plant, not a separate
    layout, so n ≈ 0.69 partly reflects Duiker's own scaling assumption.
  - KBR vs Duiker footprints are **not verified as like-for-like scopes**
    (Duiker excludes NH₃ storage and H₂ compression beyond 50 bar(g); KBR
    excludes offsites & utilities). Check scope before comparing the two
    footprints directly.
- **2026-09-30** — Footprint charts (`kbr_footprint_scaling.png`,
  `duiker_footprint_scaling.png`) now show **sqft alongside m²**: point labels,
  100 ktpa label, formula box, and a right-hand sqft axis (a unit conversion of
  the same values, not a second measure). Conversion 1 m² = 10.7639 sqft
  (international foot, 0.3048 m exact). In sqft: KBR 37,674 / 47,361 / 76,693 /
  80,729 sqft at 12/24/68/80 ktpa, Area ≈ 13,194 × ktpa^0.41 → ≈88,595 sqft @
  100 ktpa; Duiker ≈9,688 sqft @ 12 ktpa, 39,396 sqft @ 276 tpd,
  Area ≈ 1,750 × ktpa^0.69 → ≈41,724 sqft @ 100 ktpa [all DERIVED].
- **2026-09-30** — Footprint chart labels now state the capacity next to each
  m²/sqft value (KBR 12/24/68/80 ktpa; Duiker 12 ktpa (36 tpd) and ≈92 ktpa
  (276 tpd)). All four charts label the extrapolated point "100 ktpa".
- **2026-09-30** — Fast-forwarded `main` to `claude/capex-reference-table-pqneh6`
  (`fc2649e`): Duiker CAPEX chart, KBR/Duiker footprint charts (m² + sqft,
  capacity-labelled), `tools/licensor_charts.py`.
- **2026-09-30** — Added `tcoedatabase/figures/duiker_ahc_block_diagram.png`
  (generated by `tools/duiker_block_diagram.py`): simplified block flow
  diagram of Duiker's AHC. Duiker's own Figure 3 BFD is an image lost in the
  PDF→Markdown conversion, so the diagram is **reconstructed from Duiker's
  text** (§2 & Table 2, §3.2, §3.4, §3.6, §3.9, Tables 5 & 7). Stream values
  are from Table 5 (NH₃-fired, 12 ktpa). The heat-exchanger arrangement is
  **indicative**: Duiker states gas–gas heat recovery to the NH₃ inlet but
  not the exact exchanger network. Labelled as such on the image.
- **2026-09-30 — Correction to the "Duiker NH₃:H₂ ratio discrepancy" entry
  above**: the 7.03-vs-7.05 difference is **inside Duiker's own package**, not
  only between the TCOE database and the source. `duiker-johor-hub.md` states
  7.05 t/t in §3.5 but 7.03 kg/kg in §3.9.1 Table 7, and Table 5's mass
  balance gives 10,448 / 1,487 kg/h = 7.03. The TCOE figure (7.03) therefore
  matches Duiker's Table 5/7. Flagged, not reconciled; confirm with Duiker.
- **2026-09-30** — Added `tcoedatabase/figures/kbr_h2act_block_diagram.png`
  (generated by `tools/kbr_block_diagram.py`): simplified KBR H₂ACT® block
  flow diagram, built from KBR's Process Description I.D
  (Gentari-PR-GEN-PSD-001, Rev 0, 22 Dec 2025, §1–6), with equipment tags as
  given by KBR. Stream values are from I.E (12 ktpa, 100% cracked-gas fuel):
  NH₃ 10,290 kg/h (247.0 MTPD), H₂ 1,426 kg/h (34.2 MTPD), PSA tail-gas fuel
  7,634 kg/h, cracked-gas fuel 1,233 kg/h, NG 0 (417.9 kg/h in 100% NG mode),
  power 342 kWh/t H₂. Chosen to match the Duiker NH₃-fired diagram. Start-up
  system omitted.
- **2026-09-30 — H₂ battery-limit pressure conflict widened (flagged, not
  reconciled)**: KBR now states **three** values: 28 bar(g) (I.D §4 and main
  package §3.3 KPI table), **27 bar(g) (I.E Feed & Product Summary)**, and
  20 bar(g) minimum (main package §3.1/§3.8). The block diagram shows
  "27–28 bar(g)*" with a footnote. Confirm with KBR.
