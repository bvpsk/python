
def binary(a):
    if a==1:
        return '1'
    if a == 0:
        return '0'
    if a//2 == 1:
        return str(a%2)+'1'
    else:
        b = a%2
        return str(b)+binary(a//2)
    

a = binary(9999)
print int (a[::-1])
