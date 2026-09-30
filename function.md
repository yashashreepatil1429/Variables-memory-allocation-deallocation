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
