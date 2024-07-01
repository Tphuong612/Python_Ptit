    
from datetime import datetime

class Khach:
    def __init__(self, id,  name, phong, nhan, tra, dv) -> None:
        self.id = f'KH{id:02d}'
        self.name =  name
        self.phong = phong
        self.nhan = nhan
        self.tra = tra
        self.dv = dv
    def tg(self):
        begin = datetime.strptime(self.nhan, "%d/%m/%Y")
        end = datetime.strptime(self.tra, "%d/%m/%Y")
        time = end - begin
        return time.days + 1
    def total(self):
        s = self.phong
        t = self.tg()
        d = self.dv
        if s.startswith('1'):
            kq = t*25 + d
        elif s.startswith('2'):
            kq = t*34 + d
        elif s.startswith('3'):
            kq = t*50 + d
        else:
            kq = t*80 + d
        return kq
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.phong} {self.tg()} {self.total()}'
    
def cmp(a):
    return a.total() 

t = int(input())
dsKhach = []
for i in range(t):
    name = input().strip()
    phong = input().strip()
    nhan = input().strip()
    tra = input().strip()
    dv = int(input())
    a = Khach(i+1, name, phong, nhan, tra, dv)
    dsKhach.append(a)
ds_sorted = sorted(dsKhach, key=cmp, reverse=True)
for i in ds_sorted:
    print(i)
"""
3
Huynh Van Thanh
103 
05/06/2010
05/06/2010
15
Le Duc Cong
106 
08/03/2010
01/05/2010
220
Tran Thi Bich Tuyen
207
10/04/2010
21/04/2010
96
"""
    
            