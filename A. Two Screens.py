t = int(input())
for _ in range (t):
    s1 = input()
    s2 = input()
    l1 = len(s1)
    l2 = len(s2)
    same = 0
    for i in range(min(l1,l2)):
        if( s1[i]!=s2[i]):
            break
        same+=1
    ans = 0
    if same == 0:
        ans = l1+l2
    else: ans = l1+l2+1-same
    print(ans)