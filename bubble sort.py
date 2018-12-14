#n = map(int,raw_input("enter by splitting").split())
from time import time
n = [99261,715043,391138,512394,592326,599442,949821,35728,241469,940357,749424,485063,448379,104007,496202,492669,181672,474212,69992,435972,610558,224576,996808,983725,674053,137594,645524,490099,927047,427015]
m = len(n)
for i in range(m):
    for j in range(0,m-i-1):
        if n[j] > n[j+1]:
            t = n[j]
            n[j] = n[j+1]
            n[j+1] = t
t = time()
print n
t1 = time()
print t1 - t
