import re


s = input()
k = int(input())
a = re.findall(r'\d{2}', s)
d = dict()
for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
kq = []
for i, j in d.items():
    if j >= k:
        kq.append((i, j))
kq.sort(key=lambda x: x[0])
check = 0
if len(kq) != 0:
    check = 1
    for i in kq:
        print(*i)
else:
    check == 0
    print("NOT FOUND")
    
'''
124356141111434356149
2
124356141111434356149
10
'''