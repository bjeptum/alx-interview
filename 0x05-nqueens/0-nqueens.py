#!/usr/bin/python3
"""
N Queens Problem Module
"""
import sys


def is_safe(board, row, col, N):
    """
    Function to check if it's safe to place a queen at board[row][col]
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# Backtracking function to solve N-Queens


def solve_n_queens_util(board, col, N, solutions):
    # If all queens are placed, add the solution to the list
    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    # Try placing a queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place a queen
            board[i][col] = 1

            # Recur to place the rest of the queens
            solve_n_queens_util(board, col + 1, N, solutions)

            # If placing queen in board[i][col] doesn't lead to a solution
            # Remove the queen (Backtrack)
            board[i][col] = 0

# Solve N-Queens and return all solutions


def solve_n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)
    return solutions

# Main function to handle user input and output solutions


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(N)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
