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

def read_matrix(rows, cols, matrix_name="matrix"):
    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Enter row {i + 1}: ").strip()
            values = row_input.split()
            if len(values) != cols:
                print(f"Error: Please enter exactly {cols} values.")
                continue
            try:
                row = [int(value) for value in values]
                matrix.append(row)
                break
            except ValueError:
                print("Error: Please enter only integer values.")
    return matrix


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    return transposed


def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0]) if rows > 0 else 0
    result = []
    for i in range(rows):
        row_sum = []
        for j in range(cols):
            row_sum.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row_sum)
    return result


def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0]) if rows_a > 0 else 0
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0]) if rows_b > 0 else 0

    result = []
    for i in range(rows_a):
        result_row = []
        for j in range(cols_b):
            value = 0
            for k in range(cols_a):
                value += matrix_a[i][k] * matrix_b[k][j]
            result_row.append(value)
        result.append(result_row)
    return result


def print_matrix(matrix):
    if not matrix:
        print("[]")
        return
    col_widths = [0] * len(matrix[0])
    for row in matrix:
        for j, value in enumerate(row):
            col_widths[j] = max(col_widths[j], len(str(value)))

    for row in matrix:
        row_text = "  ".join(str(value).rjust(col_widths[j]) for j, value in enumerate(row))
        print(row_text)


def read_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Error: Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid integer.")


def main():
    # Part A: Transpose a matrix
    print("Part A — Transpose a Matrix")
    rows = read_positive_int("Enter number of rows: ")
    cols = read_positive_int("Enter number of columns: ")
    matrix = read_matrix(rows, cols)
    print("\nOriginal Matrix:")
    print_matrix(matrix)
    transposed = transpose_matrix(matrix)
    print("\nTransposed Matrix:")
    print_matrix(transposed)

    # Part B: Add two matrices
    print("\nPart B — Add Two Matrices")
    print(f"Enter the first {rows}x{cols} matrix:")
    matrix_a = read_matrix(rows, cols)
    print(f"Enter the second {rows}x{cols} matrix:")
    matrix_b = read_matrix(rows, cols)
    summed = add_matrices(matrix_a, matrix_b)
    print("\nSum of matrices:")
    print_matrix(summed)

    # Part C: Multiply two matrices
    print("\nPart C — Multiply Two Matrices")
    rows_a = read_positive_int("Enter number of rows for matrix A: ")
    cols_a = read_positive_int("Enter number of columns for matrix A: ")
    rows_b = read_positive_int("Enter number of rows for matrix B: ")
    cols_b = read_positive_int("Enter number of columns for matrix B: ")

    if cols_a != rows_b:
        print("Error: Number of columns in A must equal number of rows in B.")
        return

    print("Enter matrix A:")
    matrix_a = read_matrix(rows_a, cols_a)
    print("Enter matrix B:")
    matrix_b = read_matrix(rows_b, cols_b)
    product = multiply_matrices(matrix_a, matrix_b)
    print("\nProduct A × B:")
    print_matrix(product)


if __name__ == "__main__":
    main()

