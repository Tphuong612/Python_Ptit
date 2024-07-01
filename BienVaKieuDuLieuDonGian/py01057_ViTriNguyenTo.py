import math
def nt(s):
    if s<2:
        return False
    for i in range(2, int(math.sqrt(s))+1):
        if s%i==0:
            return False
    return True

def check(n):
    for i in range(len(n)):
        if (nt(i) and not nt(int(n[i]))) or (not nt(i) and nt(int(n[i]))):
            return False
    return True

t = int(input())
while t>0:
    t -= 1
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")           