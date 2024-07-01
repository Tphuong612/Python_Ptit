n, m = map(int, input().split()) #n hàng, m cột
matran = []
for i in range(n):
    hang = [int(x) for x in input().split()]
    matran.append(hang)

if n>m:
    kc = n - m
    dem = 0
    for i in range(n):
        if (i+1) % 2 == 1 and dem < kc: 
            dem += 1
            continue
        for j in range(m):
            print(matran[i][j], end=" ")
        print()
else:
    kc = m - n
    for i in range(n):
        dem = 0
        for j in range(m):
            if (j+1)%2==0 and dem < kc:
                dem += 1
                continue
            print(matran[i][j], end=" ")
        print()
                
            
'''
6 4
2 8 7 6
6 3 2 6
7 2 2 8
9 9 9 8
9 6 6 3
7 7 4 9

4 6
2 8 7 6 4 3
6 3 2 6 7 2
7 2 2 8 9 1
9 9 9 8 0 7
'''