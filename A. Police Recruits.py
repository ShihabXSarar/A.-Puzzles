n=int(input())
arr = list(map(int,input().split()))
police=0
crime=0
for i in range(0,n):
    if arr[i]>0:
        police+=arr[i]

    else:
        if police>=1:
            police-=1
        else:
            crime+=1


print(crime)