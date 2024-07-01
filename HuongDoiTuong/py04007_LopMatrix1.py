class Matrix:
    def __init__(self, l, r, c) -> None:
        self.l = l
        self. r= r
        self.c = c
    def nhap(self):
        matran = []
        for i in range(self.r):
            hang = [int(x) for x in input().split()]
            matran.append(hang)
        self.l = matran
    def ChuyenVi(self):
        matran = [[0 for _ in range(self.r)] for _ in range(self.c)] 
        for i in range(self.r):
            for j in range(self.c):
                matran[j][i] = self.l[i][j]
        return Matrix(matran, self.c, self.r)
    def mul(self, b):
        kq = [[0 for _ in range(self.r)] for _ in range(b.c)]
        for i in range(self.r):
            for j in range(b.c):
                for k in range(self.c):
                    kq[i][j] += self.l[i][k]*b.l[k][j]
        return Matrix(kq, self.r, b.c)
    def display(self):
        res = ''
        for i in range(self.r):
            for j in range(self.c):
                res += str(self.l[i][j]) + ' '
            res += '\n'
        print(res)
        
if __name__=='__main__': 
    t = int(input())
    while t>0:
        t -= 1
        l = []
        r, c = map(int, input().split())    
        a = Matrix(l, r, c)
        a.nhap()
        b = a.ChuyenVi()
        kq = a.mul(b)
        kq.display()
