from task6 import word_count

def test_wrod_count():
	"""Test that word_count returns the correct amount of words"""
	result = word_count()
	assert result == 127
