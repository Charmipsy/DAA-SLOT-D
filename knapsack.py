def knapsack_greedy(weights, values, capacity):
    """
    Solves the 0/1 Knapsack problem using a greedy approach.
    """
    n = len(weights)
    # Calculate value density for each item
    value_density = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    # Sort items by value density in descending order
    value_density.sort(reverse=True)

    total_value = 0
    total_weight = 0
    selected_items = []

    for vd, weight, value in value_density:
        if total_weight + weight <= capacity:
            selected_items.append((weight, value))
            total_weight += weight
            total_value += value
        else:
            # Fraction of the item that fits in the knapsack
            fraction = (capacity - total_weight) / weight
            selected_items.append((weight * fraction, value * fraction))
            total_weight = capacity
            total_value += value * fraction
            break

    return total_value, selected_items

# Example usage:
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

max_value, selected_items = knapsack_greedy(weights, values, capacity)
print("Maximum value achievable:", max_value)
print("Selected items (weight, value):", selected_items)
