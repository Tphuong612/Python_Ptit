import math
l, r = map(int, input().split())
for i in range(l, r+1):
    for j in range(l+1, r+1):
        for k in range(l+2, r+1):
            if i<j and j<k and math.gcd(i, j)==1 and math.gcd(j, k)==1 and math.gcd(i, k)==1:
                print(f'({i}, {j}, {k})')