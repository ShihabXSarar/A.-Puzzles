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
    arr = list(map(int, input().split()))
    flag = True
    for i in range(n - 1):
        itvl = abs(arr[i] - arr[i + 1])
        if itvl != 5 and itvl != 7:
            flag = False
            break
    print("YES" if flag else "NO")
    pass


# ==================================================
#                     EXECUTION
# ==================================================

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
