def sang():
    a = [True]*100 #khoi tao tat ca cac so tu 0-->99 deu la snt
    a[0] = a[1] = False
    #Nếu một số là số nguyên tố, thì tất cả các bội của nó không phải số nguyên tố
    for i in range(2, 11):
        if a[i] == True:
            for j in range(i*i, 100, i): 
                a[j] = False
                
    for i in range(1, 100):
        if a[i]==True:
            print(i, )         

sang()   
# while True:
#     s = input()
#     if s == '-1':
#         break
#     else:
#         l, r = map(int, s.split())
#         n = int(input())
        

