def solution(n=1000):
	for a in range(1, n):
		for b in range(a + 1, n - a):
			c = 1000 - a - b
			if a**2 + b**2 == c**2:
				return a * b* c

result = solution()
print(result)
