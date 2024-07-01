#Cách này không AC
# from collections import Counter


# t = int(input())
# while t > 0:
#     t -= 1
#     n = int(input())
#     l = []
#     for i in range(n):
#         tmp = int(input())
#         l.append(tmp)
#     print(max(l, key=l.count)) #count để đếm số lần xuất hiện
    
'''
3
3
999
999
19
4
13
333
333
13
3
11
12
13
'''

t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    l = [0]*1005
    for i in range(n):
        tmp = int(input())
        l[tmp] += 1
    m = max(l)
    for i in range(1005):
        if l[i] == m:
            print(i)
            break
    