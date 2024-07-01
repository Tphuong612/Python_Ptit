def convert(time):
    gio = int(time[:2])
    phut = int(time[-2:])
    return gio*60 + phut
class Game:
    def __init__(self, id, name, vao, ra) -> None:
        self.id = id
        self.name = name
        self.vao = convert(vao)
        self.ra = convert(ra)
        self.tg = self.ra - self.vao
    def tinhGio(self):
        a = self.tg
        gio = a//60
        phut = a - gio*60
        return f'{gio} gio {phut} phut'
    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.tinhGio()}"
t = int(input())
MangGame = []
for i in range(t):
    id = input()
    name = input()
    vao = input()
    ra = input()
    a = Game(id, name, vao, ra)
    MangGame.append(a)
MangGame_sorted = sorted(MangGame, key= lambda x: x.tg, reverse=True)
for i in MangGame_sorted:
    print(i)
'''
3
01T
Nguyen Van An
09:00
10:30
06T
Hoang Van Nam
15:30
18:00
02I
Tran Hoa Binh
09:05
10:00
'''