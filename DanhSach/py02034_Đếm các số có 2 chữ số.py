import re


s = input()
a = re.findall(r'\d{2}', s)
d = {}
for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
for i in d.keys():
    print(i, d[i])
'''
124356141111434356149
'''
