n = raw_input('enter string:')
m = len(n)
result = []
for i in range(m):
    if n[i] in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
        result.append(n[i])
print ''.join(result)
