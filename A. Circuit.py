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
    total = 0
    s = list(map(int, input().split()))
    total = sum(s)
    mn = total % 2
    mx = min(total, 2 * n - total)
    print(mn, mx)
    pass


# ==================================================
#                     EXECUTION
# ==================================================

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
