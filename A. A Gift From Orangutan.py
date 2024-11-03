# ==================================================
#              COMPETITIVE PROGRAMMING
# ==================================================
"""
Author: ${"Shihab Sarar"}
Created on: 11/2/2024
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
    numbers = list(map(int, input().split()))

    m = min(numbers)
    maxi = max(numbers)

    result = (n - 1) * (maxi - m)
    print(result)
    pass


# ==================================================
#                     EXECUTION
# ==================================================

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
