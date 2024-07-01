import functools as f
import math

def mul(s):
    tich = 1
    for i in str(s):
        tich *= int(i)
    return tich

def cmp(a, b):
    if mul(a) != mul(b):
        return mul(a) - mul(b)
    else:
        return a-b    
t = int(input())
while t>0:
    t -= 1
    n = input()
    a = list(int(x) for x in input().split())
    a.sort(key = f.cmp_to_key(cmp))
    for i in a:
        print(i, end = ' ')
    print()
'''
1
8
143 43 22 99 7 9 1111 10000000
'''