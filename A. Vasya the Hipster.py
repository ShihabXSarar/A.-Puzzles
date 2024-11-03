a,b = list(map(int,input().split()))
dif=min(a,b)
p= max(a,b)-min(a,b)
p=p//2
print(dif,p)