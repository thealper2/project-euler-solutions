def solution():
	cnt =0
	for n in range(1, 10000):
		x = n
		is_lychrel = True
		is_palindrome = lambda x: str(x) == str(x)[::-1]
		for _ in range(50):
			x = x + int(str(x)[::-1])
			if is_palindrome(x):
				is_lychrel = False
				break

		if is_lychrel:
			cnt += 1

	return cnt

result = solution()
print(result)
