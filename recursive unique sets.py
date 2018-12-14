import numpy as np
from itertools import combinations





x = int(raw_input('enter unique number:'))
n = int(raw_input('enter power:'))
y = x**(1.0/n)
index = [i+1 for i in range(int(y))]
m = len(index)
for j in range(m+1):
    for i in combinations(index,j):
        pass
print i[0] + i[8]
    
