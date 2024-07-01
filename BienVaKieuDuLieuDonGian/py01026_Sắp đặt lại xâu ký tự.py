def check(s1, s2):
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

t = int(input())
for i in range(t):
    l1, l2 = [], []
    s1 = input()
    s2 = input()
    l1.extend(s1)
    l2.extend(s2)
    
    l1.sort()
    l2.sort()
    if check(l1, l2):
        print(f'Test {i+1}: YES')
    else:
        print(f'Test {i+1}: NO')
'''
4
testing
intestg
abc
aabbbcccc
abcabcbcc
aabbbcccc
abc
xyz
'''
        