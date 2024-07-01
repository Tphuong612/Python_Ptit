class GV:
    def __init__(self, id, ten, ma, tin, cm) -> None:
        self.id = f'GV{id:02d}'
        self.ten = ten
        self.ma = ma
        self.tin = tin
        self.cm = cm
    def mon(self):
        s = self.ma
        if s.startswith('A'):
            return 'TOAN'
        elif s.startswith('B'):
            return 'LY'
        else:
            return 'HOA'
    def uu(self):
        s = self.ma
        if s.endswith('1'): 
            return 2
        elif s.endswith('2'):
            return 1.5
        elif s.endswith('3'):
            return 1
        else:
            return 0
    def sum(self):
        diem = self.tin*2 + self.cm + self.uu()
        return diem
    def loai(self):
        if self.sum() >= 18:
            return "TRUNG TUYEN"
        else: 
            return "LOAI"
    def __str__(self) -> str:
        return f'{self.id} {self.ten} {self.mon()} {self.sum():.1f} {self.loai()}'
def cmp(a):
    return a.sum()  

t = int(input())
ds = []
for i in range(t):
    name = input().strip()
    ma = input().strip()
    tin = float(input())
    cm = float(input())
    a = GV(i+1, name, ma, tin, cm)
    ds.append(a)
ds_sorted = sorted(ds, key=cmp, reverse=True)
for i in ds_sorted:
    print(i)
'''
3
Le Van Binh
A1
7.0
3.0
Tran Van Toan
B3
4.0
7.0
Hoang Thi Tam
C2
7.0
6.0
'''