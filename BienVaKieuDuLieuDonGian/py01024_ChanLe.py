def ChanLe(s):
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    for i in range(len(s)-1):
        if abs(int(s[i]) - int(s[i+1])) != 2:
            return False
    if sum%10 == 0:
        return True
    return False

t = int(input())
while t>0:
    t -= 1
    n = input()
    if(ChanLe(n)):
        print("YES")
    else:
        print("NO")