#-*-coding:utf-8 -*-
"""
 When editor Gao gathers the data of a survey, she found it was quite boring to filter each column and
 got the final result from a sheet like this:
 question 1 - choice one | question 1 - choice tow | question 2 - choice one | question 2 - choice two ...
 a real question looks like this "1.你的阅读出发点或动力主要是下面哪一项或哪些项？-个人兴趣"
 She asked me for help.
 After I made clear that she wanted data like this question 1 how many people choose choice one ...,
 I wrote the following code to process the data:
"""
import csv

title = "table head"     #  question 1 - choice one | question 1 - choice tow | question 2 - choice one | question 2 - choice two ...
title = title.split()

result = {}
for i in range(len(title)):
    result[title[i]] = []

cr = csv.reader(open('from_editor.csv', 'rb'))
for row in cr:
    for choice_num in range(0, len(row)):
        result[title[choice_num]].append((row[choice_num]))

result  =  sorted(result.items(),key=lambda e: int(e[0].split('.')[0]),reverse=False) # sort the dict by number string in key

for keys, values in result:
   print keys
   single_item = set(values[1:])
   single_item = list(single_item)
   column_dict = {}
   for item in single_item:
       if item != "":
           column_dict[item] = values.count(item)
   for k, v in column_dict.items():
      print k, v
   print '\r\n'




 
       
       
