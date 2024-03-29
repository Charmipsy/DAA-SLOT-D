def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
arr = [int(x) for x in input("Enter the elements of the array separated by space: ").split()]
selection_sort(arr)
print("Array after sorting:", arr)
