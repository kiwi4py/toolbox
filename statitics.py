#-*-coding:utf-8 -*-
import csv

title = "table head"
title = title.split()

result = {}
for i in range(len(title)):
    result[title[i]] = []

cr = csv.reader(open('from_editor.csv', 'rb'))
for row in cr:
    for choice_num in range(0, len(row)):
        result[title[choice_num]].append((row[choice_num]))

result  =  sorted(result.items(),key=lambda e: int(e[0].split('.')[0]),reverse=False)

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




 
       
       
