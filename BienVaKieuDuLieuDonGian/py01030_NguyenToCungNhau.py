import math

n, k = map(int, input().split())
dem = 0
for i in range(10**(k-1), 10**k):
    if(math.gcd(n, i) == 1):
        dem += 1
        print(i, end=" ")
    if dem==10:
        dem = 0
        print()
