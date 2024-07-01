# l1 = [1,2,3,4,5,6,7,8,9]
# l2 = [1,2,4,8,9]
# same = list(filter(lambda x: (x in l2), l1))
# print(same)

# from collections import Counter


# l1 = ['bcda', 'abce', 'adcb', 'aaaa', 'xyzt', 'dabc']
# s = 'bacd'
# dao = list(filter(lambda x: Counter(s) == Counter(x), l1))
# print(dao)

l1 = ['bcda', 'abce', 'adcb', 'aaaa', 'xyzt', 'dabc']
s = 'bacd'
dao = list(filter(lambda x: sorted(s) == sorted(x), l1))
print(dao)