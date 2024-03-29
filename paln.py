def is_palindrome(s):

    s = ''.join(char.lower() for char in s if char.isalnum())
    
    return s == s[::-1]

string = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
