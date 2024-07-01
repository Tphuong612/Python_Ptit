
f = [0, 1, 1]
for i in range(3, 93):
    f.append(f[i-1] + f[i-2])   
        
t = int(input())
while t>0:
    t -= 1
    a, b = map(int, input().split())
    for i in range(a, b+1):
        print(f[i], end=" ")
    print()