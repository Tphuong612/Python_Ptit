t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    d = dict()
    for i in a:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    for i in d.keys():
        if d[i] % 2 == 1:
            print(i)        
'''
2
7
1 2 3 2 3 1 3
5
1 1 3 3 2
'''