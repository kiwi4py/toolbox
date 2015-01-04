def make_py(fid):
    name = "a" + str(fid) + "-refer_name.py"
    f = file(name,"w")
    content = """
import re
import sys
import py2exe
from distutils.core import setup
name = "G:/pylab/referencename/" + str(%d) + "-referenc.py"
setup(console=[name])
""" %fid
    f.write(content)
    f.close()
