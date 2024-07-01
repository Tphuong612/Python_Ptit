def chung(a, b):
    l = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            l.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j +=1
    return l
    
t = int(input())
for _ in range(t):
    n, m, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    tmp = chung(a, b)
    # print(tmp)
    chung3 = chung(tmp, c)
    if len(chung3) == 0:
        print("NO")
    else:
        print(*chung3)

'''
3
6 5 8
1 5 10 20 40 80
5 7 20 80 100
3 4 15 20 30 70 80 120
3 5 4
1 5 5
3 4 5 5 10
5 5 10 20
3 3 3
1 2 3
4 5 6
7 8 9
'''
