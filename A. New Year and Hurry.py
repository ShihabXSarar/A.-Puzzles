n,k=map(int,input().split())
ttime=240
count=0
for i in range(1,n+1):
    k+=(i*5)
    if k <= ttime:
        count+=1
    else:
        break
print(count)

