def lexicographically_smallest_string(t, test_cases):
    results = []

    for case in test_cases:
        n, s = case
        if n % 2 == 0:
            # If the number of operations is even, the lexicographically smallest string
            # will be the string itself since reversing an even number of times will bring it back to the original string.
            results.append(s)
        else:
            # If the number of operations is odd, reversing once will change the order of characters,
            # so the lexicographically smallest string will be the result of concatenating the string with its reverse.
            result = s + s[::-1]
            results.append(result)

    return results

# Example usage:
t = int(input())  # Number of test cases
test_cases = []

for _ in range(t):
    n = int(input())  # Number of operations
    s = input()  # String
    test_cases.append((n, s))

results = lexicographically_smallest_string(t, test_cases)

for result in results:
    print(result)



