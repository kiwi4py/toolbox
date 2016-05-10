#coding:utf-8
#author: kipi

import os
import re

css_base = "G:\spyder\classics\OPS\css"
classics_file = "G:\spyder\classics\OPS\css"
classics_file_names = os.listdir(classics_file)
classics_file_names = [i for i in classics_file_names if i.endswith("css")]


def highlight(css_name):
    css_file = open(os.path.join(css_base, css_name), "r+")
    css_rules = css_file.read()
    css_file.close()
    css_rules += " .sensitive {color: red;}"
    css_file = open(os.path.join(css_base, css_name), "r+")
    css_file.write(css_rules)
    css_file.close()

for i in classics_file_names:
    highlight(i)
print "ok"
