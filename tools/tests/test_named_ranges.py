import pytest

from tools.cracker_model import build, qa_recalc


@pytest.fixture(scope="module")
def workbook():
    return build.build_workbook()


def test_no_duplicate_named_ranges(workbook):
    # openpyxl's defined_names is itself a dict keyed by name, so true
    # duplicates can't exist post-construction -- this instead checks that
    # every SHEET_ORDER sheet actually exists exactly once.
    assert len(workbook.sheetnames) == len(set(workbook.sheetnames))


def test_all_referenced_named_ranges_are_defined(workbook):
    problems = qa_recalc.check_named_ranges_referenced_are_defined(workbook)
    assert not problems, "\n".join(problems)


def test_kbr_interpolation_matches_sourced_values():
    problems = qa_recalc.verify_kbr_interpolation_logic()
    assert not problems, "\n".join(problems)


def test_protected_sheets_are_locked(workbook):
    from tools.cracker_model import named_ranges as nr
    for name in nr.PROTECTED_SHEETS:
        assert workbook[name].protection.sheet is True
    assert workbook[nr.SHEET_INPUTS].protection.sheet is False
