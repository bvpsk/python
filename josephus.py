n = int(raw_input("enter no. of persons : "))
ai = [i for i in range(50) if 2**i <= n]
print 2*(n - 2**(len(ai) - 1)) + 1