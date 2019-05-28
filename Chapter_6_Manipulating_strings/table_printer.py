#! python3
'''
Write a function named printTable() that takes a list of lists of strings
and displays it in a well-organized table with each column right-justified.
Assume that all the inner lists will contain the same number of strings.
'''

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose'],
              ['x', 'x', 'x', 'x']]


def print_table(table):
    max_length_list = []

    # defining max character for each row to use it as column width
    for y in range(len(table)): # 3
        max_number = 0
        for x in range(len(table[y])): # 4
            if max_number < len(table[y][x]):
                max_number = len(table[y][x])
        max_length_list.append(max_number)

    # printing the table values
    for x in range(len(table[0])): # 4
        print("")
        for y in range(len(table)): # 3
            print(table[y][x].rjust(max_length_list[y]), end=" ")


print_table(table_data)
