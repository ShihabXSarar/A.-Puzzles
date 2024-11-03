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
    if 1900 <= n:
        print("Division 1")
    elif 1600<=n or n>=1899:
        print("Division 2")
    elif 1400<=n or n>=1599:
        print("Division 3")
    else:
        print("Division 4")
    pass


# ==================================================
#                     EXECUTION
# ==================================================

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
