def solution():
	largest = 0
	is_pandigital = lambda x: len(str(x)) == 9 and set(str(x)) == set('123456789')
	for i in range(1, 10000):
		concat = ''
		n = 1
		while len(concat) < 9:
			concat += str(i * n)
			n += 1

		if len(concat) == 9 and is_pandigital(concat):
			num = int(concat)
			if num > largest:
				largest = num

	return largest


result = solution()
print(result)
