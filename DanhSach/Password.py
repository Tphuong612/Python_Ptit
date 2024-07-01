s = "Phuong123@"
hoa, thuong, so, dacBiet = 0, 0, 0, 0
for i in s:
    if i.islower(): 
        thuong += 1
    if i.isupper():
        hoa += 1
    if i.isdigit():
        so += 1
    if not i.isdigit() and not i.isalpha() and not i.isspace():
        dacBiet += 1
if hoa!=0 and thuong!=0 and so!=0 and dacBiet!=0 and len(s)>=6 and len(s)<=16:
    print("YES")
else:
    print("NO")
