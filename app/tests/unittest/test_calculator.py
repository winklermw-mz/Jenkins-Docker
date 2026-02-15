import pytest
from src.calculator import Calculator

def test_add_positive_numbers():
    calc = Calculator()
    assert calc.add(2.5, 3.5) == 6.0

def test_add_integers():
    calc = Calculator()
    assert calc.add(1, 2) == 3

def test_add_negative_numbers():
    calc = Calculator()
    assert calc.add(-1.0, -1.0) == -2.0

def test_add_zero():
    calc = Calculator()
    assert calc.add(5.0, 0) == 5.0

def test_add_wrong_type():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.add("1", 2)

def test_sub_positive_numbers():
    calc = Calculator()
    assert calc.sub(2.5, 3.5) == -1.0

def test_sub_zero():
    calc = Calculator()
    assert calc.sub(5.0, 0) == 5.0

def test_mult_positive_numbers():
    calc = Calculator()
    assert calc.mult(3.0, 4.0) == 12.0

def test_mult_with_zero():
    calc = Calculator()
    assert calc.mult(5.0, 0) == 0.0

def test_mult_negative_numbers():
    calc = Calculator()
    assert calc.mult(-2.0, 3.0) == -6.0

def test_mult_wrong_type():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.mult("2", 3)

def test_div_positive_numbers():
    calc = Calculator()
    assert calc.div(10.0, 2.0) == 5.0

def test_div_floating_point():
    calc = Calculator()
    assert calc.div(5.0, 2.0) == 2.5

def test_div_by_zero():
    calc = Calculator()
    with pytest.raises(TypeError, match="Second parameter must not be zero"):
        calc.div(10.0, 0)

def test_div_wrong_type():
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.div(10.0, "2")