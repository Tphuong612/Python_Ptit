m = 10**9 + 7
def bipow(a, b): # Tính Lũy Thừa
    if b == 0: 
        return 1
    x = bipow(a, b//2)%m
    if b%2==0:
        return x*x
    else:
        return x*x*a
def dec_to_bin(n):
    return str(bin(n))[2::]
t = int(input())
while t>0:
    t -= 1
    n, k = map(int, input().split())
    tong = 0
    s = dec_to_bin(k)
    mu = s[::-1]
    for i in range(len(mu)):
        if mu[i] == '1':
            tong += bipow(n, i)
            tong %= m
    print(tong)