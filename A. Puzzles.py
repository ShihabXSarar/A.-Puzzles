n,a=map(int,input().split())
arr=[a]
arr=list(map(int,input().split()))
arr=sorted(arr)
count=arr[a-1]-arr[0]
for i in range(n,a+1):
    d = arr[i -1] - arr[i-n]
    d=abs(d)
    count=min(count,d)
print(count)