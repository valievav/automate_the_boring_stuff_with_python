'''
Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with 'and'
inserted before the last item.
'''

spam = ['apples', 'bananas', 'tofu', 'cats']


def list_to_string(list):
    for item in list[0:-1]:
        print(item, end=", ")
    print("and " + list[-1])


list_to_string(spam)

