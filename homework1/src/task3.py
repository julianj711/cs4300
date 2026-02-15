def pos_neg_zero(numToCheck):
	if numToCheck == 0:
		return "The number is 0"
	elif numToCheck < 0:
		return "Negative Number"
	else:
		return "Positive Number"

def prime_numbers():
	"""0 found / start at first prime"""
	count = 0
	num = 2
	"""Keep this running until 10 are found"""
	while count < 10:
		is_prime = True
		for i in range(2, int(num ** .5) + 1):
			if num % i == 0:
				is_prime = False
				break
		"""When a prime is found print and increment counter"""
		if is_prime:
			print(num)
			count += 1
		num += 1

def sum_of_numbers():
	total = 0
	repeat = 1
	while repeat <= 100:
		total += repeat
		repeat += 1
	return total
