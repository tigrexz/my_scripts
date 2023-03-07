import re
filename = 'keywords-1.txt'

reg1 = re.compile(r'(\w+\s?\w+)[\n\r,:\.]*')    # works for text with one line or mutiple lines

with open(filename) as f:
    keywords = f.read()


mo1 = reg1.findall(keywords)
print(mo1)

str = ''
for i in mo1:
    str += f'\"{i}\" OR '
#print(str)
print(str.rstrip(' OR'))
