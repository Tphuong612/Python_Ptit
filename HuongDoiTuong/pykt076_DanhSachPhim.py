from datetime import datetime
class BoPhim:
    def __init__(self,id, ma, ngay, ten, stap) -> None:
        self.id = f'P{id:03d}'
        self.ma = ma
        self.ten = ten
        self.ngay = datetime.strptime(ngay, "%d/%m/%Y")
        
        self.stap = stap
        self.loai = ""
    def __str__(self) -> str:
        return f'{self.id} {self.loai} {self.ngay.strftime("%d/%m/%Y")} {self.ten} {self.stap}'
        
class TheLoai:
    def __init__(self, id, ten) -> None:
        self.id = f'TL{id:03d}'
        self.ten = ten

n, m = [int(x) for x in input().split()]
dsTheLoai = []
for i in range(n):
    ten = input()
    a = TheLoai(i+1, ten)
    dsTheLoai.append(a)
    
dsBoPhim = []
for i in range(m):
    ma = input()
    ngay = input()
    name = input()
    tap = int(input())
    b = BoPhim(i+1, ma, ngay, name, tap)
    dsBoPhim.append(b)
for i in dsBoPhim:
    for j in dsTheLoai:
        if i.ma == j.id:
            i.loai = j.ten
            break
dsBoPhim_sorted = sorted(dsBoPhim, key=lambda x: (x.ngay, x.ten, -x.stap))
for i in dsBoPhim_sorted:
    print(i)
'''
2 3
Hai huoc
Tinh cam
TL001
25/11/2021
Phim so 1
10
TL001
04/12/2021
Phim so 2
15
TL002
25/11/2021
Phim so 3
5
'''
