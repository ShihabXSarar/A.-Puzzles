n, k, l, c, d, p, nl, np = list(map(int,input().split()))
total_slice = c*d
total_drink = k*l
total_drink = total_drink/nl
total_salt= p/np
drinks = min(total_drink,total_salt,total_slice)//n
print(int(drinks))