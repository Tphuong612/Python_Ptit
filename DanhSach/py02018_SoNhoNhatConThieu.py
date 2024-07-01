t = int(input())
a = sorted(list(int(x) for x in input().split()))
for i in range(1, 30002):
    if i not in a:
        print(i)
        break
