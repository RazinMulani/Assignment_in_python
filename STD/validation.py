# Validation.py

import re ## regular expration module, use for email validation

#functions

def is_empty(value):

    value = value.strip() # Remove Spaces From Begining To End

    # If Nothing remain the field is empty
    if value == "":
        return True

    return False


# Valid Name
def valid_name(name):
    # Remove Space From The Name
    name = name.replace(" ","")

    # Check Wether Every Characters is an aplhabet
    if name.isalpha():
        return True
    return False

# Valid Age
def valid_age(age):
    # Check If Age Contains Only Degate
    if age.isdigit():
        age = int(age)

        # chack age range
        if age >= 1 and age <= 100:
            return True

    return False


# Valid Phone Number
def valid_phone(phone):
    # Check If Phone Contain Only Numbers
    if phone.isdigit():
        #phone = int(phone)

        #Check Phone Lenbth
        if len(phone) == 10:
            return True

    return False

# Valid Mail

def valid_email(email):
    # regular expression module
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    # Match Email With Pattern
    if re.match(pattern, email):
        return True
    return False













