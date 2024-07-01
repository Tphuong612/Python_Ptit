from math import *

n = int(input())
mt = []
for i in range(n):
    row = input()
    tmp = [x for x in row]
    mt.append(tmp)
# print(mt)  
sum = 0
for i in mt: #Tính theo hàng
    dem = 0
    for j in i:
        if j == 'C' or j=='c':
            dem += 1
    if dem >= 2:
        sum += comb(dem, 2)

for i in range(n): #Tính theo cột
    dem = 0
    for j in range(n):
        if mt[j][i] == 'C' or mt[j][i] == 'c':
            dem += 1
    if dem>=2:
        sum += comb(dem, 2)
                   
print(sum)

'''
4
CC..
C..C
.CC.
.CC.
'''