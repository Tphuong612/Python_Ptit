t = int(input())
while t>0:
    t -= 1
    n, m, k = map(int, input().split())
    a = list(x for x in input().split())
    b = list(x for x in input().split())
    c = list(x for x in input().split())
    giao = list.intersection(a, b, c)
    if len(giao) ==0:
        print("NO")
    else:
        print(" ".join(giao))
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