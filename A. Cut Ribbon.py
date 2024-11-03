def max_ribbon_pieces(n, a, b, c):
    # Initialize dp array with -1 (indicating no valid cutting)
    dp = [-1] * (n + 1)
    dp[0] = 0  # Base case: 0 length has 0 pieces

    # Iterate over all lengths from 1 to n
    for i in range(1, n + 1):
        if i >= a:
            dp[i] = max(dp[i], dp[i - a] + 1)
        if i >= b:
            dp[i] = max(dp[i], dp[i - b] + 1)
        if i >= c:
            dp[i] = max(dp[i], dp[i - c] + 1)

    # The answer is the value at dp[n]
    return dp[n]

# Input
n, a, b, c = map(int, input().split())

# Output the result
print(max_ribbon_pieces(n, a, b, c))
