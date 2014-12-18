#coding: utf-8
import os
import shutil

f = open("bookid-img.txt", "r")
base = "" # file path here
items = f.readlines()
for i in items:
    i = i.split("\t")
    bookid = int(i[0].replace('\xef\xbb\xbf',""))
    imgname = i[1].strip("\r\n")
    path = base + str(bookid)
    sourceDir = base + imgname
    os.mkdir(path)
    targetDir = base + str(bookid) + "/" + imgname.decode("utf-8")
    shutil.copy(sourceDir,  targetDir)
