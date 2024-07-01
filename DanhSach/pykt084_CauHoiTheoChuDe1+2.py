t = int(input())
gr = [] #dùng để lưu câu hỏi theo chủ đề
d = {} #dùng để lưu kết quả
for _ in range(t):
    s = input()
    if s != "":
        gr.append(s)
    else:
        d[gr[0]] = len(gr) - 1
        gr.clear()
if len(gr) != 0: #do chủ đề cuối cùng bị thiếu 
    d[gr[0]] = len(gr) - 1
for i, j in d.items():
    print(f'{i}: {j}')

'''
9
Home/accommodation
What kind of housing/accommodation do you live in?
Who do you live with?
How long have you lived there?

Study
Describe your education
What is your area of specialization?
Why did you choose to study that major?
'''