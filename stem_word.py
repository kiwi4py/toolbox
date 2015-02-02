import nltk
from nltk.stem import SnowballStemmer


words = open('book-words.txt', 'r+').read()
word_list = words.split()
print len(word_list)

stemmer = SnowballStemmer("english")
count = 0
word_list_new = [stemmer.stem(i.decode('utf-8')) for i in word_list]
vob =  set(word_list_new)
print 'ok'
print len(vob)
for i in sorted(vob):
    print i

