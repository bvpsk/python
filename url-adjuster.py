fi = open('urls.txt','r')
contents = fi.read()
n = len(contents)
i = 0
urls = []
while i< n:
    i+=1
    if contents[i:i+7] == 'http://' or contents[i:i+8] == 'https://':
        #print 'a'
        j = i+1
        temp = 'h'
        while contents[j:j+7] != 'http://' and contents[j:j+8] != 'https://':
            try:
                temp+=contents[j]
                j+=1
            except:
                break
        if len(temp) > 1:
            i = j
            urls.append(temp)
for i in range(10):
    print urls[i]
fi.close()
