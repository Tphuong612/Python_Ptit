import math


def nt(n):
    if n<2:
        return False
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

n, x = map(int, input().split())
dem = 0
print(x, end=" ")
i = 2
while dem < n:
    if nt(i):
        dem += 1
        x += i
        print(x, end = " ")
    i += 1
    
        