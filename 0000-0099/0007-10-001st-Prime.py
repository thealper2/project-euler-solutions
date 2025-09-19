def is_prime(num):
	for n in range(2, int(num**0.5)+1):
		if num % n == 0:
			return False

	return True

def solution():
	result = []
	i = 2
	while len(result) < 10001:
		if is_prime(i):
			result.append(i)

		i += 1

	return result[-1]

result = solution()
print(result)
