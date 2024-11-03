t = int(input())
for _ in range(t):
    a = input()
    sum = 0
    even= 0
    zero = False
    for d in a:
        x = int(d)
        sum += x
        if x == 0:
            zero = True
        elif x % 2 == 0:
            even += 1

    if zero and sum % 3 == 0 and even >= 1:
        print("red")
    else:
        print("cyan")
