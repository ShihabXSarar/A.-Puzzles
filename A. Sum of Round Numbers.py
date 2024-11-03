t=int(input())
for _ in range(t):
    n=int(input())
    org=n
    count=0
    rem=0
    arr=[]
    while(org):
        rem=org%10
        org=(org-rem)/10
        count+=1
    rem=0
    i=10
    while(count>=0):
        if n%i != 0:
            r=n%i
            arr.append(n%i)
            n=n-r
        i*=10
        count-=1
    print(len(arr))
    print(*arr)