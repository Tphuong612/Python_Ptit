import math


def nt(n):
    if n<2:
        return False
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

t = input()
a = list(int(x) for x in input().split())
d = dict()
for x in a:
    if nt(x): 
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
for i in d:
    print(i, d.get(i))
'''
10
2 4 7 5 7 8 9 3 7 2
'''