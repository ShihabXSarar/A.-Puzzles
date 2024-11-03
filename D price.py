#matrix
import numpy as np
row,col=map(int,input().split())
matrix=np.zeros((row,col),dtype=int)
for i in range(row):
    t=list(map(int,input().split()))
    for j in range(col):
        matrix[i][j]=t[j]
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=" ")
    print()
