import functools as f
import math

def sum(s):
    tong = 0
    for i in str(s):
        tong += int(i)
    return tong

def cmp(a, b):
    if sum(a) != sum(b):
        return sum(a) - sum(b)
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