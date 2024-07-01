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
        #nhap kich thuoc
        kt = []
        while len(kt) < 2:
            kt.extend(int(x) for x in input().split())
        r, c = kt[0], kt[1]
        
        #nhap ma tran  
        nhap = []
        while (len(nhap) <r*c):
            nhap.extend(int(x) for x in input().split())
        #print(nhap)
        
        mt = []
        for i in range(r):
            tmp = nhap[(c*i): (c*i+c)]
            mt.append(tmp)  
        #print(mt)
        
        #tinh toan
        a = Matrix(mt, r, c)
        b = a.ChuyenVi()
        kq = a.mul(b)
        kq.display()
