def calculate_discount(purchase_amount):
	if purchase_amount < 0:
		raise ValueError("Purchase amount cannot be negative.")

	if purchase_amount >= 5000:
		discount_rate = 0.20
	elif purchase_amount >= 3000:
		discount_rate = 0.10
	elif purchase_amount < 300:
		discount_rate = 0.05
	else:
		discount_rate = 0

	discount_amount = purchase_amount * discount_rate
	final_amount = purchase_amount - discount_amount
	return discount_amount, final_amount


purchase_amount = float(input("Enter the purchase amount in rupees: "))

try:
	discount_amount, final_amount = calculate_discount(purchase_amount)
	print(f"Discount amount: Rs {discount_amount:.2f}")
	print(f"Final payable amount: Rs {final_amount:.2f}")
except ValueError as error:
	print(error)