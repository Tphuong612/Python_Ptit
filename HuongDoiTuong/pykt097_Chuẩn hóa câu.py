import re
from sys import stdin
def dau(i):
    i = i.strip()
    if i[-1] != '.' and i[-1] != '!' and i[-1] != '?' :
        i += '. '
    else:
        i = i[:len(i)-1].strip() + i[-1]
    return i 

cau = []
for n in stdin:    
    # n = input()
    # if n == "":
    #     break
    tmp = n.split(r'[.!?]|\n')
    cau.extend(tmp)
kq = []
for i in cau:
    i = re.sub(" +", " ", i)
    i = i.capitalize()
    i = dau(i)
    kq.append(i)
for i in kq:
    print(i)
'''
Chuong trinh Dao Tao CLC nganh CNTT duoc Thiet     Ke theo chuan quoc te.
co 03 chuyen nganh la: Cong  nghe phan mem, Tri tue nhan tao va An toan thong tin
muc tieu cua chuong trinh la trang bi cho sinh vien cac ky nang nghe nghiep
moi    CAC BAN danG ky     thaM giA !
'''
    