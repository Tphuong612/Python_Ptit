import gc


t = int(input())
while t>0:
    t -= 1
    n = int(input())
    l = [int(x) for x in input().split()]
    
    sum = 0
    for _ in range(3):
        l_min = min(l)
        sum += l_min
        l.remove(l_min)
    print(sum)
    # del l
    # gc.collect()
'''
2
7
1 2 3 0 -1 8 10 
7
9 8 20 3 4 -1 0
'''   