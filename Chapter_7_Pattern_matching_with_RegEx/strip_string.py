"""
Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to
strip, then whitespace characters will be removed from the beginning and
end of the string. Otherwise, the characters specified in the second argument
to the function will be removed from the string.
"""
import re

def strip(string, char = ' '): # setting up default char value if nothing is passed
    regex = re.compile(r"^{0}*|{0}*$".format(char))
    strip_result = regex.sub("", string)
    return strip_result

text = input("Please enter text\n")
char = input("Please enter strip value(s)\n")

if char == '':
    print(strip(text))
else:
    print(strip(text, char))

