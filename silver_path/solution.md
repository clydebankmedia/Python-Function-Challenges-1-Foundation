# 🧭 The Silver Path Solution Code


<details><summary>The Silver Lock</summary>

```python
"""
Function: is_even(num)
Purpose: Determine if a number is even or odd.

Input:
  - num: a number (e.g. 4, 7, 0)
Output:
  - True if num is even
  - False if num is odd

Note:
  Uses the modulus operator (%) which returns the remainder of division.
  Example: 4 % 2 = 0 → even; 5 % 2 = 1 → odd
"""

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

# Optional (More Pythonic):
# def is_even(num):
#     return num % 2 == 0
```
</details>



<details><summary>The Age Seal</summary>

```python
"""
Function: can_vote(age)
Purpose: Check if a person is old enough to vote.

Input:
  - age: a number representing years
Output:
  - True if age is 18 or older
  - False otherwise
"""

def can_vote(age):
    if age >= 18:
        return True
    else:
        return False

# Optional (More Pythonic):
# def can_vote(age):
#     return age >= 18
```
</details>



<details><summary>The Sundial Chamber</summary>

```python
"""
Function: check_weather(temp)
Purpose: Return a weather description based on temperature.

Input:
  - temp: a number (degrees)
Output:
  - "cold" if 10 or below
  - "mild" if between 11 and 25
  - "hot" if 26 or above

Note:
  Order matters — the first matching condition stops the rest from running.
"""

def check_weather(temp):
    if temp <= 10:
        return "cold"
    elif temp <= 25:
        return "mild"
    else:
        return "hot"

```
</details>



<details><summary>The Weather Dial</summary>

```python
"""
Function: check_weather(temp)
Purpose: Return a weather description based on temperature.

Input:
  - temp: a number (degrees)
Output:
  - "cold" if 10 or below
  - "mild" if between 11 and 25
  - "hot" if 26 or above

Note:
  Order matters — the first matching condition stops the rest from running.
"""

def check_weather(temp):
    if temp <= 10:
        return "cold"
    elif temp <= 25:
        return "mild"
    else:
        return "hot"

```
</details>



<details><summary>The Balance Scale</summary>

```python
# The Balance Scale
# Write a function called compare_weights(a, b) that
# - Accepts two numbers, a and b
# - Returns "equal", "left heavier", or "right heavier"

def compare_weights(a, b):
    if a == b:
        return "equal"
    elif a > b:
        return "left heavier"
    else:
        return "right heavier"

# Sample calls:
print(compare_weights(5, 5))   # "equal"
print(compare_weights(7, 3))   # "left heavier"
print(compare_weights(2, 9))   # "right heavier"
```
</details>



<details><summary>The Day-Wheel</summary>

```python
"""
Function: get_day_type(date_str)
Purpose: Tell whether a given date is a weekend or weekday.

Input:
  - date_str: a date string (like "2025-09-13")
Output:
  - "weekend" if Saturday (6) or Sunday (0)
  - "weekday" otherwise

Note:
  datetime.date() creates a date object.
  The weekday() method returns 0–6 for Monday–Sunday, so we adjust to match.
"""

import datetime

def get_day_type(date_str):
    date = datetime.date.fromisoformat(date_str)  # "YYYY-MM-DD"
    day = date.weekday()  # Monday=0, Sunday=6
    if day in (5, 6):
        return "weekend"
    else:
        return "weekday"

```
</details>



<details><summary>The Truth Stone</summary>

```python
# The Truth Stone
# Write a function called check_truth(a, b) that
# - Accepts two boolean values (True or False)
# - Returns "both true" if both values are true
# - Returns "one true" if only one is true
# - Returns "none true" if both are false

def check_truth(a, b):
    # Your code here
    pass

# Sample calls:
check_truth(True, True)     # "both true"
check_truth(True, False)    # "one true"
check_truth(False, False)   # "none true"
```
</details>



<details><summary>The Echo Chamber</summary>

```python
"""
Function: repeat_word(word, n)
Purpose: Repeat a word n times, separated by spaces.

Input:
  - word: a string
  - n: a positive number
Output:
  - A single string with the word repeated n times

Note:
  Shows how to use loops to build a string step-by-step.
  Adds a space between each word except the first.
"""

def repeat_word(word, n):
    if n <= 0:
        return ""
    result = ""
    for i in range(1, n + 1):
        if i > 1:
            result = result + " "
        result = result + word
    return result

# Optional (More Pythonic):
# def repeat_word(word, n):
#     if n <= 0:
#         return ""
#     return " ".join([word] * n)

```
</details>