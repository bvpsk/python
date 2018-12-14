
def bi(a):
    if a==1:
        return '1'
    if a == 0:
        return '0'
    if a//2 == 1:
        return str(a%2)+'1'
    else:
        b = a%2
        return str(b)+bi(a//2)
    
def binary(a):
    a = bi(a)
    return int (a[::-1])
print binary(10)
