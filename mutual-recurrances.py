def x(n,a,b,c,e,f,g,dix,diy):
    if n in dix:
        return dix[n]
    elif n < 0:
        return 1
    else:
        temp = x(n-a,a,b,c,e,f,g,dix,diy)+y(n-b,a,b,c,e,f,g,dix,diy)+y(n-c,a,b,c,e,f,g,dix,diy)+(n*(d**n))
        dix[n] = temp
        return temp

def y(n,a,b,c,e,f,g,dix,diy):
    if n in diy:
        return diy[n]
    elif n < 0:
        return 1
    else:
        temp = y(n-e,a,b,c,e,f,g,dix,diy)+x(n-f,a,b,c,e,f,g,dix,diy)+x(n-g,a,b,c,e,f,g,dix,diy)+(n*(h**n))
        diy[n] = temp
        return temp
    

a =6
b = 7
c = 5
d = 1
e = 7
f = 9
g = 4
h = 9
n = 5980
dix = {}
diy = {}
fx = x(n,a,b,c,e,f,g,dix,diy) % (1000000000)
fy = y(n,a,b,c,e,f,g,dix,diy) % (1000000000)
print fx,fy
