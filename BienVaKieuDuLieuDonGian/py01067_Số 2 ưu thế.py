l = []
kq = []
def check(s):
    if s.count('2') > len(s)//2:
        return True
    return False
def sinh():
    l.extend(('1', '2'))
    # print(*l)
    kq.extend(('2'))
    while len(kq) <= 1000:
        top = l.pop(0)
        if check(top+'0'): kq.append(top + '0')
        if check(top+'1'): kq.append(top + '1')
        if check(top+'2'): kq.append(top + '2')
        
        l.append(top + '0')
        l.append(top + '1')
        l.append(top + '2')
        # print(top)
    # for i in kq:
    #     print(i, end=" ")

sinh()
t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(n):
        print(kq[i], end=" ")
    print()
