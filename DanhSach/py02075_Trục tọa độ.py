#tư tưởng tham lam
t = int(input())
for _ in range(t):
    n = int(input())
    day = []
    for _ in range(n):
        a1, a2 = map(int, input().split())
        day.append((a1, a2))
    day.sort(key=lambda x: (x[1], x[0]))
    dem = 0
    dodai = 0
    for i in day:
        if i[0] >= dodai:
            dodai = i[1]
            dem += 1
    print(dem)
    # for i in day:
    #     print(*i)
'''
1
10
39 55
37 74
0 1
19 25
65 76
51 52
19 21
5 94
46 65
32 40
'''