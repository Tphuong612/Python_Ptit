def my_round(x):
    #xu ly lam tron
    l = list(x)
    for i in range(len(l)-1, 0, -1):
        if int(l[i]) >= 5:
            l[i] = '0'
            l[i-1] = str(int(l[i-1]) + 1)
            
    #cong lai thanh 1 string
    kq = ''
    for i in range(len(l)):
        kq += l[i]
    return kq
    
t = int(input())
while t>0:
    t -= 1
    n = input()
    mu = 10**(len(n)-1)
    print(round(float(my_round(n))/mu)*mu)

