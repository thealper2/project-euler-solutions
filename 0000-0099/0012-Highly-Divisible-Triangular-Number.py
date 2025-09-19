import math

def count_divisors(x):
	cnt = 1
	n = x
	p = 2

	while p ** 2 <= n:
		if n % p == 0:
			e = 0
			while n % p == 0:
				n //= p
				e += 1

			cnt *= (e + 1)

		p += 1 if p == 2 else 2

	if n > 1:
		cnt *= 2

	return cnt

def solution(limit=500):
	n = 1
	while True:
		if n % 2 == 0:
			a = n // 2
			b = n + 1

		else:
			a = n
			b = (n + 1) // 2

		divisors = count_divisors(a) * count_divisors(b)
		if divisors > limit:
			return n * (n + 1) // 2

		n += 1


result = solution()
print(result)
