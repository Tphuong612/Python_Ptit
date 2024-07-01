#bản chất sap xếp rồi tìm số lần mà số sau - so truoc > k
n, k = [int(x) for x in input().split()]
a = sorted([int(x) for x in input().split()])
s = 1 #luôn bằng 1 (trong tường hợp có 1 phần tử là chính nó)
for i in range(1, len(a)):
    if a[i] - a[i-1] > k:
        s += 1
print(s)
'''
7 1
2 6 1 7 3 4 9

7 1
1 3 4 5 2 7 6
'''