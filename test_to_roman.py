import pytest

def to_roman(number: int) -> str:
    if number < 0:
        raise ValueError("Negative values not suported")
    values = [1000, 500, 100, 50, 10, 5, 1]
    names = ["M", "D", "C", "L", "X", "V", "I"]
    out = ""
    for i in range(len(values) - 1):
        while number >= values[i]:
            out += names[i]
            number -= values[i]
        for j in range(i + 1, len(values)):
            diff = values[i] - values[j]
            if number >= diff and j % 2 == 0:
                out += names[j] + names[i]
                number -= diff
                break

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

def test_nine():
    assert to_roman(9) == "IX"

def test_large():
    assert to_roman(1918) == "MCMXVIII"
