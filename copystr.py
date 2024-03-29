def copy_string(source, destination, index=0):
    if index == len(source):
        return destination
    else:
        destination += source[index]
        return copy_string(source, destination, index + 1)

# Example usage:
source_str = input("Enter the source string: ")
destination_str = copy_string(source_str, "")
print("Copied string:", destination_str)
