def odd(n):
    while n % 2 == 0:
        n //= 2
    return n > 1
t = int(input())
for _ in range(t):
    n = int(input())
    print("YES" if odd(n) else "NO")