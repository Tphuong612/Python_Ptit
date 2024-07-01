
#import functools as f

class HoaDon:
    def __init__(self,id, ten, cu, moi) -> None:
        self.id = f'KH{id:02d}'
        self.ten = ten
        self.cu = cu
        self.moi = moi
        self.luong = moi - cu
    def sum(self):
        a = self.luong
        if a<=50:
            sum = a*100*1.02
        elif a<=100:
            sum = (50*100 + (a-50)*150)*1.03
        else:
            sum = (50*100 + 50*150 + (a-100)*200)*1.05
        return round(sum)
    def __str__(self) -> str:
        return f'{self.id} {self.ten} {round(self.sum())}'
def cmp(a):
    return a.sum()

t = int(input())
MangHoaDon = []
for i in range(t):
    ten = input()
    cu = int(input())
    moi = int(input())
    a = HoaDon(i+1, ten, cu, moi)
    MangHoaDon.append(a)
MangHoaDon.sort(key=cmp, reverse=True)
for i in MangHoaDon:
    print(i)
'''
3
Le Thi Thanh
468
500
Le Duc Cong
160
230
Ha Hue Anh
410
612
'''