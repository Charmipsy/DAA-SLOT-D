def count_digits(num):
    if num == 0:
        return 0
    return 1 + count_digits(num // 10)

def is_armstrong(num, n):
    if num == 0:
        return 0
    return (num % 10) ** n + is_armstrong(num // 10, n)

def check_armstrong(num):
    num_of_digits = count_digits(num)
    sum_of_powers = is_armstrong(num, num_of_digits)
    return sum_of_powers == num

# Example usage:
num = int(input("Enter a number to check if it's an Armstrong number: "))
if check_armstrong(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
