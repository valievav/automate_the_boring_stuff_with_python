import re
import random
import string

# storing generated passwords
passwords = []

# generating random valid and invalid passwords
def valid_password(length):
    p = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    passwords.append(p)

def invalid_password_lower_letter_number(length):
    p = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    passwords.append(p)

def invalid_password_upper_letter_number(length):
    p = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    passwords.append(p)

def invalid_password_no_number(length):
    p = ''.join(random.choices(string.ascii_letters, k=length))
    passwords.append(p)

# populating passwords list
valid_password(8)
valid_password(9)
invalid_password_lower_letter_number(3)
invalid_password_upper_letter_number(8)
invalid_password_no_number(12)

# selecting password
user_password = random.choice(passwords)

# validating password against rules
def password_length(password):
    if len(password) < 7:
        return False
    else:
        return True

def lowercase_letter(password):
    if re.search(r"[a-z]", password) is None:
        return False
    else:
        return True

def uppercase(password):
    if re.search(r"[A-Z]", password) is None:
        return False
    else:
        return True

def digits(password):
    if re.search(r"[0-9]", password) is None:
        return False
    else:
        return True

# validation on meeting all the requirements
def password_validator(password):
    if password_length(password) is True \
            and lowercase_letter(password) is True \
            and uppercase(password) is True \
            and digits(password) is True:
        print(f"{user_password} is valid password")
        return password # added this line because it returned None with value
    else:
        print(f"{user_password} is NOT a valid password")
        return password # added this line because it returned None with value

password_validator(user_password)


