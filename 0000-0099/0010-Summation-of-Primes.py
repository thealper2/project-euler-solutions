def solution(limit=2_000_000):
	sieve = [True] * limit
	sieve[0] = sieve[1] = False
	for i in range(2, int(limit ** 0.5) + 1):
		if sieve[i]:
			for j in range(i * i, limit, i):
				sieve[j] = False

	return sum(i for i, is_prime in enumerate(sieve) if is_prime)

result = solution()
print(result)
