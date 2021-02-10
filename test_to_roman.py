import pytest

def to_roman(number: int) -> str:
    if number < 0:
        raise ValueError("Negative values not suported")
    return "I" * number

def test_zero():
    assert to_roman(0) == ""

def test_negative():
    with pytest.raises(ValueError):
        to_roman(-42)

def test_one():
    assert to_roman(1) == "I"
