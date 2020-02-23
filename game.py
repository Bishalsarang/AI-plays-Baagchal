from utilities import can_move


class Game(object):
    def __init__(self):
        self.current_turn = 'Goat'
        self.winner = None
        self.goats_in_hand = 20
        self.goats_killed = 0

        self.grid = [['_' for _ in range(5)] for _ in range(5)]
        self.board_init()

    def board_init(self):
        # Place tiger at corners
        self.grid[0][0] = self.grid[0][4] = self.grid[4][0] = self.grid[4][4] = 'T'

    def switch_turn(self):
        if self.current_turn == 'Goat':
            self.current_turn = 'Tiger'
        else:
            self.current_turn = 'Goat'

    def is_game_over(self):
        if self.goats_killed >= 4:
            self.winner = "Tiger"
            return True

        for i in range(5):
            for j in range(5):
                if self.grid[i][j] == 'T':
                    if can_move(self.grid, i, j):
                        return False

        self.winner = "Goat"
        return True

    def __repr__(self):
        return f"Current Turn {self.current_turn} | Goats in hand {self.goats_in_hand} "
