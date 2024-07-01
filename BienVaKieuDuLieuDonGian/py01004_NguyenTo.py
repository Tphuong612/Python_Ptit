import math
def nt(x):
    if x<2:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x%i == 0:
            return False
    return True

t = int(input())
while t>0:
    t -= 1
    n = int(input())
    k = 0
    for i in range(1, n, 1):
        if(math.gcd(i, n) == 1): 
            k = k + 1
    if nt(k): 
        print("YES")
    else: 
        print("NO")
    