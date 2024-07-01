giatri = 9
list = [1,2,3,4,5,6,7,8,9,10, 5, 1, 6, 7, 4.5, 4.5]
set = set(list)
for i in set:
    if i in set and giatri-i in set and i<giatri/2:
        print(i, giatri-i) 
    if i == giatri/2 and list.count(i)>=2: 
        print(i, i)