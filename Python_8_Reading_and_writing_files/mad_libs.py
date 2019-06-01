'''
Create a Mad Libs program that reads in text files and lets the user add
their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
appears in the text file. The program would find these occurrences
and prompt the user to replace them. The results should be printed
to the screen and saved to a new text file.
'''

import re

# extracting text from file
file = open("mad_libs_text.txt")
text = file.read()
file.close()

keywords = ('ADJECTIVE', 'NOUN', 'VERB', 'ADVERB')

# detecting keywords and substituting them with user input
def keywords_substitutor(string, keywords_list):

    # checks each keyword from the list against string till no match is found
    while True:

        keyword_found = False # flag used to determine if string has any match after the iteration

        for keyword in keywords_list:
            regex = re.compile(r"{0}".format(keyword), re.IGNORECASE)
            result = regex.search(string)

            user_value = ''
            if result:
                user_value = input(f"Please enter {keyword}:\n")
                keyword_found = True # function won't exit the loop when this flag is True (loop through keys again)

            if user_value != '':
                string = regex.sub(user_value, string, count=1) # change 1st occurrence of the keyword


        if keyword_found == False: # if nothing found during last iteration, return result
            return string


result = keywords_substitutor(text, keywords)
print(result)

# creating new file with results
new_file = open("mad_libs_new_text.txt", "w")
new_file.write(result)
new_file.close()

