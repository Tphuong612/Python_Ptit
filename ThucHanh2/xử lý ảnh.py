
import sys

t=int(sys.stdin.readline())
while t>0:
    n,m,k=map(int,sys.stdin.readline().split())
    a=[[0]*(m+1)]
    for i in range(n):
        a.append([0]+[int(i) for i in sys.stdin.readline().split()])
    b=[[0]*(m+1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            b[i][j]=b[i][j-1]+b[i-1][j]-b[i-1][j-1]+a[i][j]
    for i in range(1,n-k+2):
        for j in range(1,m-k+2):
            print((b[i+k-1][j+k-1]-b[i+k-1][j-1]-b[i-1][j+k-1]+b[i-1][j-1])//(k*k),end=" ")
        print()
    t-=1
    
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