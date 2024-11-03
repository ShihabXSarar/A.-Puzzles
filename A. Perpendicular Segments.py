t = int(input())
for _ in range(t):
    a, b, k = map(int, input().split())
    val = min(a, b)
    print(f"0 {val} {val} 0")
    print(f"0 0 {val} {val}")

