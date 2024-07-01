import math

def nt(n):
    if n<2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0: return False
    return True
    
def check(s):
    if not nt(len(s)):
        return False
    else:
        dem1 = dem2 = 0
        for i in range(len(s)):
            if s[i]=='2' or s[i]=='3' or s[i]=='5' or s[i]=='7': 
                dem1 += 1
            else:
                dem2 += 1
        if dem1 > dem2: 
            return True
        else:
            return False

t = int(input())
while t>0:
    t -= 1
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
           