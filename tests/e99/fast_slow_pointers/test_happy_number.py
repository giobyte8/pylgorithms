from e99.fast_slow_pointers.happy_number import (
    is_happy_number,
    sum_squared_digits
)


def test_sum_squared_digits_25():
    assert sum_squared_digits(25) == 29

def test_sum_squared_digits_100():
    assert sum_squared_digits(100) == 1

def test_sum_squared_digits_0():
    assert sum_squared_digits(0) == 0

def test_sum_squared_digits_1():
    assert sum_squared_digits(1) == 1


def test_is_happy_number_28():
    assert is_happy_number(28)

def test_is_happy_number_4():
    assert not is_happy_number(4)

def test_is_happy_number_1():
    assert is_happy_number(1)

def test_is_happy_number_long():
    assert not is_happy_number(2147483646)
