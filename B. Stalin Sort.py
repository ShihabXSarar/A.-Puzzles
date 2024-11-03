def solve():
    n = int(input())
    a = list(map(int, input().split()))
    inf = int(1e9 + 7)
    ans = inf
    for i in range(n):
        cnt = 0
        for j in range(i + 1, n):
            if a[j] > a[i]:
                cnt += 1
        ans = min(ans, cnt + i)
    print(ans)
t = int(input())
for _ in range(t):
    solve()
