import math


def nt(n):
    if n<2:
        return False
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

t = int(input())
while t>0:
    t -= 1
    n = int(input())
    l = list()
    for i in range(10, n):
        s = str(i)
        if int(s[::-1]) < n and s != s[::-1] and nt(i) and nt(int(s[::-1])) and i not in l :
            l.append(i)
            l.append(int(s[::-1]))
    print(" ".join(str(x) for x in l))
    '''

'''
    