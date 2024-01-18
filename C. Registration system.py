n=int(input())
d={}
for _ in range(0,n):
    a=input()
    if a in d:
        print(a+str(d[a]))
        d[a]+=1
    else:
        print("OK")
        d[a]=1