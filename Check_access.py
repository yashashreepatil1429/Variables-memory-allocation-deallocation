def check_access(age, has_id, is_employee):
	if (age >= 18 and has_id) or is_employee:
		return "Access granted"
	return "Access denied"


age = int(input("Enter age: "))
has_id_response = input("Do you have an ID? (yes/no): ").strip().lower()
employee_response = input("Are you an employee? (yes/no): ").strip().lower()

if has_id_response not in ("yes", "no") or employee_response not in ("yes", "no"):
	print("Please answer yes or no.")
else:
	has_id = has_id_response == "yes"
	is_employee = employee_response == "yes"
	print(check_access(age, has_id, is_employee))