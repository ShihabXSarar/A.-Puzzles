t = int(input())
arrn = list(map(int,input().split()))
arrk = list(map(int,input().split()))
for i in range (t):
    print(pow(2,arrk[i],pow(10,9)+7))

