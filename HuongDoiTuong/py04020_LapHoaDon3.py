class MatHang:
    def __init__(self, ma, ten, sl, dg, ck) -> None:
        self.ma = ma
        self.ten = ten
        self.sl = sl
        self.dg = dg
        self.ck = ck

    def tong(self):
        return self.sl*self.dg - self.ck
    def __str__(self) -> str:
        return f'{self.ma} {self.ten} {self.sl} {self.dg} {self.ck} {self.tong()}'
def cmp(a):
    return a.tong()
t = int(input())
ds = []
for i in range(t):
    ma = input()
    ten = input()
    sl = int(input())
    dg = int(input())
    ck = int(input())
    a = MatHang(ma, ten, sl, dg, ck)
    ds.append(a)
ds_sorted = sorted(ds, key=cmp, reverse=True)
for x in ds_sorted:
    print(x)
'''
3
ML01
May lanh SANYO
12
4000000
2400000
ML02
May lanh HITACHI
4
2550000000
0
ML03
May lanh NATIONAL
5
3000000
150000
'''    
    
        