def is_perfect_number(num):
    # Check for edge cases
    if num <= 1:
        return False

    # Find all divisors of the number and sum them
    divisor_sum = 1  # 1 is always a divisor
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisor_sum += i
            if i != num // i:
                divisor_sum += num // i

    # Check if the sum of divisors equals the number
    return divisor_sum == num

# Example usage:
num = 28
if is_perfect_number(num):
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")
def min_max_sequence(numbers):
    if not numbers:
        return []

    sequences = []
    current_sequence = [numbers[0]]

    for num in numbers[1:]:
        if num == current_sequence[-1] + 1:
            current_sequence.append(num)
        else:
            sequences.append((min(current_sequence), max(current_sequence)))
            current_sequence = [num]

    sequences.append((min(current_sequence), max(current_sequence)))

    return sequences

# Example usage:
numbers = [1, 2, 3, 6, 7, 8, 10, 11, 12, 15]
sequences = min_max_sequence(numbers)
for sequence in sequences:
    print("Minimum:", sequence[0], " Maximum:", sequence[1])
