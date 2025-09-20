from itertools import permutations


def solution():
	perm = list(permutations([0,1,2,3,4,5,6,7,8,9]))
	return perm[999999]


result = solution()
print(result)
