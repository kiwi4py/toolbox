#coding:utf-8

import os
import shutil

def get_file_directory(directories):
    file_list = []
    for root, dirs, files in os.walk(directories):
        file_list.append(dirs)
    return file_list[0]

def get_exe_file(directories):
    file_list = []
    exe_file = []
    for root, dirs, files in os.walk(directories):
            file_list.append(files)
    for i in file_list[0]:
        if i.endswith("exe"):
            exe_file.append(i)
    #exe_file.remove("w9xpopen.exe")
    return exe_file

def copyfile(sourceDir, targetDir):
    shutil.copy(sourceDir,  targetDir)


def get_name(directories):
    file_list = []
    for root, dirs, files in os.walk(directories):
        file_list.extend(files)
    return file_list
    



            
            
        

    

