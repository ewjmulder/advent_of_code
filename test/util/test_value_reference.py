from src.util.value_reference import ValueReference


def test_value_reference():
    assert ValueReference(None).value is None
    assert ValueReference(1).value == 1
    assert ValueReference("abc").value == "abc"
