import math


t = int(input())
while t>0:
    t -= 1
    a = int(input())
    b = int(input())
    ucln = math.gcd(a,b)
    print(ucln)
    