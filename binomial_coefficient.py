def binomial_coefficient(n, k):
    # Create a 2D table to store results of subproblems
    C = [[0 for _ in range(k+1)] for _ in range(n+1)]

    # Calculate binomial coefficient values bottom-up
    for i in range(n+1):
        for j in range(min(i, k)+1):
            # Base cases
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                # Calculate the coefficient using the recurrence relation
                C[i][j] = C[i-1][j-1] + C[i-1][j]

    return C[n][k]

# Example usage:
n = 5
k = 2
print("Binomial coefficient of", n, "choose", k, "is", binomial_coefficient(n, k))
