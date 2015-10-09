#coding: utf-8

from xml.etree.ElementTree import ElementTree as ET
from xml.dom import minidom


tree = ET()


def parseRaw(in_path):
        tree.parse(in_path)
        return tree


def parseDict(tree):
        entrys = tree.findall("entry")
        for entry in entrys:
                body = entry.find("body")
                category = body.findall("category")
                for c in category:
                        senses = c.findall("sense")
                        for sense in senses:
                             examples = sense.findall("example")
                             for example in examples:
                                sense.remove(example)
                phrases = body.findall("phrase")
                for p in phrases:
                        senses = p.findall("sense")
                        for sense in senses:
                             examples = sense.findall("example")
                             for example in examples:
                                sense.remove(example)
                        
        tree.write('shawn-dict/' + filename, encoding="utf-8",xml_declaration=True) 

if __name__ == "__main__":
        filelist = ["12" + chr(number) + ".xml" for number in range(65, 91)]
        for filename in filelist:
                tree = parseRaw(filename)
                parseDict(tree)
        
                
        

