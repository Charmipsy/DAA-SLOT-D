def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example usage:
arr = sorted([int(x) for x in input("Enter sorted list of integers separated by space: ").split()])
target = int(input("Enter the target number to search: "))
result = binary_search(arr, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found in the list.")
