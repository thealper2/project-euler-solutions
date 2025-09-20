def solution():
	names = eval(open('0022_names.txt').read())
	names = sorted(names)
	total_score = 0
	for idx, name in enumerate(names, start=1):
		total_score += idx * sum(ord(c) - ord('A') + 1 for c in name)

	return total_score

result = solution()
print(result)
