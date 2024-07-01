def check(s):
    for i in range(len(s)):
        if s[0] == s[1]:
            return False
        else:
            if i%2==0 and i!=0 and s[0] != s[i] :
                return False
            if i%2==1 and i!=0 and s[1] != s[i] :
                return False
    return True

t = int(input())
while t>0:
    t -= 1
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")