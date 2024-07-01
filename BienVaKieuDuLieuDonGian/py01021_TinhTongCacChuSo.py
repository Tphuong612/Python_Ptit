t = int(input())
while t>0:
    t -= 1
    s = input()
    tu = list()
    sum = 0
    for i in s:
        if i.isdigit():
            sum += int(i)
        else:
            tu.append(i)
    tu.sort()
    kq = "".join(tu) + str(sum)
    print(kq)
'''
2
AC2BEW3
ACCBA10D2EW30
'''