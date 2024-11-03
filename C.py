def solve():
    length = int(input())
    binary_str = input()
    zeros = []
    ones = []
    for idx in range(length - 1):
        if binary_str[idx] == '0':
            zeros.append(idx)
        else:
            ones.append(idx)
    ones.reverse()
    zero_idx = len(zeros) - 1
    one_idx = len(ones) - 1
    total = length * (length + 1) // 2
    for i in range(length - 1, -1, -1):
        while zero_idx >= 0 and zeros[zero_idx] >= i:
            zero_idx -= 1
        while one_idx >= 0 and ones[one_idx] >= i:
            one_idx -= 1
        if binary_str[i] == '1':
            if zero_idx >= 0:
                total -= i + 1
                zero_idx -= 1
            elif one_idx >= 0:
                total -= i + 1
                one_idx -= 1
    print(total)
t = int(input())
for _ in range(t):
    solve()
