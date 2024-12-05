# ==================================================
#              COMPETITIVE PROGRAMMING
# ==================================================
"""
Author: ${"Shihab Sarar"}
Created on: 11/23/2024
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
    a,b = map(int,input().split())
    hi = 0
    for i in range (20,-1,-1):
        if (a>>i)& 1:
            hi = i
            break
    count = 0
    lim = min((1<<(hi+1)),b)
    for i in range (1,lim+1):
        res = i ^ a
        if res and (a%res==0 or i %res == 0):
            count +=1
    print(count)
    pass


# ==================================================
#                     EXECUTION
# ==================================================

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
