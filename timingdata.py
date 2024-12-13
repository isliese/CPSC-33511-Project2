
import time
import random

# Validate the grid (same as the one from your previous code)
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

# Function to generate a random grid of size n x n
def generate_grid(n):
    grid = []
    for i in range(n):
        grid.append([random.choice(['.', 'X']) for _ in range(n)])
    return grid

# Function to time the algorithm on grids of different sizes
def time_algorithm_for_sizes(sizes, algorithm):
    timings = []
    for n in sizes:
        if not validate_field(grid):
            print(f"Invalid field for grid size {n} x {n}.")
            continue
        
        # Measuring execution time
        start_time = time.time()
        if algorithm == "dp":
            valid_paths_count = soccer_dyn_prog(grid)
        elif algorithm == "exhaustive":
            valid_paths_count, _ = soccer_exhaustive(grid)
        end_time = time.time()

        elapsed_time = end_time - start_time
        timings.append((n, elapsed_time))
        print(f"Using {algorithm} algorithm, grid size {n} x {n} took {elapsed_time:.6f} seconds. Paths: {valid_paths_count}")
    return timings

# Define different grid sizes (in terms of n x n)
sizes = [10, 100, 1000, 5000, 7500, 10000]

# Generate random grid of size n x n
grid = generate_grid(n)  

# Time both algorithms
dp_timing_data = time_algorithm_for_sizes(sizes, algorithm="dp")
exhaustive_timing_data = time_algorithm_for_sizes(sizes, algorithm="exhaustive")

# Save collected data into separate files
with open('dp_timing_results.txt', 'w') as f:
    for n, t in dp_timing_data:
        f.write(f"{n}x{n}: {t:.6f} seconds\n")
    print("Dynamic Programming execution times saved to 'dp_timing_results.txt'")

with open('exhaustive_timing_results.txt', 'w') as f:
    for n, t in exhaustive_timing_data:
        f.write(f"{n}x{n}: {t:.6f} seconds\n")
    print("Exhaustive search execution times saved to 'exhaustive_timing_results.txt'")
