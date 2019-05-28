#! python3
# Finds phone numbers & email addresses on the clipboard and paste found result back to the clipboard

import pyperclip, re


def phone_number_email_extractor(text):

    phone_regex = re.compile(r'''
                (\d{3}|\(\d{3}\))?              # area code
                (?(1)(-|\s))?                   # separator - searched for ONLY when first group is found
                (\d{3})                         # first 3 digits
                (-|\s)?                         # separator
                (\d{4})                         # last 4 digits
                (\s*(ext.|x|ext)\s*\d{2,5})?    # extension
                ''', re.VERBOSE)

    email_regex = re.compile(r'''
                ([a-zA-Z0-9._+-]+)               # username
                (@)                              # @ symbol
                ([a-z0-9-]+ )                    # domain name
                (\.[a-z]{2,4})                   # dot and top-level domain
                (\.[a-z]{2,4})?                  # dot and second-level domain
                ''', re.VERBOSE)

    matches = []

    for group in re.findall(phone_regex, text):
        phone_number = ""
        if group[0] != "":
            phone_number = group[0] + "-"
        phone_number += '-'.join([group[2], group[4]]) + group[5]
        matches.append(phone_number)

    for group in re.findall(email_regex, text):
        email = "".join([group[0], group[1], group[2], group[3], group[4]])
        matches.append(email)

    result_count = len(matches)
    result = '\n'.join(matches) # join list values into string to insert it into clipboard
    return result_count, result


# insert text into clipboard
pyperclip.copy(
    "800-420-7240, (123)456 8900 and 9993334444 as well as 863-9900 are all my numbers."
    "My work number is 415 863 9950 ext. 3456 or 888-420-7240."
    "As for the email, write me at my_email@dragon-post.com, my+email@dragon.fire.com or my@ok.ua."
)

# insert text from clipboard into a variable
text = pyperclip.paste()

# execute extractor
result_count, result = phone_number_email_extractor(text)

# insert resulted phone and emails into clipboard
if result_count > 0:
    pyperclip.copy(result)
    print(f"{result_count} results are copied to the clipboard: \n{result}")
else:
    print("No phone numbers or emails found")

