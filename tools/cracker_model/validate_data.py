"""Pre-build citation check: every sourced figure in data.py must be
traceable to a Citation or an Assumption. Run standalone (`python -m
tools.cracker_model.validate_data`) or via pytest (test_data_citations.py).

`Fact.__post_init__` already enforces this at construction time for any
value wrapped in `Fact(...)`. This module additionally verifies (a) every
`Fact` reachable from the module's public namespace is well-formed --
belt-and-suspenders in case a future edit builds a `Fact` dynamically and
bypasses the normal import-time check -- and (b) every bulk data table
(KBR_CASES, CASALE_ROWS, ...) carries a companion `*_CITATION` constant,
since individual rows in those tables are plain dataclasses (not
per-cell `Fact` objects) for readability.
"""
import dataclasses
from tools.cracker_model import data as data_module


class CitationError(Exception):
    pass


def _iter_facts(obj, seen=None):
    """Yield every Fact instance reachable from obj (module/dict/list/dataclass)."""
    if seen is None:
        seen = set()
    if id(obj) in seen:
        return
    seen.add(id(obj))

    if isinstance(obj, data_module.Fact):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from _iter_facts(v, seen)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            yield from _iter_facts(v, seen)
    elif dataclasses.is_dataclass(obj) and not isinstance(obj, type):
        for f in dataclasses.fields(obj):
            yield from _iter_facts(getattr(obj, f.name), seen)


def check_all_facts_cited():
    problems = []
    count = 0
    for name in dir(data_module):
        if name.startswith("_"):
            continue
        value = getattr(data_module, name)
        for fact in _iter_facts(value):
            count += 1
            has_source = fact.citation is not None or fact.assumption is not None
            has_na = fact.value is None and fact.na_reason is not None
            if not (has_source or has_na):
                problems.append(f"{name}: Fact({fact.value} {fact.unit}) lacks citation/assumption/na_reason")
    return count, problems


# Bulk tables that use plain dataclass rows (not per-cell Fact) -- each
# must have a companion module-level "<TABLE>_CITATION" constant.
_BULK_TABLES_REQUIRING_CITATION = ["KBR_CASES", "CASALE_ROWS"]


def check_bulk_tables_have_citation():
    problems = []
    for table_name in _BULK_TABLES_REQUIRING_CITATION:
        citation_name = f"{table_name}_CITATION"
        if not hasattr(data_module, citation_name):
            problems.append(f"{table_name} has no companion {citation_name} constant")
            continue
        citation = getattr(data_module, citation_name)
        if not isinstance(citation, data_module.Citation):
            problems.append(f"{citation_name} is not a Citation instance")
    return problems


def check_assumptions_reference_memory_md():
    """Every Assumption should point at a memory.md entry description."""
    problems = []
    for name in dir(data_module):
        if name.startswith("_"):
            continue
        value = getattr(data_module, name)
        for fact in _iter_facts(value):
            if fact.assumption is not None and not fact.assumption.memory_md_ref.strip():
                problems.append(f"{name}: Assumption has no memory_md_ref")
    return problems


def run() -> None:
    fact_count, fact_problems = check_all_facts_cited()
    table_problems = check_bulk_tables_have_citation()
    memory_problems = check_assumptions_reference_memory_md()
    all_problems = fact_problems + table_problems + memory_problems

    print(f"Checked {fact_count} Fact instances across data.py")
    if all_problems:
        print(f"FAILED -- {len(all_problems)} citation problem(s):")
        for p in all_problems:
            print(f"  - {p}")
        raise CitationError(f"{len(all_problems)} uncited/unlabeled figure(s) in data.py")
    print("All figures in data.py are cited or explicitly labeled ASSUMPTION/N-A.")


if __name__ == "__main__":
    run()
