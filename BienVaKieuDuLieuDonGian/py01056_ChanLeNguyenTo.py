import math
def nt(s):
    if s<2:
        return False
    for i in range(2, int(math.sqrt(s))+1):
        if s%i==0:
            return False
    return True

def check(n):
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
        if (i%2==0 and int(n[i])%2==1) or (i%2==1 and int(n[i])%2==0):
            return False
    if not nt(sum):
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
        
    