class Ca:
    def __init__(self, ma, ngay, gio, phong) -> None:
        self.ma = f'C{ma:03d}'
        self.ngay = ngay
        self.gio = gio
        self.phong = phong
    def __str__(self) -> str:
        return f"{self.ma} {self.ngay} {self.gio} {self.phong}"
    
with open("tệp văn bản\CATHI.in") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
# for i in lines:
#     print(i)

n = lines[0]
dem = 0
ds = []
for i in range(1, len(lines), 3):
    dem += 1
    ngay = lines[i]
    gio = lines[i+1]
    phong = lines[i+2]
    a = Ca(dem, ngay, gio, phong)
    ds.append(a)
ds_sorted = sorted(ds, key=lambda x: (x.ngay, x.gio, x.ma))    
for i in ds_sorted:
    print(i)
    
