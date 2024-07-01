#Làm theo yêu cầu đề bài thôi
for _ in range(int(input())):
    n, m = map(int, input().split())
    l = [int(x) for x in input().split()]
    max_l = max(l)
    index_max = -1
    for i in range(len(l)):
        if l[i] == max_l:
            index_max = i
            break
    l.insert(index_max, m)
    for i in l: #in số âm trước
        if i < 0:
            print(i, end=" ")
    for i in l:
        if i >= 0: 
            print(i, end=" ")
    print()# print(*l)
    