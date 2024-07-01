import re
s = ""
while True:
    try:
        tmp = input()
        s += tmp + " "
    except EOFError:
        break
s1 = re.sub(r'\s+',' ', s)
text = re.split("[.?!]", s1)
for i in text:
    print(i.strip().capitalize())
'''
ky thi LAP TRINH ICPC PTIT  bat dau to chuc     tu     nam 2010. nhu vay, nam nay la          tron 10 nam!
 vay CO PHAI NAM NAY LA KY THI LAN THU 10?        khong phai! nam nay la KY THI LAN THU 11.
'''
# import re

# text = "Đây là    câu có   nhiều    dấu cách."

# # Thay thế nhiều dấu cách bằng một dấu cách
# modified_text = re.sub(r'\s+', ' ', text)

# print(modified_text)