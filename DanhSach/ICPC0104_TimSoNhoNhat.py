import re


t = int(input())
while t>0:
    t -= 1
    s = input()
    so = map(int, re.findall(r'\d+', s))
    print(min(so))