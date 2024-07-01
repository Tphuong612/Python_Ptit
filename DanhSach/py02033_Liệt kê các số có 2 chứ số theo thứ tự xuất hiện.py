import re


s = input()
a = re.findall(r'\d{2}', s)
kq = []
for i in a:
    if i not in kq:
        kq.append(i)
print(*kq)
'''
124356141111434356149
'''
