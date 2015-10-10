#coding: utf-8

import re

filelist = ["12" + chr(number) + ".xml" for number in range(65, 91)]
for i in filelist:
        s = open(i, "r").read()
        s = re.sub(">(\s+?)<", "><", s)
        s = re.sub("\s{3,}", "", s)
        f = open("shawn-dict-simplified" + "//" + i, "w")
        f.write(s)
        f.close()

        
                
        

