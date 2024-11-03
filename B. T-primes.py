import math

MAX_LIMIT = int(1e6) + 1
is_prime = [True] * MAX_LIMIT
is_prime[0] = is_prime[1] = False

for i in range(2, int(math.sqrt(MAX_LIMIT)) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_LIMIT, i):
            is_prime[j] = False

t_primes = set(i * i for i in range(MAX_LIMIT) if is_prime[i])

n = int(input())
arr = map(int, input().split())

for x in arr:
    if x in t_primes:
        print("YES")
    else:
        print("NO")
