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


# Finds all valid paths in the grid using an exhaustive search
# Takes a list of lists representing the field grid as a parameter
# Returns the total number of valid paths and a list for each valid path sequence represented by right arrows and down arrows
def soccer_exhaustive(field):
    # Find number of rows in the grid
    r = len(field)
    # Find number of columns in the grid
    c = len(field[0])
    # Formula to calculate the number of moves required to reach the bottom-right corner
    n = r + c - 2
    # Represents the number of valid paths
    counter = 0
    # List of lists for storing valid paths as a set of moves
    valid_paths = []

    # Generates every possible sequence of moves for the given field represented by binary numbers
    for bits in range(2**n):
        # Start at top left cell
        current_row = 0
        current_col = 0
        # Track the current path with a list of down arrows and right arrow characters
        path = []
        # Initially assume path is valid
        valid = True

        # Turn the binary number into a sequence of arrows
        # If the kth bit is a 1 it becomes a down arrow
        # Otherwise, it is a 0 and becomes a right arrow
        # The arrow is appended to the list named path
        for k in range(n):
            if (bits >> k) & 1:
                current_row += 1
                path.append("↓")
            else:
                current_col += 1
                path.append("→")

            # If position is no longer within the bounds of the grid...
            # Or the position is moved to a blocked cell...
            # Program marks current path as invalid
            if (
                current_row >= r
                or current_col >= c
                or field[current_row][current_col] in {"X", "x"}
            ):
                valid = False
                break
        # If the path ends at the bottom right corner unobstructed...
        # Total number of valid paths is incremented by 1
        # Current path list gets added to valid_path list of lists
        if valid and current_row == r - 1 and current_col == c - 1:
            counter += 1
            valid_paths.append(path)
    # Returns the total number of valid paths as well as the arrow sequences for each valid path
    return counter, valid_paths


# 3x3 grid
# represented by a list of lists
field = [[".", ".", "X"], [".", "X", "."], [".", ".", "."]]


"""
# 9x8 grid from example in directions
field = [
    [".", ".", ".", ".", ".", ".", "X", ".", "X"],
    ["X", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "X", ".", ".", ".", "X", "."],
    [".", ".", "X", ".", ".", ".", ".", "X", "."],
    [".", "X", ".", ".", ".", ".", "X", ".", "."],
    [".", ".", ".", ".", "X", ".", ".", ".", "."],
    [".", ".", "X", ".", ".", ".", ".", ".", "X"],
    [".", ".", ".", ".", ".", ".", ".", ".", "."]
]
"""

"""
# Completely open field
field = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
"""

"""
# One row field with path blocked by an 'X'
field = [".", ".", "X", ".", "."]
"""

# Check if the input grid of the field is valid
# If it is invalid print an error message
if not validate_field(field):
    print("Invalid field.")

else:
    # If the grid  is valid find all valid paths using an exhaustive search
    valid_paths_count, valid_paths_sequences = soccer_exhaustive(field)
    # Print message when no valid paths exist
    if valid_paths_count == 0:
        print("No valid paths exist.")
    # Otherwise print number of valid paths as well as each valid path arrow sequence
    else:
        print(f"Total valid paths: {valid_paths_count}")
        print("Valid paths:")
        count = 1
        # Turns each arrow sequence into a string before printing
        for path in valid_paths_sequences:
            print("Path {}: ".format(count), end="")
            print(" ".join(path))
            count += 1
