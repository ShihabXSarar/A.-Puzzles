k,r = list(map(int,input().split()))
sum = 0
for i in range(1,10000000000000):
    sum+= k
    if(sum%10==0 or sum%10==r):
        print(i)
        break
    else:
        continue