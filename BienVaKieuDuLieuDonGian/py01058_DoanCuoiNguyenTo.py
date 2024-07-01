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
    tmp = int(n[-4:])
    if nt(tmp):
        print("YES")
    else:
        print("NO")
        
