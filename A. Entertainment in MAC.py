t=int(input())
for _ in range (t):
    n=int(input())
    a=input()
    b=""
    if ord(a[0])<=ord(a[len(a)-1]):
        a=a
        print(a)
    else:
        b+=a[::-1]
        b+=a
        print(b)