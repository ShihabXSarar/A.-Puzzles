n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
count = arr[0] - 1

for i in range(m-1):
    if arr[i] > arr[i + 1]:
        count += n - (arr[i] - arr[i + 1])

    elif arr[i] < arr[i+1]:
        count += arr[i+1] - arr[i]

print(count)