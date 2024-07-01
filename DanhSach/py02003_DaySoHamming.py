from math import log

ls = [] #danh sách chứa các số hamming
n = 10**18
def ktao():
    a = int(log(n, 2))
    b = int(log(n, 3))
    c = int(log(n, 5))
    # print(type(a))
    # print(a, b, c)
    for i in range(c+1):
        for j in range(b+1):
            for k in range(a+1):
                hamming = (5**i)*(3**j)*(2**k)
                ls.append(hamming)
    ls.sort()
    
def bi_search(n, a): #tìm kiếm giá trị n trong 1 mảng a
    l = 0
    r = len(a)-1
    while (l<=r):
        m = (l+r)//2
        if a[m]==n:
            return m
        elif a[m] > n:
            r = m-1
        else: 
            l = m+1
    return -1

ktao()
t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    pos = bi_search(n, ls) 
    if pos != -1:
        print(pos+1)
    else:
        print("Not in sequence")
    
    
    