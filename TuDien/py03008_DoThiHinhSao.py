
from collections import Counter


n = int(input())
t = n - 1 
my_list = list()
while t>0:
    t -= 1
    x, y = map(int, input().split())
    my_list.append(x)
    my_list.append(y)
counter = Counter(my_list)
check = 0
for x in counter:
    if counter[x] == n - 1:
        print("Yes")
        check = 1
        break
if check == 0: 
    print("No")