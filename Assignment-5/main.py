def print_board(board, step_description=""):
    """Prints the current state of the board with an optional description."""
    if step_description:
        print(step_description)
    for row in board:
        print(" ".join(row))
    print("-" * 25)

def is_safe(board, row, col, n):
    """Checks if a queen can be safely placed at board[row][col]."""
    # Check the current row on the left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check the lower-left diagonal
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens_util(board, col, n, solutions):
    """Recursive utility to solve N-Queens and log intermediate steps."""
    # Base case: If all queens are placed across all columns, save it
    if col == n:
        valid_solution = [" ".join(row) for row in board]
        solutions.append(valid_solution)
        print_board(board, "\n*** VALID SOLUTION FOUND IN THE SPACE ***")
        return

    # Try placing a queen in all rows of the current column one by one
    for row in range(n):
        print(f"Evaluating: Row {row}, Col {col}...")
        
        if is_safe(board, row, col, n):
            # Move forward: Place the queen
            board[row][col] = 'Q'
            print_board(board, f"--> PLACED queen at ({row}, {col}). Intermediate state:")
            
            # Recurse to the next column
            solve_n_queens_util(board, col + 1, n, solutions)
            
            # Backtrack: Remove the queen to explore other branches/solutions
            board[row][col] = '.'
            print_board(board, f"<-- BACKTRACKING: Removed queen from ({row}, {col}). Intermediate state:")
        else:
            print(f"    [!] Unsafe to place at ({row}, {col}) due to attacks.")

def main():
    print("=== N-Queens Backtracking Solver ===")
    
    # Assignment Requirement: Take user input n value
    try:
        n = int(input("Enter the value of n (must be > 1): "))
        
        # Assignment Requirement: Show the solution space for n > 1
        if n <= 1:
            print("Invalid input. The value of n must be strictly greater than 1.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    # Initialize an empty n x n board represented by '.'
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    print(f"\n--- Starting Search for {n}x{n} Board ---\n")
    
    # Trigger the backtracking algorithm starting at column 0
    # Assignment Requirement: Show all intermediate steps (handled inside the util function)
    solve_n_queens_util(board, 0, n, solutions)

    # Output the final accumulated solution space
    print("\n=========================================")
    print(f"FINAL SOLUTION SPACE FOR n={n}")
    print("=========================================")
    
    if not solutions:
        print(f"No solutions exist for n={n}.")
    else:
        print(f"Found {len(solutions)} distinct valid solution(s):\n")
        for idx, solution in enumerate(solutions):
            print(f"Solution {idx + 1}:")
            for row in solution:
                print(row)
            print()

if __name__ == "__main__":
    main()