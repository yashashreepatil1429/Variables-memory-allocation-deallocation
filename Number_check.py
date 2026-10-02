def check_number(number):
	return {
		"even or odd": "Even" if number % 2 == 0 else "Odd",
		"divisible by 3": number % 3 == 0,
		"divisible by 5": number % 5 == 0,
	}


number = int(input("Enter an integer: "))
results = check_number(number)

print(f"{number} is {results['even or odd']}.")
print(f"Divisible by 3: {results['divisible by 3']}")
print(f"Divisible by 5: {results['divisible by 5']}")