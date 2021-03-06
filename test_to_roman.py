import pytest

VALUES = [1000, 500, 100, 50, 10, 5, 1]
NAMES = ["M", "D", "C", "L", "X", "V", "I"]

def to_roman(number: int) -> str:
    if number < 0:
        raise ValueError("Negative values not suported")
    out = ""
    for i in range(len(VALUES) - 1):
        while number >= VALUES[i]:
            out += NAMES[i]
            number -= VALUES[i]
        for j in range(i + 1, len(VALUES)):
            diff = VALUES[i] - VALUES[j]
            if number >= diff and j % 2 == 0:
                out += NAMES[j] + NAMES[i]
                number -= diff
                break
    return out + NAMES[-1] * number

def _value_at(roman: str, index: int) -> int:
    return VALUES[NAMES.index(roman[index])]

def from_roman(roman: str) -> int:
    out = 0
    for i in range(len(roman)):
        this_value = _value_at(roman, i)
        if i < len(roman) - 1 and this_value < _value_at(roman, i + 1):
            this_value *= -1
        out += this_value
    return out

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

def test_nine():
    assert to_roman(9) == "IX"

def test_large():
    assert to_roman(1918) == "MCMXVIII"

def test_from():
    assert from_roman("") == 0

def test_from_I():
    assert from_roman("I") == 1

def test_from_IV():
    assert from_roman("IV") == 4

def test_from_broken():
    with pytest.raises(ValueError):
        from_roman("broken")

def test_from_large():
    assert from_roman("MCMXVIII") == 1918

def test_from_liberty():
    assert from_roman("MDCCLXXVI") == 1776

def test_to_liberty():
    assert to_roman(1776) == "MDCCLXXVI"

