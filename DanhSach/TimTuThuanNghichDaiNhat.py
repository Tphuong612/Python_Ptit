d = dict()
len_max = -1
file = open('VANBAN.in', 'r')
for line in file:
    s = line.split()
    for x in s:
        if x == x[::-1]:
            len_max = max(len_max, len(x))
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
for x, y in d.items():
    if len_max == len(x):
        print(x, y)