def is_palindrome(num):
	bin_num = bin(num)[2:]
	a = str(num) == str(num)[::-1]
	b = bin_num == bin_num[::-1]
	return a and b


def solution():
	limit = 1000000
	total = 0
	for n in range(1, limit):
		if is_palindrome(n):
			total += n

	return total


result = solution()
print(result)
