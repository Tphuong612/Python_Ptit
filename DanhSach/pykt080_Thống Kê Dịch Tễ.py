dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

m, n = map(int, input().split()) # m hàng, n cột
matrix = []
for i in range(m):
    a = [int(x) for x in input().split()]
    matrix.append(a)
    
# print(matrix)
vt = []
for i in range(m):
    for j in range(n):
        if matrix[i][j] == -1:
            vt.append([i, j])
sum = 0
while len(vt) > 0:
    top = vt.pop(0)
    for i in range(8):
        x = top[0] + dx[i]
        y = top[1] + dy[i]
        if x >= 0 and y >= 0 and x < m and y < n:
            sum += matrix[x][y]
            matrix[x][y] = 0
print(sum)