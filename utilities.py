
x_equals_y_operations = [(0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0),
                                 (1, 1)]
x_not_equals_y_operations = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def is_game_over(grid, goats_killed):
    if goats_killed >= 5:
        return True, "Tiger"

    for i in range(5):
        for j in range(5):
            if grid[i][j] == 'T':
                if can_move(grid, i, j):
                    return False, "None"

    return True, "Goat"

def is_reachable_to_eat(grid, row1, col1, row2, col2):
    operations = x_equals_y_operations.copy()
    if row1 % 2 != col1 % 2:
        operations = x_not_equals_y_operations.copy()

    for offset_x, offset_y in operations:
        # Next ma chai goat hunx
        next_x, next_y = row1 + offset_x, col1 + offset_y
        if is_inside_board(next_x, next_y) and grid[next_x][next_y] == 'G':
            next_next_x, next_next_y = row1 + 2 * offset_x, col1 + 2 * offset_y
            if is_inside_board(next_next_x, next_next_y) and (next_next_x, next_next_y) == (row2, col2):
                return True
    return False

def locate_goat_to_be_eaten(grid, row1, col1, row2, col2):
    operations = x_equals_y_operations.copy()
    if row1 % 2 != col1 % 2:
        operations = x_not_equals_y_operations.copy()

    for offset_x, offset_y in operations:
        # Next ma chai goat hunx
        next_x, next_y = row1 + offset_x, col1 + offset_y
        if is_inside_board(next_x, next_y) and grid[next_x][next_y] == 'G':
            next_next_x, next_next_y = row1 + 2 * offset_x, col1 + 2 * offset_y
            if is_inside_board(next_next_x, next_next_y) and (next_next_x, next_next_y) == (row2, col2):
                return next_x, next_y
    return -1, -1



def graphics_coordinates_to_index(graphic_board, x, y):
    for i in range(5):
        for j in range(5):
            if graphic_board[i][j] == (x, y):
                return i, j

def can_move(grid, row, col):
    operations = x_equals_y_operations.copy()
    if row % 2 != col % 2:
        operations = x_not_equals_y_operations.copy()

    for offset_x, offset_y in operations:
        next_x, next_y = row + offset_x, col + offset_y
        if is_inside_board(next_x, next_y) and grid[next_x][next_y] == '_':
            return True
        next_next_x, next_next_y = row + 2 * offset_x, col + 2 * offset_y
        if is_inside_board(next_next_x, next_next_y) and grid[next_next_x][next_next_y] == '_':
            return True
    return False

def is_inside_board(row, col):
    return 0 <= row < 5 and 0 <= col < 5

def is_reachable(row1, col1, row2, col2):
    operations = x_equals_y_operations.copy()
    if row1 % 2 != col1 % 2:
        operations = x_not_equals_y_operations.copy()

    for offset_x, offset_y in operations:
        next_x, next_y = row1 + offset_x, col1 + offset_y
        if is_inside_board(next_x, next_y) and (next_x, next_y) == (row2, col2):
            return True
    return False

