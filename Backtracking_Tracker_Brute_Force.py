import numpy as np
import time

class SudokuSolver:
    def __init__(self, board, size=9):
        self.board = np.array(board)
        self.size = size
        self.subgrid_size = int(np.sqrt(self.size))
        self.iterations = 0 # Track all placements
        self.backtracks = 0 # Tracl all backtracks
        self.timestamps = [] # Track timestamps for placements
        self.backtrack_timestamps = []  # Track timestamps for backtracks


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
                self.timestamps.append(time.time())
                if self.solve():
                    return True
                # Backtrack Case:
                self.board[row, col] = 0 # Reset previous cell
                self.backtracks += 1 # Increment backtrack counter
                self.backtrack_timestamps.append(time.time())  # Record backtrack timestamp
    
        return False

import tkinter as tk
from tkinter import messagebox
import time
import matplotlib.pyplot as plt
import sys
import json
import os

class SudokuGUI:
    def __init__(self, root, sample_board=None):
        self.root = root
        self.root.title("Sudoku Solver")
        self.size = 9
        self.sample_board = sample_board
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
                # Populate with the sample board if provided
                if self.sample_board and row < len(self.sample_board) and col < len(self.sample_board[row]):
                    value = self.sample_board[row][col]
                    if value != 0:
                        entry.insert(0, str(value))
                        entry.config(state='disabled')  # Make predefined values uneditable

    def create_buttons(self):
        """Create control buttons."""
        tk.Button(self.root, text="Solve", command=self.solve_board).grid(row=self.size + 2, columnspan=self.size)
        self.time_label = tk.Label(self.root, text="Time Taken: N/A")
        self.time_label.grid(row=self.size + 3, columnspan=self.size)
        self.iterations_label = tk.Label(self.root, text="Iterations: N/A")
        self.iterations_label.grid(row=self.size + 4, columnspan=self.size)

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

    def solve_board(self):
        """Solve the Sudoku puzzle and display metrics."""
        board = self.get_board()
        solver = SudokuSolver(board, self.size)
        start_time = time.time()
        if solver.solve():
            end_time = time.time()
            self.set_board(solver.board)
            self.time_label.config(text=f"Time Taken: {end_time - start_time:.2f} seconds")
            self.iterations_label.config(text=f"Iterations: {solver.iterations}")
            self.plot_iteration_frequency(solver.timestamps)
            self.plot_backtrack_frequency(solver.backtrack_timestamps)

            # Print Number of Iterations and Backtracks:
            print(f"Iterations (placements): {solver.iterations}")
            print(f"Backtracks: {solver.backtracks}")
        else:
            messagebox.showinfo("Sudoku Solver", "No solution exists!")

    def plot_iteration_frequency(self, timestamps):
        """Plot the frequency of iterations over time."""
        if len(timestamps) < 2:
            messagebox.showinfo("Sudoku Solver", "Not enough data to plot!")
            return
        time_differences = [t - timestamps[0] for t in timestamps]
        plt.figure(figsize=(10, 6))
        plt.plot(time_differences, range(len(time_differences)), marker='o')
        plt.xlabel('Time (seconds since start)')
        plt.ylabel('Iteration Count')
        plt.title('Frequency of Iterations Over Time')
        plt.grid()
        plt.show()

    def plot_backtrack_frequency(self, backtrack_timestamps):
        """Plot the frequency of backtracking events over time."""
        if len(backtrack_timestamps) < 2:
            messagebox.showinfo("Sudoku Solver", "Not enough data to plot backtracks!")
            return
        backtrack_differences = [t - backtrack_timestamps[0] for t in backtrack_timestamps]
        plt.figure(figsize=(10, 6))
        plt.plot(backtrack_differences, range(len(backtrack_differences)), marker='x', label='Backtracks')
        plt.xlabel('Time (seconds since first backtrack)')
        plt.ylabel('Backtrack Count')
        plt.title('Frequency of Backtracking Events Over Time')
        plt.legend()
        plt.grid()
        plt.show()

def load_board(file_name):
    """Load a Sudoku board from a JSON file in the 'levels' folder."""
    file_path = os.path.join("levels", file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_name} does not exist in the 'levels' folder.")
    with open(file_path, 'r') as file:
        return json.load(file)
    
# Run the GUI
if __name__ == "__main__":
    # Load a sample level board if specified in CLI
    sample_board = None
    if len(sys.argv) > 1:
        print("Loading Pre-defined level")
        file_name = sys.argv[1]
        sample_board = load_board(file_name)

    # Run the GUI with the loaded board
    root = tk.Tk()
    app = SudokuGUI(root, sample_board=sample_board)
    root.mainloop()

    # Print Number of Iterations and Backtracks
    # print(f"The number of backtracks is: {SudokuSolver.back}")