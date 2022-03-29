"""
Name: <Bryce Wren>
<tictactoe>.py
"""


def build_board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board


def print_board(board):
    """ prints the values of baord """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def is_legal(board, position):
    index_board = board[position - 1]
    return str(index_board).isnumeric()


def fill_spot(board, position, character):
    board = board
    character = character.strip().lower()
    board[position - 1] = character


def winning_game(board):
    for i in range(0, 8, 3):
        horizontal = (board[i] == board[i + 1]) and (board[i + 1] == board[i + 2])
        if horizontal:
            return True
    for i in range(0, 3):
        vertical = (board[i] == board[i + 3]) and (board[i + 3] == board[i + 6])
        if vertical:
            return True
    if (board[0] == board[4]) and (board[4] == board[8]):
        return True
    if (board[2] == board[4]) and (board[4] == board[6]):
        return True
    return False


def game_over(board):
    if winning_game(board):
        return True
    for position in range(1, 9):
        if is_legal(board, position):
            return False
    return True


def get_winner(board):
    if winning_game(board):
        x_count = 0
        o_count = 0
        for position in board:
            if position == 'x':
                x_count += 1
            elif position == 'o':
                o_count += 1
        if x_count == o_count:
            return 'o'
        else:
            return 'x'
    else:
        return None


def play(board):
    character = "x"
    while not game_over(board):
        print_board(board)
        user_position = eval(input("{}'s, choose a position:".format(character)))
        while not is_legal(board, user_position):
            user_position = eval(input("{}'s, choose a position:".format(character)))
        fill_spot(board, user_position, character)
        if character == "x":
            character = 'o'
        else:
            character = "x"

    if winning_game(board):
        winner = get_winner(board)
        print("{} win".format(winner))
    else:
        print("Tie")


def main():
    while True:
        board = build_board()
        play(board)
        user_type = input('play again?')
        if user_type[0] != 'y':
            break


if __name__ == '__main__':
    main()
