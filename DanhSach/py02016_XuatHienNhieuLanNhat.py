
t = int(input())
while t>0:
    t -= 1
    n = int(input())
    a = list(int(x) for x in input().split())
    d = dict()
    for i in range(len(a)):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    sorted_dict = dict(sorted(d.items(), key = lambda item : item[1], reverse = True))
    # for i in sorted_dict:
    #     print(i, " ", sorted_dict.get(i))
    kq = next(iter(sorted_dict.values()))
    if kq <= int(n)//2:
        print("NO")
    else: 
        l = list()
        for i in sorted_dict:
            if sorted_dict.get(i) == kq and kq:
                l.append(i)
        l.sort()
        print(l[0])
        
            
    
'''
2
9
3 3 4 2 4 4 2 4 4
8
3 3 4 2 4 4 2 4
'''