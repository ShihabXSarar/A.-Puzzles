def is_composite(num):
    if num < 4:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return True
    return False

def find_composite_pair(n):
    for x in range(4, n):
        y = n - x
        if is_composite(x) and is_composite(y):
            return x, y

n = int(input())
x, y = find_composite_pair(n)
print(x, y)
