
prime = [1]*(10**6+1)
def sang():
    prime[0], prime[1] = 0, 0
    for i in range(2, 1001):
        if prime[i]==1:
            for j in range(i*i, 10**6+1, i):
                prime[j] = 0
                
sang()
t = int(input())
while t>0:
    t -= 1
    n = int(input())
    dem = 0
    for i in range(n+1):
        if i+6<= n and ((prime[i]==1 and prime[i+2]==1 and prime[i+6]==1) or (prime[i]==1 and prime[i+4]==1 and prime[i+6]==1)):
            dem +=1
    print(dem)