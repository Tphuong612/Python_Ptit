s = input()
thuong, hoa = 0, 0
for i in range(len(s)):
    if s[i].islower(): 
        thuong += 1
    else: 
        hoa += 1
if thuong >= hoa:
    print(s.lower())
else: 
    print(s.upper())