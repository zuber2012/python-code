from itertools import permutations

my_list = [1, 2, 3]
# Generating all permutations
perms = list(permutations(my_list))
# Printing the permutations
print(perms)  # Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]