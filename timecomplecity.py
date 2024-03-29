ef multiply_matrices_time_complexity(m, n, p):
    time_complexity = m * p * n
    return time_complexity

# Example usage:
m = int(input("Enter the number of rows in matrix A: "))
n = int(input("Enter the number of columns in matrix A (and rows in matrix B): "))
p = int(input("Enter the number of columns in matrix B: "))

time_complexity = multiply_matrices_time_complexity(m, n, p)
print("Time complexity of multiplying two matrices of size", m, "x", n, "and", n, "x", p, "is:", time_complexity)
