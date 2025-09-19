def solution():
	max_seq = 0
	max_num = None
	for i in range(2, 1_000_000):
		t = i
		seq = 1
		while t > 1:
			if t % 2 == 0:
				t //= 2
			else:
				t = 3 * t + 1

			seq += 1

		if seq >= max_seq:
			max_seq = seq
			max_num = i

	return max_num

result = solution()
print(result)

