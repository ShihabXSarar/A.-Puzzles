def can_paint(positions, length, gap_limit):
    if length % 2 == 0:
        for idx in range(1, length, 2):
            if positions[idx] - positions[idx - 1] > gap_limit:
                return False
        return True
    for skip_pos in range(0, length, 2):
        valid = True
        i = 0
        while i < length:
            if i == skip_pos:
                i -= 1
            elif i + 1 < length and positions[i + 1] - positions[i] > gap_limit:
                valid = False
                break
            i += 2
        if valid:
            return True
    return False
def find_min_gap():
    length = int(input())
    cells = list(map(int, input().split()))
    low, high, min_gap = 1, int(1e18), -1
    while low <= high:
        mid = (low + high) // 2
        if can_paint(cells, length, mid):
            min_gap = mid
            high = mid - 1
        else:
            low = mid + 1
    print(min_gap)
test_cases = int(input())
for _ in range(test_cases):
    find_min_gap()
