def KhongGiam(s):
    for i in range(len(s)-1):
        if int(s[i]) > int(s[i+1]):
            return False
    return True

t = int(input())
while t>0:
    t -= 1
    n = input()
    if KhongGiam(n):
        print("YES")
    else:
        print("NO")