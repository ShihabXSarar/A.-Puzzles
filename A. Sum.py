import heapq as hq
t = int(input())
for _ in range (t):
    a, b, c = list(map(int, input().split()))
    num = [a,b,c]
    second= hq.nlargest(2,num)
    s_largest = second[1]

    if min(a,b,c)+s_largest == max(a,b,c):
        print("YES")
    else:
        print("NO")
