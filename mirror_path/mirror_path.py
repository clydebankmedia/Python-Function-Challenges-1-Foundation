
import re
import datetime

# ===========================================

# 🪩 On the Mirror Path - Chamber 1


# The Mirror Gate: Reverse the Word
# This challenge is worth 9 points.

# Write a function called reverse_word(text) that
# - Accepts a string
# - Returns the string reversed
# Example: "hello" → "olleh"


def reverse_word(text):
    # TODO: Add a for loop here.
    # Inside the loop, add each character to 'reversed_text'.
    pass


# Sample calls (uncomment to test your code):
print(reverse_word("hello"))      # "olleh"
print(reverse_word("Python"))     # "nohtyP"
print(reverse_word("racecar"))    # "racecar"

# ===========================================

# 🪩 On the Mirror Path - Chamber 2


# The Weather Dial
# This challenge is worth 6 points.

# Write a function called check_weather(temp) that
# - Accepts a number temperature
# - Returns "cold", "mild", or "hot" based on ranges you define

def check_weather(temp):
    # Your code here
    pass

# Sample calls (uncomment to test your code):
# Note: assumies ranges cold ≤10, mild 11–25, hot >25)
# print(check_weather(5))     # "cold"
# print(check_weather(18))    # "mild"
# print(check_weather(32))    # "hot"



# ===========================================


# The Day-Wheel: Weekend or Weekday
# This challenge is worth 6 points.
# Write a function called get_day_type(date_str) that
# - Returns "weekday" or "weekend"


def get_day_type(date_str):
    # Starter scaffolding:
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


# The Totem of Multiplication
# This challenge is worth 9 points.

# Write a function called multiply_all(nums) that
# - Accepts a list of numbers
# - Returns the product of all numbers
# Example: multiply_all([2, 3, 4]) → 24

def multiply_all(nums):    
    # Your code here
    # TODO: Use a for loop to go through each number in nums
    # Multiply each number into total
    pass

# Sample calls (uncomment to test your code):
# print(multiply_all([2, 3, 4]))     # 24
# print(multiply_all([5, 5, 5]))     # 125
# print(multiply_all([10, 1, -2]))   # -20






# ===========================================

# 🪩 On the Mirror Path - Secret Chamber 


# The Cipher Beyond: Password Strength
# This challenge is worth 12 points.

# Write a function called check_password_strength(password) that
# - Accepts a string
# - Returns "weak", "medium", or "strong" based on these rules:
#   * "weak" → fewer than 6 characters
#   * "medium" → at least 6 characters with letters and numbers
#   * "strong" → at least 8 characters, letters, numbers, and a special symbol


def check_password_strength(password):
    # Regular expression (regex) to detect special symbols
    special_char_regex = r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?~]"
    # Regex to detect any digit (0-9)
    number_regex = r"\d"
    # Regex to detect any uppercase or lowercase letter
    letter_regex = r"[a-zA-Z]"

  # Flag that determines if password includes a special symbol.
    # This line uses re.search() to check the password against the
    # special character regex.
    # You’ll need to use the same re.search() method to check it against
    # the number and letter patterns as well.
    # Check the result by using print(has_special_symbol).
    has_special_symbol = re.search(special_char_regex, password)

    # Your code here
    # TODO: Use similar checks for numbers and letters
    # Then use if/elif logic to return "weak", "medium", or "strong"
    pass


# Sample calls (uncomment to test your code):
# print(check_password_strength("abc"))         # "weak"
# print(check_password_strength("abc123"))      # "medium"
# print(check_password_strength("Abc123!@"))    # "strong"
