t = int(input())
for _ in range(t):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    t_op = 0
    for diag_st in range(n):
        min_val = 0
        row, col = diag_st, 0
        while row < n and col < n:
            min_val = min(min_val, matrix[row][col])
            row += 1
            col += 1
        t_op += abs(min_val)
        if diag_st > 0:
            min_val = 0
            row, col = 0, diag_st
            while row < n and col < n:
                min_val = min(min_val, matrix[row][col])
                row += 1
                col += 1
            t_op += abs(min_val)
    print(t_op)
