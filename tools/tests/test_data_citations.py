from tools.cracker_model import validate_data


def test_all_facts_cited_or_labeled():
    count, problems = validate_data.check_all_facts_cited()
    assert count > 0, "no Fact instances discovered -- check_all_facts_cited traversal is broken"
    assert not problems, "\n".join(problems)


def test_bulk_tables_have_citation():
    problems = validate_data.check_bulk_tables_have_citation()
    assert not problems, "\n".join(problems)


def test_assumptions_reference_memory_md():
    problems = validate_data.check_assumptions_reference_memory_md()
    assert not problems, "\n".join(problems)
