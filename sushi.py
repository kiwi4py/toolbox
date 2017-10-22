#-*-coding:utf-8 -*-

import re
import urllib2
from bs4 import BeautifulSoup as BS

#该函数将指定诗词列表页，做成一锅美味的汤，因为是用整个列表页做的，姑且叫它html_soup汤吧！
def get_soup(list_page_number):
    url = "http://www.shicimingju.com/chaxun/zuozhe/9_" \
          + list_page_number + ".html#chaxun_miao"
    response = urllib2.urlopen(url) 
    html = response.read()
    html_soup = BS(html)
    return html_soup

def get_detail_page_number(html_soup):
    for div in html_soup.find_all("div", class_=shici_class):
        ul = div.find_all("ul")
        ul = str(ul)
        detail_page_number = re.findall(pattern,ul)
    return detail_page_number

shici_class = "shicilist"
sushi_detail_page_number = []
pattern = re.compile("/chaxun/list/(\d+).html")
all_links = []
for list_page_number in range(2, 88):
    list_page_number = str(list_page_number)
    html_soup = get_soup(list_page_number)
    detail_page_number = get_detail_page_number(html_soup)
    sushi_detail_page_number.extend(detail_page_number)
    
print len(sushi_detail_page_number)

# week 2
# In:诗词详情页网址中的编号 Out:诗词详情页的BS实例
def get_poem_soup(detail_page_number):
    url = "http://www.shicimingju.com/chaxun/list/" \
          + detail_page_number + ".html"
    response = urllib2.urlopen(url)
    poem_html = response.read()
    poem_html_soup = BS(poem_html)
    return poem_html_soup

# In:诗词详情页的BS实例 Out：诗词标题和内容
def get_poem(poem_html_soup):
    div = poem_html_soup.find(id="middlediv")
    for sub_div in div.find_all("div", class_="zhuti"):
        title = sub_div.find_all("h2")
        content = sub_div.find(id="shicineirong")
        print title[0].text       
        print content.text
        
# 用赤壁怀古这首词，验证代码是否符合预期        
detail_page_number = "3710"
poem_html_soup = get_poem_soup(detail_page_number)
get_poem(poem_html_soup)
