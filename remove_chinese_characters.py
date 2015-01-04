#coding: utf-8
import re
import os
import shutil


def get_name(directories):
    file_list = []
    for root, dirs, files in os.walk(directories):
        file_list.extend(files)
    return file_list

def copyfile(sourceDir, targetDir):
    shutil.copy(sourceDir,  targetDir)

files_path =  "your path here, such as E:/~/files"
print files_path

file_list = get_name(files_path)
print file_list

chinese_token = re.compile(r"[\x80-\xff]+")
for i in range(len(file_list)):
    f = file(files_path + "/" + file_list[i], "r")
    s = f.read()
    s = re.sub(chinese_token, "", s)
    new_txt =  "E:/~/files/processed/" + file_list[i]
    new_file = file(new_txt, "w")
    new_file.write(s)
    f.close()
    new_file.close()
    
