def sum_of_divisors(n):
	divisors = 1
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			divisors += i
			if i != n // i:
				divisors += n // i

	return divisors

def solution():
	amicables = set()
	for a in range(2, 10000):
		b = sum_of_divisors(a)
		if b != a and sum_of_divisors(b) == a:
			amicables.add(a)
			amicables.add(b)

	return sum(amicables)


result = solution()
print(result)
