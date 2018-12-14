import re
k=""
for i in re.findall("[A-Z,a-z]*",raw_input("enter any string")):
     k+=i
print(k)
