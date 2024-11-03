def min_operations_to_simple_permutation(test_cases):
    results = []

    for n, permutation in test_cases:
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if not visited[i]:
                current = i
                cycle_length = 0

                while not visited[current]:
                    visited[current] = True
                    current = permutation[current] - 1
                    cycle_length += 1

                if cycle_length > 1:
                    swaps += cycle_length - 1

        results.append(swaps)

    return results


def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1
    test_cases = []

    for _ in range(t):
        n = int(data[index])
        index += 1
        permutation = list(map(int, data[index].split()))
        index += 1
        test_cases.append((n, permutation))

    results = min_operations_to_simple_permutation(test_cases)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
