p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    tmp = input().split()
    k = int(tmp[0])
    if(k == 0): break
    s = tmp[1]
    kq =""
    for i in range(len(s)):
        j = p.find(s[i])
        kq += p[(j+k)%28]
    print(kq[::-1])


