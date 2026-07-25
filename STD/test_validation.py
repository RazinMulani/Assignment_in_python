#test_validation.py

# Import all validation functions
from validation import *


print("----- Empty Validation -----")

print(is_empty(""))            # True
print(is_empty("Python"))      # False


print("\n----- Name Validation -----")

print(valid_name("Razin"))          # True
print(valid_name("Razin Mulani"))   # True
print(valid_name("Razin123"))       # False


print("\n----- Age Validation -----")

print(valid_age("22"))         # True
print(valid_age("150"))        # False


print("\n----- Phone Validation -----")

print(valid_phone("9876543210"))    # True
print(valid_phone("98765"))         # False


print("\n----- Email Validation -----")

print(valid_email("abc@gmail.com"))     # True
print(valid_email("abcgmail.com"))      # False
