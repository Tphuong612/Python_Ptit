t = int(input())
while t>0:
    t -= 1
    s = input()
    kq = ''
    for i in range(len(s)):
        if(not s[i].isdigit()):
            kq += s[i]
        else:
            kq += s[i-1]*(int(s[i]) - 1)
    print(kq)
