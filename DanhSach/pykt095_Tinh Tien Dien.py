import re


class TienDien:
    def __init__(self, id, ten, loai, cu, moi):
        tmp = re.sub(" +", " ", ten)
        self.ten = tmp.strip().title()
        self.loai = loai
        self.cu = cu
        self.moi = moi
        self.id = f'KH{id:02d}'
    def tienvuot(self):
        used = self.moi - self.cu
        tien = 0
        if self.loai == 'A':
            if used > 100:
                vuot = used - 100
                tien = vuot*1000
        if self.loai == 'B':
            if used > 500:
                vuot = used - 500
                tien = vuot*1000
        if self.loai == 'C':
            if used > 200:
                vuot = used - 200
                tien = vuot*1000
        return tien
    
    def thue(self):
        return self.tienvuot()//20
    
    def dinhmuc(self):
        used = self.moi - self.cu
        if self.loai == 'A':
            if used >= 100:
                dinhmuc = 100*450
            else:
                dinhmuc = used*450
        if self.loai == 'B':
            if used >= 500:
                dinhmuc = 500*450
            else:
                dinhmuc = used*450
        if self.loai == 'C':
            if used >= 200:
                dinhmuc = 200*450
            else:
                dinhmuc = used*450
        return dinhmuc
    def tong(self):
        return self.thue() + self.dinhmuc() + self.tienvuot()
    def __str__(self) -> str:
        return f'{self.id} {self.ten} {self.dinhmuc()} {self.tienvuot()} {self.thue()} {self.tong()}'
def cmp(a):
    return a.tong()
n = int(input())
ds = []
for i in range(n):
    name = input()
    loai, cu, moi = input().split()
    cu = int(cu)
    moi = int(moi)
    a = TienDien(i+1, name, loai, cu, moi)
    ds.append(a)
ds_sorted = sorted(ds, key=cmp, reverse=True)
for i in ds_sorted:
    print(i)
'''
3
 nGuyEn Hong Ngat
C 200 278
 Chu thi    minh
A 120 160
Tran Thi Thu Phuong
A 120 240
'''
        
            
        
        
        
            
        
    