#coding:utf-8

import requests
from bs4 import BeautifulSoup

USERNAME = ""
PWD = ""
TEXT = ""
PART1_OF_URL = ""
PART2_OF_URL = ""
s = requests.session()
data = {'strUsername':USERNAME,'strPassword':PWD ,'strPage': 'index.cfm'}

end_num = 5070
f = open("result.txt", "w")

def find_wanted(html):
    soup = BeautifulSoup(html)
    wanted_classes =  soup.find_all("div", class_="tab_content_div")
    print len(wanted_classes)
    for i in wanted_classes:
        sign = i.h1.find_next_sibling()
        sign_text = sign.text
        if TEXT in sign_text:
                h1 = i.h1.a.text
                part = sign.a.text
                f.write("%s \t %s \n" %(h1,part))
                
err = 0			
for i in range(1, end_num+1):
    print "ok page" + str(i)
    target = PART1_OF_URL + \
             str(i) + PART2_OF_URL
    htmlcontent = s.get(target)
    html = htmlcontent.text
    try:
        find_wanted(html)
    except:
        err += 1
        print err
               
f.close()
print err
