def check_eligibility(marks, attendance_percentage, has_backlog):
	if marks >= 60 and attendance_percentage >= 75 and not has_backlog:
		return "Eligible"
	return "Not eligible"


marks = float(input("Enter the student's marks: "))
attendance_percentage = float(input("Enter attendance percentage: "))
backlog_response = input("Does the student have a backlog? (yes/no): ").strip().lower()

if backlog_response not in ("yes", "no"):
	print("Please enter yes or no for backlog status.")
else:
	has_backlog = backlog_response == "yes"
	print(check_eligibility(marks, attendance_percentage, has_backlog))