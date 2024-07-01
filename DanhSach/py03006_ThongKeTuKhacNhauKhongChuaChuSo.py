
import re


n = int(input())
s =""
while n>0:
    n -= 1
    s += input()+" "
a = re.findall(r'[a-z]+', s.lower())
d = dict()
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
sd = dict(sorted(d.items(), key = lambda x: (-x[1], x[0])))
for i in sd:
    print(i, d.get(i))
       
'''
3
PTIT duy tri hoc phi on dinh nam 2019 va khong tang trong nam 2020-2021 va 2021-2022!
Khi dich benh xuat hien PTIT trich hon 6 ty dong ho tro sinh vien PTIT
voi muc ho tro 500000 dong/sinh vien PTIT.
'''  