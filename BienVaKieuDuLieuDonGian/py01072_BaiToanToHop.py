from itertools import combinations
n, k = map(int, input().split())
ls = map(int, input().split())
kq = list(set(ls))
kq.sort()
#print(kq)
combinations_result = combinations(kq, k)
for i in combinations_result:
    print(*i)