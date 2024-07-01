n, m = map(int, input().split())
a = [int(x) for x in input().split()]
d = dict()
for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
b = sorted(list(set(d.values())), reverse=True) # săp xếp số lần xuất hiện khác nhau theo thứ tự giảm dần
if len(b) == 1:
    print('NONE')
else:
    kq = sorted(list(d.items()), key=lambda x: x[0])
    for i in kq:
        if i[1] == b[1]: #giá trị lơn thứ 2
            print(i[0])
    # print(kq)
# print(*b)
'''
10 4
2 3 1 2 3 4 1 2 3 2

8 4
1 2 3 4 4 3 2 1
'''