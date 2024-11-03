t = int(input())
for _ in range(t):
    n, m, a, b = map(int, input().split())
    ans = 0
    ans += m - b
    ans += (n - a) * (m - 1)
    ans += (n - a) * m
    print(ans)
