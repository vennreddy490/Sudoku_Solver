# Sudoku_Solver

**Authors**: Venn Reddy, Sravanthi Pallabothu, Nikhila Raj

**General Project Information**: \
This project is split into 2 key parts: solvers and visualizers. The programs are denoted below, but the project is intentionally designed so that you can run each program to demonstrate a different implementation. For Backtracking_Tracker_Brute_Force.py, Backtracking_Tracker_Most_Constrained.py, and visualizer_MRV.py, you can run them and edit a blank board manually, or pass in a level (as shown below). 

We've tried to keep our documentation clear in our code in in-line comments, but most of our documentation can be found in method docstrings, especially since the methods are short and very modularized. 

 ### 1) Backtracking_Tracker_Brute_Force.py
**Program Structure:**
 
 **SudokuSolver:** Backtracking-based solver with methods for validation, finding empty cells, and solving while tracking iterations and backtracks.
 **SudokuGUI:** Interactive Tkinter-based GUI for input, solving, and displaying results, including performance plots.
 **Utilities:** File handling to load puzzles from JSON, and plotting for iterations and backtracks over time.

**Program Operation:** \
Users can input a puzzle through the GUI or load a predefined board. The program solves it using backtracking while tracking metrics like iterations and backtracks. Results, including the solution, solving time, and stats, are displayed in the GUI, with optional visual plots. It also handles unsolvable puzzles and insufficient data gracefully.

**Command to run the file**:\
Option 1) ```python Backtracking_Tracker_Brute_Force.py``` (for blank board) \
Option 2) ```python Backtracking_Tracker_Brute_Force.py medium.json``` (to pass in "medium" level from the levels/ directory.)

 ### 2) Backtracking_Tracker_Most_Constrained.py
**Program Structure:**\
Uses find_most_constrained_empty to prioritize the most constrained cell (the one with the fewest valid options).\
 Introduces a heuristic to reduce the search space by evaluating constraints before placing numbers.\
  More efficient due to the heuristic, particularly for complex puzzles. Backtracking with a pre-selection step that identifies the most promising cell.

**Program Operation:**\
Same operation as above program.

**Command to run the file**:\
Option 1) ```python Backtracking_Tracker_Most_Constrained.py``` (for blank board) \
Option 2) ```python Backtracking_Tracker_Most_Constrained.py medium.json``` (to pass in "medium" level from the levels/ directory.)

### 3) Backtracking_Tracker_Propagation.py
**Program Structure:**\
AC-3 implementaion ensures arc consistency in constraint satisfaction problems by iteratively pruning variable domains. It checks all arcs, removing values from a variable's domain that are inconsistent with connected variables, and propagates changes to related arcs. \
Also utilizes forward checking during backtracking to remove inconsistent values from connected variables' domains as a variable is assigned. While forward checking is a more localized method that prunes during assignment, AC-3 performs global constraint propagation before assignments, offering stronger pruning and potentially reducing search space more effectively.

**Program Operation:**\
Runs a board using CSP automatically (no user input). Can load a level by modifying the "board" passed in to a solver in the main method.

**Command to run the file**:\
``` python Backtracking_Tracker_Most_Propagation.py```

### 4) visualizer_Brute_Force.py
**Program Structure:**
The Sudoku solver provides an interactive experience through a Tkinter GUI, where users can observe the algorithm's process, with visual cues indicating valid or invalid moves. It displays important metrics such as time taken, recursive calls, and iterations, helping users track the algorithm’s progress.

**Program Operation:** \
Same operation as above programs, although cannot load preset level.

**Command to run the file:**\
```python visualizer_Brute_Force.py```

### 5) visualizer_MRV.py
**Program Structure:**
Similar to the visualizer.py program above, although uses the Minimum Remaining Values variable selection ordering to improve operation and efficiency. Can also be used with a preset level.

**Program Operation:** \
Same operation as above program, and allows user to pass in preset level.

**Command to run the file:**\
Option 1) ```python visualizer_MRV.py``` (for blank board) \
Option 2) ```python visualizer_MRV.py medium.json``` (to pass in "medium" level from the levels/ directory.)
