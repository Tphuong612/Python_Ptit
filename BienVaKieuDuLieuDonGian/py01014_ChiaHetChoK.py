import math

a, k, n = map(int, input().split())
b = math.ceil(float(a)/k)*k - a
check = 0
while b+a <= n and b != 0:
    print(b, end = " ")
    check = 1
    b += k
if check == 0:
    print("-1")
    

    