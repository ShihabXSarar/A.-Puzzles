# ==================================================
#              COMPETITIVE PROGRAMMING
# ==================================================
"""
Author: ${"Shihab Sarar"}
Created on: 11/1/2024
Description: 
"""
# ==================================================
import sys
import math
from collections import defaultdict, deque
from heapq import heappop, heappush


# ==================================================
#                    UTILITY FUNCTIONS
# ==================================================


# ==================================================
#                    SOLUTION FUNCTION
# ==================================================

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = n
    l, r = 1, n
    while l <= r:
        mid = (l + r) // 2
        found = False
        if mid == 1:
            ans = min(ans, n - 1)
            l = mid + 1
            continue
        for i in range(n - mid + 1):
            if a[i] + a[i + 1] > a[i + mid - 1]:
                found = True
                break
        if found:
            ans = min(ans, n - mid)
            l = mid + 1
        else:
            r = mid - 1
    print(ans)

    pass


# ==================================================
#                     EXECUTION
# ==================================================

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
