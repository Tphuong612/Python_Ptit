from itertools import combinations
n, k = [int(x) for x in input().split()]
ten = input().split()
ten_khac = sorted(list(set(ten)))

kq = combinations(ten_khac, k)
for i in kq:
    print(*i)
