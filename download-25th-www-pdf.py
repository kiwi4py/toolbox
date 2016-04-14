#download pdf

from bs4 import BeautifulSoup as BS
import urllib2

url = "http://www2016.net/proceedings/forms/proceedings.htm"
base = "http://www2016.net/proceedings"
response = urllib2.urlopen(url) 
html = response.read()
soup= BS(html)

for link in soup.find_all('a'):
    link_text = link.get('href')
    link_text  = str(link_text)
    split_link_text = link_text.split("/")
    pdf_name = split_link_text[-1]
    if link_text.endswith("pdf"):
        pdf_url = base + link_text[2:]
        try:
            pdf_file = urllib2.urlopen(pdf_url)
            with open(pdf_name, 'wb') as output:
                output.write(pdf_file.read())
                output.close()
        except:
            print pdf_url
