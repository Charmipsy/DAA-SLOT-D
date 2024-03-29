import sys

def optimal_bst(keys, freq):
    n = len(keys)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][i] = freq[i - 1]

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = sys.maxsize
            freq_sum = sum(freq[i - 1:j])

            for k in range(i, j + 1):
                cost = freq_sum + (dp[i][k - 1] if k > i else 0) + (dp[k + 1][j] if k < j else 0)
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[1][n]

# Example usage:
keys = [10, 12, 20, 35]
freq = [34, 8, 50, 28]
print("Cost of optimal BST:", optimal_bst(keys, freq))
