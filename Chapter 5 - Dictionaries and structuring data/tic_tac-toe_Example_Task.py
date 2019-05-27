game_board = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' '
}


def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] + '\n'
          + '-+-+-' + '\n'
          + board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'] + '\n'
          + '-+-+-' + '\n'
          + board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


turn = 'X'

for i in range(len(game_board)):
    print_board(game_board)

    while True:
        move = input(f"Turn for {turn}. Move on which space?\n")
        if move not in game_board:  # check that move is valid
            print("No such move. Try again.")
        else:
            if game_board[move] == ' ':  # check that move has not been taken
                game_board[move] = turn
                break
            else:
                print("Move is taken. Try again.")

    # winning combinations
    win_top_row = game_board['top-L'] == game_board['top-M'] == game_board['top-R'] in ('X', 'O')
    win_middle_row = game_board['mid-L'] == game_board['mid-M'] == game_board['mid-R'] in ('X', 'O')
    win_low_row = game_board['low-L'] == game_board['low-M'] == game_board['low-R'] in ('X', 'O')

    win_left_column = game_board['top-L'] == game_board['mid-L'] == game_board['low-L'] in ('X', 'O')
    win_middle_column = game_board['top-M'] == game_board['mid-M'] == game_board['low-M'] in ('X', 'O')
    win_right_column = game_board['top-R'] == game_board['mid-R'] == game_board['low-R'] in ('X', 'O')

    win_diagonal_left_right = game_board['top-L'] == game_board['mid-M'] == game_board['low-R'] in ('X', 'O')
    win_diagonal_right_left = game_board['top-R'] == game_board['mid-M'] == game_board['low-L'] in ('X', 'O')

    winning_combinations = [win_top_row, win_middle_row, win_low_row,
                            win_left_column, win_middle_column, win_right_column,
                            win_diagonal_left_right, win_diagonal_right_left]

    if True in winning_combinations:
        print("*"*2 + "Congratulations!!! You have won!" + "*"*2)
        print_board(game_board)
        break
    else:
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
