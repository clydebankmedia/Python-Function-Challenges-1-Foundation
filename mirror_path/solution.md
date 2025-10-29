# 🪩 The Mirror Path Solution Code

<details><summary>The Mirror Gate</summary>

```python
"""
Function: reverse_word(s)
Purpose: Reverse the letters in a string.

Input:
  - s: a word (string)
Output:
  - the same word, but reversed

Note:
  Uses a for loop that counts backwards (from end to start).
  This can be tricky! Start at len(s) - 1 and decrease by 1 each time until i reaches 0 (the first letter).
"""

def reverse_word(s):
    reversed_word = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_word = reversed_word + s[i]
    return reversed_word

# Optional (More Pythonic):
# def reverse_word(s):
#     return s[::-1]
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

<details><summary>The Secret Chamber</summary>


</details>