from datetime import datetime
class Mon:
    def __init__(self, ma, ten) -> None:
        self.ma = ma
        self.ten = ten
class Ca:
    def __init__(self, id, maMon, ngay, gio, nhom) -> None:
        self.id = f'T{id:03d}'
        self.maMon = maMon
        self.ngay = datetime.strptime(ngay, "%d/%m/%Y")
        self.gio = datetime.strptime(gio, "%H:%M")
        self.nhom = nhom
        self.ten = ""
    def __str__(self) -> str:
        return f'{self.id} {self.maMon} {self.ten} {self.ngay.strftime("%d/%m/%Y")} {self.gio.strftime("%H:%M")} {self.nhom}'
    
n, m = [int(x) for x in input().split()]
dsMon = []
for i in range(n):
    ma = input()
    ten = input()
    a = Mon(ma, ten)
    dsMon.append(a)

dsCa = []
for i in range(m):
    s = input().split()
    ma = s[0]
    ngay = s[1]
    gio = s[2]
    nhom = s[3]
    b = Ca(i+1, ma, ngay, gio, nhom)
    # print(b)
    dsCa.append(b)

for i in dsCa:
    for j in dsMon:
        if i.maMon == j.ma:
            i.ten = j.ten
            break
        

dsCa_sorted = sorted(dsCa, key=lambda x: (x.ngay, x.gio))

for x in dsCa_sorted:
    print(x)
'''
2 10
INT1155
Tin hoc co so 2
INT1339
Ngon ngu lap trinh C++
INT1155 25/11/2021 08:00 01
INT1155 04/12/2021 08:00 02
INT1155 04/12/2021 13:30 03
INT1155 25/11/2021 13:30 04
INT1155 25/11/2021 15:00 05
INT1339 25/11/2021 08:00 01
INT1339 25/11/2021 08:00 02
INT1339 04/12/2021 13:30 03
INT1339 04/12/2021 13:30 04
INT1339 04/12/2021 15:00 05
'''