# Sudoku_Solver

Authors: Venn Reddy, Sravanthi Pallabothu, Nikhila Raj


 # 1) Backtracking_Tracker_Brute_Force
**Program Structure:**
 
 **SudokuSolver:** Backtracking-based solver with methods for validation, finding empty cells, and solving while tracking iterations and backtracks.
 **SudokuGUI:** Interactive Tkinter-based GUI for input, solving, and displaying results, including performance plots.
 **Utilities:** File handling to load puzzles from JSON, and plotting for iterations and backtracks over time.
#
**Program Operation:**

Users can input a puzzle through the GUI or load a predefined board. The program solves it using backtracking while tracking metrics like iterations and backtracks. Results, including the solution, solving time, and stats, are displayed in the GUI, with optional visual plots. It also handles unsolvable puzzles and insufficient data gracefully.

Command to run the file: "python Backtracking_Tracker_Brute_Force.py medium.json"

 # 2) Backtracking_Tracker_Most_Constrained
**Program Structure:**
Uses find_most_constrained_empty to prioritize the most constrained cell (the one with the fewest valid options).

Introduces a heuristic to reduce the search space by evaluating constraints before placing numbers.

More efficient due to the heuristic, particularly for complex puzzles.

Backtracking with a pre-selection step that identifies the most promising cell.
#
**Program Operation:**

Command to run the file: "python Backtracking_Tracker_Most_Constrained.py medium.json"

# 3) sudoku_solver
**Program Structure:**
The Sudoku solver provides an interactive experience through a Tkinter GUI, where users can observe the algorithm's process, with visual cues indicating valid or invalid moves. It displays important metrics such as time taken, recursive calls, and iterations, helping users track the algorithm’s progress.
#
**Program Operation:**

Command to run the file: "python sudoku_solver.py"

# 4) sudoku_solver_comparision
Gives the comparision between the algorithms like AC-3 and Backtracking in terms of efficiency.
