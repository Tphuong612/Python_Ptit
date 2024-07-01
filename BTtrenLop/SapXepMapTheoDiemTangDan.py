l = [('english', 88), ('science', 90), ('math', 97), ('social science', 80), ('art', 88)]
l_sorted = sorted(l, key=lambda x: (-x[1], x[0]))
print(l_sorted)

l = [1,3,5,7,9]
l2 = map(lambda x: x*x, l)
print(list(l2))

