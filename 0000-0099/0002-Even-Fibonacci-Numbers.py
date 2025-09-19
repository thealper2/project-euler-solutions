def solution():
	fib = [0, 1]
	result = 0
	while result <= 4_000_000:
		val = fib[-1] + fib[-2]
		fib.append(val)
		if val % 2 == 0:
			result += val

	return result

result = solution()
print(result)
