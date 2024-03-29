def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def print_fibonacci_series(count):
    if count <= 0:
        print("Invalid input. Count should be a positive integer.")
        return
    else:
        print("Fibonacci Series:")
        for i in range(count):
            print(fibonacci(i), end=" ")

# Example usage:
count = 10  # Change the count to the desired number of Fibonacci numbers
print_fibonacci_series(count)
