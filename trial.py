from random import randint as rand
i=0
t=open("t.txt","w")
s=open("s.txt","w")
while i<25:
 a=rand(1,15)
 a=str(a)
 b=rand(1,40)
 b=str(b)
 t.write(a)
 s.write(b)
 i+=1
s.close()
t.close()
s=open("s.txt","r")
t=open("t.txt","r")
j=s.read()
print(j)
k=t.read()
print(k)
s.close()
t.close()
