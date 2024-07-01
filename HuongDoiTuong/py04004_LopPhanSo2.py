import math


class PhanSo:
    def __init__(self, t, m) -> None:
        self.t = t
        self.m = m
    def rutgon(self):
        ucln = math.gcd(self.t, self.m)
        tu = self.t//ucln
        mau = self.m//ucln
        kq = PhanSo(tu, mau)
        return kq
        #return f"{tu:d}/{mau:d}"
    def add(self, q):
        tu = self.t*q.m + self.m*q.t
        mau = self.m*q.m
        kq = PhanSo(tu, mau)
        return kq
    def display(self):
        kq = self.rutgon()
        print(f"{kq.t:d}/{kq.m:d}")
        
        
if __name__ == '__main__':
    arr = input().split()
    p = PhanSo(int(arr[0]), int(arr[1]))
    q = PhanSo(int(arr[2]), int(arr[3]))
    kq = p.add(q)
    kq.display()
    
    