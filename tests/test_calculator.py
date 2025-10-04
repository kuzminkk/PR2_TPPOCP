from calculator import add, sub, mul, div
import pytest

def test_add():
    assert add(2, 2) == 4   # проверка 2+2=4

def test_sub():
    assert sub(5, 3) == 2

def test_mul():
    assert mul(3, 4) == 12

def test_div():
    assert div(10, 2) == 5

def test_power():
    assert power(2, 3) == 8

def test_div_zero():
    import pytest
    with pytest.raises(ValueError):
        div(1, 0)
