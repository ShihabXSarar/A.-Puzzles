# Function to calculate the total water needed for a given height h
def calculate_total_water_needed(a, h):
    return sum(max(0, ai - h) for ai in a)


# Function to find the maximum height of the tank
def find_max_height(n, x, a):
    left, right = 1, max(a)

    while left <= right:
        mid = (left + right) // 2
        water_needed = calculate_total_water_needed(a, mid)

        if water_needed <= x:
            # We can build a tank with height mid using at most x units of water
            left = mid + 1
            max_height = mid
        else:
            right = mid - 1

    return max_height


# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    # Find and print the maximum height of the tank
    max_height = find_max_height(n, x, a)
    print(max_height)
