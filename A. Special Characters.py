t=int(input())
for _ in range(t):
    n=int(input())
    a=[]
    if(n%2!=0):
        print("NO")
    else:
        for i in range(1,n//2):

            a.append('A'*2)
print(*a)