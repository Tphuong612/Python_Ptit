# t = int(input())
# l = [] #chứa ma trận
# sum = [] #chua tổng các hàng
# for i in range(t):
#     a = [int(x) for x in input().split()]
#     tmp = 0
#     for x in a:
#         tmp += x
#     sum.append(tmp)
#     l.append(a)

# y = [] #chứa các hiệu a[0] - a[1], a[1] - a[2],...
# for i in range(t-1):
#     y.append((sum[i]-sum[i+1])//2)

# ans = []
# ans.append((l[0][1] + y[0])//2) #a[0]

# for i in y:
#     ans.append(ans[-1] - i)

# for i in ans:
#     print(i, end=' ')

'''
4
0 3 6 7
3 0 5 6
6 5 0 9
7 6 9 0
'''
n = int(input())
a, b = [[0]] * n, []
s = 0
for i in range(n) :
    a[i] = [int(x) for x in input().split()]
    b.append(sum(a[i]))
    s += b[-1]
if n == 2 :
    for i in b :
        print(int(i / 2), end = ' ')
else :
    s = int(s / 2 / (n - 1))
    for i in b :
        print(int((i - s) / (n - 2)), end = ' ')