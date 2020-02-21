# Author: Bishal Sarang
from collections import  namedtuple
import pydot
graph = pydot.Dot(graph_type="graph")

grid = [['_' for _ in range(6)] for _ in range(6)]
# Place tiger at corners
grid[0][0] = grid[0][5] = grid[5][0] = grid[5][5] = 'T'

num_of_goats_to_be_placed = 20
num_of_goats_on_board = 0
num_of_goats_eaten = 0


# E, E:
# (2, 2)
# (x, y) -> (x, y - 1), (x, y + 1), (x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)
#
# E, O:
# (2, 3)
# (x, y) -> (x, y - 1), (x, y + 1), (x + 1, y), (x - 1, y)
#
# O, E:
# (1, 2)
# (x, y) -> (x, y - 1), (x, y + 1), (x + 1, y), (x - 1, y)
#
#
# O, O
# (1, 3)
# (x, y) -> (x, y - 1), (x, y + 1), (x - 1, y - 1), (x - 1, y), (x - 1, y + 1),  (x + 1, y - 1), (x + 1, y), (x + 1, y + 1),

"""Next Move"""
x_equals_y_operations = [(0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)]
x_not_equals_y_operations = [(1, -1), (0, 1), (1, 0), (-1, 0)]
""""""



Move = namedtuple('Move', "move_type, move_from, move_to")

def is_inside_board(row, col):
    return 0 <= row < 6 and 0 <= col < 6

def is_cell_vacant(grid, row, col):
    return grid[row][col] == '_'

def cell_has_goat(grid, row, col):
    return grid[row][col] == 'G'

def main():
    x, y = 0, 0

    grid[0][1] = 'G'
    for offset_x, offset_y in x_equals_y_operations:
        """Find next vacant position to move"""
        next_x, next_y = x + offset_x, y + offset_y
        if is_inside_board(next_x, next_y) and is_cell_vacant(grid, next_x, next_y):
            grid[next_x][next_y] = 'T'
            grid[x][y] = '_'
            print(*grid, sep='\n')
            grid[next_x][next_y] = '_'
            grid[x][y] = 'T'
            print("*******************************")
        """
            Check if goat can be eaten
        """
        next_x_after_jump, next_y_after_jump =  x + 2 * offset_x, y + 2 * offset_y
        if is_inside_board(next_x, next_y) and  cell_has_goat(grid, next_x, next_y) and is_cell_vacant(grid, next_x_after_jump, next_y_after_jump):
            grid[next_x_after_jump][next_y_after_jump] = 'T'
            grid[x][y] = '_'
            grid[next_x][next_y] = '_'
            print("Tiger eats goat")
            print(*grid, sep='\n')
            grid[next_x_after_jump][next_y_after_jump] = '_'
            grid[x][y] = 'T'
            grid[next_x][next_y] = 'G'
            print("*******************************")










if __name__ == '__main__':
    main()