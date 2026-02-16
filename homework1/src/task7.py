import numpy as np

def dot_product(vector1, vector2):
	"""Calculate the dot product between two vectors"""
	a = np.array(vector1)
	b = np.array(vector2)
	return np.dot(a, b)

