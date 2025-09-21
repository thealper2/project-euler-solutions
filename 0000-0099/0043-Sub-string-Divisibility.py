from itertools import permutations


def has_property(num_str):
	divisors = [2, 3, 5, 7, 11, 13, 17]
	for i in range(1, 8):
		substring = num_str[i:i+3]
		if int(substring) % divisors[i - 1] != 0:
			return False

	return True

def solution():
	digits = '0123456789'
	total_sum = 0

	for perm in permutations(digits):
		if perm[0] == '0':
			continue

		num_str = ''.join(perm)
		if has_property(num_str):
			total_sum += int(num_str)

	return total_sum


result = solution()
print(result)
