t = int(input())


for _ in range(t):
    word = input()
    flag = False
    check = "codeforces"
    for i in range(len(check)):
        if(word == check[i]):
            flag = True

            break

    if flag:
        print("YES")
    else:
        print("NO")
