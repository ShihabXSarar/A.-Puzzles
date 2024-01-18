
def calculate_points(grid):
    points = 0
    ring_values = [1, 2, 3, 4, 5]

    for i in range(10):
        for j in range(10):
            if grid[i][j] == 'X':
                ring = min(i, j, 9 - i, 9 - j)
                points += ring_values[ring]

    return points

t = int(input())

for _ in range(t):
    grid = [input() for _ in range(10)]

    points = calculate_points(grid)
    print(points)
