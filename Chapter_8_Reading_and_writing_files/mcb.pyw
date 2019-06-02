#! Python3
# mcb.pyw - Multiclipboard project. Saves and loads text to the clipboard.

# How to use:         open Terminal under current working directory and run commands.
# Please see help_printer() for details on available operations and syntax.
# Usage examples:    python mcb.pyw save user_name - saves current clipboard content under "user_name" keyword
#                    python mcb.pyw user_name - copies to clipboard content from "user_name" keyword

import shelve, pyperclip, sys

# saving clipboard content to shelve
def content_saver(shelf_file, keyword):

    def recorder(shelf_file, keyword):
        content = pyperclip.paste()
        shelf_file[keyword] = content
        print(f"Content [{content}] is saved under keyword [{keyword}]")

    # checking that keyword is new
    if keyword not in shelf_file.keys():
        recorder(shelf_file, keyword)
    else:
        user_answer = input(f"This keyword already exists with the content [{shelf_file[keyword]}]. "
                            "Do you want to rewrite it [R] or exit [E]?\n")
        if user_answer.lower() == "r":
            recorder(shelf_file, keyword)
        else:
            return


# copying all keywords to the clipboard
def all_keywords_lister(shelf_file):
    keywords = str(list(shelf_file.keys()))
    pyperclip.copy(keywords)
    print(f"List of keywords {keywords} is copied to the clipboard")


# copying keywords content to the clipboard
def content_printer(shelf_file, keyword):
    # checking that keyword exists
    if keyword in shelf_file.keys():
        pyperclip.copy(shelf_file[keyword])
        print(f"Content [{shelf_file[keyword]}] is copied to the clipboard")
    else:
        user_answer = input("No such keyword. Do you want to check a list of possible keywords [L], "
                            "save current clipboard content under the keyword [S] or exit [E]?\n")
        if user_answer.lower() == "l":
            all_keywords_lister(shelf_file)
        elif user_answer.lower() == "s":
            content_saver(shelf_file, keyword)
        else:
            return


# deleting keyword with its content
def content_remover(shelf_file, keyword):
    # checking that keyword exists
    if keyword in shelf_file.keys():
        del shelf_file[keyword]
        print(f"Keyword [{keyword}] with its content is deleted from the shelve")
    else:
        user_answer = input("There is no such keyword. Do you want to check a list of possible keywords [L]"
                            " or exit [E]?\n")
        if user_answer.lower() == "l":
            all_keywords_lister(shelf_file)
        else:
            return


# deleting all keywords
def all_kewords_remover(shelf_file):
    shelf_file.clear()
    print("All keywords with its content is deleted from the shelve")


# getting list of all possible operations and syntax
def help_printer():
    print("\nAvailable operations:\n"
          "* mcb.pyw save <keyword> - saves clipboard content under <keyword>\n"
          "* mcb.pyw <keyword> - copies to the clipboard content of the <keyword>\n"
          "* mcb.pyw delete <keyword> - removes <keyword> with its content\n"
          "* mcb.pyw list - copies to the clipboard the list of all keywords\n"
          "* mcb.pyw delete - removes all keywords with their content\n"
          "* mcb.pyw help - prints all available operations to the console")


shelf_file = shelve.open("mcb") # object with dictionary like structure to store {keyword:content} values

# sys.argv - returns command line from cmd as a list, e.g., mvb.pyw[0] save[1] keyword[2]
# check for empty input
try:
    sys.argv[1] != ''
except IndexError:
    print("Please enter the command. Use 'help' to get info on possible operations")
    sys.exit()

operation_arg = sys.argv[1].lower()  # argument that defines the type of operation
args_length = len(sys.argv)

# defining the operation
if operation_arg == "save" and args_length == 3:        # e.g. mcb.pyw save user_name
    content_saver(shelf_file, sys.argv[2])
elif operation_arg == "delete" and args_length == 3:    # e.g. mcb.pyw delete user_name
    content_remover(shelf_file, sys.argv[2])
elif operation_arg == "list" and args_length == 2:      # e.g. mcb.pyw list
    all_keywords_lister(shelf_file)
elif operation_arg == "delete" and args_length == 2:    # e.g. mcb.pyw delete
    all_kewords_remover(shelf_file)
elif operation_arg == "help" and args_length == 2:      # e.g. mcb.pyw help
    help_printer()
elif args_length == 2:                                  # e.g. mcb.pyw user_name
    content_printer(shelf_file, sys.argv[1])
else:
    print("Wrong syntax. Use 'help' to get info on possible operations")

shelf_file.close()
