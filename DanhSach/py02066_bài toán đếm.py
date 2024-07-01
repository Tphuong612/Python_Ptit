n = int(input())
a = []
while True:
    s = input()
    for i in s.split():
        a.append(int(i))
    if len(a) == n:
        break

a.sort()
max_a = max(a)
min_a = min(a)
kq = []
for i in range(1, min_a):
    kq.append(i)
for i in range(min_a, max_a):
    if i not in a:
        kq.append(i)
if len(kq) == 0:
    print("Excellent!")
else:
    for i in kq:
        print(i, end='\n')
        
# for i in range(n):
'''
4
1 2 3 5

7
4 5 7 8 9 
10 11

5
1 2 3
4
5

'''
    