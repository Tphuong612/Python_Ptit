def check(n):
    if len(n)%2==0:
        return False
    if n[0] == n[1]:
        return False
    for i in range(2,len(n),2):
        if n[0] != n[i]:
            return False
    return True

t = int(input())
while t>0:
    t -= 1
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")