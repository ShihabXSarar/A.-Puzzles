t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    x = input()
    s = input()
    n = len(x)
    m = len(s)
    flag = 1
    count = 0
    c=m//2
    for j in range(m):
        for k in range(len(x)-m+1):
            if x[k:k + m] == s:
                flag = 0
                break
        if flag ==0:
            break
        x = x + x
        count += 1

    if flag == 1:
        print("-1")
    else:
        print(count)
