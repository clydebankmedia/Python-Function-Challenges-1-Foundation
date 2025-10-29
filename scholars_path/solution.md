# 📜 The Scholar's Path Solution Code

<details><summary>The Scholar's Tablet</summary>

```python
"""
Function: to_letter_grade(score)
Purpose: Convert a numeric score (0–100) to a letter grade.

Input:
  - score: a number between 0 and 100
Output:
  - "A", "B", "C", "D", or "F"

Note:
  Works by checking score ranges in order using if/elif.
  The first true condition runs, and the rest are skipped.
"""

def to_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
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



<details><summary>The Totem of Multiplication</summary>

```python
"""
Function: multiply_all(nums)
Purpose: Multiply all numbers inside a list.

Input:
  - nums: a list of numbers (e.g., [2, 3, 4])
Output:
  - The product of all numbers

Note:
  Lists start counting at index 0.
  A for loop visits each value, multiplying it into 'total'.
"""

def multiply_all(nums):
    total = 1
    for num in nums:
        total = total * num
    return total

# Optional (More Pythonic):
# from math import prod
# def multiply_all(nums):
#     return prod(nums)

```
</details>




