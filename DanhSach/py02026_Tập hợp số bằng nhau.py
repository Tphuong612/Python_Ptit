def check(a, b):
    if len(a) != len(b):
        return False
    else:
        a = sorted(list(a))
        b = sorted(list(b))
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
    return True

n, m = map(int, input().split())
a = set([int(x) for x in input().split()])
b = set([int(x) for x in input().split()])
if check(a, b):
    print("YES")
else:
    print("NO")
'''
12 18
1 2 3 4 5 1 2 3 5 4 1 2
1 1 1 1 1 1 1 1 1 2 3 4 5 5 5 5 5 5
'''