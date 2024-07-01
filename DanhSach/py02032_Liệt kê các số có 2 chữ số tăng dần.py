import re


s = input()
a = re.findall(r'\d{2}', s) 
kq = sorted(list(set(a)))
print(*kq)
'''
124356141111434356149
'''
