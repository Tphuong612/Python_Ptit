
class SinhVien:
    def __init__(self, msv, ht, l) -> None:
        self.msv = msv
        self.ht = ht
        self.l = l
        self.cc = 10
        self.note = ""
    def setCC(self, str):
        muon = str.count("m")
        vang = str.count("v")
        kq = 10 - muon - 2*vang
        if kq < 0:
            self.cc = 0
        else:
            self.cc = kq
    def Note(self):
        cc = self.cc
        if cc == 0:
            self.note = "KDDK"
        return self.note
    def __str__(self) -> str:
        return f'{self.msv} {self.ht} {self.l} {self.cc} {self.Note()}'
    
t = int(input())
sv = []
for i in range(t):
    msv = input()
    name = input()
    lop = input()
    a = SinhVien(msv, name, lop)
    sv.append(a)
for i in range(t):
    msv, kq = input().split()
    for j in sv:
        if msv == j.msv:
            j.setCC(kq)
            break
for i in sv:
    print(i)
'''
4
B19DCCN999
Le Cong Minh
D19CQAT02-B
B19DCCN998
Tran Truong Giang
D19CQAT02-B
B19DCCN997
Nguyen Tuan Anh
D19CQCN04-B
B19DCCN994
Nguyen Tuan Anh
D19CQCN04-B
B19DCCN998 xxxmxmmvmx
B19DCCN997 xmxmxxxvxx
B19DCCN999 xvxmxmmvvm
B19DCCN994 xxxxxxxxxx
'''
        