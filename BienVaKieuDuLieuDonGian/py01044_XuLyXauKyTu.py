
s1 = set(list(x for x in input().lower().split()))
s2 = set(list(x for x in input().lower().split()))
giao = sorted(set.intersection(s1, s2))
hop = sorted(set.union(s1, s2)) 
print(" ".join(hop))
print(" ".join(giao)) 
'''
Lap trinh huong doi tuong
Ngon ngu lap trinh C++
'''     