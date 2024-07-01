def Gia(loai, ghe):
    if loai == "Xe_con":
        if ghe == "5":
            return 10000
        elif ghe == "7":
            return 15000
    elif loai == "Xe_tai" and ghe == "2":
        return 20000
    elif loai == "Xe_khach":
        if ghe =="29":
            return 50000
        elif ghe =="45":
            return 70000
  
t = int(input())
l = []
d = {}
for i in range(t):
    l.append(input())
    
for i in l:
    a = i.split(" ")
    loai = a[1]
    ghe = a[2]
    state = a[3]
    date = a[4]
    if state == "IN":
        if date not in d.keys():
            d[date] = Gia(loai, ghe)
        else:
            d[date] += Gia(loai, ghe)
for i, j in d.items():
    print(f'{i}: {j}')
'''
5
30F-123.15 Xe_con 5 OUT 06/11/2021
30F-123.15 Xe_con 5 IN 06/11/2021
30H-123.15 Xe_con 7 IN 06/11/2021
29H-222.68 Xe_tai 2 IN 07/11/2021
30G-511.15 Xe_con 5 IN 07/11/2021
'''    
        
    

    
        