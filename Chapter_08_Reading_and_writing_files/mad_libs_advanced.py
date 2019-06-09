'''
More advanced solution to mad_libs.py task that preserves input order and forbids keywords as a user values to avoid loops.

INPUT ORDER logic:
This solution prompts user input in the same order as keywords appear in the text.
It's important when text have several duplicated keywords like NOUN, VERB, VERB, ADVERB and we need precision with input order.
Previous solution didn't accommodated for it and would ask for NOUN, VERB, ADVERB, VERB.
This version keeps the order intact and asks for NOUN, VERB, VERB, ADVERB according to the text.
'''

import re

# extracting text from file
file = open("mad_libs_text.txt")
text = file.read()
file.close()


# detecting keywords and replacing them with user input
def replace_keywords(string):

    keywords = ('ADJECTIVE', 'NOUN', 'VERB', 'ADVERB')
    str_len = len(string)
    i = 1 # active max character number for text sample

    # iterating through text and replacing keywords with user values
    while i <= str_len:

        for keyword in keywords:
            text_sample = string[0:i] # getting text sample and growing it with each iteration
            regex = re.compile(r"{0}".format(keyword))
            result = regex.search(text_sample)

            user_value = ''
            if result:
                user_value = input(f"Please enter {keyword}:\n")

                # excluding keywords from user values to avoid loops
                while user_value.upper() in keywords:
                    print("Keywords are not allowed as new values")
                    user_value = input(f"Please enter {keyword}:\n")
            else:
                i +=1 # to grow text sample

            if user_value != '':
                updated_text_sample = regex.sub(user_value, text_sample, count=1) # replacing keyword in a sample
                string = string.replace(text_sample, updated_text_sample) # updating string with user value

                # updating string-related variables with the string update
                i = len(updated_text_sample) # new active max char number (e.g., was: i=20, now: i=30 => no sense to iterate through 20-30 as it has no keyword)
                str_len = len(string) # setting length of the new string

    return string


result = replace_keywords(text)
print(result)

# creating new file with results
new_file = open("mad_libs_new_text.txt", "w")
new_file.write(result)
new_file.close()
