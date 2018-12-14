def rec(i,x,n,prev):
    if i**n + prev >= x:
        if i**n + prev == x:
            return prev
        if i**n + prev > x:
            return 0
    else:
 #       y = 11
        y = x**(1.0/n)
        print y
 #       y = i+2
        for j in range(i+1,int(y)+2):
            return i**n + rec(j,x,n,i**n)


x = int(input('enter number:'))
n = int(input('enter power:'))
c = 0
i = 1
ra= []
ii = []
while i**n <=x:
    ii.append(i)
    r = rec(i,x,n,0)
    ra.append(r)
    if r == x:
        c+=1
    i+=1
print c
print ra
print ii
