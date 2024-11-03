s,n=list(map(int,input().split()))
flag=0
x=n
y=2
game=[]
for i in range (x):
    t=list(map(int,input().split()))
    game.append(t)
game=sorted(game)
"""
for row in game:
    print(row)
"""
for i in range(x):
    for j in range(2):
        if s >= game[i][0]:
            s+=game[i][1]
        else:
            flag=1
            break
if flag==0:
    print("YES")
else:
    print("NO")