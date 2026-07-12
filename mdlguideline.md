# mdlguideline.md — Engineering Excel Development Specification

> Applies to every engineering calculation workbook (`.xlsx`) produced in
> this repo — starting with the ammonia cracker modeling database. Read
> alongside [`CLAUDE.md`](./CLAUDE.md) (repo scope, agent persona,
> No-Fabrication Rule) and [`memory.md`](./memory.md) (data provenance,
> sourced figures). This document governs *form* (how a workbook is built);
> `CLAUDE.md` governs *content* (what numbers are trustworthy and how they
> must be sourced). Where the two overlap — e.g. citing a source for a
> calculated value — `CLAUDE.md` wins.

---

## 0. Purpose

Define the standard for developing engineering calculation tools in Excel
for this repo, so every workbook (cracker sizing, licensor comparison,
tolling economics, CI/RFNBO screening, etc.) is technically accurate,
visually professional, easy to use, and maintainable across sessions and
contributors.

Philosophy for every workbook:

**Professional Engineering + Excellent User Experience + Complete
Transparency**

A user should understand what the tool does within minutes, confidently
enter design inputs, verify every calculation, and generate a professional
output suitable for engineering documentation — without inspecting hidden
formulas.

---

## 1. Design Principles

Every workbook shall satisfy:

- Professional appearance
- Intuitive navigation
- Minimal user effort
- Transparent calculations
- Easy verification
- Fully traceable formulas
- Version controlled
- Ready for future expansion
- **Fully traceable to a source document** (per `CLAUDE.md` §5 No-Fabrication
  Rule — every constant or reference value in the workbook must resolve to a
  cited document in `Licensor/`, `tolling/`, `tcoedatabase/`, an external
  standard, or a labeled assumption logged in `memory.md`)

The workbook should feel like a lightweight engineering application rather
than a traditional spreadsheet.

---

## 2. Workbook Structure

### 2.1 Cover sheet (`Cover`)

Landing page. Include:

- Tool name (e.g. "Ammonia Cracker Sizing & CI Screening Tool")
- Gentari / project identifier
- Brief description of scope
- Engineering discipline (process / chemical engineering)
- Applicable standards (see §11)
- Version number, release date, author, reviewer, approval status
- Revision history (mirrors the workbook's own changelog, not a substitute
  for `memory.md`)
- Disclaimer — must state the accuracy class of any cost figures carried in
  the workbook (Class III–V, per `CLAUDE.md` §5) and that licensor/tolling
  data is commercially confidential and indicative unless noted firm
- Navigation buttons: ▶ Start · 📖 User Guide · 📊 Calculation · 📈 Dashboard
  · 📄 Report

### 2.2 User Guide (`Guide`)

- Purpose, scope, assumptions, limitations
- Required inputs and units (state SI-first per `CLAUDE.md` §6; if a
  licensor source used imperial or LHV/HHV inconsistently, note the
  conversion applied)
- Calculation workflow (a short flow diagram or numbered list referencing
  each `Calc_XX` sheet)
- Output interpretation
- References (full citation list, see §11)
- FAQ

### 2.3 Input sheet (`Inputs`)

The **only** sheet where users enter data.

- Clean layout, no clutter, grouped sections, consistent units
- Drop-downs for any categorical input with a fixed valid set (licensor
  name, fuel mode, feedstock ammonia grade, certification framework —
  EU RFNBO / Korea KEEI)
- Automatic validation, error highlighting

Suggested sections for a cracker workbook:

- **Project Information** — Project name, site (Johor / Antwerp / Rotterdam
  / other, per `CLAUDE.md` §1 project table), client, engineer, date
- **Design Conditions** — feed NH₃ flowrate, temperature, pressure, ambient
  conditions
- **Cracker/Licensor Parameters** — licensor selection (dropdown sourced
  from `tblLicensors`), fuel mode (clean/NH₃-fired vs. NG-fired vs. blended),
  catalyst family, reactor architecture
- **Equipment Parameters** — dimensions, thickness, safety factors,
  turndown
- **Certification Screening** — target framework (EU RFNBO / Korea KEEI),
  auto-flags pass/fail against the CI ceiling per `CLAUDE.md` §4 (worded as
  "would/would not clear," never "qualifies" — see §9 below)

Color coding (see §6 for hex values):

