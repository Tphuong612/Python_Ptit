#code nay ko AC
import math


class Point:
    def __init__(self, x, y) -> None: # -> None co nghia la ko co gia tri tra ve
        self.x = x
        self.y = y
    def distance(self, p2):
        x0 = self.x - p2.x
        y0 = self.y - p2.y
        kc = math.sqrt(x0**2 + y0**2)
        return kc
    
class Triangle:
    def __init__(self, p1, p2, p3) -> None:
        self.a = p1.distance(p2)
        self.b = p2.distance(p3)
        self.c = p1.distance(p3)
    def chuvi(self):
        a = self.a
        b = self.b
        c = self.c
        if b +c<= a or a+c <= b or a+b<= c:
            print('INVALID')
        else:
            print('%.3f'%(a+b+c))
      
if __name__=='__main__':
    t = int(input())
    l = list()
    while t>0:
        t -= 1
        k = input().strip()
        l.append(k)
        
    for i in l:
        s = i.split()
        a = Point(float(s[0]), float(s[1]))
        b = Point(float(s[2]), float(s[3]))
        c = Point(float(s[4]), float(s[5]))
        TamGiac = Triangle(a, b, c)
        TamGiac.chuvi()
        s.clear()
'''
3
0 0 0 5 0 199
1 1 1 1 1 1
0 0 0 5 5 0
'''