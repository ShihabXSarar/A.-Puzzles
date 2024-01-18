t=int(input())
for _ in range (t):
    n=int(input())
    arr = list(map(int,input().split()))
    arr=sorted(arr)
    arr[0]+=1
    product=1
    for i in range(0,n):
        product*=arr[i]
    print(product)