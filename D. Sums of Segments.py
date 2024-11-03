def compute_prefix_and_weights(arr, n):
    prefix = [0] * (n + 1)
    prefix_weight = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + arr[i]
        prefix_weight[i] = prefix_weight[i - 1] + i * arr[i]
    return prefix, prefix_weight
def compute_sum_prefix_and_weights(prefix, prefix_weight, n):
    sum_prefix = [0] * (n + 1)
    sum_prefix_weight = [0] * (n + 1)
    for i in range(1, n + 1):
        sum_prefix[i] = sum_prefix[i - 1] + prefix[i]
        sum_prefix_weight[i] = sum_prefix_weight[i - 1] + prefix_weight[i]
    return sum_prefix, sum_prefix_weight
def compute_sum_blocks(n):
    sum_blocks = [0] * (n + 1)
    for i in range(1, n + 1):
        sum_blocks[i] = i * n - (i * (i - 1)) // 2
    return sum_blocks
def get_sum_b(k, C, n, sum_blocks, prefix, prefix_weight, sum_prefix, sum_prefix_weight):
    if k == 0:
        return 0
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if sum_blocks[mid] >= k:
            right = mid
        else:
            left = mid + 1
    l = left

    sum_blocks_lm1 = sum_blocks[l - 1] if l > 1 else 0
    p = k - sum_blocks_lm1
    term1 = l * C
    sum_prefix_lm2 = sum_prefix[l - 2] if l > 2 else 0
    sum_prefix_weight_lm2 = sum_prefix_weight[l - 2] if l >= 2 else 0
    term2 = (n + 1) * sum_prefix_lm2
    term3 = sum_prefix_weight_lm2
    prefix_sum = prefix[l + p - 1] - prefix[l - 1]
    prefix_weight_sum = prefix_weight[l + p - 1] - prefix_weight[l - 1]
    term4 = (p + l) * prefix_sum
    term5 = prefix_weight_sum
    return (l - 1) * C - term2 + term3 + term4 - term5
def main():
    n = int(input())
    arr = [0] + list(map(int, input().split()))

    prefix, prefix_weight = compute_prefix_and_weights(arr, n)
    sum_prefix, sum_prefix_weight = compute_sum_prefix_and_weights(prefix, prefix_weight, n)
    sum_blocks = compute_sum_blocks(n)

    C = (n + 1) * prefix[n] - prefix_weight[n]

    q = int(input())
    for _ in range(q):
        li, ri = map(int, input().split())
        sum_ri = get_sum_b(ri, C, n, sum_blocks, prefix, prefix_weight, sum_prefix, sum_prefix_weight)
        sum_li_1 = get_sum_b(li - 1, C, n, sum_blocks, prefix, prefix_weight, sum_prefix, sum_prefix_weight)
        print(sum_ri - sum_li_1)

if __name__ == "__main__":
    main()
