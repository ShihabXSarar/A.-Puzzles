n,m = map(int,input().split())
count = 0
for i in range(max(n,m)):
    if m==0 or n==0:
        break
    else:
        m-=1
        n-=1
        count+=1
if count%2 == 1:
    print("Akshat")
else:
    print("Malvika")
