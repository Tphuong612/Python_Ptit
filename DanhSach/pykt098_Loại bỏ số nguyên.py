def check(s): #Kiem tra xem s phai la so nguyen hay không
    if not s.isdigit():
        return False
    else:
        for i in s:
            if not i.isdigit():
                return False
        so = int(s)
        if so <= 2147483647 and so >= -2147483648 : 
            return True
        else:
            return False
    
a = [] #danh sách chứa những chuỗi kp là số nguyên     
with open("tệp văn bản\Data.in.txt", 'r') as file:
# file = open('DATA.in', 'r')
    for line in file:
        for i in line.split():
            if not check(i):
                a.append(i)
a.sort()
print(*a, sep=" ")