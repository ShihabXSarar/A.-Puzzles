import numpy as np
n,m=list(map(int,input().split()))
a=np.zeros((n,m), dtype=str)
for i in range(0,n):
    for j in range(0,m):
        a[i][j]= "$"

for i in range(n):
    for j in range(m):
        print(a[i][j],end="")
    print()
