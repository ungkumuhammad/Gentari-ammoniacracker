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
- **2026-07-08** — Built KBR H2ACT® equipment list verification + 100 ktpa H₂ capacity sizing,
  cross-highlighted against Casale/Duiker/Technip-Nippon Sanso; delivered as
  `kbr_100ktpa_sizing.pdf`. See new "Equipment List & 100 ktpa H₂ Capacity Sizing" section above
  for the full assumption log.
