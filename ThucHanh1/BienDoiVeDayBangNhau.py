#ý tưởng: ở mỗi số tìm xem thay đổi về nó thì cần bao nhiêu bước, từ đó chọn ra số bé nhất
t = int(input())
a = [int(x) for x in input().split()]
dem = [0]*len(a) 
for i in range(t):
    for j in range(t):
        dem[i] += abs(a[i]-a[j])
buoc_min = min(dem)
ind = dem.index(buoc_min)
print(buoc_min, a[ind])


        
