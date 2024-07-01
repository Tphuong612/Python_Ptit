def doiSangPhut(time):
    return int(time[0])*60 + int(time[2:])
class CuaRo:
    def __init__(self, ht, dv, den) -> None:
       self.ht = ht
       self.dv = dv
       self.den = den
       self.id = ""
       self.setId()
       self.vt = 0
       self.setV()
    def setId(self):
        id = ""
        for i in self.dv.split():
            id += i[0]
        for i in self.ht.split():
            id += i[0]
        self.id = id
        
    def tg(self):
        time = doiSangPhut(self.den) - doiSangPhut('6:00')
        return time/60
    def setV(self):
        vt = round(120/self.tg())
        self.vt = vt
    def __str__(self) -> str:
        return f"{self.id} {self.ht} {self.dv} {self.vt} Km/h"

t = int(input())
ds = []
for i in range(t):
    ht = input().strip()
    dv = input().strip()
    den = input().strip()
    a = CuaRo(ht, dv, den)
    ds.append(a)
ds_sorted = sorted(ds, key = lambda x: x.den)
for i in ds_sorted:
    print(i)
"""
3
Tran Vu Minh
Ha Noi
8:30
Vu Ngoc Hoang
Hoa Binh
8:20
Pham Dinh Tan
An Giang
8:45
"""
    
    