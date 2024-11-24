import os
import random

VALID_COLUMNS = ['a','b','c']
VALID_ROWS = ['1','2','3']

moves = {column: {row: {'mark': None, 'position': int(index + 1)*4} for row in VALID_ROWS}
                for index, column in enumerate(VALID_COLUMNS)}

user1 = {'name':'Sofia', 'mark': 'x'}
user2 = {'name':'Computer', 'mark': 'o'}

COLUMN_STRING = "    " + "   ".join(VALID_COLUMNS) + "  "
BOARD_SPACE = "   "
BOARD_LINE_PIECE = "---"
BOARD_CONNECTOR = "+"
BOARD_SEPARATOR = "|"
EMPTY_ROW = "  " \
        + (BOARD_SPACE + BOARD_SEPARATOR) * (len(VALID_COLUMNS) - 1) \
        + BOARD_SPACE
BOARD_LINE = "   " \
        + (BOARD_LINE_PIECE + BOARD_CONNECTOR) * (len(VALID_COLUMNS) - 1) \
        + BOARD_LINE_PIECE
row_strings = [row + EMPTY_ROW for row in VALID_ROWS]

def board_display():
    """Prints the board"""
    print(COLUMN_STRING)

    for string in row_strings[:-1]:
        print(string)
        print(BOARD_LINE)

    print(row_strings[-1])

def updated_board_display(moves_dict = moves):
    """Updates the board with moves, then prints the board"""

    for index, string in enumerate(row_strings):
        string = row_strings[index]
        for row_list in moves_dict.values():
            for row_number, values in row_list.items():
                if values['mark'] is not None and int(row_number) - 1 == index:
                    string = string[:values['position']] \
                        + values['mark'] \
                        + string[(values['position'] + 1):]
        row_strings[index] = string

    board_display()

def prompt(text):
    """Formatted input prompt"""
    return input(f"\n>>> {text}:\n")

def move_input_strip(string):
    """Returns the stripped user move input with case removed"""
    return ''.join([char for char in string.casefold() if char in VALID_COLUMNS + VALID_ROWS])

def invalid_move(string):
    """Returns True if the user's entered move is invalid"""
    move = move_input_strip(string)
    return (move.isalpha() or move.isnumeric()) or len(move) != 2

def move_coordinates(string):
    """Returns the alphabetical column and numeric row from a valid input string"""
    column = ''
    row = ''
    for character in string.casefold():
        if character.isalpha():
            column = character
        if character.isnumeric():
            row = character
    return column, row

def get_user_mark_list(user, moves_dict = moves):
    """Returns a nested list of a user's moves in [column, row] format"""
    return [[[column, row_num]
         for row_num, values in row.items() if values['mark'] == user['mark']]
         for column, row in moves_dict.items()
        ]

def get_diagonal_moves(moves_dict = moves):
    """Returns lists of the possible diagonal moves on the board, for each diagonal"""
    possible_moves = [[[column, row_num]
         for row_num in row]
         for column, row in moves_dict.items()
        ]
    diagonal_1 = []
    diagonal_2 = []

    for index, move in enumerate(possible_moves):
        diagonal_1.append(move[index])
        diagonal_2.append(list(reversed(move))[index])

    return diagonal_1, diagonal_2

def empty_space(coords, moves_dict = moves):
    """Retruns true if a given move has no mark"""
    return moves_dict[coords[0]][coords[1]]['mark'] is None

def diagonal_move_logic(diagonal):
    """Returns the best column and row selection for a diagonal move"""
    moves_possible = [coords for coords in diagonal if empty_space(coords)]

    try:
        [chosen_column, chosen_row] = moves_possible[0]
        return chosen_column, chosen_row
    except IndexError:
        return None

def row_or_column_move_logic(priority, columns, rows):
    """Returns the best column and row selection for a horizontal or vertical move"""
    if priority == "columns":
        moves_possible = [col[1] + row[1] for col in columns for row in rows
                         if moves[col[1]][row[1]]['mark'] is None]
    else:
        moves_possible = [col[1] + row[1] for row in rows for col in columns
                         if moves[col[1]][row[1]]['mark'] is None]

    for move in moves_possible:
        if moves[move[0]][move[1]]['mark'] is None:
            chosen_column = move[0]
            chosen_row = move[1]
            break

    return chosen_column, chosen_row

def get_full_rows_columns(moves_dict = moves):
    """Returns 2 lists, one with full columns and one with full rows"""
    possible_moves = [[[column, row_num]
         for row_num, values in row.items() if values['mark'] is not None]
         for column, row in moves_dict.items()
        ]

    mark_counts = {key: 0 for key in VALID_COLUMNS + VALID_ROWS}

    for column in possible_moves:
        for mark in column:
            mark_counts.setdefault(mark[1], 0)
            mark_counts[mark[1]] += 1
            mark_counts.setdefault(mark[0], 0)
            mark_counts[mark[0]] += 1

    full_columns = [key for [key, value] in mark_counts.items()
                    if key.isalpha() and value == len(VALID_COLUMNS)]
    full_rows = [key for [key, value] in mark_counts.items()
                    if key.isnumeric() and value == len(VALID_ROWS)]

    return full_columns, full_rows

def get_sorted_columns_rows(row_column_mark_counts, full_columns, full_rows):
    """Returns lists of columns and rows, sorted by the number of marks, 
        in [mark count, (row or column)] format"""
    sorted_columns = sorted([[count, key] for [key, count] in row_column_mark_counts.items()
                            if key.isalpha() and key not in full_columns], reverse = True)
    sorted_rows = sorted([[count, key] for [key, count] in row_column_mark_counts.items()
                            if key.isnumeric() and key not in full_rows], reverse = True)

    return sorted_columns, sorted_rows

