from collections import Counter


s = "vietnamvietna"
d = dict()
for i in s: 
    if i in d.keys(): 
        d[i] += 1
    else:
        d[i] = 0
print(d)

c = Counter(s)
for i in c:
    print(i,c[i])
