# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def get_matrix(name):
    """Reads matrix dimensions and values from user input."""
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        if len(row) != cols:
            raise ValueError(f"Expected {cols} values, got {len(row)}.")
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    """Displays a 2D list in a neat, aligned grid."""
    if not matrix:
        return
    max_width = max(len(str(val)) for row in matrix for val in row)
    for row in matrix:
        print(" ".join(f"{val:>{max_width}}" for val in row))

def transpose_matrix(matrix):
    """Part A: Flips rows and columns."""
    if not matrix:
        return []
    rows, cols = len(matrix), len(matrix[0])
    transposed = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    return transposed

def add_matrices(mat1, mat2):
    """Part B: Element-wise addition of two identical-sized matrices."""
    rows, cols = len(mat1), len(mat1[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = mat1[i][j] + mat2[i][j]
    return result

def multiply_matrices(mat1, mat2):
    """Part C: Dot product of two matrices."""
    rows_a, cols_a = len(mat1), len(mat1[0])
    rows_b, cols_b = len(mat2), len(mat2[0])
    
    if cols_a != rows_b:
        raise ValueError("Cannot multiply: Columns of A must equal Rows of B.")
        
    result = [[0] * cols_b for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result

if __name__ == "__main__":
    # PART A
    print("--- PART A: TRANSPOSE ---")
    mat_a = get_matrix("Matrix A")
    print("Original Matrix:")
    print_matrix(mat_a)
    print("Transposed Matrix:")
    print_matrix(transpose_matrix(mat_a))
    print("\n")

    # PART B
    print("--- PART B: ADDITION ---")
    print("Enter dimensions for Matrix 1:")
    mat_b1 = get_matrix("Matrix 1")
    print("Enter dimensions for Matrix 2 (must match Matrix 1):")
    mat_b2 = get_matrix("Matrix 2")
    if len(mat_b1) != len(mat_b2) or len(mat_b1[0]) != len(mat_b2[0]):
        print("Error: Matrices must be the same size for addition.")
    else:
        print("Sum Matrix:")
        print_matrix(add_matrices(mat_b1, mat_b2))
    print("\n")

    # PART C
    print("--- PART C: MULTIPLICATION ---")
    print("Enter dimensions for Matrix A (M x N):")
    mat_c1 = get_matrix("Matrix A")
    print(f"Enter dimensions for Matrix B (N x {len(mat_c1[0])}):")
    # Forcing the user to input the correct N for rows to prevent crashes
    rows_b = len(mat_c1[0]) 
    cols_b = int(input("Enter number of columns: "))
    mat_c2 = []
    for i in range(rows_b):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        mat_c2.append(row)
        
    print("Product Matrix (A x B):")
    print_matrix(multiply_matrices(mat_c1, mat_c2))

