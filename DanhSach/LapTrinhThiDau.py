class Team:
    def __init__(self, idTeam, ten, truong) -> None:
        self.idTeam = f'Team{idTeam:02d}'
        self.ten = ten
        self.truong = truong
class ThiSinh:
    def __init__(self, id, ht, idTeam) -> None:
        self.id = f'C{id:03d}'
        self.ht = ht
        self.idTeam = idTeam
        self.tenTeam = ""
        self.truong = ""
    def __str__(self) -> str:
        return f"{self.id} {self.ht} {self.tenTeam} {self.truong}"
n = int(input())
dsTeam = []
for i in range(n):
    ten = input()
    truong = input()
    a = Team(i+1, ten, truong)
    dsTeam.append(a)
m = int(input())
dsts = []
for i in range(m):
    ht = input()
    maTeam = input()
    b = ThiSinh(i+1, ht, maTeam)
    dsts.append(b)

for i in dsts:
    for j in dsTeam:
        if i.idTeam == j.idTeam:
            i.tenTeam = j.ten
            i.truong = j.truong
            break
dsts.sort(key=lambda x: x.ht)
for i in dsts:
    print(i)
'''
2
BAV_MIS
Banking Academy of Vietnam
FTU Knights1
Foreign Trade University
6
Le Trung Toan
Team01
Nguyen Trinh Quoc Long
Team01
Giang Minh Tung
Team01
Nguyen Hang Giang
Team02
Nguyen Thanh Nhan
Team02
Nguyen Viet Duc
Team02
'''