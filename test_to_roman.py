import pytest

def to_roman(number: int) -> str:
    if number < 0:
        raise ValueError("Negative values not suported")
    values = [5, 1]
    names = ["V", "I"]
    out = ""
    for i, _ in enumerate(values[:-1]):
        while number >= values[i]:
            out += names[i]
            number -= values[i]

    return out + names[-1] * number

def test_zero():
    assert to_roman(0) == ""

def test_negative():
    with pytest.raises(ValueError):
        to_roman(-42)

def test_one():
    assert to_roman(1) == "I"

def test_five():
    assert to_roman(5) == "V"

def test_six():
    assert to_roman(6) == "VI"
