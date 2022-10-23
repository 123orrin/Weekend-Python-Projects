"""
SUDOKU
By Orrin Dahanaggamaarachchi

GENERAL NOTES
- User inputted rows and columns are indexed starting at 1
- All other row and column computation is done with indexes starting at 0
- Linecache starts its indexing at 1
- MUST INCLUDE the sudoku_database.csv file to generate sudoku's
    - Source: Kaggle by KYUBYONG PARK, https://www.kaggle.com/datasets/bryanpark/sudoku
"""

import math
import linecache
import random

def create_board():
    line_num = random.randint(2, 1000001)
    line = linecache.getline('sudoku_database.csv', line_num)
    board = []
    unchangeable = []
    for i in range(0, 81):
        board.append(int(line[i]))
        if int(line[i]) != 0:
            unchangeable.append(i)
    return board, unchangeable

def print_board(board):
    index = 0
    print(" | ", end="")
    while index < 81:
        print(f" {board[index]} ", end="")
        if (index + 1) % 3 == 0:
            print(f" | ", end="")
        if (index + 1) % 9 == 0 and (index + 1) % 27 != 0:
            print("\n---------------------------------------")
            print(" | ", end="")
        if (index + 1) % 27 == 0:
            print("\n=======================================")
            if index != 80:
                print(" | ", end="")
        index += 1

def get_row_num(location):
    return math.floor((location) / 9)

def get_col_num(location):
    while location >= 9:
        location -= 9
    return location

def get_row(location, board):
    row_num = get_row_num(location)
    row = []
    row_start = row_num * 9
    for i in range(0, 9):
        row.append(board[row_start + i])
    return row

def get_col(location, board):
    col_num = get_col_num(location)
    col = []
    while col_num <= 80:
        col.append(board[col_num])
        col_num += 9
    return col

def get_location_from_index(row_num, col_num):
    return row_num * 9 + col_num

def get_3x3(location, board):
    row_num = get_row_num(location)
    row_num_start = math.floor(row_num / 3) * 3
    col_num = get_col_num(location)
    col_num_start = math.floor(col_num / 3) * 3

    the_3x3 = []
    for i in range(0, 3):
        for j in range(0, 3):
            the_3x3.append(board[get_location_from_index(row_num_start + i, col_num_start + j)])
    return the_3x3

def check_game_rules(number, location, board, user=False):
    # Number is Valid
    if number < 1 or number > 9:
        if user:
            print("Number must by between 1 and 9")
        return False
    # RULE 1 (row rule): No identical numbers in the row
    row = get_row(location, board)
    if number in row:
        if user:
            print(f"{number} is already in the row")
        return False
    # RULE 2 (col rule): No identical numbers in the col
    col = get_col(location, board)
    if number in col:
        if user:
            print(f"{number} is already in the column")
        return False
    # RULE 3 (3x3 rule): No identical numbers in the 3x3
    the_3x3 = get_3x3(location, board)
    if number in the_3x3:
        if user:
                print(f"{number} is already in the grid")
        return False
    # ALL Rules Passed
    return True

def check_general_rules(row_num, col_num, location, unchangeable, user=False):
    if location in unchangeable:
        if user:
            print("That is an unchangeable number!")
        return False
    elif row_num > 9 or row_num < 1:
        if user:
            print("Not a Valid Row")
        return False
    elif col_num > 9 or col_num < 1:
        if user:
            print("Not a Valid Col")
        return False
    return True

def is_valid_move(board, number, row_num, col_num, location, unchangeable, user=False):
    if check_general_rules(row_num, col_num, location, unchangeable, user):
        if number == 0:
            return True
        if check_game_rules(number, location, board, user):
            return True
    return False

def make_move(number, row_num, col_num, board, unchangeable, user=False, location=None):
    if location == None:
        location = get_location_from_index(row_num - 1, col_num - 1)
    
    if is_valid_move(board, number, row_num, col_num, location, unchangeable, user):
        board[location] = number
        return True
    else:
        return False

def is_win(board):
    if 0 not in board:
        return True
    return False

    
def play_sudoku():

    print("Welcome to Sudoku")
    print("Created by Orrin Dahanaggamaarachchi\n")
    print("The game is easy. Just enter any number between 1-9 in the boxes")
    print("Fill the board to win.\n")

    print("There are only 3 simple rules:")
    print("1. ROW RULE: There can be no identical numbers in any given row")
    print("2. COLUMN RULE: There can be no identical numbers in any given column")
    print("3. MATRIX RULE: There can be no identical numbers in the specified 3x3 matrices\n")

    print("Simple Enough, right?")
    print("If you get tired, press 'q' to quit")
    print("If you would like to undo a move, just put a 0 (zero) back in")
    print("Goodluck and have fun!\n")

    board, unchangeable = create_board()
    print_board(board)
    quit = False

    while not is_win(board):
        # Get User Input
        input_row = input("Please enter the row: ")
        if input_row == 'q':
            quit = True
            break
        input_col = input("Please enter the column: ")
        if input_col == 'q':
            quit = True
            break
        input_num = input("Please enter the number: ")
        if input_num == 'q':
            quit = True
            break
        input_row = int(input_row)
        input_col = int(input_col)
        input_num = int(input_num)
        
        if make_move(input_num, input_row, input_col, board, unchangeable, user=True):
            print_board(board)
    
    if quit:
        print("Take a break and try again later")
        print("Goodbye!")
    else:
        print("Congratulations!")
        print("You completed the Sudoku. Hope you had fun!")
        print("See you later")

if __name__ == '__main__':
    play_sudoku()
