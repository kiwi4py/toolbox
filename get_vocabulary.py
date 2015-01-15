#-*-coding: utf-8 -*-
import nltk

from os_file_util import get_name



def get_a_book_content(bookname):
    book_content = open(bookname,"r+").read()
    return book_content

def clean_book(bookcontent):
    pass

def remove_name(bookcontent):
    pass

def remove_specifi_noun(bookcontent):
    pass
    

def get_a_book_vocabulary(clean_book_content):
    book_token = nltk.word_tokenize(book_content)
    book_nltk_text = nltk.Text(book_token)
    book_vocabulary = set(book_nltk_text)
    vocabulary_num = len(book_vocabulary)
    return  book_vocabulary, vocabulary_num

file_list = get_name(r"G:\pylab\export\export")
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
    

    
