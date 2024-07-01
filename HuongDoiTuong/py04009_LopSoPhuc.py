class SoPhuc:
    def __init__(self, t, a) -> None:
        self.t = t
        self.a = a
    def add(self, o):
        thuc = self.t + o.t
        ao = self.a + o.a 
        return SoPhuc(thuc, ao)
    def mul(self, o):
        thuc = self.t*o.t - self.a*o.a 
        ao = self.t*o.a + o.t*self.a
        return SoPhuc(thuc, ao)
    def display(self):
        res = ""
        res += str(self.t)
        if self.a > 0:
            res += " + " + str(self.a) + "i"
        else:
            res += " - " + str(abs(self.a)) + "i"
        return res
        
t = int(input())
while t > 0:
    t -= 1
    s = input().split()
    a = SoPhuc(int(s[0]), int(s[1]))
    b = SoPhuc(int(s[2]), int(s[3]))
    c = (a.add(b)).mul(a)
    d = (a.add(b)).mul(a.add(b))
    print(c.display(), d.display(), sep=", ")