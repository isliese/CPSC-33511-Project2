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


def soccer_dynamic(field):
    # Find number of rows in the grid
    r = len(field)
    # Find number of columns in the grid
    c = len(field[0])
    # ...



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
