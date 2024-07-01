from math import gcd
for j in range(int(input())): 
    a = {0: 0}
    b = [0]
    n = int(int(input()))
    l = list(map(int, input().split()))
    c = list(map(int, input().split()))
    for i in range(n):
        for p in b:
            d = gcd(p, l[i])
            cost = a[p] + c[i]
            if d not in a:
                a[d] = cost
                b.append(d)
            elif a[d] > cost:
                a[d] = cost
            print(d, a[d], b)
    if 1 not in a:
        a[1] = -1
    print(a[1])
    
# t = int(input()) #nhập số lượng bộ test
# while t > 0:
#     t -= 1
#     n = int(input()) #nhập sô lượng thẻ trong trò chơi
#     l = list(map(int, input().split())) #nhập giá trị của các thẻ 
#     c = list(map(int, input().split())) #nhập chi phí của các thẻ
#     a = {0: 0} #lưu trữ (, chi phí)
#     b = [0] #
#     for i in range(n):
#         for p in b: