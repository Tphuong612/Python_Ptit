t = int(input())
d = dict()
while t>0:
    t -= 1
    ma = input()
    mon = input()
    ht = input()
    d[ma] = mon + " " + ht
result = dict(sorted(d.items(), key=lambda x: (x[0], x[1])))
for key, value in result.items():
    print(key +" "+ value)
'''
2
MUL1320
Nhap mon da phuong tien
Bai tap lon + Van dap truc tuyen
BAS1203
Giai tich 1
Thi viet + Van dap truc tuyen
'''