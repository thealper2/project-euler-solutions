def solution():
	N = (1001 - 1) // 2
	total = 1
	for k in range(1, N + 1):
		total += 16 * k * k + 4 * k + 4

	return total

result = solution()
print(result)
