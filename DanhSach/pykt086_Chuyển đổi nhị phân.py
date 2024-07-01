#chú ý cơ số 16 sẽ có cả chữ "ABCEF"
def convert(sum, a):
    if sum == 0:
        return 0
    
    base = '0123456789ABCDEF'
    kq = ""
    while sum!=0:
        p = base[sum%a]
        kq += p
        sum //= a
    return kq[::-1]

with open("tệp văn bản\DATA.in", 'r') as f:
    lines = f.readlines()
dong = []
for i in lines:
    dong.append(i.strip())

n = int(dong[0])
for i in range(1, len(dong)-1, 2):
    cs, b = int(dong[i]), dong[i+1].rstrip()
    sum = 0
    b1 = b[::-1]
    # print(cs, b)
    for j in range(len(b1)):
        sum += int(b1[j])*(2**j)
    print(convert(sum, cs))
