#coding: utf-8

#所有的笔记。
#notes = [[1, 2], [1, 2, 3], [4, 5, 6, 7], [4, 5, 6, 7, 8, 9, 10], [11, 12]]
notes = [[1, 2], [2, 3], [4, 5, 6, 7], [4, 5, 6, 7, 8, 9, 10], [11, 12], [1, 13]]
#notes = [[1, 2], [2, 3], [4, 5, 6, 7], [ 8, 9, 10], [11, 12]]

#建立空集合，用来盛放笔记的每一个词。
temp_list = set()
for i in notes:
    for j in i:
       temp_list.add(j)

note_element = list(temp_list)
print note_element

#为笔记的每个词和含有该词的笔记建立对应关系，并把该词的所有笔记合到一起。
ele_note_dict = {}
for i in note_element:
    note_list = []
    for note in notes:
        if i in note:
            note_list.extend(note)
    ele_note_dict[i] = note_list
print ele_note_dict

"""
ele_note_dict的内容如下
1: [1, 2, 1, 13],
2: [1, 2, 2, 3],
3: [2, 3],
4: [4, 5, 6, 7, 4, 5, 6, 7, 8, 9, 10],
5: [4, 5, 6, 7, 4, 5, 6, 7, 8, 9, 10],
6: [4, 5, 6, 7, 4, 5, 6, 7, 8, 9, 10],
7: [4, 5, 6, 7, 4, 5, 6, 7, 8, 9, 10],
8: [4, 5, 6, 7, 8, 9, 10],
9: [4, 5, 6, 7, 8, 9, 10],
10: [4, 5, 6, 7, 8, 9, 10],
11: [11, 12],
12: [11, 12],
13: [1, 13]
"""
            
covered = [-100] #用来盛放已经画过线的词。max函数参数不能为空，初始化随便用了一个很小的值。

lines =  [] #用来盛放最后的划线。

"""
遍历对应关系的每个词，如果该词没有被遍历过，且大于被遍历过的最大位置的词,
则把该词及含有该词的笔记的最后的词，即一条线，保存到lines中。把最后一个词保存到covered中。
"""

for k in ele_note_dict.keys():
    if k > max(covered):
        end = max(ele_note_dict[k])
        line = (k, end)
        lines.append(line)
        covered.append(end)

print lines

    

    
