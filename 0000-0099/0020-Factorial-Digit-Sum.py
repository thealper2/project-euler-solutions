import math

def solution():
	f = math.factorial(100)
	s_f = str(f)
	return sum(int(d) for d in s_f)

result = solution()
print(result)
