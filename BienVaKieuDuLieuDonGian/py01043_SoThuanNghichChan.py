def ThuanNghich(s):
    if len(s)%2==1 or s != s[::-1]:
        return False
    for i in range(len(s)):
        if int(s[i])%2==1:
            return False
    return True

def sinh2(n):
    for i in range(10, 100):
        if i<n and ThuanNghich(str(i)):
            print(i, end=" ")
        elif i>n:
            break
            
def sinh4(n):
    for i in range(1000, 10000):
        if i<n and ThuanNghich(str(i)) :
            print(i, end=" ")
        elif i>n:
            break
        
def sinh6(n):
    for i in range(100000, 1000000):
        if i<n and ThuanNghich(str(i)) :
            print(i, end=" ")
        elif i>n:
            break           
t = int(input())
while t>0:
    t -= 1
    n = input()
    if len(n) == 2 or len(n) == 3:
        sinh2(int(n))
    elif len(n) == 4 or len(n) == 5:
        sinh2(int(n))
        sinh4(int(n))
    elif len(n) == 6:
        sinh2(int(n))
        sinh4(int(n))
        sinh6(int(n))
    print()