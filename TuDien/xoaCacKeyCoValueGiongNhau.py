test_dict = {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}
d = dict()

for key, value in test_dict.items():
    if value not in d.values():
        d[key] = value
print(d)

       