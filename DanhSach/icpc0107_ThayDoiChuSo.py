
def timMin(s, min, max):
    kq = s.replace(str(max), str(min))
    return int(kq)
def timMax(s, min, max):
    kq = s.replace(str(min), str(max))
    return int(kq)

t = int(input())
while t >0:
    t -= 1
    p, q = map(int, input().split())
    n = 2
    a = list()
    while n > 0:
        s = input().strip().split()
        for x in s:
            a.append(x)
        n -= len(s)
    x1, x2 = a[0], a[1]
   
    minx = min(p, q)
    maxx = max(p, q)

    summin = timMin(x1, minx, maxx) + timMin(x2, minx, maxx)
    summax = timMax(x1, minx, maxx) + timMax(x2, minx, maxx)
    print(summin, summax)