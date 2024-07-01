def check(s):
    if len(s)<3:
        return False
    x = max(s)
    if s.find(x) == len(s) - 1:
        return False
    for i in range(0, s.find(x)-1):
        if s[i] >= s[i+1]:
            return False
    for i in range(s.find(x), len(s)-1):
        if s[i] <= s[i+1]:
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