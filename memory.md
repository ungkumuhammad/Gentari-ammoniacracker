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
- **2026-07-08** — Added "Derived Assessment — Licensor CAPEX Normalized to
  100 ktpa H₂" section: none of the 5 licensor packages quote CAPEX at exactly
  100 ktpa, so produced labeled [DERIVED] estimates via power-law regression
  (KBR, using KBR's own 4 quoted cost/capacity points) or generic six-tenths
  scaling (Duiker, Topsoe — single anchor point each, low confidence); Casale
  and Technip flagged N/A (zero cost anchors / tolling-fee-only, cannot
  estimate CAPEX without fabricating inputs). Full method notes and caveats
  recorded so the derivation is reproducible and re-auditable.
