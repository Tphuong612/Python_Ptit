from functools import cmp_to_key


class DienThoai:
    def __init__(self, date, ht, sdt) -> None:
        self.date = date
        self.ht = ht
        self.sdt = sdt
    # def ngay(self):
    #     return self.date[5:]
    def ten(self):
        s = self.ht.split()
        return s[len(s)-1]
    def ho(self):
        s = self.ht.split()
        h = ' '.join(s[0:len(s)-1])
        return h
    def __str__(self) -> str:
        return f'{self.ht}: {self.sdt} {self.date}'
    
def cmp(a, b):
    '''
    Nếu a.ten() < b.ten(), trả về -1 (số âm), nghĩa là a sẽ đứng trước b trong danh sách đã sắp xếp.
    Nếu a.ten() > b.ten(), trả về 1 (số dương), nghĩa là a sẽ đứng sau b trong danh sách đã sắp xếp.
    Nếu a.ten() == b.ten(), tiếp tục so sánh ho().
    cmp(a, b) = -1, tức là a đứng trc b
    cmp(a, b) = 1, tức là a đứng sau b
    '''
    if a.ten() != b.ten():
        return (a.ten() > b.ten()) - (a.ten() < b.ten())
    else:
        return (a.ho() > b.ho()) - (a.ho() < b.ho()) 

with open("tệp văn bản\SOTAY.txt", 'r') as file:
    lines = file.readlines() #mỗi dòng sẽ tự thêm 1 kí tự '\n'
file.close()    
dong = [] #chứa các dòng của tệp tin được loại bỏ kí tự '\n'
for i in lines:
    dong.append(i.rstrip())
# for i in dong:
#     print(dong)
    
ngay_index = [] #chứa các dòng chưa ngày      
dem = 0
list_dt = [] 
while dem < len(dong): #xét từ trên xuống dưới thôi, nếu chưa có ngày, ngày sẽ là phần tử ngay_index cuối cùng
    if dong[dem].startswith("Ngay"):
        ngay_index.append(dem) #Lưu lại chỉ số dòng chứa ngày
        ngay = dong[dem].split(' ')
        date = ngay[1]
        
        ht = dong[dem+1]
        sdt = dong[dem+2]
        a = DienThoai(date, ht, sdt)
        list_dt.append(a)
        dem += 3
        
    else:
        ngay = dong[ngay_index[-1]]
        ngay = dong[ngay_index[-1]].split(' ')
        date = ngay[1]
        
        ht = dong[dem]
        sdt = dong[dem+1]
        a = DienThoai(date, ht, sdt)
        list_dt.append(a)
        dem += 2
list_dt.sort(key=cmp_to_key(cmp))
with open("tệp văn bản\DienThoai.txt", 'w') as f:
    for i in list_dt:
        f.writelines(str(i)+'\n')      
f.close