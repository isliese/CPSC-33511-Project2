# Checks the grid for valid inputs
# Takes a list of lists representing the field grid as a parameter
# Returns True if the grid is valid and returns False if it is invalid
def validate_field(field):
    # Check if the grid is empty or has no rows
    if not field or not field[0]:
        return False
    # Find number of columns in the grid
    c = len(field[0])

    # Ensures each row has the same number of columns as the first row
    for row in field:
        if len(row) != c:
            return False
        # Checks each cell for one of three valid characters
        for char in row:
            if char not in {".", "X", "x"}:
                return False

    return True


# Finds valid paths from (0,0) to (i,j) in the grid using a dynamic programming
# The number of paths to (i,j) is the sum of paths from (i-1,j) and (i,j-1), provided those cells are valid
# Takes a list of lists representing the field grid as a parameter
# Returns the total number of valid paths
def soccer_dyn_prog(field):
    # Find number of rows in the grid
    r = len(field)
    # Find number of columns in the grid
    c = len(field[0])
    # Corner case: if the start or end cell is blocked
    if field[0][0] == "X" or field[r-1][c-1] == "X":
        return 0
    
    # Initialize the DP table
    A = [[0] * c for _ in range(r)]
    # Base case: start position
    A[0][0] = 1  

    # General cases:
    for i in range(r):
        for j in range(c):
            if field[i][j] == "X":
                A[i][j] = 0  # Blocked cells
            else:
                if i > 0:  # Add paths from above
                    A[i][j] += A[i-1][j]
                if j > 0:  # Add paths from left
                    A[i][j] += A[i][j-1]

    return A[r-1][c-1]
    

# 3x3 grid
# represented by a list of lists
field = [[".", ".", "X"], [".", "X", "."], [".", ".", "."]]

# 9x8 grid from example in directions
field = [ 
['.', '.', '.', '.', '.', '.', 'X','.','X'],
['X', '.', '.', '.', '.', '.', '.', '.', '.'],
['.', '.', '.', 'X', '.', '.', '.', 'X', '.'],
['.', '.', 'X', '.', '.', '.', '.', 'X', '.'],
['.', 'X', '.', '.', '.', '.', 'X', '.', '.'],
['.', '.', '.', '.', 'X', '.', '.', '.', '.'],
['.', '.', 'X', '.', '.', '.', '.', '.', 'X'],
['.', '.', '.', '.', '.', '.', '.', '.', '.'] 
]


# Check if the input grid of the field is valid
# If it is invalid print an error message
if not validate_field(field):
    print("Invalid field.")

else:
    # If the grid  is valid find all valid paths using an exhaustive search
    valid_paths_count = soccer_dyn_prog(field)
    # Print message when no valid paths exist
    if valid_paths_count == 0:
        print("No valid paths exist.")
    # Otherwise print number of valid paths 
    else:
        print(f"Total valid paths: {valid_paths_count}")
        
