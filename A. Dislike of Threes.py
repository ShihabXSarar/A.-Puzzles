def seive(n):
    numbers = []
    i = 1
    while len(numbers) < 1001:
        if i % 3 != 0 and i % 10 != 3:
            numbers.append(i)
        i += 1
    return numbers[n]
t = int(input())
for _ in range(t):
    n = int(input())
    print(seive(n-1))
