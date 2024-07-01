class ThiSinh:
    def __init__(self, name, dob, m1, m2, m3) -> None:
        self.name = name
        self.dob = dob
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.tong = m1+m2+m3

    def display(self):
        res = self.name + " "+ self.dob + " " + "{:.1f}".format(self.tong)
        print(res)

if __name__=='__main__':
    name = input()
    dob = input()
    m1 = float(input())
    m2 = float(input())
    m3 = float(input())
    a = ThiSinh(name, dob, m1, m2, m3)
    a.display()
'''
Nguyen Hoang Ha
11/10/2001
4.5
10.0
5.5
'''