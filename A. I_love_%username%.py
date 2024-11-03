n=int(input())
a=list(map(int,input().split()))
count1=0
count2=0
for i in range(1,n):
    flag1 = 0
    flag2 = 0
    for j in range(i-1,-1,-1):
        if a[i]<=a[j]:
            flag1=1
    if(flag1==0):
        count1+=1
for i in range(1,n):
    flag2 = 0
    for j in range(i-1,-1,-1):
        if a[i]>=a[j]:
            flag2=1
    if (flag2 == 0):
        count2 += 1
print(count1+count2)