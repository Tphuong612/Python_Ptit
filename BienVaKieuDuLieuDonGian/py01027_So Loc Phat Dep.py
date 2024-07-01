import re
s = input()
s1 = re.sub("688", "1", s)
s2 = re.sub("68", "1", s1)
s3 = re.sub("6", "1", s2)
check = 1
for i in s3:
    if i != '1':
        check = 0
        break
if check==1:
    print("YES")
else:
    print("NO")