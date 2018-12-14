from random import randint as r
from time import time
t = time()
n = []
for i in range(10):
    n.append(r(0,100))
a = []
print n
def verif(cu,tar):
    if len(tar) == 1:
        if cu > tar[0]:
            a.append([cu,tar[0]])
    else:
        length = len(tar)/2
        t1 = verif(cu,tar[:length])
        t2 = verif(cu,tar[length:])
    

for i in range(9):
    cursor = n[i]
    target = n[i+1:]
    verif(cursor,target)
t1 = time()
print a
print t1- t
