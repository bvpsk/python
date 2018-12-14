m=raw_input('enter string:')
n= list(m)
l = len(n)
a=[]
s =['a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','q','w','e','r','t','y','u','i','o','p','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
for i in range(l):
    if n[i] in s:
        a.append(n[i])
print ''.join(a)