| Cell Type | Color |
|---|---|
| User Input | Light Yellow |
| Dropdown | Light Blue |
| Calculated | Light Gray |
| Reference | White |
| Errors | Light Red |
| Headers | Dark Blue (fill), white text |

### 2.4 Calculation sheets (`Calc_01`, `Calc_02`, …)

Separate all calculation logic from user inputs. Never let a user-editable
cell live on a `Calc_` sheet.

Suggested sheet set for cracker modeling:

- `Calc_MassEnergyBalance` — feed/product mass balance, ΔH per
  `CLAUDE.md` §3.1 (state which ΔH basis: ~92.4 kJ/mol NH₃ reaction-condition
  figure vs. the ~46 kJ/mol NH₃ standard-state figure — never mix them in
  one workbook without a labeled conversion)
- `Calc_ReactorSizing`
- `Calc_Purification` (PSA / absorption-distillation train)
- `Calc_CarbonIntensity` — direct + upstream CI, feeding the RFNBO/KEEI
  screening on `Dashboard`
- `FluidProperties`
- `Constants` — protected, named ranges only, each with a source citation
  in an adjacent comment/column

Each calculation block documents:

1. **Purpose** (one line)
2. **Equation** (engineering notation, e.g. `ΔP = f × (L/D) × (ρV²/2)`)
3. **Variables** (symbol, description, unit)
4. **Engineering reference** (standard or source document + revision date)
5. **Excel formula** (e.g. `=B12*(B15/B16)*(B13*B14^2/2)`)
6. **Result** (with unit shown, e.g. `12.6 kPa`)

### 2.5 Results Dashboard (`Dashboard`)

Executive summary:

- Pass/Fail indicators (equipment design checks)
- Key performance indicators (H₂ yield, NH₃:H₂ ratio, energy efficiency,
  direct CI in both kgCO₂/kgH₂ and gCO₂e/MJ — state the LHV basis used for
  the conversion, per `CLAUDE.md` §4.2)
- Charts (see the `dataviz` skill's palette/contrast guidance if this
  dashboard is ever rendered outside Excel, e.g. exported to an HTML
  artifact)
- Warnings, design margin, suggested improvements
- **RFNBO / KEEI screening block** — worded per §9 below, never asserting
  certification outcome

### 2.6 Report sheet (`Report`)

Auto-generated, printable (A4). Include project info, input summary,
calculation summary, design checks, final results, revision block, sign-off.
No formulas should require the report sheet itself to be unhidden/unlocked
by the user to function.

---

## 3. User Experience (UX)

- Minimal scrolling; freeze panes on headers/navigation
- Consistent navigation; hyperlinks between sections; "◀ Back to Home" on
  every non-Cover sheet
- Smart data validation with helpful input messages and plain-language
  error explanations
- Automatic unit display next to every input/output cell

---

## 4. User Interface (UI)

**Typography**

| Element | Font | Size |
|---|---|---|
| Titles | Segoe UI / Aptos / Calibri | 16–20 pt |
| Section headers | Segoe UI / Aptos / Calibri | 12–14 pt |
| Body | Segoe UI / Aptos / Calibri | 11 pt |

Generous white space; avoid overcrowding.

---

## 5. Color Theme

| Role | Color |
|---|---|
| Primary | Deep Blue |
| Secondary | Steel Gray |
| Accent | Orange |
| Success | Green |
| Warning | Amber |
| Error | Red |
| Background | White |

Maintain WCAG-reasonable contrast. If a workbook's dashboard is ever ported
to an HTML artifact, use the `dataviz` skill's palette rather than
re-deriving colors ad hoc.

---

## 6. Cell Color Reference (hex)

Use these exact fills so every workbook in the repo is visually consistent.

| Cell Type | Fill | Hex |
|---|---|---|
| User Input | Light Yellow | `#FFF2CC` |
| Dropdown | Light Blue | `#DCE6F1` |
| Calculated | Light Gray | `#F2F2F2` |
| Reference | White | `#FFFFFF` |
| Errors | Light Red | `#F8CBAD` |
| Headers | Dark Blue fill / white text | `#1F3864` / `#FFFFFF` |
| Success | Green | `#C6E0B4` |
| Warning | Amber | `#FFE699` |

---

## 7. Formula Standards

