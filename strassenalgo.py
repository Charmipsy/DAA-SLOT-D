def split_matrix(matrix):
    """Split a given matrix into four quadrants."""
    rows, cols = len(matrix), len(matrix[0])
    mid_row, mid_col = rows // 2, cols // 2

    top_left = [row[:mid_col] for row in matrix[:mid_row]]
    top_right = [row[mid_col:] for row in matrix[:mid_row]]
    bottom_left = [row[:mid_col] for row in matrix[mid_row:]]
    bottom_right = [row[mid_col:] for row in matrix[mid_row:]]

    return top_left, top_right, bottom_left, bottom_right

def add_matrices(matrix1, matrix2):
    """Add two matrices."""
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def subtract_matrices(matrix1, matrix2):
    """Subtract one matrix from another."""
    return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def strassen_multiply(matrix1, matrix2):
    """Strassen's algorithm for matrix multiplication."""
    if len(matrix1) == 1:
        return [[matrix1[0][0] * matrix2[0][0]]]

    # Split matrices into quadrants
    a, b, c, d = split_matrix(matrix1)
    e, f, g, h = split_matrix(matrix2)

    # Compute the products of the quadrants
    p1 = strassen_multiply(a, subtract_matrices(f, h))
    p2 = strassen_multiply(add_matrices(a, b), h)
    p3 = strassen_multiply(add_matrices(c, d), e)
    p4 = strassen_multiply(d, subtract_matrices(g, e))
    p5 = strassen_multiply(add_matrices(a, d), add_matrices(e, h))
    p6 = strassen_multiply(subtract_matrices(b, d), add_matrices(g, h))
    p7 = strassen_multiply(subtract_matrices(a, c), add_matrices(e, f))

    # Compute the result quadrants
    top_left = add_matrices(subtract_matrices(add_matrices(p5, p4), p2), p6)
    top_right = add_matrices(p1, p2)
    bottom_left = add_matrices(p3, p4)
    bottom_right = subtract_matrices(subtract_matrices(add_matrices(p1, p5), p3), p7)

    # Combine the result quadrants
    result = []
    for i in range(len(top_left)):
        result.append(top_left[i] + top_right[i])
    for i in range(len(bottom_left)):
        result.append(bottom_left[i] + bottom_right[i])

    return result

# Example usage:
matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

matrix2 = [
    [17, 18, 19, 20],
    [21, 22, 23, 24],
    [25, 26, 27, 28],
    [29, 30, 31, 32]
]

result = strassen_multiply(matrix1, matrix2)
for row in result:
    print(row)
