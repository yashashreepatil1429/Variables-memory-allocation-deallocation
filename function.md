# Python Functions
## 1. Why use functions?

**Answer:** Functions let you reuse code instead of repeating the same instructions. They make programs easier to organize, test, read, and maintain.

```python
def welcome(name):
	print("Welcome,", name)


welcome("Yashashree")
welcome("Riya")
```

## 2. What is a function?

**Answer:** A function is a named, reusable block of code that performs a task. It can accept input and return a result.

```python
def add(first, second):
	return first + second


print(add(2, 3))
```

## 3. What is the difference between defining and calling a function?

**Answer:** Defining a function describes its behavior. Calling it runs its body.

```python
def greet():
	print("Hello")


greet()  # Call the function.
```

## 4. Can a function have no parameters?

**Answer:** Yes. A function needs no parameters when it does not need information from its caller.

```python
def welcome():
	print("Welcome to nighan2 labs")


welcome()
```

## 5. What are parameters and arguments?

**Answer:** A parameter is a name in a function definition. An argument is the value passed to that parameter when the function is called.

```python
def welcome(name):  # name is a parameter
	print("Welcome,", name)


welcome("Yashashree")  # "Yashashree" is an argument
```

## 6. Can a function have multiple parameters?

**Answer:** Yes. Separate parameters with commas, then provide a matching argument for each one.

```python
def add(first, second):
	return first + second


print(add(10, 20))
```

## 7. What is the difference between `print()` and `return`?

**Answer:** `print()` displays information. `return` sends a value back to the caller so the program can store or use it.

```python
def add(first, second):
	return first + second


result = add(10, 20)
print(result)
```

## 8. What happens after a `return` statement?

**Answer:** `return` immediately ends that function call. Statements after it in the same call do not run.

```python
def get_number():
	return 10
	print("This line does not run")


print(get_number())
```

## 9. Can a function return more than one value?

**Answer:** Yes. Python groups comma-separated return values into a tuple. The caller can unpack the tuple into variables.

```python
def calculate(first, second):
	return first + second, first - second


sum_result, difference = calculate(10, 5)
print(sum_result)
print(difference)
```

## 10. What is a default parameter?

**Answer:** A default parameter has a value used when the caller leaves out that argument.

```python
def greet(name="Yashashree"):
	print("Hello,", name)


greet()
greet("Riya")
```

## 11. What is a positional argument?

**Answer:** A positional argument is matched to a parameter by its position in the call.

```python
def show_student(name, age):
	print(name, age)


show_student("Yashashree", 21)
```

## 12. What is a keyword argument?

**Answer:** A keyword argument names the parameter it supplies, so keyword arguments can be given in a different order.

```python
def show_student(name, age):
	print(name, age)


show_student(age=21, name="Yashashree")
```

## 13. Can positional and keyword arguments be combined?

**Answer:** Yes. Positional arguments must come before keyword arguments.

```python
def show_student(name, age, course):
	print(name, age, course)


show_student("Yashashree", 21, course="BCA")
show_student(name="Yashashree", age=21, course="BCA")
```

## 14. What does `*args` do?

**Answer:** `*args` collects any extra positional arguments into a tuple.

```python
def add_all(*numbers):
	total = 0
	for number in numbers:
		total += number
	return total


print(add_all(10, 20))
print(add_all(1, 2, 3, 4, 5))
```

## 15. What does `**kwargs` do?

**Answer:** `**kwargs` collects any extra keyword arguments into a dictionary.

```python
def show_details(**details):
	print(details)


show_details(name="Sanika", age=21, course="BCA")
```

## 16. How can parameter types be combined?

**Answer:** Required parameters come first, followed by optional parameters, `*args`, and then `**kwargs`.

```python
def example(required, optional=10, *args, **kwargs):
	return required, optional, args, kwargs
```

## 17. What is local and global scope?

**Answer:** A local variable is created inside a function and is available there. A global variable is defined outside functions and can be read inside them.

