from task3 import pos_neg_zero, prime_numbers, sum_of_numbers

def test_pos():
	assert pos_neg_zero(21) == "Positive Number"
def test_neg():
	assert pos_neg_zero(-8) == "Negative Number"
def test_zero():
	assert pos_neg_zero(0) == "The number is 0"

def test_prime_numbers(capsys):
	"""Make sure we get the first 10 primes"""
	prime_numbers()
	captured = capsys.readouterr()
	expected = "2\n3\n5\n7\n11\n13\n17\n19\n23\n29\n"
	assert captured.out == expected

def test_sum_of_numbers():
	"""Make sure it correctly sums numbers from 1-100"""
	result = sum_of_numbers()
	assert result == 5050
