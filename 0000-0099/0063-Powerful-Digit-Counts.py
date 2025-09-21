def solution():
	cnt = 0
	for n in range(23):
		for p in range(1, 10):
			if len(str(p**n)) == n:
				cnt += 1

	return cnt

result = solution()
print(result)