Every calculated value **must** contain an Excel formula. Never manually
type a calculated value — this is the Excel-workbook equivalent of the
No-Fabrication Rule in `CLAUDE.md` §5: a hardcoded number that looks
calculated is exactly the kind of unsourced figure that rule prohibits.

Formulas should be transparent, readable, structured, auditable.

**Preferred**: `LET()`, `LAMBDA()`, named ranges, structured Tables
(`tblInputs`, `tblResults`, …), dynamic arrays, `INDEX`/`XMATCH`.

**Avoid**: long nested `IF()` chains, hardcoded constants inside formulas
(pull from `Constants` sheet via named range instead), repeated
calculations, magic numbers.

> **Deviation, logged 2026-07-09**: workbooks generated by an
> openpyxl-based build pipeline (see `tools/cracker_model/` and its
> README) use classic `INDEX`/`MATCH`/`IFERROR`/named-range formulas
> instead of `LET()`/`LAMBDA()`. openpyxl writes formulas as opaque
> strings with no dynamic-array object model, and such a pipeline's build-
> time QA step (headless LibreOffice recalculation) cannot verify that
> `LET()`/`LAMBDA()` render correctly against real Excel 365 in an
> environment without Excel itself. `LET()`/`LAMBDA()` remain preferred
> wherever the build pipeline *can* verify Excel-365 rendering (e.g. a
> workbook hand-built or reviewed directly in Excel); classic formulas are
> the default for openpyxl-generated workbooks specifically. See
> `memory.md` for the dated entry recording this as a discrepancy from
> this section's stated preference, per `CLAUDE.md` §6's "flag
> discrepancies inline" convention.

Every constant pulled onto the `Constants` sheet must carry, in an adjacent
cell/comment, either:

1. A citation to the source document (`Licensor/...`, `tolling/...`,
   `tcoedatabase/...`, or an external standard), or
2. An explicit `ASSUMPTION` label — and a matching entry added to
   `memory.md` per `CLAUDE.md` §7.

---

## 8. Engineering Formula Documentation

Every major calculation documents:

- Engineering equation
- Variable definitions (symbol, description, unit)
- Reference standard (ASME / API / ISO / company standard / licensor
  document + revision date)
- Excel formula
- Engineering notes (assumptions, applicable range, caveats — e.g. the
  Topsoe 96% efficiency comparability caveat recorded in `memory.md`)

Example:

```
Equation:      Q = m × Cp × ΔT
Excel formula: =MassFlow*Cp*(OutletTemp-InletTemp)
Reference:     ASME PTC 4 / [licensor doc, rev date]
```

---

## 9. RFNBO / KEEI Screening — Wording Rule

Per `CLAUDE.md` §4.3, any workbook cell or dashboard indicator that
evaluates a CI figure against the EU RFNBO ceiling (~28.2 gCO₂e/MJ) or the
Korea KEEI threshold (<4.0 kgCO₂/kgH₂) must be worded as a conditional,
never an assertion of certification status. Use formulas/labels like:

> "Based on [source]'s indicative CI of X, this **would / would not clear**
> the [EU RFNBO / KEEI] threshold, subject to full
> additionality/correlation/certification verification."

Never output "PASS — RFNBO qualified" or equivalent as a bare Pass/Fail
badge without that qualifying language nearby (a footnote reference on the
dashboard is acceptable, provided the full wording appears in the `Guide`
or `Report` sheet).

If a workbook mixes the two frameworks' units, the conversion factor
(LHV H₂ ≈ 120 MJ/kg → 1 kgCO₂/kgH₂ ≈ 8.33 gCO₂/MJ) must be shown as a named
constant with its derivation visible, not folded silently into another
formula.

---

## 10. Data Validation & Error Handling

Validate every user input (pressure > 0, temperature within allowable
range, flowrate > 0, efficiency 0–100%, material/licensor selected from
dropdown, etc.).

Never expose raw Excel errors. Use `IFERROR()` (or `IFNA()`) to replace
`#DIV/0!`, `#N/A`, etc. with a plain-language message, e.g.:

> Invalid Input — please enter a flowrate greater than zero.

Error handling must preserve engineering integrity: never silently coerce
an invalid input into a default value that lets a downstream calculation
proceed unflagged.

---

## 11. Engineering Standards & Citations

Reference internationally recognized standards where applicable: ASME, API,
ISO, IEC, ASTM, EN, AISC, Eurocode. Always record the edition/year used.

