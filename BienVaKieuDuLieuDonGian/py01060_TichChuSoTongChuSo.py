def check(n):
    sum = 0
    for i in range(len(n)):
        if i%2==0:
            sum += int(n[i])
    if sum == 0:
        return True
    return False

t = int(input())
while t>0:
    t -= 1
    n = input()
    tong, tich = 0, 1
    for i in range(len(n)):
        if i%2==1:
            tong += int(n[i])
    if check(n):
        tich = 0
    else:
        for i in range(len(n)):
            if i%2==0 and n[i] != '0':
                tich *= int(n[i])
    print(tich, tong)
    
            
        