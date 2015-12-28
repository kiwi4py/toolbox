#coding:utf-8
import re
import requests
import codecs
from bs4 import BeautifulSoup


f = open('blank.txt','w')
text = open("Blank.htm", "r").read()
text = text.replace("\n", "")
text = text.replace("<i>", "")
text = text.replace("</i>", "")
text = text.split("<center>")


HOSTS ="HOST"
CITATIONS = "CITATIONS:"
DISTRIBUTION="DISTRIBUTION:"
excepted = []
for i in text[1:]:
    i = i.strip("\t")
    i = i.replace("\t","")
    i = i.replace(r"\n","")
    tag_b_start = i.index("<b>")
    tag_b_end = i.index("</b>")
    kind_name = i[tag_b_start+3:tag_b_end-3]
    
    if HOSTS in i:
        host_start = i.index(HOSTS)
        double_br_host = i[host_start:].index("<br><br>")
        host_html = i[host_start: double_br_host]
        host_splitted = host_html.split("</b>")
        host_name = host_splitted[0]#
        host_content = host_splitted[-1]#
    else:
        host_name = ""
        host_content = ""

    if DISTRIBUTION in i:
        dis_start = i.index(DISTRIBUTION)
        double_br = dis_start + i[dis_start:].index("<br><br>")
        dis_html = i[dis_start: double_br]
        dis_splitted = dis_html.split("</b>:")
        dis_name = dis_splitted[0]#
        dis_content = dis_splitted[-1]#
    else:
        dis_name = "\t"
        dis_content = "\t"

    if CITATIONS in i:
         #i = i.replace("CITATIONS:\n","CITATIONS:") 
         citation_start = i.index(CITATIONS)
         citation_html = i[citation_start: ]
    else:
        citation_html = ""
    if host_name !="" and dis_name != "":
        output =  kind_name + "\t" + host_name + "\t" + host_content \
                 + "\t" + dis_name + "\t" + dis_content + "\t" +  citation_html + "\n"
        output = output.replace("\t\t","")
        output = output.replace("<br>","")
        output = output.replace("<p>","")
        output = output.replace("</p>","")
        f.write(output)   
    
