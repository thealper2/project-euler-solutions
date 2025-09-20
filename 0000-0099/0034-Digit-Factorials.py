import math


def solution():
	result = 0
	f = [math.factorial(d) for d in range(0, 10)]
	for i in range(10, 100000):
		i_f = sum(f[int(d)] for d in str(i))
		if i_f == i:
			result += i

	return result


result = solution()
print(result)
