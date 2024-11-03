n,m,a,b = map(int,input().split())
if m*a>b:
    x = (n%m)*a
    if x>b:
        print(n//m * b+b)
    else: print(n//m * b+x)

else:print(n*a)