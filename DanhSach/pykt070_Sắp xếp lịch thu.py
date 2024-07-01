class Mon:
    def __init__(self, ma, ten, ht) -> None:
        self.ma = ma
        self.ten = ten
        self.ht = ht
    def __str__(self) -> str:
        return f'Môn học: {self.ten}  Mã môn: {self.ma} {self.ht}'
    
class Ca:
    def __init__(self, ma, ngay, gio, phong) -> None:
        self.ma = f'C{ma:03d}'
        self.ngay = ngay
        self.gio = gio
        self.phong = phong
    def __str__(self) -> str:
        return f"{self.ma} {self.ngay} {self.gio} {self.phong}"
    
class Lich:
    def __init__(self, maca, mamon, manhom, sl) -> None:
        self.maca = maca
        self.mamon = mamon
        self.manhom = manhom
        self.sl = sl
        self.ngay = ""
        self.gio = ""
        self.phong = ""
        self.tenmon = ""
    def setNgay(self, s):
        self.ngay = s
    def setGio(self, s):
        self.gio = s
    def setPhong(self, s):
        self.phong = s
    def setTenmon(self, s):
        self.tenmon = s
    def __str__(self) -> str:
        return f'{self.ngay} {self.gio} {self.phong} {self.tenmon} {self.manhom} {self.sl}'
def read(path):
    with open(path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines
file1 = read('tệp văn bản\MONTHI.in')
n = file1[0]
ds_mon = []
dem1 = 0
for i in range(1, len(file1), 3):
    dem1 += 1
    ma = file1[i]
    ten = file1[i+1]
    ht = file1[i+2]
    a = Mon(ma, ten, ht)
    ds_mon.append(a)
# for i in ds_mon:
#     print(i)  
     
file2 = read("tệp văn bản\CATHI.in")
m = file2[0]
ds_ca = []
dem2 = 0
for i in range(1, len(file2), 3):
    dem2 += 1
    ngay = file2[i]
    gio = file2[i+1]
    phong = file2[i+2]
    a = Ca(dem2, ngay, gio, phong)
    ds_ca.append(a)
# for i in ds_ca:
#     print(i)

file3 = read("tệp văn bản\LICHTHI.in")
ds_thi = []
k = file3[0]
for i in range(1, len(file3)):
    # b = i.split()
    maca, mamon, manhom, sl = [str(x) for x in file3[i].split()]
    a = Lich(maca, mamon, manhom, sl)
    ds_thi.append(a)
for i in ds_thi:
    for j in ds_ca:
        if i.maca == j.ma:
            i.setNgay(j.ngay)
            i.setGio(j.gio)
            i.setPhong(j.phong)
            break
    for k in ds_mon:
        if i.mamon == k.ma:
            i.setTenmon(k.ten)
            break
ds_thi_sort = sorted(ds_thi, key=lambda x: (x.ngay, x.gio, x.maca))
for i in ds_thi_sort:
    print(i)    
    
        