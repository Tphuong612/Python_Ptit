s = input()
dem1, dem2 = 0, 0
for i in s:
    if i.isdigit():
        dem1 += 1
    if i.isalpha():
        dem2 += 1
print(dem1, dem2)