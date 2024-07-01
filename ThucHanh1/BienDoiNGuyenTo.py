import math

Nmax = 10005
snt = []
def sang():
    p = [1]*10005 #coi tat ca cac so deu la snt
    p[0]=p[1]=0
    #Nếu một số là số nguyên tố, thì tất cả các bội của nó không phải số nguyên tố
    for i in range(2, round(math.sqrt(Nmax))+1):
        if p[i]==1:
            for j in range(i*i, Nmax, i):
                p[j] = 0
    for i in range(Nmax):
        if p[i]==1:
            snt.append(i)
#Tìm số lớn nhất mà nhỏ hơn hoặc bằng số đang xet --> tra ve chi so
sang()
def small(n):
    l = 0
    r = len(snt) - 1
    pos = Nmax #luu chi so
    while l<=r:
        m = (l+r)//2
        if snt[m] == n: #Nếu là snt thì trả về 0 luôn
            return 0
        elif snt[m] < n: 
            pos = m 
            l = m+1 #do r giữ nguyên nên đây là cập nhập đáp án tốt hơn
        else:
            r = m - 1
    return n-snt[pos] 

#Tìm số nhỏ nhất mà lớn hơn hoặc bằng số đang xet --> tra ve chi so
def greater(n):
    l = 0
    r = len(snt) - 1
    pos = Nmax #luu chi so
    while l<=r:
        m = (l+r)//2
        if snt[m] == n: #Nếu là snt thì trả về 0 luôn
            return 0
        elif snt[m] > n: 
            pos = m 
            r = m - 1 #do l giữ nguyên nên đây là cập nhập đáp án tốt hơn
        else:
            l = m + 1
    return snt[pos] - n

n = int(input())
a = [int(x) for x in input().split()]
ans = [0]*len(a)
for i in range(len(a)):
    ans1 = small(a[i])
    ans2 = greater(a[i])
    # print(dem1, dem2)
    ans[i] = min(ans1, ans2)   
print(max(ans))

           


