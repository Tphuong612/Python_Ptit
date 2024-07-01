#Xử lý trường hợp âm thì ko AC?
def tong(n):
    sum = 0
    for i in n:
        sum += ord(i) - ord('0')
    return sum

n = input()
# if int(n) < 0:
#     n = str(-int(n))

dem = 0
while len(n) > 1:
    n = str(tong(n))
    dem += 1
print(dem)
        
