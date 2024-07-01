
def checktn(n):
    s = str(n)
    if len(s) <= 1:
        return 0
    if s == s[::-1]:
        return 1
    return 0
nt = []
n, m = map(int, input().split())
matrix = []
for i in range(n):
    hang = [int(i) for i in input().split()]
    matrix.append(hang)
    for i in hang:
        if checktn(i) == 1:
            nt.append(i)
nt.sort()
if len(nt) == 0:
    print("NOT FOUND")
else:
    tn_max = max(nt)
    print(tn_max)
    # print(*nt)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == tn_max:
                print(f'Vi tri [{i}][{j}]')
                

'''
6 4
23 21 26 10
13 13 22 14
28 29 28 23
29 19 11 19
16 26 24 21
13 25 21 29

6 4
23 21 77 10
13 13 22 14
28 29 28 23
29 77 11 19
16 26 24 21
13 25 77 77
'''