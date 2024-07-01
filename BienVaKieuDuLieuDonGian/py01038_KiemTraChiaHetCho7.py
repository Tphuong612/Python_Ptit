t = int(input())
while t>0:
    t -= 1
    n = input()
    check = 0
    for i in range(1, 1001):
        if int(n)%7==0:
            print(n)
            check = 1
            break
        sum = int(n) + int(n[::-1])
        n = str(sum)
        
    if check == 0:
        print("-1")