# Python Functions

## 1. Why use functions?

Without a function, the same instructions may need to be repeated:

```python
print("Yashashree")
print("Riya")
print("Priya")
```

A function lets us reuse the same behavior with different values:

```python
def welcome(name):
	print("Welcome,", name)


welcome("Yashashree")
welcome("Riya")
welcome("Priya")
```

Functions support code reuse, reduce repetition, improve organization, and make programs easier to maintain and test.

## 2. What is a function?

A function is a reusable block of code that performs a specific task.

```python
def add(a, b):
	return a + b


print(add(2, 3))
```

## 3. Defining vs. calling a function

Defining a function describes what it does. The body does not run until the function is called.

```python
def greet():
	print("Hello")


greet()
```

`greet()` is the function call. It runs the function body.

## 4. A function without parameters

A function does not need parameters if it does not need input from its caller.

```python
def welcome():
	print("Welcome to nighan2 labs")


welcome()
```

## 5. Functions with parameters

A parameter is a name listed in the function definition. An argument is a value passed to the function.

```python
def welcome(name):
	print("Welcome,", name)


welcome("Yashashree")
```

Here, `name` is the parameter and `"Yashashree"` is the argument.

## 6. Multiple parameters

A function can accept more than one parameter:

```python
def add(a, b):
	print(a + b)


add(10, 20)
```

## 7. `print()` vs. `return`

`print()` displays a value. `return` sends a value back to the caller so it can be stored or used elsewhere.

```python
def add(a, b):
	return a + b


result = add(10, 20)
print(result)
```

## 8. What happens after `return`?

`return` ends the current function call. Statements after it in that call are not executed.

```python
def test():
	return 10
	print("This line does not run")


print(test())
```

## 9. Returning multiple values

Python returns multiple comma-separated values as a tuple. The caller can unpack them into separate variables.

```python
def calculate(a, b):
	return a + b, a - b, a * b


sum_result, difference, product = calculate(10, 5)
print(sum_result)
print(difference)
print(product)
```

## 10. Default parameters

A default parameter value is used when the caller does not provide that argument.

```python
def greet(name="Yashashree"):
	print("Hello,", name)


greet()
greet("Riya")
```

Default values are useful when a function has a common or optional value.

## 11. Positional arguments

Positional arguments are matched to parameters by their order.

```python
def student(name, age):
	print(name, age)


student("Yashashree", 21)
```

## 12. Keyword arguments

Keyword arguments are matched by parameter name, so their order does not matter.

```python
def student(name, age):
	print(name, age)


student(age=21, name="Yashashree")
```

## 13. Positional and keyword arguments together

Positional arguments can come before keyword arguments:

```python
def student(name, age, course):
	print(name, age, course)


student("Yashashree", 21, course="BCA")
student(name="Yashashree", age=21, course="BCA")
```

A positional argument cannot follow a keyword argument:

```python
# Invalid: positional argument follows a keyword argument.
# student(name="Yashashree", 21, course="BCA")
```

## 14. `*args`

`*args` collects any extra positional arguments into a tuple.

```python
def add(*numbers):
	total = 0
	for number in numbers:
		total += number
	return total


print(add(10, 20))
print(add(10, 20, 30))
print(add(1, 2, 3, 4, 5))
```

## 15. `**kwargs`

`**kwargs` collects extra keyword arguments into a dictionary.

```python
def show_student(**details):
	print(details)


show_student(name="Sanika", age=21, course="BCA")
```

## 16. Combining parameter types

A function can combine required parameters, a default parameter, `*args`, and `**kwargs` in this order:

```python
def example(a, b=10, *args, **kwargs):
	return a, b, args, kwargs
```

## 17. Local and global scope

A local variable is created inside a function and is available there:

```python
def test():
	x = 10
	print(x)


test()
```

A function can read a global variable defined outside the function:

```python
x = 100


def show_x():
	print(x)


show_x()
```

## 18. The `global` keyword

The `global` keyword lets a function reassign a variable defined at module scope.

```python
count = 0


def increment():
	global count
	count += 1


increment()
print(count)
```

Avoid global state when possible. Parameters and return values usually make functions easier to reuse and test.

## 19. A local name is not available outside its function

Trying to access a local variable outside the function raises `NameError`:

```python
def test():
	x = 10


test()
print(x)  # Raises NameError: x is local to test().
```

## 20. Functions can call other functions

Functions can be combined to break a larger task into smaller steps:

```python
def add(a, b):
	return a + b


def display():
	result = add(10, 20)
	print(result)


display()
```

A program's flow might look like this:

```text
main() -> validate() -> calculate() -> save() -> display()
```
## 21. Function calling flow

When Python reaches a function call, it passes the arguments to the function’s parameters, runs the function body, and returns the result to the caller.

```python
def multiply(a, b):
    return a * b


result = multiply(5, 4)
print(result)
```

Python passes `5` and `4` to `a` and `b`. The function returns `20`, which is assigned to `result`.

## 22. Functions are objects

Functions are objects in Python. You can assign a function to another variable and call it through that variable.

```python
def greet():
    print("Hello")


x = greet
x()
```

`x` refers to the same function object as `greet`.

## 23. Passing a function to another function

A function can be passed as an argument to another function. A function that accepts or returns another function is called a **higher-order function**.

```python
def square(x):
    return x * x


def process(function, value):
    return function(value)


print(process(square, 5))
```

`process` receives `square` as an argument and calls it with `5`.

## 24. Lambda functions

A lambda is a small anonymous function, often used for a simple operation.

```python
square = lambda x: x * x
print(square(5))
```

A lambda can also be used with `map()` to transform each item in a list:

```python
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)
```

This prints `[2, 4, 6, 8]`.

## 25. Recursion

A recursive function calls itself. It needs a **base case** to stop the recursion.

```python
def countdown(n):
    if n <= 0:
        return

    print(n)
    countdown(n - 1)


countdown(5)
```

The base case stops the function when `n` reaches `0` or less.

## 26. Function documentation

A docstring describes what a function does. It should be the first statement inside the function.

```python
def add(a, b):
    """Return the sum of two numbers."""
    return a + b


print(add.__doc__)
```

Docstrings help developers understand and use functions.

## 27. Type hints

Type hints communicate intended types to developers and tools. Python generally does not enforce them automatically at runtime.

```python
def add(a: int, b: int) -> int:
    return a + b
```

This indicates that `a` and `b` are expected to be integers and that the function is expected to return an integer.

## 28. A practical program: electricity bill

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
bill = calculate_bill(units)
print("Bill:", bill)
```

The `calculate_bill()` function separates the billing calculation from input and output. This makes the calculation easier to reuse, test, read, and maintain.

## 29. Function design

A well-designed function has clear inputs, performs a focused task, and produces an output. Its name and behavior should make its purpose easy to understand.

## 30. Avoid giant functions

A function that handles many unrelated tasks is difficult to understand and maintain. Break it into smaller functions with clear responsibilities.

For example, a student program could use functions like these:

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

Each function has a focused responsibility. This applies the **single-responsibility principle** to functions without requiring a class. Focused functions improve readability, testing, and maintenance.


   