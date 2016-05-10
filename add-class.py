#coding:utf-8
#author: kipi

import os
import re

css_base = "G:\spyder\classics\OPS\css"
classics_file = "G:\spyder\classics\OPS\css"
classics_file_names = os.listdir(classics_file)
classics_file_names = [i for i in classics_file_names if i.endswith("css")]


def highlight(css_name):
    css_file = open(os.path.join(css_base, css_name), "r+")
    css_rules = css_file.read()
    css_file.close()
    css_rules += " .sensitive {color: red;}"
    css_file = open(os.path.join(css_base, css_name), "r+")
    css_file.write(css_rules)
    css_file.close()

for i in classics_file_names:
    highlight(i)
print "ok"


"""
#coding:utf-8

import re
import string
from bs4 import BeautifulSoup as BS

import nltk

#english_vocab = set(w.lower() for w in nltk.corpus.words.words())

english_vocab = set([])

s = """<div class="para"><a name="chapter1"></a><h2>test</h2><div class="zh">女人</div></div>
<div class="para"><div class="en"><div class="en">诗人hello</div>"""

chinese_token = re.compile(r"[\x80-\xff]+")
all_zh = re.findall(chinese_token,s)

for i in all_zh:
    s = re.sub(i, "<div class='high'>" + i + "</div>", s)
print s


def is_word(seem_word):
    return seem_word not in english_vocab

def add_tag_for_non_word(s):
    temp_s = s
    clean_txt = re.sub(chinese_token, "", temp_s)
    rest = re.sub("<.+?>", "", clean_txt)
    rest = remove_punc(rest)
    print rest
    txt_token = rest.split()
    txt_token = list(set(txt_token))
    for i in txt_token:
        if is_word(i):
            s = s.replace(i, "<div class='nonword'>" + i + "</div>")
    print s

def remove_punc(s):
    exclude = set(string.punctuation)
    exclude_digits = set(string.digits)
    exclude = exclude | exclude_digits
    s = ''.join(ch for ch in s if ch not in exclude)
    return s

add_tag_for_non_word(s)
"""
