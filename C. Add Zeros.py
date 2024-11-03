def solve():
    n = int(input())
    a = [(0, 0)] * (n + 1)

    for i in range(1, n + 1):
        x = int(input())
        a[i] = (x, i - 1)

    a = sorted(a[1:])  # Sort from index 1 to n (ignore a[0])

    dp = {n: True}  # Initialize dp map with n as True

    for i in range(1, n):  # Start from index 1 to n-1 (0-based)
        if a[i][0] == n + 1 - (i + 1) and a[i][0] in dp:
            dp[a[i][0] + a[i][1]] = True

    ans = 0
    for x, y in dp.items():
        if y:
            ans = max(ans, x)

    print(ans)


if __name__ == "__main__":
    tests = int(input())
    for _ in range(tests):
        solve()

