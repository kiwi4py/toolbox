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


"""
有一天，我决定学习切页面。结果，我把PS中的毫米当成了像素。我切出来的窗口很小。在妻子的提醒下，我才意识到自己的错误。
于是，我打起精神，决定重新切。但是我怎么能忍受一处处地把设计宽度和高度的数字手动替换为像素。于是，我想到了Python。
简单写了几行代码，还算好用。就是split方法把冒号去掉了。需要改进。
"""
css = """         body{background-color: #919191;}
		.signin {width:188px; height:133px;background-color: #ffffff;border: 1px solid #8e8e8e;}
		.signinhead{width:188px; height:14.8px;background-color: #f5f5f5; border-bottom: 1px solid #e5e5e5;}
		.signintext{padding:4.6px 151px 3.2px 7.1px;width: 21.5px;height: 6px;}
		.closeicon{padding-left: 38px;margin-top:-14px;width: 4.2px;height:4.2px;float:right;padding-right:10px;}
		.windowbody{padding-left: 35.3px;}
		.windowbody p{font:  8px Tahoma, sans-serif;}
		.email {padding-bottom: 5px;font-size: 10px;font-color:#a7a7a7;padding-left: 3.9px;height: 12.6px;}
		.password {padding-bottom: 5px;font-size: 10px;font-color:#a7a7a7;padding-left: 3.9px;height: 12.6px;}
		 input {width: 116px; height: 11px; border: 1px solid #cccccc;}
		 .checkbox {padding-bottom: 8.8px;padding-right: 2.8px;margin-left: -55px;float:left;}
		 .remember {margin-left: -57px;font-size:7px;display:block;margin-top:4px;float:left;padding-left: 2px;}
		 .twolinks {font-color:#2258c4;padding-right:14.1px; font-size:7px;}
		 .button{border:none;width: 116px; height: 13.8px;}
		 form{margin-bottom: -12px;position: relative; margin-top: -5px;}
		
         .passwordicon {
            height: 6px;
            margin-left: -10px;
            padding-top: 8px;
            position: absolute;
            width: 5.3px;
          }
		    
        .emailicon {
            height: 4.6px;
            margin-left: -10px;
            padding-top: 11px;
            position: absolute;
            width: 6px;
          }
         .two {padding-top: 4px;}"""

s = css.split("px")
result = ""
for i in s:
    i = i.split(":")
    count = 0
    for j in i:
        count += 1
        if '#' not in j and j[-1] in [str(k) for k in range(0,10)]:
                    j.replace(' ', "")
                    j = ": " + str(float(j) * 2.83) +'px'
                    i[count-1] = j
    for m in i:
        result += "".join(m)
print result
    
