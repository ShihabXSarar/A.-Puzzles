t = int(input())
for _ in range(t):
    n = int(input())
    pos = 0
    i = 1

    while True:
        if i % 2 == 1:
            pos -= (2 * i - 1)
        else:
            pos += (2 * i - 1)

        if abs(pos) > n:
            if i % 2 == 1:
                print("Sakurako")
            else:
                print("Kosuke")
            break

        i += 1
