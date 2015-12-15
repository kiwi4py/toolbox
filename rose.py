#coding:utf-8

s = open("rose.txt", "r").read()
s = s.split("\n")
counted = []
for i in s:
    j = i.split("\t")
    if j[-1] != "":
        counted.append(j[-1])

for item in set(counted):
    left = ""
    for j in s:
        j = j.split("\t")
        if j[-1] == item:
            left = left + ";" + j[0]
    print "%s \t %s \t %s" %(item, counted.count(item), left)
