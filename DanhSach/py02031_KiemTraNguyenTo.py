import math


def nt(n):
    if n<2:
        return False
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

n, m = map(int, input().split())
a = list()
for i in range(0, n):
    s = list(int(x) for x in input().split())
    a.append(s)
for i in range(0, n):
    for j in range(0, m):
        if nt(a[i][j]):
            a[i][j] = 1
        else:
            a[i][j] = 0
        
for i in range(0, n):
    print(" ".join(str(x) for x in a[i]))
