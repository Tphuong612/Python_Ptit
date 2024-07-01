t = input()
a = list(float(x) for x in input().split())
mina = min(a)
maxa = max(a)
dem = 0
sum = 0
#print(mina, maxa)
for i in range(len(a)):
    if a[i] != mina and a[i] != maxa:
        sum += a[i]
        dem += 1
        #print(a[i], dem)
print(f'{sum/dem:.2f}')
