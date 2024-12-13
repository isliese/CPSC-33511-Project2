import time
import random

# Validate the grid
def validate_field(field):
    if not field or not field[0]:
        return False
    c = len(field[0])
    for row in field:
        if len(row) != c:
            return False
        for char in row:
            if char not in {".", "X", "x"}:
                return False
    return True

# Dynamic Programming solution for counting valid paths
def soccer_dyn_prog(field):
    r = len(field)
    c = len(field[0])
    if field[0][0] == "X" or field[r-1][c-1] == "X":
        return 0
    A = [[0] * c for _ in range(r)]
    A[0][0] = 1

    for i in range(r):
        for j in range(c):
            if field[i][j] == "X":
                A[i][j] = 0
            else:
                if i > 0:
                    A[i][j] += A[i-1][j]
                if j > 0:
                    A[i][j] += A[i][j-1]
    return A[r-1][c-1]

# Exhaustive search for counting valid paths
def soccer_exhaustive(field):
    r = len(field)
    c = len(field[0])
    n = r + c - 2
    counter = 0
    valid_paths = []

    for bits in range(2**n):
        current_row = 0
        current_col = 0
        path = []
        valid = True

        for k in range(n):
            if (bits >> k) & 1:
                current_row += 1
                path.append("↓")
            else:
                current_col += 1
                path.append("→")

            if (
                current_row >= r
                or current_col >= c
                or field[current_row][current_col] in {"X", "x"}
            ):
                valid = False
                break
        if valid and current_row == r - 1 and current_col == c - 1:
            counter += 1
            valid_paths.append(path)
    
    return counter, valid_paths

# Function to generate a controlled grid of size n x n
def generate_controlled_grid(n):
    grid = [["." for _ in range(n)] for _ in range(n)]
    for row in grid:
        row[n // 2] = "X"
    return grid

# Function to time the DP algorithm on grids of different sizes
def time_dp_algorithm(dp_sizes, output_file):
    with open(output_file, 'a') as f:
        for n in dp_sizes:
            grid = generate_controlled_grid(n)

            if not validate_field(grid):
                print(f"Invalid field for grid size {n} x {n}.")
                continue

            # Measuring execution time for Dynamic Programming
            start_time = time.time()
            dp_count = soccer_dyn_prog(grid)
            dp_time = time.time() - start_time

            result = f"{n}x{n}: {dp_time:.6f} seconds\n"
            f.write(result)
            print(f"Using dp algorithm, grid size {n} x {n} took {dp_time:.6f} seconds.")

# Function to time the Exhaustive Search algorithm on grids of different sizes
def time_exhaustive_algorithm(exhaustive_sizes, output_file):
    with open(output_file, 'a') as f:
        for n in exhaustive_sizes:
            grid = generate_controlled_grid(n)

            if not validate_field(grid):
                print(f"Invalid field for grid size {n} x {n}.")
                continue

            # Measuring execution time for Exhaustive Search
            start_time = time.time()
            exhaustive_count, _ = soccer_exhaustive(grid)
            exhaustive_time = time.time() - start_time

            result = f"{n}x{n}: {exhaustive_time:.6f} seconds\n"
            f.write(result)
            print(f"Using exhaustive algorithm, grid size {n} x {n} took {exhaustive_time:.6f} seconds.")

# Define different grid sizes for DP algorithm
dp_sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# Define different grid sizes for Exhaustive Search algorithm
exhaustive_sizes = [5, 6, 7, 8, 9, 10, 11, 12, 13]

# File to store results
output_file = 'timing_results.txt'

# Clear the output file before appending
open(output_file, 'w').close()

# Time DP algorithm
print("Timing DP algorithm...")
time_dp_algorithm(dp_sizes, output_file)

# Time Exhaustive Search algorithm
print("\nTiming Exhaustive algorithm...")
time_exhaustive_algorithm(exhaustive_sizes, output_file)
