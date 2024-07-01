import math


t = int(input())
a = list(int(x) for x in input().split())
a.sort()
for i in range(0, t):
    for j in range(i+1, t):
        if math.gcd(a[i], a[j]) == 1:
            print(a[i], a[j])