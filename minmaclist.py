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
