t = int(input())
while t>0:
    t -= 1
    s = input()
    n = len(s)
    dem = 1
    s += "!"
    for i in range(0, n):
        if s[i] == s[i+1]:
            dem += 1
        else:
            print(f'{dem}{s[i]}', end ="")
            dem = 1 #tra lai gia tri dem de su dung cho ki tu tiep theo
    print()
        