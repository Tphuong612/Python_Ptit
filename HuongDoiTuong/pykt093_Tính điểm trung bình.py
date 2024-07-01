import math
import re


class Diem:
    def __init__(self, msv, name, mon1, mon2, mon3):
        self.msv = msv
        self.name = name
        self.mon1 = mon1
        self.mon2 = mon2
        self.mon3 = mon3
        self.dtb = math.ceil((mon1*3 + mon2*3 + mon3*2)/8 *100)/100
        self.stt = ""
    def setSTT(self, s):
        self.stt = s
    def __str__(self) -> str:
        return f"{self.msv} {self.name} {self.dtb:.2f} {self.stt}"

n = int(input())
ds = []
for i in range(n):
    name = input().strip().title()
    name = re.sub(' +', ' ', name)
    mon1 = float(input())
    mon2 = float(input())
    mon3 = float(input())
    msv = f'SV{i+1:02d}'
    a = Diem(msv, name, mon1, mon2, mon3)
    ds.append(a)

ds_sort = sorted(ds, key=lambda x: (-x.dtb, x.msv))
for i in range(len(ds_sort)):
    ds_sort[i].setSTT(i+1)
for i in range(1, len(ds_sort)):
    if ds_sort[i].dtb == ds_sort[i-1].dtb:
        ds_sort[i].setSTT(ds_sort[i-1].stt)
for i in ds_sort:
    print(i)
    
'''
15
 ha Thi kieu     anh1
7
6
7
Pham    THI  HAO
6
7
6
TRAN THI THU PHUONG1
10
9 
9
TRAN    HAI            NAM1
9
9
9
lE THI NHAN1
8
8
8
 ha Thi kieu     anh2
7
6
7
Pham    THI  HAO2
6
7
6
TRAN THI THU PHUONG2
10
9 
9
TRAN    HAI            NAM2
9
9
9
lE THI NHAN2
8
8
8
 ha Thi kieu     anh3
7
6
7
Pham    THI  HAO3
6
7
6
TRAN THI THU PHUONG3
10
9 
9
TRAN    HAI            NAM3
9
9
9
lE THI NHAN3
8
8
8
'''