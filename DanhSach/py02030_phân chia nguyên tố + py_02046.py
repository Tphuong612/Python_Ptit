prime = [1]*(10**6+5)
def sang():
    prime[0] = prime[1] = 0
    for i in range(2, 10**3+1):
        if prime[i] == 1:
            for j in range(i*i, 10**6+1, i):
                prime[j] = 0

sang()
n = int(input())
a = [int(x) for x in input().split()]
b = []
for i in a:
    if i not in b:
        b.append(i)
# print(*b)
prefix_sum = [0]*len(b)
prefix_sum[0] = b[0]
for i in range(1, len(b)):
    prefix_sum[i] = prefix_sum[i-1] + b[i]
# print(*prefix_sum)

check = 0
for i in range(len(b)):
    if prime[prefix_sum[i]] == 1 and prime[prefix_sum[-1] - prefix_sum[i]] == 1:
        check = 1
        print(i)
        break
if check == 0:
    print("NOT FOUND")

#tổng cả dãy số sẽ là phần tử cuối cùng

'''
10
3 6 7 3 4 7 3 6 4 4

10
3 6 7 3 5 7 3 6 6 7
'''