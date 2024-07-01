t = int(input())
a = list(int(x) for x in input().split())
dem = 0
for u in range(t):
    for v in range(u+1, t):
        if a[u]>a[v]: 
            dem += 1
print(dem)
'''
5
2 4 1 3 5
'''