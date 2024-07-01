class TramDo:
    def __init__(self, stt, name, start, finish, mua) -> None:
        self.name = name
        self.start = start
        self.finish = finish
        self.time = 0
        self.amount = 0
        self.id = f'T{stt:02d}'
    def getName(self):
        return self.name
    def setAmount(self, x):
        self.amount += x
    def setTime(self, x):
        self.time += x
    def average(self):
        return self.amount/self.time
    def __str__(self):
        return f'{self.id} {self.name} {self.average():.2f}'
    
def doiSangPhut(time):
    return int(time[0:2])*60 + int(time[3:])  
t = int(input())
MangCacTram = []
Tram = [] #chua ten cac tram
dem = 0
for i in range(t):
    name = input()
    bd = input()
    kt = input()
    mua = int(input())
    tg = (doiSangPhut(kt) - doiSangPhut(bd))/60
    if name not in Tram:
        dem += 1
        a = TramDo(dem, name, bd, kt, mua)
        Tram.append(name)
        MangCacTram.append(a)
        a.setAmount(mua)
        a.setTime(tg)
    else:
        for j in MangCacTram:
            if j.getName() == name:
                j.setAmount(mua)
                j.setTime(tg)
                break  
for i in MangCacTram:
    print(i)
'''
10
Dong Anh
07:30
08:00
60
Cau Giay
07:45
08:12
50
Soc Son
08:00
09:15
78
Dong Anh
18:50
20:00
88
Cau Giay
19:01
20:00
77
Soc Son
19:06
20:21
66
Dong Anh
21:00
21:40
49
Cau Giay
21:50
22:20
68
Dong Anh
22:15
23:45
30
Cau Giay
22:50
23:45
35
'''