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
    n, k = map(int, input().split())
    mx_x = min(k - 1, n - k)
    found = False
    for x in range(1, mx_x + 1):
        tmp = k - 1 - x
        if tmp < 0:
            continue
        tv = 0 if tmp % 2 == 0 else 1
        mn_p = min(k - 1 - x, n - k - x)
        if tv > mn_p:
            continue
        cm = 1 + 2 * x
        l = k - tv - 1
        r = n - k - tv
        if l < x or r < x:
            continue
        pos = []
        p = 1
        for _ in range(x - 1):
            pos.append(p)
            p += 1
        if x > 0:
            pos.append(p)
            p += l - x + 1
        pos.append(p)
        p += 2 * tv + 1
        for _ in range(x - 1):
            pos.append(p)
            p += 1
        if x > 0:
            pos.append(p)
            p += r - x + 1
        if p - 1 == n:
            print(cm)
            print(*pos)
            found = True
            break
    if not found:
        t0 = (n - 1) // 2
        if t0 == k - 1:
            print(1)
            print(1)
        else:
            print(-1)
    pass


# ==================================================
#                     EXECUTION
# ==================================================

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
