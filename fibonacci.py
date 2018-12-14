n=int(input("Enter a number:"))
a=b=1
print(a)
print(b)
i=0
while(i<n):
 x=a+b
 a=b
 b=x
 i+=1
 print(x)
