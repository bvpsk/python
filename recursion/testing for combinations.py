def rec(index,i,summ,x,n,m):
    if i<m-1:
        if summ + (index[i+1])**n == x:
            return summ + (index[i+1])**n
        if summ + (index[i+1])**n > x:
            return summ
    if i == m-1:
        return summ
    if i < m-1:
        summ = summ + (index[i+1])**n
        #print summ
        return rec(index,i+1,summ,x,n,m)

x =1000
n = 3
i = x**(1.0/n)
index = [j+1 for j in range(int(i))]
print index
m = len(index)
print m
summ = (index[0])**n
print summ
ans = rec(index,0,summ,x,n,m)
print ans
