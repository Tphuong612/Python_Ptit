prime = [1]*1005
def sang():
    prime[0] = prime[1] = 0
    for i in range(2, int(1005**(1/2))+1):
        for j in range(i*i, 1005, i):
            prime[j] = 0
            
sang()
def sortPrime(a):
    nt = []
    for i in a:
        if prime[i] == 1:
            nt.append(i)
    nt.sort()
    j = 0
    for i in range(len(a)):
        if prime[a[i]] == 1:
            a[i] = nt[j]
            j += 1
    print(*a)

n = int(input())
a = list(map(int, input().split()))
sortPrime(a)
'''
8
4 6 3 8 7 2 5 9
'''