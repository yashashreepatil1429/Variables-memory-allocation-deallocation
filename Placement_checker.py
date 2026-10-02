def check_placement(age, marks, attendance_percentage, experience, has_backlog):
	if experience < 0:
		raise ValueError("Experience cannot be negative.")

	placement_eligible = (
		age >= 18
		and marks >= 60
		and attendance_percentage >= 75
		and not has_backlog
	)

	if experience == 0:
		category = "Fresher"
	elif experience >= 2:
		category = "Experienced"
	else:
		category = "Junior"

	return placement_eligible, category


try:
	age = int(input("Enter age: "))
	marks = float(input("Enter marks: "))
	attendance_percentage = float(input("Enter attendance percentage: "))
	experience = float(input("Enter years of experience: "))
	backlog_response = input("Does the student have a backlog? (yes/no): ").strip().lower()

	if backlog_response not in ("yes", "no"):
		print("Please enter yes or no for backlog status.")
	else:
		has_backlog = backlog_response == "yes"
		placement_eligible, category = check_placement(
			age, marks, attendance_percentage, experience, has_backlog
		)
		eligibility = "Yes" if placement_eligible else "No"
		print(f"Placement eligible: {eligibility}")
		print(f"Candidate category: {category}")
except ValueError as error:
	print(f"Invalid input: {error}")