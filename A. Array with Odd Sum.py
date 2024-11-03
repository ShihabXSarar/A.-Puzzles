t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    odd_count = sum(1 for x in a if x % 2 != 0)
    even_count = n - odd_count
    if odd_count == 0 or (odd_count % 2 == 0 and even_count == 0):
        print("NO")
    else:
        print("YES")
