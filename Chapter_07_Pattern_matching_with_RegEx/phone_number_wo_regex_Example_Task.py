def is_phone_number(text):
    if len(text) != 12:
        return False
    if not text[0:3].isdecimal():
        return False
    if not text[3] == '-':
        return False
    if not text[4:7].isdecimal():
        return False
    if not text[7] == '-':
        return False
    if not text[8:12].isdecimal():
        return False
    return True

test_text = "355-345-6968"
print(f"{test_text} is a phone number: " + str(is_phone_number(test_text)))

