#coding: -*-utf-8-*-
"""
One day, the mobile developer came to me for a simple algorithm of drawing lines for the words that have notes.
The requirement is that in a piece of text, let's use number to designate each single word, 1 up to 13, for example,
if there are a note for 1 and 2, and another note for 2 and 3, there is no other notes that contain 
any of these three word, so we will draw a single line that ranges from 1 to 3. After a few trials, I have a solution. Frankly speaking, I am not good at 
algorithms. I think there must be some more powerful ones, which are expected to be more efficiency in time and may save
more space. Paste here just for the recording my learning experience.
"""

#笔记。
#notes = [[1, 2], [1, 2, 3], [4, 5, 6, 7], [4, 5, 6, 7, 8, 9, 10], [11, 12]]


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
