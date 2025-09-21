def is_prime(n):
	if n < 2:
		return False

	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			return False

	return True

def is_pandigital(n):
	s = str(n)
	return set(s) == set(''.join(str(d) for d in range(1, len(s)+1)))

def solution():
	result = 0
	for num in range(2, 10_000_000):
		if is_prime(num) and is_pandigital(num):
			result = num

	return result


result = solution()
print(result)
