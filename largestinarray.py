def find_largest(arr):
    if not arr:
        return "Array is empty"
    
    max_element = arr[0]
    for element in arr:
        if element > max_element:
            max_element = element
    
    return max_element

# Example usage:
array = [int(x) for x in input("Enter the elements of the array separated by space: ").split()]
largest_element = find_largest(array)
print("The largest element in the array is:", largest_element)
