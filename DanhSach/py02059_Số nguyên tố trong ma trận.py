from math import sqrt


def checknt(n):
    if n<2:
        return 0
    for i in range(2, int(sqrt(n))+1):
        if n%i==0:
            return 0
    return 1
nt = []
n, m = map(int, input().split())
matrix = []
for i in range(n):
    hang = [int(i) for i in input().split()]
    matrix.append(hang)
    for i in hang:
        if checknt(i) == 1:
            nt.append(i)
nt.sort()
if len(nt) == 0:
    print("NOT FOUND")
else:
    nt_max = max(nt)
    print(nt_max)
    # print(*nt)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == nt_max:
                print(f'Vi tri [{i}][{j}]')
                

'''
6 4
23 21 26 10
13 13 22 14
28 29 28 23
29 19 11 19
16 26 24 21
13 25 21 29
'''