```python
message = "Hello"


def show_message():
	local_message = "Welcome"
	print(message)
	print(local_message)


show_message()
```

## 18. What does the `global` keyword do?

**Answer:** `global` tells Python that an assignment inside a function should reassign a variable defined at module scope. Avoid global state when parameters and return values can do the job.

```python
count = 0


def increment():
	global count
	count += 1


increment()
print(count)  # 1
```

## 19. Can a local variable be used outside its function?

**Answer:** No. A local variable is limited to its function. Referencing it outside that function raises `NameError`.

```python
def create_value():
	local_value = 10


create_value()
# print(local_value)  # NameError: local_value is not defined here.
```

## 20. Can functions call other functions?

**Answer:** Yes. Calling smaller functions from another function helps divide a larger task into clear steps.

```python
def add(first, second):
	return first + second


def display_sum():
	result = add(10, 20)
	print(result)


display_sum()
```

A program might call functions in this order: `main()` -> `validate()` -> `calculate()` -> `save()`.

## 21. What happens when a function is called?

**Answer:** Python matches arguments to parameters, runs the function body, and sends the returned value back to the caller.

```python
def multiply(first, second):
	return first * second


result = multiply(5, 4)
print(result)  # 20
```

## 22. Are functions objects in Python?

**Answer:** Yes. A function can be assigned to another variable, and that variable can be used to call the same function.

```python
def greet():
	print("Hello")


greet_alias = greet
greet_alias()
```

## 23. Can a function be passed to another function?

**Answer:** Yes. A function that accepts or returns another function is called a higher-order function.

```python
def square(number):
	return number * number


def process(operation, value):
	return operation(value)


print(process(square, 5))  # 25
```

## 24. What is a lambda function?

**Answer:** A lambda is a small anonymous function containing a single expression. Use `def` for functions that need a name or multiple statements.

```python
double = lambda number: number * 2
print(double(4))
```

For example, `map()` applies a function to each item in an iterable:

```python
numbers = [1, 2, 3, 4]
doubled = list(map(lambda number: number * 2, numbers))
print(doubled)  # [2, 4, 6, 8]
```

## 25. What is recursion?

**Answer:** Recursion happens when a function calls itself. A base case stops the calls from continuing indefinitely.

```python
def countdown(number):
	if number <= 0:  # Base case
		return

	print(number)
	countdown(number - 1)


countdown(5)
```

## 26. What is a function docstring?

**Answer:** A docstring is a string at the start of a function that describes its purpose. Tools such as `help()` can display it.

```python
def add(first, second):
	"""Return the sum of two numbers."""
	return first + second


print(add.__doc__)
```

## 27. What are type hints?

**Answer:** Type hints document the types a function expects and returns. Python does not generally enforce them at runtime.

```python
def add(first: int, second: int) -> int:
	return first + second
```

## 28. How can functions be used in a practical program?

**Answer:** Put a focused calculation in a function, then call it from the part of the program that handles input and output.

```python
def calculate_bill(units):
	if units <= 100:
		amount = units * 2
	elif units <= 200:
		amount = 100 * 2 + (units - 100) * 4
	else:
		amount = 100 * 2 + 100 * 4 + (units - 200) * 6

	return amount + 100


units = int(input("Enter units: "))
print("Bill:", calculate_bill(units))
```

## 29. What makes a function well-designed?

**Answer:** A well-designed function has a clear name, focused responsibility, understandable inputs, and a useful result. Small functions are easier to test and reuse.

## 30. Why should giant functions be avoided?

**Answer:** A function that handles many unrelated tasks is difficult to understand, test, and maintain. Split the work into smaller functions with clear responsibilities.

```python
def get_student():
	"""Get student information."""
	pass


def validate_student(student):
	"""Check that student information is valid."""
	pass


def calculate_result(student):
	"""Calculate the student's result."""
	pass


def save_student(student):
	"""Save the student information."""
	pass


def display_student(student):
	"""Display the student information."""
	pass
```

Each function above has one main responsibility, making the program easier to read, test, and maintain.


