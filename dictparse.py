#coding: utf-8

from xml.etree.ElementTree import ElementTree as ET

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
                        if len(senses) > 5:
                                toremove = senses[5:]
                                senses = senses[:5]
                                for to in toremove:
                                        c.remove(to)
                        for sense in senses:
                             examples = sense.findall("example")
                             for example in examples:
                                sense.remove(example)
                phrases = body.findall("phrase")
                hyphs = body.findall("hyph")
                grams = body.findall("gram")
                usages = body.findall("usage")
                derivatives = body.findall("derivative")
                for h in hyphs:
                        body.remove(h)
                        
                for p in phrases:
                    body.remove(p)

                for g in grams:
                        body.remove(g)

                for u in usages:
                        body.remove(u)

                for d in derivatives:
                        body.remove(d)
                        
        tree.write('shawn-dict-simplified/' + filename, encoding="utf-8",xml_declaration=True) 

if __name__ == "__main__":
        filelist = ["12" + chr(number) + ".xml" for number in range(65, 91)]
        for filename in filelist:
                tree = parseRaw(filename)
                parseDict(tree)
        
