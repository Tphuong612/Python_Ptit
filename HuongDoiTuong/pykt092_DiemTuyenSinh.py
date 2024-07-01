import functools as f 
def chuan(str):
    a = str.split()
    kq = " ".join(a)
    return kq
class SV:
    def __init__(self, id, ht, diem, dt, kv) -> None:
        self.id = f'TS{id:02d}'
        self.ht = ht
        self.diem = diem
        self.dt = dt
        self.kv = kv
        # self.tong = 0
        # self.sum()
        
    def uuKv(self):
        kv = self.kv
        if kv == 1:
            return 1.5
        elif kv == 2:
            return 1
        elif kv == 3:
            return 0
        
    def uuDt(self):
        dt = self.dt
        if dt == 'Kinh':
            return 0
        else:
            return 1.5
        
    def sum(self):
        return self.diem + self.uuKv() + self.uuDt()
    
    def loai(self):
        if self.sum() >= 20.5:
            return "Do"
        else:
            return "Truot"
    def __str__(self) -> str:
        return f'{self.id} {self.ht} {self.sum():.1f} {self.loai()}'
    
def cmp(o1, o2):
    if o1.sum()!=o2.sum(): 
        return -(o1.sum() - o2.sum())
    else:
        return o1.id < o2.id
    

n = int(input())
ds = []
for i in range(n):
    ht = chuan(input().strip().title())
    diem = float(input())
    dt = input().strip().title()
    kv = int(input())
    a = SV(i+1, ht, diem, dt, kv)
    ds.append(a)
ds.sort(key=f.cmp_to_key(cmp))
# ds.sort(key=lambda x: (-x.tong, x.id))
for i in ds:
    print(i)
    
'''
3
Nguyen  hong ngat
22
Kinh
1
  Chu thi MINh
14
Dao
3
  Chu thi MHang
26
Dao
3
'''
    


    
            