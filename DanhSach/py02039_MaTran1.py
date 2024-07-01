n = int(input())
a = list()
for i in range(0, n):
    s = list(int(x) for x in input().split())
    a.append(s)
k = int(input())
sum = 0
cheo = 0
for i in range(0, n):
    for j in range(0, n):
        sum += a[i][j]
        if i==j:
            cheo += a[i][j]
sum1 = 0 #tong cac ptu nam phia tren

for i in range(0, n):
    for j in range(i+1, n):
        sum1 += a[i][j]
sum2 = sum - sum1 - cheo #tong cac phan tu nam phia duoi
lech = abs(sum1-sum2)
if lech<=k:
    print("YES")
else:
    print("NO")
print(lech)
'''
5
2 8 10 6 7
6 3 2 6 9
10 2 6 2 8
9 9 7 9 8
9 6 5 6 9
5
'''