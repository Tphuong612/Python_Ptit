import math
def nt(s):
    if s<2:
        return False
    for i in range(2, int(math.sqrt(s))+1):
        if s%i==0:
            return False
    return True

t = int(input())
while t>0:
    t -= 1
    n = input()
    cuoi = int(n[-3:])
    dau = int(n[:3])
    #print(dau, cuoi)
    if nt(dau) and nt(cuoi):
        print("YES")
    else:
        print("NO")
        
