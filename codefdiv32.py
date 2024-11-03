t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    # Sort the threadlet lengths
    threadlets = [a, b, c]
    threadlets.sort()

    if threadlets[0]==threadlets[1]==threadlets[2]:
        print("YES")
    for i in range(3):
        if threadlets[1] - threadlets[0]> threadlets[0]:
            if threadlets[1] - threadlets[0]== threadlets[0]
    if threadlets[1] - threadlets[0]== threadlets[0] and threadlets[3] - threadlets[0] == threadlets[1]:
        print("YES")
    else:
        print("NO")
