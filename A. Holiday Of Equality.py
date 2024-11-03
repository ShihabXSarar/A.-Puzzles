n = int(input())
a = list(map(int,input().split()))
m = max(a)

sum = 0
for i in range(n):
    if m!=a[i]:
        sum+= m-a[i]

print(sum)