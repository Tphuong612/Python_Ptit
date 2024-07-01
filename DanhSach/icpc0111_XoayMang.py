t = int(input())
while t>0:
    t -= 1
    n, d = map(int, input().split())
    ls = list(input().split())
    print(" ".join(ls[d:]), end =" ")
    print(" ".join(ls[:d]))
    