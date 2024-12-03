import numpy as np
import time
import tkinter as tk
from tkinter import messagebox


class SudokuSolver: #implements the logic for solving the puzzle using backtracking
    def __init__(self, board, size=9, gui=None):
        self.board = np.array(board)
        self.size = size #(4*4 or 9*9)
        self.subgrid_size = int(np.sqrt(self.size))
        self.iterations = 0 # no.of valid moves
        self.recursive_calls = 0  # Track the number of recursive calls during backtracking
        self.attempted_cells = []  # Track the cells and numbers attempted
        self.gui = gui

    def is_valid(self, row, col, num):
        """Check if placing num at (row, col) is valid."""
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

    def is_board_valid(self):
        """Validate the entire board for duplicates."""
        # Check rows and columns for duplicates
        for i in range(self.size):
            if not self.is_unique(self.board[i, :]) or not self.is_unique(self.board[:, i]):
                return False

        # Check subgrids for duplicates
        for row in range(0, self.size, self.subgrid_size):
            for col in range(0, self.size, self.subgrid_size):
                if not self.is_unique(self.board[row:row + self.subgrid_size, col:col + self.subgrid_size].flatten()):
                    return False
        return True

    @staticmethod
    def is_unique(array):
        """Check if an array has unique non-zero elements."""
        non_zero_elements = array[array > 0]
        return len(non_zero_elements) == len(set(non_zero_elements))

    def find_empty(self):
        """Find an empty cell (0)."""
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i, j] == 0:
                    return i, j  # Returns a tuple(row, column) representing the coordinates of the empty cell
        return None  # None if no empty cells are found

    def visualize(self, row, col, num, valid):
        """Visualize the current step in the GUI."""
        if self.gui:
            # Highlight the current cell
            color = "green" if valid else "red"
            self.gui.entries[row][col].config(bg=color)
            if num != 0:
                self.gui.entries[row][col].delete(0, tk.END)
                self.gui.entries[row][col].insert(0, str(num))
            self.gui.root.update_idletasks()
            time.sleep(0.05)  # Pause for visualization

    def solve(self):
        """Solve using backtracking."""
        empty = self.find_empty()
        if not empty:
            return True  # Solution found

        row, col = empty
        self.recursive_calls += 1  # Increment recursive call counter
        for num in range(1, self.size + 1):
            valid = self.is_valid(row, col, num)
            self.attempted_cells.append((row, col, num, valid))  # Log the attempted move
            self.visualize(row, col, num, valid)  # Visualize the decision process
            if valid:
                self.board[row, col] = num
                self.iterations += 1

                if self.gui:
                    self.gui.iterations_label.config(text=f"Iterations: {self.iterations}")
                    self.gui.search_space_label.config(
                        text=f"Recursive Calls: {self.recursive_calls}, Attempted Moves: {len(self.attempted_cells)}"
                    )
                    self.gui.root.update_idletasks()

                if self.solve():
                    return True
                # Backtracking
                self.board[row, col] = 0
                self.visualize(row, col, 0, True)  # Undo visualization

        return False


class SudokuGUI:
    def __init__(self, root):
        self.root = root # Tkinter root window
        self.root.title("Sudoku Solver")
        self.size = 9
        self.entries = None
        self.create_dropdown()
        self.create_grid()
        self.create_buttons()

    def create_dropdown(self):
        """Dropdown menu for board size."""
        tk.Label(self.root, text="Select Board Size:").grid(row=0, column=0, columnspan=2)
        self.board_size_var = tk.StringVar(self.root)
        self.board_size_var.set("9x9")
        dropdown = tk.OptionMenu(self.root, self.board_size_var, "9x9", "4x4", command=self.change_size)
        dropdown.grid(row=0, column=2, columnspan=2)

    def change_size(self, selection):
        """Update the board size based on user selection."""
        self.size = 9 if selection == "9x9" else 4
        self.create_grid()

    def create_grid(self):
        """Create Sudoku grid based on the selected size."""
        if self.entries:
            for row in self.entries:
                for entry in row:
                    entry.destroy()
        self.entries = [[None for _ in range(self.size)] for _ in range(self.size)]
        for row in range(self.size):
            for col in range(self.size):
                entry = tk.Entry(self.root, width=3, font=('Arial', 18), justify='center')
                entry.grid(row=row + 1, column=col)
                self.entries[row][col] = entry

    def create_buttons(self):
        """Create control buttons."""
        tk.Button(self.root, text="Solve", command=self.solve_board).grid(row=self.size + 2, columnspan=self.size)
        self.time_label = tk.Label(self.root, text="Time Taken: N/A")
        self.time_label.grid(row=self.size + 3, columnspan=self.size)
        self.iterations_label = tk.Label(self.root, text="Iterations: N/A")
        self.iterations_label.grid(row=self.size + 4, columnspan=self.size)
        self.search_space_label = tk.Label(self.root, text="Recursive Calls: N/A, Attempted Moves: N/A")
        self.search_space_label.grid(row=self.size + 5, columnspan=self.size)

    def get_board(self):
        """Extract the board from the GUI."""
        board = []
        for row in range(self.size):
            current_row = []
            for col in range(self.size):
                value = self.entries[row][col].get()
                current_row.append(int(value) if value.isdigit() else 0)
            board.append(current_row)
        return board

    def set_board(self, board):
        """Display the solved board in the GUI."""
        for row in range(self.size):
            for col in range(self.size):
                self.entries[row][col].delete(0, tk.END)
                self.entries[row][col].insert(0, str(board[row][col]))
                self.entries[row][col].config(bg="white")  # Reset background color

    def solve_board(self):
        """Solve the Sudoku puzzle and display metrics."""
        board = self.get_board()
        solver = SudokuSolver(board, self.size, gui=self)
        if not solver.is_board_valid():
            messagebox.showerror("Sudoku Solver", "Invalid board! Check for duplicates.")
            return

        self.start_time = time.time()
        if solver.solve():
            end_time = time.time()
            self.set_board(solver.board)
            self.time_label.config(text=f"Time Taken: {end_time - self.start_time:.2f} seconds")
            self.iterations_label.config(text=f"Iterations: {solver.iterations}")
            self.search_space_label.config(
                text=f"Recursive Calls: {solver.recursive_calls}, Attempted Moves: {len(solver.attempted_cells)}"
            )
        else:
            messagebox.showinfo("Sudoku Solver", "No solution exists!")


# Run the GUI
if __name__ == "__main__":
    print("Starting Sudoku Solver GUI...")  # Debug: Startup message
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
    print("GUI loop has exited.")  # Debug: After GUI exits
