import functools as f


n = int(input())
d = dict()
while n>0:
    n -= 1
    ten = input().lower().title()
    c, t = map(int, input().split())
    d[ten] = [c, t]
sd = dict(sorted(d.items(), key = lambda x: (-x[1][0], x[1][0], x[0])))
for i in sd:
    print(i, d[i][0], d[i][1])

'''
2
Nguyen Van NAM
167 600
Tran THI Ngoc
168 600
'''