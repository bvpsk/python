def r(p):
    q = []
    s = len(p)
    if s == 1:
        print (p[0]*2)-1
    else:
        if s%2 == 0:
            for i in range(s):
                if i%2 == 0:
                    q.append(p[i])
            r(q)
        else:
            for i in range(s):
                if i%2 !=0:
                    q.append(p[i])
            r(q)
n = int(raw_input('enter no.of persons:'))
p = [i+1 for i in range(n)]
r(p)
