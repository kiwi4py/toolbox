#coding: utf-8
import os
import sys
import shutil
from PIL import Image


imgbase = "C:/Users/zly/Desktop/original/original/"
all_img = os.walk(imgbase)
imglist = []
for i in all_img:
    imglist.append(i[-1])
imglist = imglist[0]
   
base = "C:/Users/zly/Desktop/"

for i in imglist:
    infile = imgbase + i
    outfile = "C:/Users/zly/Desktop/original/640/" + i 
    im = Image.open(infile)
    out = im.resize((640, 920), Image.ANTIALIAS)
    out.save(outfile)

