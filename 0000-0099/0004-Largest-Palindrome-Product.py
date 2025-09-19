def solution():
	max_prod = float('-inf')
	for i in range(100, 1000):
		for j in range(i + 1, 1000):
			s = str(i * j)
			if s == s[::-1]:
				max_prod = max(max_prod, int(s))

	return max_prod

result = solution()
print(result)
