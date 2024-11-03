t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr = sorted(arr)
    result = [1]*n
    point=0
    for i in range (n-1):
        if arr[i]==arr[i+1]:
            result[point]+=1
        else:

            point += 1
    result = sorted(result,reverse= True)
    print(sum(result[0:k]))