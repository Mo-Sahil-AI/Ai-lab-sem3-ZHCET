# N-Queens Backtracking Visualizer

A Python implementation of the classic N-Queens problem that solves the board while visually logging the algorithm's step-by-step process. This tool demonstrates exactly how backtracking works by printing every queen placement, dead end, and backtrack step in real-time.

## Features

* **Dynamic Board Size:** Takes standard user input to generate any `n x n` board configuration (where `n > 1`).
* **Algorithmic Visualization:** Prints the 2D grid at every step in the process, revealing the exact trial-and-error pathway the computer takes.
* **Complete Solution Space:** Exhaustively checks all possibilities to find and display every valid board configuration, rather than stopping at the first discovered solution.

## Prerequisites

* Python 3.x installed on your local machine. No external libraries or dependencies are required.

## Installation & Usage

1. Save the provided Python code to a file named `main.py` on your computer.
2. Open your terminal or command prompt, navigate to the folder where you saved the file, and execute the script:
   ```bash
   python main.py



## How It Works

This solver implements a classic Backtracking approach, progressing step-by-step and actively reversing course whenever a rule is violated:

* **Moving Forward:** The algorithm processes the board one column at a time, strictly from left to right. It scans the current column from top to bottom and places a queen in the first cell that is entirely safe (not under horizontal or diagonal attack by any previously placed queens).
* **Identifying Dead Ends:** If every single row in a given column is under attack, the algorithm recognizes that the current board configuration is a dead end and cannot yield a valid solution.
* **Backtracking:** Upon hitting a dead end, the algorithm retreats to the previous column. It picks up the queen it just placed, clears that cell, and attempts to move the queen down to the next available safe row before moving forward again.
* **Recording Solutions:** When the algorithm successfully advances past the final column (`col == n`), it means all queens have been safely placed. The program saves this valid board state and then intentionally triggers a backtrack, forcing the algorithm to continue searching until every possible layout has been discovered.