import math
t = int(input())
while t>0:
    t -= 1
    n = int(input())
    
    if n==1:
        print("1")
    else: 
        print("1 *", end = "")
        for i in range(2, math.ceil(math.sqrt(n))+1):
            if n%i == 0:
                dem = 0
                while n%i==0:
                    dem += 1
                    n /= i
                else:
                    print(f' {i}^{dem} ', end="")
                if n!=1:
                    print("*", end="")
        if n!=1: 
            print(f' {int(n)}^{1} ', end ="")
        print()