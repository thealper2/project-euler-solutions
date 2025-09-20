def solution():
	result = 0
	for i in range(10, 1000000):
		digit_sum = sum(int(d)**5 for d in str(i))
		if i == digit_sum:
			result += i

	return result

result = solution()
print(result)
