s = input().strip().title().split()
print(" ".join(s))

str1 = "Hello World!"
print(str1[-5:-2])

str1 = "Vi du ham replace() Python ham ham ham "
print (str1.replace("Python", "Python tren VietTuts.Vn"))
print (str1.replace("ham", "phuong thuc", 3))

n = 3
txt = "Hello Python {}"
print(txt.format(n))

def mypoint(str1, num1):
    result = "Tôi tên %-10s, số điểm point là %05d." % (str1, num1)
    print(result)

mypoint("Kiyoshi", 15)
#>> Tôi tên Kiyoshi   , số điểm point là    15.

mypoint("Duy An",1925)
#>> Tôi tên Duy An    , số điểm point là  1925.

f = 0.123

print(f'percent: {f:.2%}')
# percent: 12.30%

s = 'hello'
print(s[-5:-2])

import re

s1 = '1ab23cdef456'
m1 = re.findall(r'\d', s1)  
print(m1)
#>> ['1', '2', '3', '4', '5', '6']

s2 = 'Thứ 6 ngày 25 tháng 6 năm 2021, 21:30'
m2 = re.findall(r'\d+:\d+', s2)  
print(m2)
#>> ['6', '2', '5', '6', '2', '0', '2', '1', '2', '1', '3', '0']

