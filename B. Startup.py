from collections import defaultdict

def solve(n, k, b):
    m = defaultdict(list)
    for x, y in b:
        m[x].append(y)

    a = []
    for values in m.values():
        values.sort(reverse=True)
        a.append(sum(values))

    a.sort(reverse=True)
    return sum(a[:min(n, len(a))])

if __name__ == "__main__":
    t = int(input())
    results = []

    for _ in range(t):
        n, k = map(int, input().split())
        b = []
        for _ in range(k):
            b.append(tuple(map(int, input().split())))
        results.append(solve(n, k, b))

    for result in results:
        print(result)