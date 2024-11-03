a,b,c=map(int,input().split())
arr=[a,b,c]
arr=sorted(arr)
count=arr[1]-arr[0]
count+=arr[2]-arr[1]
print(count)