For this repo specifically, also cite:

- The licensor technical package and revision date (`Licensor/<vendor>/...`)
- The tolling commercial package and date (`tolling/<party>/...`)
- `tcoedatabase/WIP_Ammonia_Cracker_Database.md` section reference, where a
  figure is drawn from the TCOE synthesis rather than a raw licensor doc
- RFNBO (RED II/III delegated acts) or KEEI framework document, when citing
  a regulatory threshold

Carry forward the accuracy class (Class III–V, ±X%) on every CAPEX/OPEX/
tariff figure, per `CLAUDE.md` §5.

---

## 12. Protection Strategy

Protect: calculation sheets, `Constants`, named ranges, reference data.
Allow editing only in designated input cells on `Inputs` (and `Cover`
project-info fields, if editable). Use sheet protection with a documented
(non-secret) password stored in the workbook's `Settings` sheet, not
communicated out-of-band.

---

## 13. Performance

- Avoid volatile functions (`NOW()`, `OFFSET()`, `INDIRECT()`) unless
  necessary
- Minimize repeated calculations; compute once, reference elsewhere
- Prefer `INDEX`/`XMATCH` over deeply nested `VLOOKUP` chains

---

## 14. Maintainability

Each workbook includes: version history, revision notes, developer
comments, change log, assumptions, known limitations, future improvements.
This is the workbook-local record; it does not replace `memory.md`, which
remains the repo-wide source of truth for decisions and sourced data
points. If a workbook's local assumption list and `memory.md` ever
disagree, `memory.md` wins — update the workbook to match, per
`CLAUDE.md` §7.

---

## 15. Naming Convention

**Worksheets**: `Cover`, `Guide`, `Inputs`, `Calc_01`, `Calc_02`, …,
`References`, `Dashboard`, `Report`, `Settings`

**Named ranges** — general engineering:

`FluidDensity`, `PipeDiameter`, `MassFlowRate`, `DesignPressure`,
`AmbientTemperature`

**Named ranges** — ammonia cracker specific (extend as needed, keep
PascalCase, no abbreviation ambiguity):

`NH3FeedRate`, `H2ProductRate`, `NH3ToH2MassRatio`, `CrackerFuelMode`,
`CrackingTemp`, `CrackingPressure`, `H2Purity`, `EnergyEfficiency`,
`DirectCI_kgCO2perkgH2`, `DirectCI_gCO2eperMJ`, `RFNBOCeiling_gCO2eperMJ`,
`KEEIThreshold_kgCO2perkgH2`, `LicensorSelected`, `AccuracyClass`

**Tables**: `tblInputs`, `tblMaterials`, `tblResults`, `tblConstants`,
`tblLicensors`, `tblTollingParties`

---

## 16. Deliverables Checklist

Every workbook produced in this repo should include:

- [ ] Professional cover page
- [ ] User guide
- [ ] Structured input sheet
- [ ] Fully documented calculations (equation, variables, reference,
      formula, result)
- [ ] Formula transparency (no hardcoded calculated values)
- [ ] Engineering + repo-source references (§11)
- [ ] Interactive dashboard with correctly worded RFNBO/KEEI screening (§9)
- [ ] Printable report
- [ ] Protected calculation sheets
- [ ] Version history / revision log
- [ ] Consistent UI/UX (§§3–6)
- [ ] Error validation (§10)
- [ ] Expandable architecture (new licensors/sites addable without
      restructuring)
- [ ] Every constant traceable to a citation or a logged `memory.md`
      assumption (§7)

---

## 17. Vision

Build Excel engineering tools comparable to professional engineering
software while retaining Excel's flexibility. Every workbook should be
intuitive for first-time users, trustworthy for engineering review, and
maintainable for future enhancements — and, in this repo specifically,
held to the same sourcing discipline as the written comparison matrices in
`tcoedatabase/`. A user should be able to understand the workflow, enter
validated inputs, review every calculation, and produce a professional
engineering report without needing to inspect or modify hidden formulas.

---

## 18. Next Step (not yet created)

A companion `copilot.md` (or AI-development guideline) should tell an AI
assistant exactly how to generate each worksheet, apply naming conventions
and formatting rules, and follow formula-writing practices, so every future
ammonia cracker modeling workbook in this repo is generated consistently
against this specification. Track this as an open item in `memory.md` until
it exists.
