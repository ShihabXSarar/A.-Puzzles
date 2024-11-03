t=int(input())
for _ in range(t):
    st=input()
    a=0
    b=0
    for i in range (len(st)):
        if st[i]=='A':
            a+=1
        else:
            b+=1

    if a>b:
        print("A")
    else: print("B")