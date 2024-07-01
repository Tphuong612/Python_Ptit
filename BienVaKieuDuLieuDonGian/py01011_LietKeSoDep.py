
def ThuanNghich(s):
    if len(s)%2==1 or s != s[::-1]:
        return False
    for i in range(len(s)):
        if int(s[i])%2==1:
            return False
    return True

t = int(input())
while t>0:
    t -= 1
    n = int(input())
    for i in range(22, n):
        if ThuanNghich(str(i)):
            print(i, end=" ")
    print()
    