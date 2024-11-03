n,l=map(int,input().split())
arr=list(map(int,input().split()))
m=0
arr=sorted(arr)
for i in range(n-1):
    if(arr[i+1]-arr[i]>m):
        m=arr[i+1]-arr[i]
x=float(arr[0])
y=float(m/2)
ans=max(x,y)
z=float(l-arr[n-1])
ans=max(z,ans)
print("{:.10f}".format(ans))
