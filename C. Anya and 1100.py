
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
def is1100(s, i):
    return s[i:i + 4] == "1100"


# ==================================================
#                    SOLUTION FUNCTION
# ==================================================

def solve():
    global pos
    s = input().strip()
    n = len(s)
    pos = set()
    for i in range(n - 3):
        if is1100(s, i):
            pos.add(i)
    q = int(input())
    for _ in range(q):
        i, v = input().split()
        i = int(i) - 1
        v = int(v)
        if (int(s[i]) == v):
            print("NO" if not pos else "YES")
            continue
        for j in range(max(0, i - 3), i + 1):
            if is1100(s, j):
                pos.discard(j)
        s = s[:i] + str(v) + s[i + 1:]
        for j in range(max(0, i - 3), i + 1):
            if is1100(s, j):
                pos.add(j)
        print("NO" if not pos else "YES")

# ==================================================
#                     EXECUTION
# ==================================================

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()

