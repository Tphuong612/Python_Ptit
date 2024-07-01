for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    a = set(a) #loại bỏ trùng lặp
    a_min = min(a)
    a_max = max(a)
    kq = (a_max - a_min + 1) - len(a)
    print(kq)
'''
2
5
4 5 3 8 6
3
2 1 3
'''