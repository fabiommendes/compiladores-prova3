import pytest
from datetime import date
try:
    from calculadora_resposta import evaluate
except ImportError:
    from calculadora import evaluate


def test_numbers_are_coerced_to_tuples():
    assert evaluate('42') == (42.0, 0)
    assert evaluate('-42') == (-42.0, 0)
    assert evaluate('3.14') == (3.14, 0)


def test_parse_number_with_error():
    assert evaluate('42(1.5)') == (42.0, 1.5)
    assert evaluate('0.5(0.1)') == (0.5, 0.1)


def test_parse_number_with_relative_error():
    assert evaluate('100(5%)') == (100.0, 5.0)
    assert evaluate('-20(10%)') == (-20.0, 2.0)


def test_can_define_variables():
    assert evaluate('x = 10(0.1)') == (10.0, 0.1)
    assert evaluate('x + 1') == (11.0, 0.1)


def test_sum_and_subtraction():
    assert evaluate('2 + 4') == (6, 0)
    assert evaluate('2(0.1) + 4(0.1)') == (6, 0.2)
    assert evaluate('2 - 4') == (-2, 0)
    assert evaluate('2(0.1) - 4(0.1)') == (-2, 0.2)


def test_mul_div():
    assert evaluate('2 * 4') == (8, 0)
    assert evaluate('2(1) * 4(2)') == (8, 8)
    assert evaluate('2 / 4') == (0.5, 0)
