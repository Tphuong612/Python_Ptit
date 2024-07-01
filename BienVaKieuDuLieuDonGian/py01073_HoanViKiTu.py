from itertools import permutations
s = input()
permutation_result = permutations(s)
for perm in permutation_result:
    print(''.join(perm))
