test = 10
s = set()
while test>0:
    data = input()
    base = data.split()
    test -= len(base)
    for i in range(0, len(base)):
        s.add(int(base[i])%42)
print(len(s))

'''
42 84 252 420 840
126 42 84 420 126
'''