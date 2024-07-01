#kiểm tra hai trường hợp: n = p^8 và n = p^2 * q^2

from math import log, sqrt
n = int(input())
maxn = n+5
prime = [1]*(maxn+1)

def sang(n):
    prime[0] = prime[1] = 0
    for i in range(2, int(sqrt(maxn))+1):
        for j in range(i*i, maxn, i):
            prime[j] = 0
    
def nt(n):
    if n < 2:
        return 0
    for i in range(2, int(sqrt(n))+1):
        if n%i==0:
            return 0
    return 1
def check1(i):
    if i > 0:
        test = i**(1/8)
        if test == int(test) and prime[int(test)]==1:
            return 1
    return 0

def check2(n): #phân tích thừa số nguyên tố
    mu = []
    for i in range(2, int(sqrt(n))+1):
        dem = 0
        while n%i==0:
            dem += 1
            n = n//i
        if dem > 0:
            mu.append(dem)
    if n > 1:
        mu.append(1)
    if len(mu) == 2:
        if mu[0] == 2 and mu[1] == 2:
            return 1
    return 0  


sang(maxn)
dem = 0
for i in range(n+1):
    if check1(i) or check2(i):
        # print(i)
        dem += 1
print(dem)
    