
import datetime

# ===========================================

# 📜 On the Scholar's Path - Chamber 1


# The Scholar's Tablet: Grade Converter
# This challenge is worth 6 points.

# Write a function called to_letter_grade(score) that
# - Accepts a number from 0 to 100
# - Returns "A", "B", "C", "D", or "F" depending on the score range


def to_letter_grade(score):
    # Your code here
    pass


# Sample calls (uncomment to test your code):
print(to_letter_grade(95))   # "A"
print(to_letter_grade(82))   # "B"
print(to_letter_grade(67))   # "D"
print(to_letter_grade(45))   # "F"


# ===========================================

# 📜 On the Scholar's Path - Chamber 2


# The Age Seal: Can You Vote?
# This challenge is worth 3 points.

# Write a function called can_vote(age) that
# - Accepts an age as a number
# - Returns True if age is 18 or greater
# - Returns False otherwise

def can_vote(age):
    # Your code here
    pass

# Sample calls (uncomment to test your code):
# print(can_vote(20))   # True
# print(can_vote(18))   # True
# print(can_vote(16))   # False


# ===========================================


# The Weather Dial
# This challenge is worth 6 points.

# Write a function called check_weather(temp) that
# - Accepts a number temperature
# - Returns "cold", "mild", or "hot" based on ranges you define

def check_weather(temp):
    # Your code here
    pass

# Sample calls (uncomment to test your code):
# Note: assumes ranges: cold ≤10, mild 11–25, hot >25)
# print(check_weather(5))     # "cold"
# print(check_weather(18))    # "mild"
# print(check_weather(32))    # "hot"


# ===========================================


# The Echo Chamber: Repeat That Word
# This challenge is worth 9 points.


# Write a function called repeat_word(word, n) that
# - Accepts a string (word) and a positive number (n)
# - Returns an empty string ("") if n is less than or equal to 0
# - Otherwise, returns the word repeated n times, separated by spaces
# Example: repeat_word("hi", 3) → "hi hi hi"

def repeat_word(word, n):
    # Your code here
    pass

# Sample calls (uncomment to test your code):
# print(repeat_word("hi", 3))         # "hi hi hi"
# print(repeat_word("echo", 5))       # "echo echo echo echo echo"
# print(repeat_word("Python", 1))     # "Python"


# ===========================================

# 📜 On the Scholar's Path - Chamber 3


# The Day-Wheel: Weekend or Weekday
# This challenge is worth 6 points.


# Write a function called get_day_type(date_str) that
# - Returns "weekday" or "weekend"


def get_day_type(date_str):
    # Starter scaffolding:
    # Note: datetime import is located at top of script file
    # Creates a datetime object from the string
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d")

    """
    You notice a poem written on the wall:
      "The datetime object tells the way,
       With weekday() you’ll see the day.
       From 0 for Monday to 6 for Sunday,
       print the date's weekday() to find your way."
    """

    # Your code here
    # TODO: Use if/else to return "weekend" if day is Saturday (5) or Sunday (6),
    # and otherwise return "weekday".
    pass

# Sample calls (uncomment to test your code):
# print(get_day_type("2025-09-13"))   # "weekend" (Saturday)
# print(get_day_type("2025-09-14"))   # "weekend" (Sunday)
# print(get_day_type("2025-09-15"))   # "weekday" (Monday)


# ===========================================


# The Sundial Chamber: Greet by Time
# This challenge is worth 6 points.


# Write a function called greet(hour) that
# - Accepts an hour from 0 to 23
# - Returns "Good morning", "Good afternoon",
#   or "Good evening" depending on the time

def greet(hour):
    # Your code here
    pass

# Sample calls (uncomment to test your code):
# print(greet(7))     # "Good morning"
# print(greet(13))    # "Good afternoon"
# print(greet(20))    # "Good evening"


# ===========================================


# The Totem of Multiplication
# This challenge is worth 9 points.

# Write a function called multiply_all(nums) that
# - Accepts a list of numbers
# - Returns the product of all numbers
# Example: multiply_all([2, 3, 4]) → 24

def multiply_all(nums):
    total = 1  # Start with 1 because multiplying by 0 would erase everything

    # Your code here
    # TODO: Use a for loop to go through each number in nums
    # Multiply each number into total

    return total

# Sample calls:
# print(multiply_all([2, 3, 4]))     # 24
# print(multiply_all([5, 5, 5]))     # 125
# print(multiply_all([10, 1, -2]))   # -20
