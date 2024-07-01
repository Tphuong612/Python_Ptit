#TLE 
t = int(input())
while t > 0:
    t -= 1
    a, b = [int(x) for x in input().split()]
    
    l =[0]*10
    for i in range(a, b+1):
        s = str(i)
        l[0] += s.count('0')
        l[1] += s.count('1')
        l[2] += s.count('2')
        l[3] += s.count('3')
        l[4] += s.count('4')
        l[5] += s.count('5')
        l[6] += s.count('6')
        l[7] += s.count('7')
        l[8] += s.count('8')
        l[9] += s.count('9')
    
    print(" ".join([str(x) for x in l]))
    