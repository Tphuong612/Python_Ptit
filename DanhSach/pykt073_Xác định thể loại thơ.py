import re


n = int(input())
test = ""
for _ in range(n):
    s = input().split()
    test += str(len(s))
t1 = test.replace('7777', '2')
t2 = re.sub("[68]+", '1', t1)
print(len(t2))
for i in t2:
    print(i)
# dem = 1
# for i in test:
#     if i == '2':
#         dem
# dem = test.count('7777')
# print(dem)
# print(test)
'''
8
Minh ve minh co nho ta
Muoi lam nam ay thiet tha man nong
Minh ve minh co nho khong
Nhin cay nho nui nhin song nho nguon
Mot canh hai canh lai ba canh
Tran troc ban khoan giac chang lanh
Canh bon canh nam vua chop mat
Sao vang nam canh mong hon bay
'''