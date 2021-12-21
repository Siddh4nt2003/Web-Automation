import random
from bs4 import BeautifulSoup
#filepath = "D:\\Downloaded files\\abcd.html"
quotelist = list()
with open('D:\\Downloaded files\\abcd.html','r',encoding='utf-8') as abcd:
    content = abcd.read()
    #print(content)
    soup = BeautifulSoup(content,'lxml')
    a = soup.find_all('div',attrs={"class" : "quoteText"})
    for row in a:
        quotelist.append(row.text)
    c = list(quotelist)
    #print(c.size())
d = random.randint(1,30)
quotename = c[d]