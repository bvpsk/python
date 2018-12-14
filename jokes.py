def fact(m):
    if m == 1 or m == 0:
        return 1
    else:
        return m*fact(m-1)
n = int(raw_input())
l = []
for i in range(n):
    l.append(map(int,raw_input().split()))
ans = []
for li in l:
    m = li[0]
    d = li[1]
    s = str(d)
    dd = [int(s[i]) for i in range(len(s))]
    dd = dd[::-1]
    if max(dd)<=m:
        p = 0
        for i in range(len(dd)):
            po = m**i
            p+=po*dd[i]
        ans.append(p)
c = {}
completed = []
for t in ans:
    if t not in completed:
        completed.append(t)
        target = t
        combinations = 0
        for i in ans:
            if target == i:
                combinations+=1

        try:
            one = fact(combinations)
            two = fact(combinations-2)
            combi = one/(two*2)
            c[target] = combi
        except:
            pass
su = 0
for i in c:
    su+=c[i]
print su
