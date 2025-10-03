def sum_of_divisors(n: int) -> int:
	sum_ = 1
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			sum_ += i
			if i != n // i:
				sum_ += n // i

	return sum_


def is_abundant(n: int) -> bool:
	return sum_of_divisors(n) > n


def solution():
	limit = 28123
	abundants = []
	for i in range(12, limit + 1):
		if is_abundant(i):
			abundants.append(i)

	can_be_written = [False] * (limit + 1)
	for i in range(len(abundants)):
		for j in range(i, len(abundants)):
			s = abundants[i] + abundants[j]
			if s <= limit:
				can_be_written[s] = True
			else:
				break

	result = sum(i for i in range(1, limit + 1) if not can_be_written[i])
	return result


result = solution()
print(result)
