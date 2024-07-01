while 1:
    a = list(int(i) for i in input().split())
    if a == [0, 0, 0, 0]: 
        break
    dem = 0
    while not (a[0] == a[1] and a[1] == a[2] and a[2] == a[3]):
        dem += 1
        tmp = a[0]
        a[0] = abs(a[0] - a[1])
        a[1] = abs(a[1] - a[2])
        a[2] = abs(a[2] - a[3])
        a[3] = abs(a[3]-tmp)
    else: 
        print(dem)