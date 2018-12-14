import urllib2 as urllib
from re import findall
url="http://www.inkakinada.com/help/important-phone-numbers"
html=urllib.urlopen(url)
htm=html.read()
htmlstr=htm.decode()
pdata=findall("\d{4} \d{2,3} \d{4}",htmlstr)
for i in pdata:
    print(i)
