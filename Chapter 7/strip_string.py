'''
Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to
strip, then whitespace characters will be removed from the beginning and
end of the string. Otherwise, the characters specified in the second argument
to the function will be removed from the string.
'''
import re

def strip(string, symbol = ' '): # setting up default symbol value if nothing is passed

        # separate left and right regexes for asymmetrical strips
        # custom regexes based on symbol parameter value
        left_regex = re.compile(r"^{0}".format(symbol))
        right_regex = re.compile(r"{0}$".format(symbol))

        # wrapping in try-catch to avoid NoneType error in case of no match
        try:
            left_char = left_regex.search(string).group()
        except AttributeError:
            left_char = None

        try:
            right_char = right_regex.search(string).group()
        except AttributeError:
            right_char = None

        # strip logic
        if symbol == left_char == right_char: # strip for both sides
            s1 = left_regex.sub("", string)
            s2 = right_regex.sub("", s1)
            return s2
        elif symbol == left_char: # strip for left only
            s = left_regex.sub("", string)
            return s
        elif symbol == right_char: # strip for right only
            s = right_regex.sub("", string)
            return s
        else:
            print("Nothing to strip")

text = "/asd/ "
print(strip(text, "/"))