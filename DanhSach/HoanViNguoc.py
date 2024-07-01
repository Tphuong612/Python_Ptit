
from itertools import permutations


def hoanvi(n):
    l = []
    ds = []
    for i in range(n):
        l.append(i+1)
    ds = permutations(l)
    kq = []
    dem = 0
    for i in ds:
        dem += 1
        k = "".join(str(x) for x in i)
        kq.append(k)
    print(len(kq))
    kq.sort(reverse=True)
    for x in kq:
        print(x, end=" ")
t = int(input())
while t > 0:
    t -= 1
    n = int(input()) 
    hoanvi(n)
    print()
