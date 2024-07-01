def GiaiThua(n):
    if n == 1: return 1
    else: return n*GiaiThua(n-1)

a = 5
print(GiaiThua(5))

GiaiThua = 1
for i in range(2, 5+1):
    GiaiThua *= i
print(GiaiThua)