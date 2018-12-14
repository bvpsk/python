a = list(map(lambda l:list(map(int,l.split(","))),raw_input("Enter A : ").split()))
b = list(map(lambda l:list(map(int,l.split(","))),raw_input("Enter B : ").split()))
def transpose(m):
    d = []
    for i in range(len(m[0])):
        d.append([])
        for j in range(len(m)):
            d[i].append(0);

    for i in range(len(m)):
        for j in range(len(m[0])):
            d[j][i] = m[i][j]
    return d
c = transpose(b)
p = []
for d1 in a:
    p.append([])
    for d2 in c:
        p[len(p) - 1].append(sum(list(map(lambda one,two:one*two,d1,d2))))
print p
