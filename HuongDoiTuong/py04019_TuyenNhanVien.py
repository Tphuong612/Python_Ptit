class NhanVien:
    def __init__(self, id, name, lt, th) -> None:
        self.id = id
        self.name = name
        self.lt = lt
        self.th = th
    def diem(self):
        if self.lt > 10:
            self.lt /= 10
        if self.th > 10:
            self.th /= 10
        return (self.th + self.lt)/2 
    def xepLoai(self):
        a = self.diem()
        if a > 9.5:
            return "XUAT SAC"
        elif a >= 8:
            return "DAT"
        elif a >= 5:
            return "CAN NHAC"
        else:
            return "TRUOT"
            
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.diem():.2f} {self.xepLoai()}'
def cmp(a):
    return a.diem()
nv = []
t = int(input())
for i in range(t):
    id = 'TS0' + str(i+1)
    name = input()
    lt = float(input())
    th = float(input())
    a = NhanVien(id, name, lt, th)
    nv.append(a)
nv_sorted = sorted(nv, key = cmp, reverse=True)
for i in nv_sorted:
    print(i)
'''
3
Nguyen Thai Binh
45
75
Le Cong Hoa
4
4.5
Phan Van Duc
56
56
'''        