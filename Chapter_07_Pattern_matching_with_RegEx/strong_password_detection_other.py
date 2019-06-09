# Another solution to strong_password_detection.py task

import re


def strong_password_detection(password):
    if not 20>=len(password)>=8:
        return None

    password_regex_lowercase = re.search(r"[a-z]+", password)
    password_regex_uppercase = re.search(r"[A-Z]+", password)
    password_regex_number = re.search(r"[0-9]+", password)

    try:
        password_regex_lowercase.group()
        password_regex_uppercase.group()
        password_regex_number.group()
        return True
    except AttributeError:
        return False


password = "Q12werty"
strong_password_detection(password)

# working with results
if strong_password_detection(password) is True:
    print("The password is strong")
elif strong_password_detection(password) is False:
    print("The password is weak")
else:
    print("Password length must be between 8 and 20 characters")
