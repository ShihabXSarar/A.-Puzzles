t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    possible = True
    for i in range(n - 1):
        if arr[i + 1] - arr[i] > 1:
            possible = False
            break

    if possible:
        print("YES")
    else:
        print("NO")
