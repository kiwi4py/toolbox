#coding:utf-8
import requests
import codecs
from bs4 import BeautifulSoup

FRONT = ""
END = ""

s = requests.session()
f = codecs.open('stone.txt','w','utf-8')
for i in range(0, 1263, 30):
    url = FRONT + str(i) + END
    target = s.get(url)
    html = target.text
    soup = BeautifulSoup(html)
    tables = soup.find_all("table", class_="collapseParas")
    table = tables[0]
    text = table.text
    text = text.replace(u'\r\n\t\t\t\r\n\r\n\t\t\t\n\n\n\xa0\xa0\xa0\xa0\xa0\n\n\n', "\n")
    text = text.replace(u"\xa0\r\n\r\n\t\t\t", "\t")
    text = text.replace(u"\n\xa0\xa0\n", "\t")
    text = text.replace(u"\n\n\n\n", "\n")
    text = text.replace(u"\n\n\n", "")
    text = text.replace(u"\xa0\xa0\xa0\xa0\xa0","\n")
    text = text.replace(u"\n\n", "\n")
    f.write(text)
    print 'ok' + str(i)
