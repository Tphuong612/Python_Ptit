def diem(a):
    if a >= 39 and a <= 40:
        return 9.0
    if a >= 37 and a <= 38:
        return 8.5
    if a >= 35 and a <= 36:
        return 8.0
    if a >= 33 and a <= 34:
        return 7.5
    if a >= 30 and a <= 32:
        return 7.0
    if a >= 27 and a <= 29:
        return 6.5
    if a >= 23 and a <= 26:
        return 6.0
    if a >= 20 and a <= 22:
        return 5.5
    if a >= 16 and a <= 19:
        return 5.0
    if a >= 13 and a <= 15:
        return 4.5
    if a >= 10 and a <= 12:
        return 4.0
    if a >= 7 and a <= 9:
        return 3.5
    if a >= 5 and a <= 6:
        return 3.0
    if a >= 3 and a <= 4:
        return 2.5
t = int(input())
for _ in range(t):
    a = input().split()
    read = diem(int(a[0]))
    listen = diem(int(a[1]))
    speak = float(a[2])
    write = float(a[3])
    overall = (read + listen + speak + write)/4
    tmp = overall - int(overall)
    if tmp < 0.25:
        overall = int(overall)
    elif 0.25 <= tmp and  tmp < 0.75:
        overall = int(overall) + 0.5
    elif overall - int(overall) >= 0.75:
        overall = int(overall) + 1.0

        
    print(overall)
'''
2
15 25 5.0 5.5
22 32 6.0 6.0
'''
     