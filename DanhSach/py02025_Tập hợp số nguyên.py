n, m = map(int, input().split())
a = set([int(x) for x in input().split()])
b = set([int(x) for x in input().split()])
giao =sorted(list(a.intersection(b)))
hieuAB = sorted(list(a.difference(b)))
hieuBA = sorted(list(b.difference(a)))
print(*giao)
print(*hieuAB)
print(*hieuBA)
'''
5 6
1 2 3 4 5
3 4 5 6 7 8
'''