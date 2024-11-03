import math
import numpy as np

n = int(input())
arr = np.zeros(n, dtype=int)

t = list(map(int, input().split()))
for i in range(n):
    count = 0
    arr[i] = t[i]
    check = math.ceil(math.sqrt(arr[i]))
    for j in range(2, check + 1):  # Include 'check' in the loop
        if arr[i] % j == 0:
            count += 1
            if count>1:
                break

    if count == 1:
        print("YES")
    else:
        print("NO")

