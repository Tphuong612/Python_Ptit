# a = [-1, 1, 9]
# b = [-2, -1, 0, 2, 1, 9, 1000]
from pstats import SortKey

#c1: kiem tra list con lien tiep
a = [-1, 1, 9]
con = ''.join(map(str, a))
b = [-1, 0, 2, 1, 9, 1000]
cha = ''.join(map(str, b))
if con not in cha:
    print("NO")
else:
    print("YES")
    
# #c2://kiem tra xau con ko lien tiep
# a = [-1, 1, 9]
# b = [-2, -1, 0, 2, 1, 9, 1000]
# a.sort()
# b.sort()
# check = 1
# for i in range(len(a)):
#     if b.count(a[i]) == 0:
#         check = 0
#         print("NO")
#         break
# if check == 1:
#     print("YES")
