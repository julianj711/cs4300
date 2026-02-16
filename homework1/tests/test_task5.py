from task5 import favorite_books, student_database

def test_favorite_books_returned_length():
	"""Test to see if only 3 books are returned"""
	result = favorite_books()
	assert len(result) == 3

def test_favorite_books_first_book():
	"""Test that the first book is correct"""
	result = favorite_books()
	assert result[0] == ("Secrets of the Millionaire Mind", "T. Harv Eker")

def test_student_database_ID_check():
	"""Test that Jimmy's ID is correct"""
	result = student_database()
	assert result["Jimmy"] == 123

def test_student_database_all_students():
	"""Test that all expected students are in database"""
	result = student_database()
	assert "Jimmy" in result
	assert "Joe" in result
	assert "Jim" in result
