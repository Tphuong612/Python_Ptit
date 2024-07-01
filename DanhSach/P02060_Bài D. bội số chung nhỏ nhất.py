from math import gcd, sqrt

m = 10**9 + 7

def lcm(x, y):
    return x*y//gcd(x,y)

def count_pairs(a, b):
    tich = 1
    for i in range(a, b+1):
        tich *= i
        tich %= m
    
    #print(tich)
    count = 0
    uoc = []
    for i in range(1, int(sqrt(tich))+1):
        if tich%i==0:
            uoc.append(i)
            if i != tich//i:
                uoc.append(tich//i)
    #print(*uoc)
    uoc.sort()
    for i in range(len(uoc)):
        for j in range(i+1, len(uoc)):
            if lcm(uoc[i], uoc[j]) == tich:
                count += 1
                
    kq = 2*count + 1 #có tính lặp lại, +1 là do có cặp (tích, tích) vd: (6, 6) = 6
    return kq % m

t = int(input())
kq = []
for _ in range(t):
    a, b = map(int, input().split())
    #count_pairs(a, b)
    # print(count_pairs(a, b))
    kq.append(count_pairs(a, b))
for i in kq:
    print(i)
