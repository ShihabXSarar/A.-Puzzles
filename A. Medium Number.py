t = int(input())
for _ in range(t):
    arr = list(map(int,input().split()))
    ans = sorted(set(arr))[-2]
    print(ans)