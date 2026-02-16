from task4 import calculate_discount
"""Test integer only"""
def test_calculate_discount_int():
	assert calculate_discount(100, 15) == 85

"""Test float only"""
def test_calculate_discount_float():
        assert calculate_discount(100.5, 5.5) == 94.9725

"""Test integer and float"""
def test_calculate_discount_int_float():
        assert calculate_discount(100, 15.5) == 84.5

"""Test float and integer"""
def test_calculate_discount_float_int():
        assert calculate_discount(95.5, 10) == 85.95
