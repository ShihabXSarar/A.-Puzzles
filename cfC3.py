def can_choose_numbers(n, k, x):
    # Calculate the maximum possible sum using the last k-1 numbers
    max_sum = (n * (n + 1) // 2) - (k * (k - 1) // 2)

    # Check if x is within the range [k, max_sum]
    if k <= x <= max_sum:
        return "YES"
    else:
        return "NO"

def main():
    t = int(input())
    for _ in range(t):
        n, k, x = map(int, input().split())
        result = can_choose_numbers(n, k, x)
        print(result)

if __name__ == "__main__":
    main()
