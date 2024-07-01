def testcase():
    s = input()
    check = 1
    for i in range(len(s)):
        if s[i] != '4' and s[i] != '7': 
            check = 0
            break
    if check == 0:
        print("NO")
    else: 
        print("YES")

t = int(input())
while t>0:
    t -= 1
    testcase()
    
    
