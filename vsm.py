#-*-coding: utf-8-*-
from __future__ import division
import math
from numpy import *

def get_doc():
    doc = [ ['he','is','my', 'good','friend'],
            ['she','is','my', 'best','friend'],
            ['she','is','my', 'good','friend'],
            ['his','name','is', 'same','to'],
            ['his','is', 'not', 'her', 'good','boyfriend'],
            ['his','is', 'not', 'her', 'good','boyfriend'],
            ['he','is','my', 'goo','friend'] ]
    return doc

def get_vocablist(doc):
    vocab = set([])
    for i in doc:
        vocab = vocab | set(i)
    return list(vocab)

def get_vectorized_doc(vocablist, inputSet):
    returnVec = [0] * len(vocablist)
    for word in inputSet:
        if word in vocablist:
            returnVec[vocablist.index(word)] += 1
        else:
            print "the word %s is not in the vocabulary" %word
    return returnVec

def get_df(key, returnVec):
    df = returnVec[vocablist.index(key)]/max(returnVec)
    return df

def get_n(key, doc):
    n = 0
    for i in doc:
        if key in i:
            n = n + 1
    return n

def get_idf(key, returnVec, n, doc):
    N = len(doc)
    n = get_n(key, doc)
    if n != 0:
        idf = math.log(N/n)
    else: idf = 0
    return idf

def get_weighteddoc(eachdoc, vocablist):
    weighteddoc = [0] * len(vocablist)
    for key in vocablist:
        returnVec = get_vectorized_doc(vocablist, eachdoc)
        tf = get_df(key, returnVec)
        n = get_n(key, eachdoc)
        idf = get_idf(key, returnVec, n, eachdoc)
        weightedscore = tf * idf
        weighteddoc[vocablist.index(key)] = weightedscore
    return weighteddoc

def vsm(doc1, doc2):
    weighteddoc1 = get_weighteddoc(doc1, vocablist)
    weighteddoc2 = get_weighteddoc(doc2, vocablist)
    diancheng = 0
    for i in range(len(weighteddoc1)):
        diancheng = diancheng + weighteddoc1[i] * weighteddoc2[i]
    return diancheng

def get_the_most_similar(doc):
    doc1 = doc[0]
    resultlist = []
    for i in range(1, len(doc)):
        diancheng = vsm(doc1, doc[i])
        resultlist.append(diancheng)
        result = max(resultlist)
        index = resultlist.index(result)
    return doc[index+1]

doc = get_doc()
vocablist = get_vocablist(doc)
result = get_the_most_similar(doc)
print result
