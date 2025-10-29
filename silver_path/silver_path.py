import datetime

# ===========================================


# 🧭 On the Mirror Path - Chamber 1

# The Silver Lock: Even or Odd
# This challenge is worth 3 points.

# Write a function called is_even(num) that
# - Returns True if the number is even
# - Returns False if the number is odd

def is_even(num):
    # Your code here
    pass


# Sample calls:
print(is_even(4))   # True
print(is_even(7))   # False
print(is_even(0))   # True


# ===========================================

# 🧭 On the Mirror Path - Chamber 2


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
# print(greet(9))     # "Good morning"
# print(greet(15))    # "Good afternoon"
# print(greet(21))    # "Good evening"


# ===========================================


# The Weather Dial
# This challenge is worth 6 points.

# Write a function called check_weather(temp) that
# - Accepts a number temperature
# - Returns "cold", "mild", or "hot" based on ranges you define


def check_weather(temp):
    # Your code here
    pass


# Sample calls (assuming ranges: cold ≤10, mild 11–25, hot >25):
# Note: uncomment to test your code
# print(check_weather(5))     # "cold"
# print(check_weather(18))    # "mild"
# print(check_weather(32))    # "hot"


# ===========================================

# 🧭 On the Mirror Path - Chamber 3


# The Gem Counter
# This challenge is worth 3 points.

# Write a function called count_gems(n) that
# - Accepts a number n
# - Uses a for loop to add numbers from 1 to n
# - Returns the total sum


def count_gems(n):
    # Your code here
    pass


# Sample calls (uncomment to test your code):
# print(count_gems(3))   # 6   (1 + 2 + 3)
# print(count_gems(5))   # 15  (1 + 2 + 3 + 4 + 5)
# print(count_gems(1))   # 1


# ===========================================


# The Balance Scale
# This challenge is worth 6 points.

# Write a function called compare_weights(a, b) that
# - Accepts two numbers, a and b
# - Returns "equal", "left heavier", or "right heavier"


def compare_weights(a, b):
    # Your code here
    pass


# Sample calls (uncomment to test your code):
# print(compare_weights(5, 5))   # "equal"
# print(compare_weights(7, 3))   # "left heavier"
# print(compare_weights(2, 9))   # "right heavier"


# ===========================================


# The Day-Wheel: Weekend or Weekday
# This challenge is worth 6 points.

# Write a function called get_day_type(date_str) that
# - Returns "weekday" or "weekend"


def get_day_type(date_str):
    # Starter scaffolding:
    # Note: datetime is imported at the top of this file
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

# 🧭 On the Mirror Path - Chamber 4


# The Truth Stone
# This challenge is worth 6 points.

# Write a function called check_truth(a, b) that
# - Accepts two boolean values (True or False)
# - Returns "both true" if both values are true
# - Returns "one true" if only one is true
# - Returns "none true" if both are false


def check_truth(a, b):
    # Your code here
    pass


# Sample calls (uncomment to test your code):
# check_truth(True, True)     # "both true"
# check_truth(True, False)    # "one true"
# check_truth(False, False)   # "none true"


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
# print(repeat_word("hi", 3))        # "hi hi hi"
# print(repeat_word("echo", 5))      # "echo echo echo echo echo"
# print(repeat_word("Python", 1))    # "Python"
