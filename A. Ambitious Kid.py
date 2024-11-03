import sys
n = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
if 0 in A:
    print(0)
else:
    min_abs_value = float('inf')
    for a in A:
        min_abs_value = min(min_abs_value, abs(a))

    print(min_abs_value)
