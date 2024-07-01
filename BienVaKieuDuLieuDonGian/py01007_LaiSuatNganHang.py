import math
t = int(input())
while t>0:
    t -= 1
    n, x, m = map(float, input().split())
    year = math.ceil(math.log(m/n, 1+x/100))
    print(year)