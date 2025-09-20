def is_prime(num):
	if num < 2:
		return False

	for n in range(2, int(num**0.5)+1):
		if num % n == 0:
			return False

	return True


def solution():
	result = []
	number = 10
	while len(result) < 11:
		if is_prime(number):
			s = str(number)
			is_all = True
			for i in range(len(s)):
				d = int(s[i:])
				if not is_prime(d):
					is_all = False
					break

			for i in range(len(s), 0, -1):
				d = int(s[:i])
				if not is_prime(d):
					is_all = False
					break

			if is_all:
				result.append(number)

		number += 1

	return sum(result)


result = solution()
print(result)
