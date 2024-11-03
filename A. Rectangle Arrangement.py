t = int(input())

for _ in range(t):
    n = int(input())
    max_w = 0
    max_h = 0
    for _ in range(n):
        wi, hi = map(int, input().split())
        max_w = max(max_w, wi)
        max_h = max(max_h, hi)
    p = 2 * (max_w + max_h)
    print(p)

