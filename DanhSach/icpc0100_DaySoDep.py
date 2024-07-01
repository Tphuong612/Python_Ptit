#Ý tưởng: nếu 1 cặp mà không đc coi là đẹp thì thêm đến bao giờ max > 2k với  MINsau = 2*MINtruoc
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range (0, len(a) - 1):
        k = 2 * min(a[i], a[i + 1])
        while max(a[i], a[i + 1]) > k:
            cnt+=1 
            k*=2
    print(cnt)