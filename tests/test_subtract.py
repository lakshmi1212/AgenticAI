import pytest
from src.math_operations import subtract

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2

def test_subtract_mixed_sign_numbers():
    assert subtract(-5, 3) == -8
    assert subtract(5, -3) == 8

def test_subtract_zero():
    assert subtract(0, 0) == 0
    assert subtract(0, 5) == -5
    assert subtract(5, 0) == 5

def test_subtract_floats():
    assert subtract(5.5, 3.1) == pytest.approx(2.4)
    assert subtract(-5.5, -3.1) == pytest.approx(-2.4)
