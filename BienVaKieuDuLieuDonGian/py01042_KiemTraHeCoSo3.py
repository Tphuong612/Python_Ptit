def check(x):
    for i in x:
        if i!='1' and i!='2' and i!='0':
            return False
    return True

t = int(input())
while t>0:
    t -= 1
    s = input()
    if(check(s)):
        print("YES")
    else:
        print("NO")
        