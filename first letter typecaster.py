nn = raw_input('Enter Sentence:')
n = list(nn)
m = len(n)
for i in range(m):
    if i == 0:
        n[i] = n[i].upper()
    try:
        if n[i] == ' ':
            n[i+1] = n[i+1].upper()
    except IndexError:
        pass
print ''.join(n)
