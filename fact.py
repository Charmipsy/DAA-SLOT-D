def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Example usage:
num = int(input("Enter a number to find its factorial: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", num, "is", factorial(num))
def find_max_min(arr, start, end):
    # Base case: If the list contains only one element
    if start == end:
        return arr[start], arr[start]

    # Base case: If the list contains only two elements
    if end == start + 1:
        return (arr[start], arr[end]) if arr[start] < arr[end] else (arr[end], arr[start])

    # Divide the array into two halves
    mid = (start + end) // 2
    max_left, min_left = find_max_min(arr, start, mid)
    max_right, min_right = find_max_min(arr, mid + 1, end)

    # Find maximum and minimum from the results of two halves
    max_value = max(max_left, max_right)
    min_value = min(min_left, min_right)

    return max_value, min_value

# Example usage:
arr = [3, 5, 1, 9, 2, 7, 4, 8, 6]
max_val, min_val = find_max_min(arr, 0, len(arr) - 1)
print("Maximum value in the list:", max_val)
print("Minimum value in the list:", min_val)
