#coding: utf-8

one = open("one.txt", "r").readlines()
two = open("two.txt", "r").readlines()

one_splitted = []

for i in one:
    i = i.strip()
    i = i.split("\t")
    name = i[0]
    original = i[0]
    original_re = "\t".join(m for m in i[1:])
    name = name.split()
    name = sorted(name)
    for j in two:
        j = j.strip()
        j = j.split("\t")
        original2_re = "\t".join(n for n in j[1:])
        name2 = j[0]
        name2 = name2.split(", ")
        name2 = sorted(name2)
        if name == name2:
            print "%s \t %s \t %s" %(original,  original_re,  original2_re)
            break
            
        
    
