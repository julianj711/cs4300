"""Calculate the discount and return the price with the discount accounted for"""
def calculate_discount(price, discount_percentage):
	discount =  (discount_percentage/100) * price
	return price - discount

