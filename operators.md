# Python Operators and Function Logic

Python operators act on values and variables. The exercises below use arithmetic, comparison, logical, membership, and conditional-expression operators.

## Operator Types

| Type | Purpose | Examples |
| --- | --- | --- |
| Arithmetic | Perform calculations | `+`, `-`, `*`, `/`, `//`, `%`, `**` |
| Assignment | Store a value in a variable | `=`, `+=`, `-=` |
| Comparison | Compare values; result is `True` or `False` | `==`, `!=`, `>`, `<`, `>=`, `<=` |
| Logical | Combine or negate conditions | `and`, `or`, `not` |
| Identity | Check whether two names refer to the same object | `is`, `is not` |
| Membership | Check whether a value occurs in a collection | `in`, `not in` |
| Bitwise | Operate on the bits of integers | `&`, `|`, `^`, `~`, `<<`, `>>` |
| Conditional expression | Choose one of two values based on a condition | `value_if_true if condition else value_if_false` |

`=` assigns a value, while `==` compares two values. Python boolean values are written `True` and `False`.

## Task 1: Arithmetic Calculator

File: [Arithmetic_operations.py](Arithmetic_operations.py)

`calculate(first, second)` returns a dictionary containing the sum, difference, product, quotient, floor quotient, and remainder. Before calculating, it checks whether the second number is zero; if so, it raises a `ValueError` because division, floor division, and remainder are undefined for a zero divisor. The main program asks for two numbers and prints each dictionary entry.

The arithmetic operators are `+`, `-`, `*`, `/`, `//`, and `%`.

## Task 2: Number Checks

File: [Number_check.py](Number_check.py)

`check_number(number)` returns a dictionary with three results:

- `number % 2 == 0` is true for an even number; otherwise the conditional expression returns `Odd`.
- `number % 3 == 0` checks divisibility by 3.
- `number % 5 == 0` checks divisibility by 5.

The `%` operator returns the remainder. A remainder of zero means the number is divisible by the divisor.

## Task 3: Marks Result

File: [Marks_checker.py](Marks_checker.py)

`check_marks(marks)` checks the highest threshold first. Marks of 75 or more return `Distinction`; otherwise, marks of 5 or more return `Pass`; all lower marks return `Fail`. Checking distinction first ensures those marks do not stop at the general pass condition.

## Task 4: Student Eligibility

File: [Student_eligibility.py](Student_eligibility.py)

`check_eligibility(marks, attendance_percentage, has_backlog)` returns `Eligible` only if all three conditions are true: marks are at least 60, attendance is at least 75%, and `has_backlog` is false. The `and` operator requires every condition to pass. The program accepts backlog status as `yes` or `no` and rejects other responses.

## Task 5: User Validation

File: [User_validation.py](User_validation.py)

`is_valid_user(username, password)` uses `and` to require both exact matches: username `admin` and password `python123`. It returns a boolean, which the main program uses to print `Valid user` or `Invalid user`.

These fixed credentials are for the exercise only. Real applications should not store or compare passwords this way.

## Task 6: Purchase Discount

File: [Discount_calculate.py](Discount_calculate.py)

`calculate_discount(purchase_amount)` selects one discount rate:

- 20% for an amount of 5000 or more.
- 10% for an amount from 3000 up to, but not including, 5000.
- 5% for an amount below 300.
- 0% for amounts from 300 up to, but not including, 3000.

It multiplies the amount by the rate to get the discount, subtracts that discount from the purchase amount, and returns both values. Negative purchase amounts raise a `ValueError`. The 300-to-2999 range is assigned no discount because the original exercise does not specify a rate for it.

## Task 7: Access Check

File: [Check_access.py](Check_access.py)

`check_access(age, has_id, is_employee)` grants access if either the person is at least 18 and has an ID, or the person is an employee. Parentheses group the `age >= 18 and has_id` condition; `or` then allows employee status to grant access independently. The function returns `Access granted` or `Access denied`.

## Task 8: Required Skills

File: [check_skill.py](check_skill.py)

The `required_skills` list contains Python, SQL, Git, and HTML. `check_skill(skill_name)` compares the input to each required skill using `casefold()`, so matching is not affected by letter case. `any()` returns true when at least one skill matches; the function then returns `Skill available`, otherwise `Skill not available`.

This uses the membership idea: checking whether an item exists in a collection. The implementation uses `any()` to perform a case-insensitive comparison.

## Task 9: Operator Calculator

File: [Calculator.py](Calculator.py)

`calculate(a, operator, b)` first checks that the operator is one of `+`, `-`, `*`, `/`, `//`, `%`, or `**`. Unsupported operators raise a `ValueError`. It also checks that `b` is not zero for `/`, `//`, and `%`, raising a `ZeroDivisionError` if it is. It then applies the selected operation and returns the result. The main program catches these errors and displays a readable message.

The `**` operator calculates exponentiation; for example, `2 ** 3` is 8.

## Task 10: Placement Eligibility and Category

File: [Placement_checker.py](Placement_checker.py)

`check_placement(age, marks, attendance_percentage, experience, has_backlog)` returns a pair: a boolean for placement eligibility and a candidate category. Eligibility requires all of the following: age is at least 18, marks are at least 60, attendance is at least 75%, and there is no backlog. These conditions are joined with `and`.

The category is determined separately from eligibility:

- Exactly 0 years of experience: `Fresher`.
- 2 or more years: `Experienced`.
- More than 0 but less than 2 years: `Junior`.

The `>= 2` rule is checked before the remaining positive experience case, so exactly 2 years is classified as `Experienced`. The age and attendance thresholds follow the assumptions used in Tasks 7 and 4; the original Task 10 statement did not specify those values explicitly. Negative experience raises a `ValueError`.

The main program converts the returned boolean to `Yes` or `No` and displays it alongside the category. A candidate's category is displayed even when they are not eligible.
