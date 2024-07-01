s = input()
while len(s)!=1:
    p = len(s)//2
    kq = int(s[:p]) + int(s[p:])
    print(kq)
    s = str(kq)