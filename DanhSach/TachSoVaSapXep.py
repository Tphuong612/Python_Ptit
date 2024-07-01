import re
l = []
n = int(input())
for i in range(n):
    s = input()
    a = re.findall('[0-9]+', s)
    for x in a:
        l.append(int(x))
l.sort()
for x in l:
    print(x)

