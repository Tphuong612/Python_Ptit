def ThuanNghich(n):
    if len(n) > 1 and n == n[::-1]:
        return True
    return False

t = int(input())
while t>0:
    t -= 1
    n = input()
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if ThuanNghich(str(sum)):
        print("YES")
    else:
        print("NO")
        