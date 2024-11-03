def minimal_disturbance(test_cases):
    results = []

    for n, a in test_cases:
        disturbance = 0
        count = {}

        # Count occurrences of each element
        for ai in a:
            if ai in count:
                count[ai] += 1
            else:
                count[ai] = 1

        print(f"Count for test case with n={n} and a={a}: {count}")  # Debug print

        max_count = max(count.values())
        print(f"Max count: {max_count}")  # Debug print

        # Calculate the minimal disturbance possible
        if max_count <= n // 2:
            disturbance = 0
        else:
            disturbance = 2 * max_count - n

        print(f"Calculated disturbance: {disturbance}")  # Debug print
        results.append(disturbance)

    return results


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1

    test_cases = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        test_cases.append((n, a))

    results = minimal_disturbance(test_cases)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
