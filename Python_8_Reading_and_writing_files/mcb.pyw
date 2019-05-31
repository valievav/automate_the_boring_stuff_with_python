#! Python3
# mcb.pyw - Multiclipboard project. Saves and loads text to the clipboard.

# How to use:   open cmd under current working directory and run next commands:
#               python mcb.pyw save <keyword>   - Saves clipboard content under keyword
#               python mcb.pyw <keyword>        - Loads keyword content to the clipboard
#               python mcb.pyw list             - Lists all keywords to the clipboard
# e.g., python mcb.pyw save user_name - saves current clipboard content under "user_name" keyword
#       python mcb.pyw user_name - copies to clipboard content from "user_name" keyword

import shelve, pyperclip, sys

# saving clipboard content to shelve
def content_saver(shelf_file, keyword):
    content = pyperclip.paste()
    shelf_file[keyword] = content
    print(f"Content [{content}] is saved under keyword [{keyword}]")


# listing all keywords
def keyword_lister(shelf_file):
    keywords = str(list(shelf_file.keys()))
    pyperclip.copy(keywords)
    print(f"List of keywords {keywords} is copied to the clipboard")


# loading content based on keyword
def content_printer(shelf_file, keyword):
    if keyword in list(shelf_file.keys()):
        pyperclip.copy(shelf_file[keyword])
        print(f"Content [{shelf_file[keyword]}] is copied to the clipboard")
    else:
        user_answer = input("No such keyword. Do you want to check a list of possible keywords [L] "
                            "or save current clipboard content under this keyword [S]?\n")
        if user_answer.lower() == "l":
            keyword_lister(shelf_file)
        elif user_answer.lower() == "s":
            content_saver(shelf_file, keyword)
        else:
            return


shelf_file = shelve.open("mcb")
user_args = sys.argv # getting command line from cmd in a list, e.g., mvb.pyw[0] save[1] keyword[2]

# defining the operation
if user_args[1].lower() == "save" and len(user_args) == 3:
    content_saver(shelf_file, user_args[2]) # passing [2] index element as it is a shelve keyword
elif user_args[1].lower() == "list" and len(user_args) == 2:
    keyword_lister(shelf_file)
elif len(user_args) == 2:
    content_printer(shelf_file, user_args[1]) # passing [1] index element as it is a shelve keyword
else:
    print("Wrong syntax. Expected formats: 'file_name.pyw save keyword', 'file_name.pyw list' or 'file_name.pyw keyword'")

shelf_file.close()
