t = int(input())
while t > 0:
    t -= 1
    n = input()
    tich = 1
    for i in range(len(n)):
        if(n[i] != '0'):
            tich *= int(n[i])
    print(tich)
    