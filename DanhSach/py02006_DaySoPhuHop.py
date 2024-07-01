t = int(input())
while t>0:
    t -= 1
    n = int(input())
    a = list(int(x) for x in input().strip().split())
    b = list(int(x) for x in input().strip().split())
    a.sort()
    b.sort()
    check = 1
    for i in range(len(a)):
        if a[i]>b[i]:
            check = 0
            break
        
    if check == 0:
        print("NO")
    else: 
        print("YES")
'''
2
4
7 5 3 2
5 4 8 7
8
7 5 3 2 5 105 45 10
2 4 0 5 6 9 75 84 
'''