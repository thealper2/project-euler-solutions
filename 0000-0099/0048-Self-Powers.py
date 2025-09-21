def solution():
	val = sum(d**d for d in range(1, 1001))
	return str(val)[-10:]

result = solution()
print(result)
