from task7 import dot_product

def test_dot_product():
	"""Test dot product calculation"""
	result = dot_product([1,2,3], [4,5,6])
	assert result == 32
