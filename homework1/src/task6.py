def word_count():
	"""Count the number of words"""
	with open('task6_read_me.txt', 'r') as file:
		content = file.read()
		words = content.split()
		wordCount = len(words)
	return wordCount

