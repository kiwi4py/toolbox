#-*-coding: utf-8 -*-
import nltk

from os_file_util import get_name

def get_a_book_content(bookname):
    book_content = open(bookname,"r+").read()
    return book_content

def clean_book(book_content):
    pass

def remove_name(book_content):
    """
    to remove name in nltk name corpus
    """
    pass

def remove_specific_noun(book_content):
    """
    to remove specific noun, e.g. states, countries
    """
    pass
    

def get_a_book_vocabulary(clean_book_content):
    book_token = nltk.word_tokenize(book_content)
    book_nltk_text = nltk.Text(book_token)
    book_vocabulary = set(book_nltk_text)
    vocabulary_num = len(book_vocabulary)
    return  book_vocabulary, vocabulary_num

file_list = get_name(r"G:\pylab\export\export")
#The following 3 lines should be useless if put py files in another directory
file_list.remove("os_file_util.py")
file_list.remove("os_file_util.pyc")
file_list.remove("vocabulary.py")

v = set()
count = 1
for i in file_list:
    book_content = get_a_book_content(i)
    bookv, v_n = get_a_book_vocabulary(book_content)
    v = v | bookv
    print count
    count += 1
    
print len(v)
v = sorted(v)
for i in v:
    print i
    

    
