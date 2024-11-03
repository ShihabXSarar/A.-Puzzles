def min_operations(n, p):
    visited = [False] * n
    cycles = 0

    for i in range(n):
        if not visited[i]:
            cycles += 1
            j = i
            while not visited[j]:
                visited[j] = True
                j = p[j] - 1

    return n - cycles


# Reading input
import sys

input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1

results = []
for _ in range(t):
    n = int(data[index])
    p = list(map(int, data[index + 1:index + n + 1]))
    index += n + 1
    results.append(min_operations(n, p))

# Output results
for result in results:
    print(result)
