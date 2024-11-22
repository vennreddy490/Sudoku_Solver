import numpy as np

class SudokuSolver:
    def __init__(self, board, size=9):
        self.board = np.array(board)
        self.size = size
        self.subgrid_size = int(np.sqrt(self.size))
        self.iterations = 0

    def is_valid(self, row, col, num):
        """Check if placing num at (row, col) is valid."""
        # Check row and column
        if num in self.board[row, :] or num in self.board[:, col]:
            return False
        # Check subgrid
        start_row = (row // self.subgrid_size) * self.subgrid_size
        start_col = (col // self.subgrid_size) * self.subgrid_size
        for i in range(start_row, start_row + self.subgrid_size):
            for j in range(start_col, start_col + self.subgrid_size):
                if self.board[i, j] == num:
                    return False
        return True

    def find_empty(self):
        """Find an empty cell (0)."""
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i, j] == 0:
                    return i, j
        return None

    def solve(self):
        """Solve using backtracking."""
        empty = self.find_empty()
        if not empty:
            return True  # Solution found
        row, col = empty
        for num in range(1, self.size + 1):
            if self.is_valid(row, col, num):
                self.board[row, col] = num
                self.iterations += 1
                if self.solve():
                    return True
                self.board[row, col] = 0
        return False