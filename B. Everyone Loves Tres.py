def compute_difference(S, n):
    sum_odd, sum_even = 0, 0

    for i in range(n):
        if (i + 1) % 2 == 1:
            sum_odd += int(S[i])
        else:
            sum_even += int(S[i])

    D = (sum_odd - sum_even) % 11
    if D < 0:
        D += 11

    return D


def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())

        if n == 1:
            print(-1)
            continue
        S = ['3'] * (n - 1) + ['6']
        D = compute_difference(S, n)

        if D == 0:
            print("".join(S))
            continue

        req = (-D) % 11
        if req < 0:
            req += 11
        odd_positions = []
        even_positions = []

        for i in range(n - 1):
            if S[i] == '3':
                if (i + 1) % 2 == 1:
                    odd_positions.append(i)
                else:
                    even_positions.append(i)

        found = False
        result = ""
        for k in range(1, n):
            if found:
                break
            for x in range(0, min(k, len(odd_positions)) + 1):
                y = k - x
                if y > len(even_positions):
                    continue

                sum_mod = ((x - y) * 3) % 11
                if sum_mod < 0:
                    sum_mod += 11

                if sum_mod == req:
                    temp = S[:]
                    for i in range(x):
                        temp[odd_positions[-1 - i]] = '6'
                    for i in range(y):
                        temp[even_positions[-1 - i]] = '6'

                    new_D = compute_difference(temp, n)

                    if new_D == 0:
                        candidate = "".join(temp)
                        if not found or candidate < result:
                            result = candidate
                            found = True

        if found:
            print(result)
        else:
            print(-1)
solve()
