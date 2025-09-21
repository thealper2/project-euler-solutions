def solution():
	cnt = 0
	for n in range(1, 101):
		val = 1
		for r in range(1, n // 2 + 1):
			val = val * (n - r + 1) // r
			if val > 1_000_000:
				if r * 2 == n:
					cnt += 1
				else:
					cnt += 2

	return cnt

result = solution()
print(result)
