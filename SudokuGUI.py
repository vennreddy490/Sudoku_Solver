import tkinter as tk
from tkinter import messagebox
import time
import SudokuSolver

class SudokuGUI:
    def __init__(self, root):
        self.root = root
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
        solver = SudokuSolver.SudokuSolver(board, self.size)
        start_time = time.time()
        if solver.solve():
            end_time = time.time()
            self.set_board(solver.board)
            self.time_label.config(text=f"Time Taken: {end_time - start_time:.2f} seconds")
            self.iterations_label.config(text=f"Iterations: {solver.iterations}")
        else:
            messagebox.showinfo("Sudoku Solver", "No solution exists!")

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
