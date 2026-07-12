# tools/cracker_model

Generates `output/Ammonia_Cracker_Sizing_Economics_v1.xlsx` — the Excel
capacity-sizing and project-economics workbook described in
`mdlguideline.md` and `/root/.claude/plans/i-want-to-start-mutable-dongarra.md`.

## Usage

```
pip install -r tools/requirements.txt
python -m tools.cracker_model.build
```

Output lands in `output/` (git-ignored — regenerate rather than commit).

## Regenerating after a data change

Every sourced figure and every labeled assumption lives in
`tools/cracker_model/data.py`. Edit there, not in the sheet-builder
modules under `tools/cracker_model/sheets/`. Then:

```
pytest tools/tests/                        # citation/named-range checks
python -m tools.cracker_model.build         # rebuild the workbook
python -m tools.cracker_model.qa_recalc     # headless LibreOffice recalc + golden-value check
```

## Adding a 6th licensor or a new tolling party

Add a `LicensorRecord` / `TollingPartyRecord` to `data.py` with full
citations (or `is_assumption=True` + a `memory.md` cross-reference for any
field that isn't sourced). `validate_data.py` will fail the build if a
numeric field is missing provenance. No sheet-layout code should need to
change — the sheets read from `data.py`'s registries.

## Known v1 deviations from `mdlguideline.md`

`mdlguideline.md` §7 prefers `LET()`/`LAMBDA()`. This build uses classic
`INDEX/MATCH`/`IFERROR`/named-range formulas instead, because openpyxl
cannot verify dynamic-array formulas render correctly against the
headless-LibreOffice recalculation this pipeline relies on for QA. See
`mdlguideline.md` §7 and `memory.md` for the logged caveat.
