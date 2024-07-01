def check(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    else:
        for i in a:
            if i.isalpha():
                return False
            if int(i) < 0 or int(i) > 255:
                return False
        return True
    
t = int(input())
for _ in range(t):
    s = input()
    if check(s):
        print('YES')
    else:
        print('NO')    
'''
2
192.168.1.1
256.255.255.255
'''        
            