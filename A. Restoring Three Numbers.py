a,b,c,d = list(map(int,input().split()))
arr = [a,b,c,d]
arr = sorted(arr)
A = arr[3]-arr[2]
B = arr[3]-arr[1]
C = arr[3]-arr[0]
print(A,B,C)