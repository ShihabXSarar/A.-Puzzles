t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    for _ in range(m):
        s = input()
        if len(s) != n:
            print("NO")
            continue
        nchar = {}
        numchar = {}
        flag = True
        for i in range(n):
            num = a[i]
            char = s[i]
            if num in nchar and nchar[num] != char:
                flag = False
                break
            if char in numchar and numchar[char] != num:
                flag = False
                break
            nchar[num] = char
            numchar[char] = num
        print("YES" if flag else "NO")