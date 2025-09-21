def solution():
	n = 1
	while True:
		s = str(n)
		s = sorted(s)
		key = tuple(s)
		if all(tuple(sorted(str(k * n))) == key for k in range(2, 7)):
			return n

		n += 1

result = solution()
print(result)
