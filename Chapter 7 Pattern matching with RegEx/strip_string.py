"""
Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to
strip, then whitespace characters will be removed from the beginning and
end of the string. Otherwise, the characters specified in the second argument
to the function will be removed from the string.
"""
import re

def strip(string, symbol = ' '): # setting up default symbol value if nothing is passed
    regex = re.compile(r"^{0}*|{0}*$".format(symbol))
    strip_result = regex.sub("", string)
    return strip_result

text = "_text_"
symbol = "_"

if symbol == '':
    print(strip(text))
else:
    print(strip(text, symbol))

