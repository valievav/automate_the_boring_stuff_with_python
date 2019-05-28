import re

text = "355-645-6968"
phone_number = re.search(r'^\d{3}-\d{3}-\d{4}$', text)

if phone_number:
    print(f"{text} is a phone number: True")
else:
    print(f"{text} is a phone number: False")
