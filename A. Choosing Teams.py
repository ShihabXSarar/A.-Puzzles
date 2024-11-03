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
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    count=0
    for i in range(n):
        if arr[i]<=5-k:
            count+=1
    print(count//3)
    pass


# ==================================================
#                     EXECUTION
# ==================================================

if __name__ == "__main__":
    solve()
