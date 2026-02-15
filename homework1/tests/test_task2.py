from task2 import get_integer, get_float, get_string, get_boolean

def test_integer():
	"""Make sure an integer is returned"""
	result = get_integer()
	assert isinstance(result, int)

def test_float():
	"""Make sure a float is returned"""
	result = get_float()
	assert isinstance(result, float)

def test_string():
	"""Make sure a string is returned"""
	result = get_string()
	assert isinstance(result, str)

def test_boolean():
	"""Make sure a boolean is returned"""
	result = get_boolean()
	assert isinstance(result, bool)
