import math


def nt(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return True
def check(n):
    sum = 0
    for i in n:
        if i not in ['2', '3', '5', '7']:
            return False
        sum += int(i)
    if nt(sum): return True
    else: return False
t = int(input())
while t>0:
    t -= 1
    n = input()
    if check(n) and nt(int(n)) and nt(int(n[::-1])):
        print("Yes")
    else:
        print("No")
