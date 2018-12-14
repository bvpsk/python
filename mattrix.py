import math
a = list(map(int,raw_input('Enter matrix elements with comma in between them:').split(',')))
n = len(a)
nn = math.sqrt(n)
for j in range(n):
    i = j+1
    if ((nn*i) - 1)%nn == (nn-1) and ((nn*i) - 1)%nn != (nn*nn)-1:
        t = a[j]
        a[j] = a[i]
        a[j+1] = t
print a
