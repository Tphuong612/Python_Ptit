class Team:
    def __init__(self, ma, ten, truong) -> None:
        self.ma = f'Team{ma:02d}'
        self.ten = ten
        self.truong = truong
        
class ThiSinh:
    def __init__(self, ma, ht, team) -> None:
        self.ma = f'C{ma:03d}'
        self.ht = ht
        self.idTeam = team
        self.tenTeam = ""
        self.truong = ""
        
    def __str__(self) -> str:
        return f'{self.ma} {self.ht} {self.tenTeam} {self.truong}'
n = int(input())
ds_team = []
for i in range(n):
    ten = input()
    truong = input()
    a = Team(i+1, ten, truong)
    ds_team.append(a)

m = int(input())
ds_ts = []
for i in range(m):
    ht = input()
    maTeam = input()
    b = ThiSinh(i+1, ht, maTeam)
    ds_ts.append(b)

for i in ds_ts:
    for j in ds_team:
        if i.idTeam == j.ma:
            i.tenTeam = j.ten
            i.truong = j.truong
            break
        
ds_ts.sort(key=lambda x: x.ht)
for i in ds_ts:
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