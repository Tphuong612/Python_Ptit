
n, m = map(int, input().split())
matrix = []
l = []
for i in range(n):
    hang = [int(i) for i in input().split()]
    matrix.append(hang)
    l.extend(hang)
    
l_min = min(l)
l_max = max(l)
kc = l_max - l_min
kq = []

for i in range(n):
    for j in range(m):
        if matrix[i][j] == kc:
            kq.append((i, j))
if len(kq) == 0:
    print("NOT FOUND")
else:
    print(kc)
    for i in kq:
        print(f'Vi tri [{i[0]}][{i[1]}]')
                

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

6 4
23 21 77 10
13 13 22 14
28 67 28 23
29 77 11 67
16 51 24 21
13 25 77 77
'''