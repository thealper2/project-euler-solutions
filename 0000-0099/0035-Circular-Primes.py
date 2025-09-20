def is_prime(num):
	if num < 2:
		return False

	for n in range(2, int(num**0.5)+1):
		if num % n == 0:
			return False

	return True


def solution():
	result = 0
	for i in range(2, 1_000_000):
		if is_prime(i):
			s = str(i)
			is_circular = True
			for j in range(1, len(s)):
				rotated = int(s[j:] + s[:j])
				if not is_prime(rotated):
					is_circular = False
					break

			if is_circular:
				result += 1

	return result

result = solution()
print(result)