def get_user_move():
    """Gets user move input and updates the move dictionary"""
    user_move = prompt("Select a square to mark (using letter and number coordinates)")

    while invalid_move(user_move):
        user_move = prompt("Choose a valid square to mark")

    column, row = move_coordinates(user_move)

    while moves[column][row]['mark'] is not None:
        user_move = prompt("That square is already taken. Choose a valid square to mark")
        while invalid_move(user_move):
            user_move = prompt("Choose a valid square to mark")
        column, row = move_coordinates(user_move)

    moves[column][row]['mark'] = user1['mark']

def get_comp_random_move():
    """Selects a computer move randomly and updates the move dictionary"""
    if winner(user1):
        print(f"\n{user1['name']} wins!")

    else:
        comp_column_selection = random.choice(VALID_COLUMNS)
        comp_row_selection = random.choice(VALID_ROWS)

        while (marks_available()
            and moves[comp_column_selection][comp_row_selection]['mark'] is not None):
            comp_column_selection = random.choice(VALID_COLUMNS)
            comp_row_selection = random.choice(VALID_ROWS)

        moves[comp_column_selection][comp_row_selection]['mark'] = user2['mark']

        print(f"{user2['name']} chose {comp_column_selection.upper() + comp_row_selection}\n")

def get_defensive_comp_move():

    full_columns, full_rows = get_full_rows_columns()
    user_marks =  get_user_mark_list(user1)
    diagonal_moves_1, diagonal_moves_2 = get_diagonal_moves()
    row_column_mark_counts, diagonal_1_streak, diagonal_2_streak = get_mark_counts(user_marks)
    sorted_columns, sorted_rows = get_sorted_columns_rows(row_column_mark_counts,
                                                          full_columns,
                                                          full_rows)

    if winner(user1):
        print(f"\n{user1['name']} wins!")

    elif not marks_available():
        pass

    else:
        row_streak = max(row[0] for row in sorted_rows)
        column_streak = max(col[0] for col in sorted_columns)

        #initialize default computer row and column selections
        comp_column_selection = sorted_columns[0][1]
        comp_row_selection = sorted_rows[0][1]

        if (diagonal_1_streak >= row_streak
            and (diagonal_1_streak >= column_streak)
            and (diagonal_1_streak >= diagonal_2_streak)
            and diagonal_move_logic(diagonal_moves_1) is not None):
            comp_column_selection, comp_row_selection = diagonal_move_logic(diagonal_moves_1)

        elif (diagonal_2_streak >= row_streak
            and (diagonal_2_streak >= column_streak)
            and diagonal_move_logic(diagonal_moves_2) is not None):
            comp_column_selection, comp_row_selection = diagonal_move_logic(diagonal_moves_2)

        elif column_streak > row_streak:
            comp_column_selection, comp_row_selection = row_or_column_move_logic("columns",
                                                                                 sorted_columns,
                                                                                 sorted_rows)

        elif row_streak >= column_streak:
            comp_column_selection, comp_row_selection = row_or_column_move_logic("rows",
                                                                                 sorted_columns,
                                                                                 sorted_rows)

        #set final move
        moves[comp_column_selection][comp_row_selection]['mark'] = user2['mark']

        #print move text
        print(f"{user2['name']} chose {comp_column_selection.upper() + comp_row_selection}\n")

def marks_available():
    marked_spaces = [[[value['mark']]
         for value in row.values() if value['mark'] is None]
         for row in moves.values()]

    return (sum(len(marks) for marks in marked_spaces))

def get_mark_counts(marks):
    mark_counts = {key: 0 for key in VALID_COLUMNS + VALID_ROWS}
    diag_1_tally = 0
    diag_2_tally = 0
    diag_1 = 0
    diag_2 = len(VALID_ROWS) + 1

    for column in marks:
        diag_1 += 1
        diag_2 -= 1
        for mark in column:
            mark_counts.setdefault(mark[1], 0)
            mark_counts[mark[1]] += 1
            mark_counts.setdefault(mark[0], 0)
            mark_counts[mark[0]] += 1

            if int(mark[1]) == diag_1:
                diag_1_tally += 1
            if int(mark[1]) == diag_2:
                diag_2_tally += 1

    return mark_counts, diag_1_tally, diag_2_tally

def winner(player):
    user_marks =  [[[col,row_num]
         for row_num, values in row.items() if values['mark'] == player['mark']]
         for col, row in moves.items()
        ]

    mark_counts, diag_1_tally, diag_2_tally = get_mark_counts(user_marks)

    return (len(VALID_ROWS) in mark_counts.values()) \
            or diag_1_tally == len(VALID_ROWS) \
            or diag_2_tally == len(VALID_ROWS)
################## Main program ##################
os.system('clear')
print("Welcome to Tic-Tac-Toe\n")
board_display()

get_comp_random_move()
updated_board_display()

while marks_available() and not winner(user1) and not winner(user2):
    get_user_move()
    os.system('clear')
    random.choice([get_comp_random_move, get_defensive_comp_move])()
    updated_board_display()

if winner(user1):
    print(f"\n{user1['name']} wins!")
elif winner(user2):
    print(f"\n{user2['name']} wins!")
else:
    print("\nIt's a tie!")

print("\nThanks for playing!")

'''
os.system('clear')
print("Welcome to Tic-Tac-Toe\n")
board_display()

while marks_available() and not winner(user1) and not winner(user2):
    get_user_move()
    os.system('clear')
    get_comp_random_move()
    updated_board_display()

if winner(user1):
    print(f"\n{user1['name']} wins!")
elif winner(user2):
    print(f"\n{user2['name']} wins!")
else:
    print("\nIt's a tie!")

print("\nThanks for playing!")
'''
