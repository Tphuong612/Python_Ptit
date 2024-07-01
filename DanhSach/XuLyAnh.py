def phantu(matran, a, b, c, d):
    sum = 0
    for x in range(a, b+1):
        for y in range(c, d+1):
            sum += matran[x][y]
    return sum
t = int(input())
while t>0:
    t -= 1
    n, m, l = [int(x) for x in input().split()]
    #ma tran n hang, m cot
    matran = []
    for x in range(n):
        hang = [int(x) for x in input().split()]
        matran.append(hang)
    k = (l-1)//2
    kq =[[0]*m]*n
    for i in range(n-l+1):
        for j in range(m-l+1):
            kq[i][j] += phantu(matran, i-k, i+k, j-k, j+k)//(l*l)
    for i in range(n-l+1):
        for j in range(m-l+1):
            print(kq[i][j], end=" ")
        print()

'''
2
4 4 3
2 1 0 0
3 2 1 1
4 5 2 1
2 2 9 0
3 3 3
1 2 3
4 5 6
7 8 9
'''
    