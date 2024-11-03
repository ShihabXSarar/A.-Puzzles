def xor_to(n):
    """ Returns XOR from 1 to n based on patterns of XOR. """
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    else:
        return 0


def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    results = []

    for _ in range(t):
        l = int(data[index])
        r = int(data[index + 1])
        i = int(data[index + 2])
        k = int(data[index + 3])
        index += 4

        mod = 1 << i  # This is 2^i

        # XOR of all numbers from l to r
        xor_r = xor_to(r)
        xor_l_minus_1 = xor_to(l - 1)
        total_xor = xor_r ^ xor_l_minus_1

        # Now we need to exclude numbers that are `k` mod `mod`
        # We will find how many numbers in the range [l, r] are equal to k mod mod
        count_k = (r // mod) - ((l - 1) // mod)

        if l <= k <= r and k % mod == k:
            total_xor ^= k  # Exclude k from the total XOR

        # Final result for this query
        results.append(total_xor)

    # Output all results
    sys.stdout.write("\n".join(map(str, results)) + "\n")


if __name__ == "__main__":
    solve()
