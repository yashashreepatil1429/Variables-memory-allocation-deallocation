def is_valid_user(username, password):
	return username == "admin" and password == "python123"


username = input("Enter username: ")
password = input("Enter password: ")

if is_valid_user(username, password):
	print("Valid user")
else:
	print("Invalid user")