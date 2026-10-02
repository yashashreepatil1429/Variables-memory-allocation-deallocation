def check_marks(marks):
	if marks >= 75:
		return "Distinction"
	if marks >= 5:
		return "Pass"
	return "Fail"


marks = float(input("Enter the student's marks: "))
print(check_marks(marks))