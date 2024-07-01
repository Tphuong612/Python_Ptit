import math


n = int(input())
sum = 0
if n%2==1:
    for i in range(0, n//2 + 1):
        sum += math.pow(-1, i)/(2*i+1)
else:
    for i in range(0, n//2):
        sum += math.pow(-1, i)/(2*(i+1))
print(f"{sum:.5f}")
