#l = map(int,raw_input("enter elements separated by comma:").split(","))
from time import time
from random import randint as r
l = []
for j in range(30):
    l.append(r(0,1000000))
print l
#l = [1,24,65,2,4,6,3,52]
def sort(d1,d2):
    temp = []
    while len(d1) != 0 and len(d2) != 0:
        if d1[0] < d2[0]:
            temp.append(d1[0])
            d1.remove(d1[0])
        else:
            temp.append(d2[0])
            d2.remove(d2[0])
    if len(d1) == 0:
        temp +=d2
    else:
        temp += d1
    return temp


def merge(a):
    if len(a) == 1 or len(a) == 0:
        return a
 
    else:
        n1 = len(a)/2
        b = merge(a[:n1])
        c = merge(a[n1:])
        return sort(b,c)
t1 = time()

print merge(l)
t = time()
print t - t1
