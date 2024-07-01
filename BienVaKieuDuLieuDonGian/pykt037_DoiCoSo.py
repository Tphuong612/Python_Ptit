a ="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
t = int(input())
while t>0:
    t -= 1
    n, b = map(int, input().split())
    kq = ""
    while n!=0:
        kq += a[n%b]
        n //= b
    print(kq[::-1])