# -*- coding: utf-8 -*-  
        
import string, urllib2
import urllib
from urllib import FancyURLopener
import re
from bs4 import BeautifulSoup


class MyOpener(FancyURLopener,object):

   version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

def get_opener():
    myopener = MyOpener()
    return myopener

def get_wholepage(url):
   myopener = get_opener()
   wholePage = myopener.open(url)
   return wholePage

   
  
