def solution():
	is_pentagonal = lambda x: ((1 + (1 + 24 * x) ** 0.5) / 6).is_integer()
	pentagonal_numbers = set()
	n = 1
	found =False
	result = 0

	while not found:
		new_pent = n * (3 * n - 1) // 2
		pentagonal_numbers.add(new_pent)

		for pent in pentagonal_numbers:
			a = is_pentagonal(pent + new_pent)
			d = abs(pent - new_pent)
			if a and d in pentagonal_numbers:
				result = d
				found = True
				break

		n += 1

	return result

result = solution()
print(result)
