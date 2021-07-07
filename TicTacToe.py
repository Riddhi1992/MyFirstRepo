
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going = True

winner = None

current_player = "X"

win_list = [('X', 'X', 'X'), ('O', 'O', 'O')]


def squares(x, y, z):
    return board[x], board[y], board[z]


def display_board():
    for k in range(3):
         print(f'{board[3*k]} | {board[3*k + 1]} | {board[3*k + 2]}')


def play_game():

    display_board()

    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner in ["X", "O"]:
        print(winner + " won.")
    elif winner is None:
        print("It's a Tie.")


def handle_turn(player):

    print(player + "'s turn.")
    position = int(input("Choose a position from 0-8: "))

    valid = False
    while not valid:

        while position not in range(9):
            position = int(input("Invalid input, Choose a position from 0-8: "))

        if board[position] == "-":
            valid = True
        else:
            print("This place is already taken, Try other.")

    board[position] = player

    display_board()


def check_if_game_over():

    check_for_winner()

    check_if_tie()


def check_for_winner():

    global winner

    row_winner = check_rows()

    column_winner = check_columns()

    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner

    elif diagonal_winner:
        winner = diagonal_winner

    else:
        winner = None


def check_rows():
    global game_still_going

    row_1 = squares(0, 1, 2) in win_list
    row_2 = squares(3, 4, 5) in win_list
    row_3 = squares(6, 7, 8) in win_list

    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]


def check_columns():
    global game_still_going

    column_1 = squares(0, 3, 6) in win_list
    column_2 = squares(1, 4, 7) in win_list
    column_3 = squares(2, 5, 8) in win_list

    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]


def check_diagonals():
    global game_still_going

    diagonals_1 = squares(0, 4, 8) in win_list
    diagonals_2 = squares(2, 4, 6) in win_list

    if diagonals_1 or diagonals_2:
        game_still_going = False
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[2]


def check_if_tie():
    global game_still_going
    game_still_going = '-' in board


def flip_player():
    global current_player
    current_player = {'X': 'O', 'O', 'X'}[current_player]


play_game()
