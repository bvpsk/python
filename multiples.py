
a = []
b = []
for i in range(900,10000):
    if i%9 == 0:
        s = str(i)
        dec = True
        for k in range(len(s)):
            if s[k]!="0" and s[k]!= "9":
                dec = False
        if(dec):
            for j in range(100,501):
                if i>=j:
                    if i%j == 0:
                        a.append(j)
                        #print str(i) + " is multiple of " + str(j) + "\n"
for i in range(100,501):
    if i not in a:
        b.append(i)
print b
print len(b)
