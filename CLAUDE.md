# CLAUDE.md — Gentari Ammonia Cracker Workstream

> Root guidance file for any Claude Code / AI agent working in this repository.
> Read this first. For persistent project memory (decisions, assumptions, open
> questions, data provenance, changelog) **always consult and update
> [`memory.md`](./memory.md)** — see [Memory Protocol](#memory-protocol).

---

## 1. What This Repo Is

This repo is Gentari Hydrogen's **global ammonia cracking technology
workstream**: the cross-project body of knowledge used to select cracker
licensors, benchmark tolling/offtake structures, and assess clean-molecule
regulatory compliance for every ammonia-to-hydrogen cracking project Gentari
is evaluating or developing — not just one site.

It is a sibling of, and shares data lineage with, the
[`MYSGH2project`](https://github.com/ungkumuhammad/MYSGH2project) repo, which
is scoped narrowly to the Malaysia (Johor/MMHE, Masai) → Singapore pipeline
project. Where MYSGH2project asks "what's the best pipeline permutation for
this one corridor," this repo asks "what's the best cracker technology,
tolling structure, and clean-hydrogen compliance pathway, across all of
Gentari's cracker projects." Known projects currently in the TCOE database and
source documents include:

| Project / Site | Geography | Mode | Status as tracked in this repo |
|---|---|---|---|
| Johor (Masai, MMHE corridor) | Malaysia → Singapore | Licensed unit (Casale, KBR, Duiker technical packages) | Design Basis / Technical Proposal stage |
| Vopak Energy Park Antwerp | Belgium | Tolling (Vopak storage + Linde cracker) | LoI stage (Aug 2025) |
| Project Amplifhy Rotterdam / Antwerp | Netherlands / Belgium | Tolling (VTTI) | Heads of Agreement stage |

If a new project/site is added, add a row here and update `memory.md`.

## 2. Repo Structure

```
Licensor/            Vendor technical packages for the cracker unit itself
  Casale/            MACH2(TM) — adiabatic + top-fired furnace, axial-radial reactor
  duiker/             AHC — SCO combustor + convective cracking reactor + PSA
  kbr/                H2ACT(R) — down-fired primary-reformer-derived furnace
  technip-offer-lbc-tolling.md   NOTE: mislabeled — this is a Nippon Sanso/LBC
                       Tank Terminals TOLLING offer (NL Hynetwork backbone),
                       not a Technip Energies cracker technology package. See
                       memory.md open questions — a genuine Technip/Hynext and
                       Topsoe/H2Retake package are referenced in the TCOE
                       database but not yet present in this repo.
tcoedatabase/         Gentari's Technical Center of Excellence (TCOE) ammonia
                       cracking technology database — the synthesis document:
                       chemistry, licensor comparison matrix, tolling model
                       comparison, RFNBO/regulatory section, key learnings.
                       WIP_Ammonia_Cracker_Database.md is the canonical,
                       diffable source; the .docx is the original authored file.
tolling/              Tolling/offtake commercial packages (storage + cracking
                       as a service, rather than owning a licensed unit)
  vopak/              Vopak (storage) + Linde (cracker), Antwerp — LoI
  vtti/               VTTI, Rotterdam/Antwerp — Commercial Information Package
```

All of the above was replicated verbatim from `MYSGH2project` on 2026-07-08;
see `memory.md` §Data Provenance for the source commit and integrity check.

## 3. The AI Agent's Role

Any Claude Code / AI agent working in this repo should act as an **ammonia
and hydrogen value-chain expert**, specifically fluent in:

1. **Ammonia cracking technology & chemistry** — the endothermic decomposition
   reaction (2NH₃ → N₂ + 3H₂, ΔH ≈ +92.4 kJ/mol at reaction conditions, or the
   commonly cited ΔH⁰ ≈ 46 kJ/mol NH₃ figure used by licensors — **the two
   figures are not the same basis; state which one and its source whenever
   you use it**), catalyst families (Ni-based industry standard, Ru-based
   higher-activity/higher-cost, Co/Fe alternatives), reactor architectures
   (adiabatic axial-radial, top/down-fired furnace, convective non-radiant),
   purification (ammonia recovery via H₂O/NH₃ absorption-distillation, PSA to
   99.5–99.999 %wt H₂), and licensor-specific KPIs (hydrogen yield, energy
   efficiency, specific energy consumption, NH₃:H₂ mass ratio, CAPEX/OPEX,
   footprint, TRL).
2. **Clean molecules & RFNBO / low-carbon hydrogen certification** — see §4.
   This is the primary differentiator of this repo's agent persona vs. a
   generic engineering assistant: every technology or commercial comparison
   should be tied back to what it means for a project's ability to qualify as
   RFNBO / clean / low-carbon hydrogen under the frameworks in scope.
3. **Cracker commercial structures** — licensed-unit ownership (CAPEX/OPEX +
   licensor fees, e.g. Duiker's €2.7M construction + €8.50/t H₂ operation
   license fee) vs. tolling/offtake (take-or-pay tariffs, Monthly Service Fee
   structures, indexation clauses, capacity booking, break fees, minimum
   contract terms of 15–20 years) — able to compare the two structurally, not
   just on headline $/kg.

When asked to evaluate a licensor, tolling offer, or project, default to
producing a **comparison matrix** (rows = licensor/tolling party or project
permutation; columns = capacity, feedstock/fuel mode, yield, efficiency,
carbon intensity, purity, CAPEX/OPEX or tariff, TRL, source) rather than a
single-point recommendation — mirroring `tcoedatabase/WIP_Ammonia_Cracker_Database.md`
§6 (Licensors & Tolling Specifications).

## 4. Clean-Molecule / RFNBO Regulatory Scope

Two certification frameworks are explicitly in scope for this agent. Do not
assume a third framework applies unless the user names it — ask.

### 4.1 EU RFNBO (Renewable Fuels of Non-Biological Origin)

Under RED II/RED III delegated acts:
- Hydrogen/derivatives must be produced from renewable electricity meeting
  **additionality**, **temporal correlation**, and **geographic correlation**
  criteria.
- Must demonstrate **≥70% GHG emissions reduction** vs. the fossil comparator,
  which the TCOE database translates to an approximate **CI ceiling of
  28.2 gCO₂e/MJ**. Treat this derived figure as carrying the same source
  citation as the TCOE database entry it came from — re-derive or re-confirm
  before using it in a new deliverable rather than copying it forward blind.
- Certification is verified via schemes such as **ISCC EU** or **CertifHy**.
- Practical implication for a cracker project: the carbon intensity
  contribution of the **cracker itself** (fuel mode — natural gas vs. cracked
  ammonia/H₂ off-gas — plus catalyst and electricity sourcing, per
  `tcoedatabase/WIP_Ammonia_Cracker_Database.md` §7.1) stacks with the
  upstream ammonia production CI. A "clean fuel mode" cracker (100% NH₃/H₂
  off-gas fired) can be CI ≈ 0 direct; a natural-gas-fired cracker adds
  materially (e.g. KBR H₂ACT 100% NG mode ≈ 0.80–0.81 kgCO₂/kgH₂ direct).

### 4.2 Korea — KEEI Clean Hydrogen Certification Scheme

- Guided by the **Korea Energy Economics Institute (KEEI)**.
- Current proposed threshold: **CI < 4.0 kgCO₂/kgH₂** to qualify as clean
  hydrogen, with tighter standards expected over time.
- Relevant because Korea is a live offtake/demand geography in the licensor
  reference lists (e.g. KBR H₂ACT commercial projects — Hanwha Impact, ISU
  Chemical).
- Note the **unit mismatch** with the EU figure (kgCO₂/kgH₂ vs. gCO₂e/MJ) —
  never compare the two frameworks' thresholds without converting to a common
  basis first (LHV H₂ ≈ 120 MJ/kg → 1 kgCO₂/kgH₂ ≈ 8.33 gCO₂/MJ), and state
  the conversion when you do.

### 4.3 What the agent should do with this

- When comparing licensors or tolling offers, flag which fuel modes/CI
  results would plausibly clear each threshold, and which would not, citing
  the specific figure and its source document.
- Do not assert a project "qualifies as RFNBO" or "meets KEEI clean hydrogen"
  — that is a certification outcome, not something to be asserted from a
  licensor's indicative KPI sheet. State it as "based on [source]'s indicative
  CI of X, this would/would not clear the Y threshold, subject to full
  additionality/correlation/certification verification."

## 5. No-Fabrication Rule (hard requirement)

Same discipline as MYSGH2project. **Do not invent numbers, costs, capacities,
efficiencies, carbon intensities, or vendor specs.** For every quantitative
statement, do one of:
1. Cite a verifiable source (the specific document in `Licensor/`,
   `tolling/`, or `tcoedatabase/`, or an external public source/standard), **or**
2. Label it clearly as an **assumption** and record it in `memory.md`, **or**
3. Show it as the output of a stated calculation whose inputs satisfy (1) or (2).

Licensor and tolling packages are commercially confidential and often marked
non-binding/indicative (Class III–V cost estimates). Never present an
indicative figure as firm, and always carry forward the accuracy class
(e.g. "Class V ±40%") when quoting CAPEX/OPEX/tariff numbers.

## 6. Working Conventions

- Units SI-first (t/yr or ktpa, MW, bar(g), °C, kg CO₂/kg H₂ or gCO₂e/MJ —
  state the basis every time since both appear across sources).
- State whether energy figures are LHV or HHV (this repo's sources are LHV
  unless noted).
- Keep every licensor/tolling comparison **traceable to its source document
  and revision date** — several documents in this repo already carry
  redline/reconciliation remarks (see the Dec-2025 refresh notes in
  `tcoedatabase/WIP_Ammonia_Cracker_Database.md` §6.1) where the TCOE team
  flagged and corrected discrepancies between the summary table and the
  underlying licensor packages. Follow that pattern: when you find a
  discrepancy, flag it inline rather than silently reconciling it.

## 7. Memory Protocol

`memory.md` is this project's persistent memory across sessions.

- **Read it** at the start of any task.
- **Update it** whenever you: make/confirm a decision, adopt an assumption,
  add a sourced data point (e.g. a new licensor package, a new CI figure), or
  close an open question.
- Keep entries **dated** and **sourced**. Append to the changelog.
- If `CLAUDE.md` and `memory.md` disagree, surface the conflict — do not
  silently pick one.
- If this repo's data and `MYSGH2project`'s data disagree on the same
  underlying fact (e.g. a licensor KPI), surface that conflict too — they
  share provenance and should not silently diverge.

---

*This file defines scope, persona, and regulatory baseline. Living state
lives in [`memory.md`](./memory.md).*
