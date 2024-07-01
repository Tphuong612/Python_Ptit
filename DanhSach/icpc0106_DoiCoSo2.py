t = int(input())
while t>0:
    t -= 1
    a = int(input()) 
    b = input()
    tmp = b[::-1]
    sum = 0
    for i in range(len(tmp)):
        sum += int(tmp[i])*pow(2, i)
    #print(sum)
    base = '0123456789ABCDEF'
    kq = ""
    while sum!=0:
        p = base[sum%a]
        kq += p
        sum //= a
    
    print(kq[::-1])
    
    
    
    