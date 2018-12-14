n = 5
a = 1
seq = []
seq.append(a)
for k in range(n):
    a = map(int,list(str(a)))
    c = 1
    cursor = 0
    cc = []
    for i in range(len(a)):
        if i != len(a) - 1:
            if a[i+1] == a[cursor]:
                c+=1
            else:
                cc.append(c)
                cc.append(a[cursor])
                c = 1
                cursor = i+1
    cc.append(c)
    cc.append(a[cursor])
    num = ""
    for j in cc:
        num += str(j)
    seq.append(int(num))
    a = num
print seq