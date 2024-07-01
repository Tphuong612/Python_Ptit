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
    a, b = map(int, input().split())
    ucln = math.gcd(a, b)
    s = str(ucln)
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    if nt(sum):
        print("YES")
    else: 
        print("NO")