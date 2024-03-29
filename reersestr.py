def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

# Example usage:
string = input("Enter a string to reverse: ")
reversed_string = reverse_string(string)
print("Reversed string:", reversed_string)
