import re
import random
import string

# storing generated passwords
passwords = []

# generating random valid and invalid passwords
def valid_pass(length):
    p = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    passwords.append(p)

def invalid_pass_lower_letter_digit(length):
    p = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    passwords.append(p)

def invalid_pass_upper_letter_digit(length):
    p = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    passwords.append(p)

def invalid_pass_no_digit(length):
    p = ''.join(random.choices(string.ascii_letters, k=length))
    passwords.append(p)

# populating passwords list
valid_pass(8)
valid_pass(11)
invalid_pass_lower_letter_digit(3)
invalid_pass_upper_letter_digit(8)
invalid_pass_no_digit(9)

# selecting password
user_password = random.choice(passwords)

# regex rules
lower_letter_regex = re.compile(r"[a-z]")
upper_letter_regex = re.compile(r"[A-Z]")
digits_regex = re.compile(r"[0-9]")

# validation on meeting all the requirements
def password_validator(password):
    r = bool(len(password) > 7
                  and lower_letter_regex.search(password)
                  and upper_letter_regex.search(password)
                  and digits_regex.search(password))
    if r is True:
        print(f"{user_password} is valid password")
    else:
        print(f"{user_password} is NOT a valid password")


password_validator(user_password)


