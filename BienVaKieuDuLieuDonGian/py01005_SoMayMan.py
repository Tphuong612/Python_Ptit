
s = input()
a, b = 0, 0
for i in range(len(s)):
    if s[i] == '4': 
        a += 1
    if s[i] == '7':
        b += 1
if a+b==4 or a+b==7: 
    print("YES")
else: 
    print("NO")


