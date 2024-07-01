n = int(input())
a = list(int(x) for x in input().split())
b = list(a)
for j in range(len(b)):
    for i in range(len(a)):
        if i+1 < len(a) and (a[i]+a[i+1])%2==0 and len(a) >= 2:
            a.remove(a[i])
            a.remove(a[i+1])
    b = list(a)
print(len(a))
'''
10
1 5 5 8 6 4 3 5 9 3
'''