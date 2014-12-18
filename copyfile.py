#coding: utf-8
"""
Editors have to enroll bookinfo into App Store which turns to be a tedious work. It's even worse because it's quite slow to 
access the App Store platform. In order to help editors to save time as much as we can, we try to put each image file into a 
foler named by its id. In this way, editors may easily find which image to upload. I wrote this tiny utility last year, but I
just can't find it. I write it again and paste it here. Hopefully I will find it next time when I use it.
"""

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
