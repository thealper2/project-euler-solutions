def solution():
	n = 100
	sum_of_squares = (n * (n + 1) * (2 * n + 1)) // 6
	square_of_sum = ((n * (n + 1)) // 2) ** 2
	return abs(sum_of_squares - square_of_sum)


result = solution()
print(result)

