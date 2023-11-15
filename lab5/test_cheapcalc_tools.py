import pytest

from cheapcalc_tools import add, subtract, multiply, divide


def test_add():
    assert add(2, 2) == 4


def test_subtract():
    assert subtract(2, 2) == 0


def test_multiply():
    assert multiply(2, 3) == 6


def test_divide():
    assert divide(10, 2) == 5


def test_add_wrong_type():
    with pytest.raises(TypeError):
        add(2, "fdfdfd")


def test_subtract_wrong_type():
    with pytest.raises(TypeError):
        subtract(2, "fdfdfdf")


def test_multiply_wrong_type():
    with pytest.raises(TypeError):
        multiply(2, "fdfdfd")


def test_divide_wrong_type():
    with pytest.raises(TypeError):
        divide(2, "fdfdfd")


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(2, 0)
