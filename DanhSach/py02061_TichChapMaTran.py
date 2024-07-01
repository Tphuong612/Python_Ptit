def type_Matrix():
    n, m = map(int, input().split())
    #ma tran n hang, m cot
    x = []
    for i in range(n): 
        x.append(list(int(i) for i in input().split())) 
    return x
    #print(x)           
def convolution(x, h, m, n):
    sum = 0
    for i in range(m):
        for j in range(n):
            tmp = h[]
            
t = int(input())
while t>0:
    t -= 1
    x = type_Matrix()
    h = type_Matrix()
    
    
# def nhap_ma_tran():
#     hang = int(input("Nhập số hàng của ma trận: "))
#     cot = int(input("Nhập số cột của ma trận: "))

#     print("Nhập các phần tử của ma trận:")
#     ma_tran = []
#     for i in range(hang):
#         # Khởi tạo hàng mới trong ma trận
#         hang_moi = []
#         for j in range(cot):
#             phan_tu = float(input(f"Nhập phần tử ở hàng {i+1}, cột {j+1}: "))
#             hang_moi.append(phan_tu)
#         # Thêm hàng vào ma trận
#         ma_tran.append(hang_moi)

#     return ma_tran

# # Sử dụng hàm để nhập ma trận
# ma_tran_nhập = nhap_ma_tran()
# print("Ma trận đã nhập:")
# for hang in ma_tran_nhập:
#     print(hang)
