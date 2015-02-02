#-*-coding: utf-8 -*-
import string

import nltk
from nltk.corpus import stopwords, names

from os_file_util import get_name

def get_stem():
    pass

def remove_punc(s):
    exclude = set(string.punctuation)
    exclude_digits = set(string.digits)
    exclude = exclude | exclude_digits
    s = ''.join(ch for ch in s if ch not in exclude)
    return s
    
def set_stop_name():
    exclude_stop_words = set(stopwords.words("english"))
    exclude_male_name = set([mn.lower() for mn in names.words("male.txt")])
    exclude_female_name = set([fn.lower() for fn in names.words("female.txt")])
    exclude = exclude_stop_words | exclude_male_name | exclude_female_name
    return exclude
    
def get_a_book_content(bookname):
    book_content = open(bookname,"r+").read()
    book_content = book_content.replace("-", " ")
    book_content_removed_punc = remove_punc(book_content)
    book_content_lowercase = book_content_removed_punc.lower()
    return book_content_lowercase

def get_a_book_vocabulary(book_content):
    book_token = nltk.word_tokenize(book_content)
    book_nltk_text = nltk.Text(book_token)
    book_vocabulary = set(book_nltk_text) - set_stop_name()
    vocabulary_num = len(book_vocabulary)
    return  book_vocabulary, vocabulary_num

file_list = get_name(r"G:\pylab\export\export1")
#print file_list[:-3]



v = set()
count = 0
for i in file_list:
    print count
    count += 1
    bookpath = "G:/pylab/export/export/"  + i
    book_content = get_a_book_content(bookpath)
    #print book_content
    bookv, v_n = get_a_book_vocabulary(book_content)
    #print bookv, v_n
    v = v | bookv
print len(v)
vocab = sorted(v)
for i in vocab:
    print i


    

    
