def calculate(a, operator, b):
	if operator not in ("+", "-", "*", "/", "//", "%", "**"):
		raise ValueError("Invalid operator.")

	if operator in ("/", "//", "%") and b == 0:
		raise ZeroDivisionError("Cannot divide by zero.")

	if operator == "+":
		return a + b
	if operator == "-":
		return a - b
	if operator == "*":
		return a * b
	if operator == "/":
		return a / b
	if operator == "//":
		return a // b
	if operator == "%":
		return a % b
	return a ** b


try:
	a = float(input("Enter the first number: "))
	operator = input("Enter an operator (+, -, *, /, //, %, **): ").strip()
	b = float(input("Enter the second number: "))
	print(f"Result: {calculate(a, operator, b)}")
except (ValueError, ZeroDivisionError) as error:
	print(f"Error: {error}")