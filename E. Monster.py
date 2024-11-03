from collections import deque

t = int(input())  # Number of test cases

for _ in range(t):
    x, y, z, k = map(int, input().split())  # Read x, y, z, k

    # BFS queue: (current damage, coins spent, operations since last attack)
    queue = deque([(0, 0, 0)])
    visited = set()  # To avoid re-processing the same state

    min_cost = float('inf')  # Initialize with a large number

    while queue:
        damage, coins, ops = queue.popleft()

        # If damage >= z, update the minimum cost
        if damage >= z:
            min_cost = min(min_cost, coins)
            continue

        # If we haven't visited this state before, mark it visited
        if (damage, ops) in visited:
            continue
        visited.add((damage, ops))

        # Option 1: Increase damage by 1 (if within k-limit)
        if ops < k:
            queue.append((damage + 1, coins + x, ops + 1))

        # Option 2: Attack with current damage
        if damage > 0:
            queue.append((damage, coins + y, 0))  # Reset ops to 0 after attack

    print(min_cost)
