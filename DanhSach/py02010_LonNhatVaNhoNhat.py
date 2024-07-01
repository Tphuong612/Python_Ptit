while True:
    n = int(input())
    if n == 0:
        break
    l = []
    for i in range(n):
        l.append(int(input()))
    l.sort()
    if l[0] == l[-1]:
        print("BANG NHAU")
    else:
        print(l[0], l[-1])
'''
5
1
2
3
4
5
3
001
22
33333333333333333333333333333333333
3
1
1
1
0
'''