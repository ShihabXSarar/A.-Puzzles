t=int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a=list(map(int,input().split()))
    count=0
    for i in range(n):
        if a[i]==k:
            count=1
            break
    if count==1:
        print("Yes")
    else:
        print("NO")

