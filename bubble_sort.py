def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage:
arr = [int(x) for x in input("Enter the elements of the array separated by space: ").split()]
bubble_sort(arr)
print("Array after sorting:", arr)
