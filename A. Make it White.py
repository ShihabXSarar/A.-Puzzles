t=int(input())
while(t>=0): #when i use while(t), it shows runtime erorr but why? but when i use for then its accepted.
    n=int(input())
    count=[]
    a=input()
    for i in range (0,n):
        if(a[i]=='B'):
            count.append(i)

    res=(count[len(count)-1]-count[0])+1
    print(res)