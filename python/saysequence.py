n = input("enter starting term of sequence:")
iterations = int(input("enter total number of terms in sequence:"))
print(int(n))
a = ["*"]
c = 1
sol = []
ind = -1
length = len(n)
for q in range(iterations):
    for i in n:
        ind+=1
        k = ind + 1
        while k<length and int(i) != a[len(a) - 1]:
            if int(n[k]) == int(n[ind]):
                c+=1
                k+=1
            else:
                break
        if int(i) != a[len(a) - 1]:
            a.append(c)
            a.append(int(i))
            sol.append(str(c))
            sol.append(str(i))
            c = 1
    a.pop(0)
    print(int(''.join(sol)))
    n = a
    a = ["*"]
    c = 1
    sol = []
    ind = -1
    length = len(n)
            

