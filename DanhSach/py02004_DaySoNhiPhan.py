t = int(input())
a = list(int(x) for x in input().split())
dem = 0
for i in range(t-1):
    if a[i] != a[i+1]:
        dem += 1    
print(dem)
'''
6
1 0 0 1 1 1
'''