t=int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = sum(a)
    move=0
    a=sorted(a)
    if ans%3==0:
        print(move)
    elif len(a)==0:
        print(move)
    else:
        for i in range(n):
            a.remove(a[i])
            move+=1
            if sum(a)%3==0:
                print(move)
                break
            elif sum(a)%3==1:
                move+=1
                print(move)
                break



