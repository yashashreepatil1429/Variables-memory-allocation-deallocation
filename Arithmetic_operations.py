def calculate(first, second):
	if second == 0:
		raise ValueError("The second number must not be zero for division.")

	return {
		"addition": first + second,
		"subtraction": first - second,
		"multiplication": first * second,
		"division": first / second,
		"floor division": first // second,
		"remainder": first % second,
	}


first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))

try:
	results = calculate(first, second)
	for operation, result in results.items():
		print(f"{operation.title()}: {result}")
except ValueError as error:
	print(error)