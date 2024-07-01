import math


class PhanSo:
    def __init__(self, t, m) -> None:
        self.t = t
        self.m = m
    def rutgon(self):
        ucln = math.gcd(self.t, self.m)
        tu = self.t//ucln
        mau = self.m//ucln
        return f"{tu:d}/{mau:d}"
    
if __name__ == '__main__':
    arr = input().split()
    ps = PhanSo(int(arr[0]), int(arr[1]))
    print(ps.rutgon())
    