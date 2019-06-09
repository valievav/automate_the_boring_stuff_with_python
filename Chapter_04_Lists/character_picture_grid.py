'''
Write code that uses following grid list of lists to print the heart image
'''


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


for x in range(len(grid[0])): # 6 columns
    for y in range(len(grid)): # 9 rows
        print(grid[y][x], end="")
    print()


'''
# other solution - printing rows instead of individual values
for i in range(len(grid[0])):
    for row in grid:
        print(row[i], end='')
    print()
'''
