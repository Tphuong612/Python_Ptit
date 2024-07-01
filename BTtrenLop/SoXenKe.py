def check(n):
    if len(n)%2==0:
        return 0
    if n[0] == n[2]: 
        return 0
    for i in range(1, len(n), 2):
        if n[1] != n[i]:
            return 0
    return 1
n = input()
if check(n): 
    print("YES")
else:
    print("NO")