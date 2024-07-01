d = dict()
len_max = -1 #dộ dài lớn nhất của xâu thuận nghịch
#with open('D:\HocTap\code\python\VANBAN.in', 'r') as file:
with open('VANBAN.in', 'r') as file:
    for line in file:
        a = line.split()
        for x in a:
            if x == x[::-1]:
                len_max = max(len_max, len(x))
                if x in d:
                    d[x] += 1
                else:
                    d[x] = 1
                    
for x, y in d.items():
    if len(x) == len_max:
        print(x + " " + str(y))
  




