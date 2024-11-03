n, k = map(int, input().split())
arr = list(map(int, input().split()))
min_sum = sum(arr[:k])
current_sum = min_sum
min_index = 0
for i in range(k, n):
    current_sum += arr[i] - arr[i - k]
    if current_sum < min_sum:
        min_sum = current_sum
        min_index = i - k + 1
print(min_index + 1)