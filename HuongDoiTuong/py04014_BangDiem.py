import math


class HocSinh:
    def __init__(self, ma, ten, dtb) -> None:
        self.ma = f'HS{ma:02d}'
        self.name = ten
        self.dtb = round(dtb, 1)
    def xepLoai(self):
        diem = self.dtb
        if diem >= 9:
            return 'XUAT SAC'
        elif diem >= 8:
            return 'GIOI'
        elif diem >= 7:
            return 'KHA'
        elif diem >= 5:
            return 'TB'
        else:
            return 'YEU'    
    def __str__(self) -> str:
        return f"{self.ma} {self.name} {self.dtb:.1f} {self.xepLoai()}"

t = int(input())
DsHS = []
for i in range(t):
    t = input()
    diem = [float(x) for x in input().split()]
    avg = ((diem[0] + diem[1])*2 + diem[2] + diem[3] + diem[4] + diem[5] + diem[6] + diem[7] + diem[8] + diem[9])/12 + 0.01
    hs = HocSinh(i + 1, t, avg)
    DsHS.append(hs)
ds = sorted(DsHS, key=lambda x: (-x.dtb, x.ma))
for i in ds:
    print(i)
'''
3
Luu Thuy Nhi
9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
Le Van Tam
8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
Nguyen Thai Binh
9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
'''