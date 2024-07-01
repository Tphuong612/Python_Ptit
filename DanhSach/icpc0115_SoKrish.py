def GiaiThua(x):
    if x == 1 or x == 0:
        return 1
    return x*GiaiThua(x-1)

t = int(input())
while t>0:
    t -= 1
    n = input()
    a = int(n)
    sum = 0
    for i in n:
        sum += GiaiThua(int(i))
    if sum==a:
        print("Yes")
    else:
        print("No")